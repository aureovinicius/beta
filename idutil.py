# -*- coding: utf-8 -*-
"""IDs estáveis de subtópico (sid) — derivados do título, independentes de posição."""
import re
import unicodedata


def slugify(text):
    t = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t or "item"


def assign_sids(disc):
    """Atribui s['sid'] estável a cada subtópico da disciplina (único por disciplina)."""
    seen = {}
    for t in disc["topicos"]:
        for s in t["subtopicos"]:
            base = slugify(s["titulo"])
            n = seen.get(base, 0) + 1
            seen[base] = n
            s["sid"] = base if n == 1 else f"{base}-{n}"


def sid_map(disc):
    """Retorna {(ti, si): sid} sem depender de 'sid' já estar atribuído."""
    seen, m = {}, {}
    for ti, t in enumerate(disc["topicos"]):
        for si, s in enumerate(t["subtopicos"]):
            base = slugify(s["titulo"])
            n = seen.get(base, 0) + 1
            seen[base] = n
            m[(ti, si)] = base if n == 1 else f"{base}-{n}"
    return m
