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


_META = {"_grupos.yaml", "_areas.yaml"}


def _carregar_raw():
    grupos = yaml.safe_load(open(os.path.join(DADOS, "_grupos.yaml"), encoding="utf-8")) or {}
    raw = {}
    for f in sorted(glob.glob(os.path.join(DADOS, "*.yaml"))):
        if os.path.basename(f) in _META:
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


def _carregar_areas_def():
    f = os.path.join(DADOS, "_areas.yaml")
    data = yaml.safe_load(open(f, encoding="utf-8")) or {}
    return data.get("areas", []), (data.get("mapa") or {})


def _resolver_areas(concursos):
    """Atribui d['area'] a cada disciplina (campo explícito > mapa) e devolve a lista de
    áreas com as disciplinas agregadas (deduplicadas por título, com os concursos que as têm).
    Falha alto se alguma disciplina ficar sem área — força a categorização de toda disciplina."""
    areas_def, mapa = _carregar_areas_def()
    sem_area = []
    for c in concursos:
        for d in c["disciplinas"]:
            aid = d.get("area") or mapa.get(d.get("slug"))
            if not aid:
                sem_area.append(f"{c['id']}/{d.get('slug')}")
            d["area"] = aid
    if sem_area:
        raise ValueError(
            "Disciplina(s) sem Área de Conhecimento (cadastre em dados/_areas.yaml "
            "ou no campo 'area:'):\n  " + "\n  ".join(sem_area))

    areas = [dict(a, disciplinas=[]) for a in areas_def]
    por_id = {a["id"]: a for a in areas}
    ocorr = {a["id"]: {} for a in areas}  # area_id -> {titulo: disciplina_agregada}
    for c in concursos:
        if c.get("oculto"):
            continue
        for d in c["disciplinas"]:
            a = por_id.get(d["area"])
            if not a:
                continue
            n_sub = sum(len(t["subtopicos"]) for t in d["topicos"])
            disc = ocorr[a["id"]].setdefault(d["titulo"], {
                "titulo": d["titulo"], "icone": d.get("icone", "📘"),
                "slug": d["slug"], "ocorrencias": []})
            disc["ocorrencias"].append({
                "concurso_id": c["id"], "concurso_nome": c["nome"],
                "orgao": c.get("orgao", ""), "slug": d["slug"], "n_subtopicos": n_sub})
    for a in areas:
        a["disciplinas"] = sorted(ocorr[a["id"]].values(), key=lambda x: x["titulo"].lower())
    return areas


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
AREAS = _resolver_areas(CONCURSOS)
AREA_POR_ID = {a["id"]: a for a in AREAS}
