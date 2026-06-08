# -*- coding: utf-8 -*-
"""Carrega os concursos a partir dos dados YAML (dados/*.yaml), resolve includes,
atribui IDs estáveis (sid) e valida o schema. Substitui o conteúdo-como-código."""
import glob
import os

import yaml

from idutil import assign_sids
from schema import validar_concurso_raw, validar_concursos

BASE = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(BASE, "dados")


def _carregar_raw():
    grupos = yaml.safe_load(open(os.path.join(DADOS, "_grupos.yaml"), encoding="utf-8")) or {}
    raw = {}
    for f in sorted(glob.glob(os.path.join(DADOS, "*.yaml"))):
        if os.path.basename(f) == "_grupos.yaml":
            continue
        c = yaml.safe_load(open(f, encoding="utf-8"))
        validar_concurso_raw(c, os.path.basename(f))
        raw[c["id"]] = c
    return raw, grupos


def _disciplina_de(raw, ref):
    cid, slug = ref.split("/", 1)
    src = raw.get(cid)
    if not src:
        raise ValueError(f"incluir: concurso '{cid}' não existe ({ref})")
    for d in src["disciplinas"]:
        if d.get("slug") == slug:
            return cid, d
    raise ValueError(f"incluir: disciplina '{slug}' não existe em '{cid}' ({ref})")


def _expandir_include(cid_origem, src_disc):
    """Inclui uma disciplina de outro concurso, marcando cada subtópico como reuso por sid.
    Se o subtópico de origem já tem 'reuse' (ex.: LP -> SEFAZ), preserva-o."""
    assign_sids(src_disc)
    nd = {k: v for k, v in src_disc.items() if k != "topicos"}
    nd["topicos"] = []
    for t in src_disc["topicos"]:
        nt = {k: v for k, v in t.items() if k != "subtopicos"}
        nt["subtopicos"] = []
        for s in t["subtopicos"]:
            ns = {"titulo": s["titulo"], "texto": s.get("texto", "")}
            ns["reuse"] = list(s["reuse"]) if "reuse" in s else [cid_origem, src_disc["slug"], s["sid"]]
            nt["subtopicos"].append(ns)
        nd["topicos"].append(nt)
    return nd


def _construir():
    raw, grupos = _carregar_raw()
    concursos = []
    for cid in sorted(raw, key=lambda k: raw[k].get("ordem", 9999)):
        c = dict(raw[cid])
        if isinstance(c.get("grupo"), str):
            c["grupo"] = grupos[c["grupo"]]
        discs = []
        for d in c["disciplinas"]:
            if "incluir" in d:
                oid, sdisc = _disciplina_de(raw, d["incluir"])
                discs.append(_expandir_include(oid, sdisc))
            else:
                discs.append(d)
        c["disciplinas"] = discs
        concursos.append(c)
    for c in concursos:
        for d in c["disciplinas"]:
            assign_sids(d)
    validar_concursos(concursos)
    _carregar_provas(concursos)
    return concursos


def _carregar_provas(concursos):
    """Anexa a cada concurso o banco de questões da prova, se existir (dados/provas/<id>.yaml)."""
    for c in concursos:
        f = os.path.join(DADOS, "provas", f"{c['id']}.yaml")
        if os.path.exists(f):
            prova = yaml.safe_load(open(f, encoding="utf-8")) or {}
            prova["questoes"] = {str(k): v for k, v in (prova.get("questoes") or {}).items()}
            c["prova"] = prova


CONCURSOS = _construir()
CONCURSO_POR_ID = {c["id"]: c for c in CONCURSOS}
