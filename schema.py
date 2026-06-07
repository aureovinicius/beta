# -*- coding: utf-8 -*-
"""Validação de schema dos dados de concursos (mensagens claras, erro isolado por arquivo)."""


class ErroSchema(Exception):
    pass


def _req(d, campos, ctx):
    for c in campos:
        if c not in d or d[c] in (None, "", []):
            raise ErroSchema(f"{ctx}: campo obrigatório ausente/vazio: '{c}'")


def validar_concurso_raw(c, fonte):
    """Valida a estrutura bruta de UM concurso (antes de resolver includes)."""
    _req(c, ["id", "nome", "orgao", "disciplinas"], fonte)
    if not isinstance(c["disciplinas"], list) or not c["disciplinas"]:
        raise ErroSchema(f"{fonte}: 'disciplinas' deve ser lista não vazia")
    for i, d in enumerate(c["disciplinas"]):
        ctx = f"{fonte} > disciplina[{i}]"
        if "incluir" in d:
            if "/" not in str(d["incluir"]):
                raise ErroSchema(f"{ctx}: 'incluir' deve ser 'concurso/slug'")
            continue
        _req(d, ["slug", "titulo", "topicos"], ctx)
        for j, t in enumerate(d["topicos"]):
            tctx = f"{ctx} > tópico[{j}]"
            _req(t, ["titulo", "subtopicos"], tctx)
            for k, s in enumerate(t["subtopicos"]):
                sctx = f"{tctx} > subtópico[{k}]"
                _req(s, ["titulo"], sctx)
                if "reuse" in s:
                    r = s["reuse"]
                    if not (isinstance(r, (list, tuple)) and len(r) == 3):
                        raise ErroSchema(f"{sctx}: 'reuse' deve ser [concurso, slug, sid]")


def validar_concursos(concursos):
    """Valida o conjunto já resolvido: sids únicos por disciplina e reuso que resolve."""
    # índice de todos os subtópicos por (cid, slug, sid)
    indice = set()
    for c in concursos:
        for d in c["disciplinas"]:
            sids = set()
            for t in d["topicos"]:
                for s in t["subtopicos"]:
                    sid = s.get("sid")
                    if not sid:
                        raise ErroSchema(f"{c['id']}/{d['slug']}: subtópico sem sid: {s.get('titulo')!r}")
                    if sid in sids:
                        raise ErroSchema(f"{c['id']}/{d['slug']}: sid duplicado: '{sid}'")
                    sids.add(sid)
                    indice.add((c["id"], d["slug"], sid))
    # toda referência de reuso aponta para um subtópico existente
    erros = []
    for c in concursos:
        for d in c["disciplinas"]:
            for t in d["topicos"]:
                for s in t["subtopicos"]:
                    if "reuse" in s:
                        alvo = tuple(s["reuse"])
                        if alvo not in indice:
                            erros.append(f"{c['id']}/{d['slug']}/{s['sid']} -> reuso inexistente {alvo}")
    if erros:
        raise ErroSchema("Reuso(s) que não resolvem:\n  " + "\n  ".join(erros))
