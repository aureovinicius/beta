# -*- coding: utf-8 -*-
"""
Gera o material do canal (YouTube) a PARTIR do conteúdo do site:
para cada tópico, um roteiro de narração (TTS) e uma descrição de YouTube com
link para a página correspondente. Saída em youtube/ (NÃO versionada no git).
"""
import os
import re

from idutil import slugify
from dados import CONCURSOS
from gerar_site import EXP, SITE_URL, get_content

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "youtube")


def limpa(t):
    """Texto pronto para TTS: sem markdown, espaços normalizados."""
    t = re.sub(r"\s+", " ", str(t).replace("\n\n", " ").replace("\n", " "))
    return t.strip()


def primeira_parte(intro, n=2):
    """Pega as primeiras n frases de um texto."""
    txt = limpa(intro)
    frases = re.split(r"(?<=[.!?])\s+", txt)
    return " ".join(frases[:n])


def narracao(c, d, t, ti, link):
    nome = c.get("grupo", {}).get("nome") if c.get("grupo") else c["nome"]
    partes = []
    partes.append(f"Olá! Bem-vindo ao Guia de Estudos. Neste vídeo vamos estudar {t['titulo']}, "
                  f"dentro de {d['titulo']}, do {nome}.")
    partes.append(limpa(t["explicacao"]))
    for s in t["subtopicos"]:
        item, _ = get_content(c["id"], d["slug"], s)
        corpo = primeira_parte(item["intro"], 2) if item else limpa(s.get("texto", ""))
        partes.append(f"{s['titulo']}. {corpo}")
        if item and item.get("pontos_chave"):
            chaves = "; ".join(limpa(p) for p in item["pontos_chave"][:3])
            partes.append(f"Pontos-chave: {chaves}.")
    partes.append("Este é só um resumo. Para estudar este assunto com a explicação completa e "
                  f"as páginas de aprofundamento, acesse o link na descrição: {link}. "
                  "Se este conteúdo te ajudou, inscreva-se no canal e bons estudos!")
    return "\n\n".join(p for p in partes if p)


def descricao(c, d, t, link):
    nome = c.get("grupo", {}).get("nome") if c.get("grupo") else c["nome"]
    titulo_video = f"{c['orgao']} | {d['titulo']}: {t['titulo']}"
    resumo = primeira_parte(t["explicacao"], 3)
    subs = ", ".join(s["titulo"] for s in t["subtopicos"])
    tags = ["concursos" if c["id"] != "enem-2026" else "enem", slugify(c["orgao"]),
            slugify(d["titulo"]), slugify(t["titulo"])]
    hashtags = " ".join("#" + re.sub(r"-", "", tg) for tg in tags if tg)
    return (
        f"{titulo_video}\n\n"
        f"{resumo}\n\n"
        f"Neste vídeo: {subs}.\n\n"
        f"👉 Conteúdo completo e aprofundado: {link}\n"
        f"📚 Plataforma de estudos: {SITE_URL}/\n\n"
        f"Material de estudo de apoio — {nome}. Confira sempre o edital/matriz oficial.\n\n"
        f"{hashtags} #estudos #aprovação"
    )


def main():
    n = 0
    for c in CONCURSOS:
        if c.get("oculto"):
            continue
        for d in c["disciplinas"]:
            for ti, t in enumerate(d["topicos"]):
                link = f"{SITE_URL}/{c['id']}/disciplinas/{d['slug']}.html#t{ti}"
                pasta = os.path.join(OUT, c["id"], d["slug"])
                os.makedirs(pasta, exist_ok=True)
                base = f"{ti:02d}-{slugify(t['titulo'])}"
                narr = narracao(c, d, t, ti, link)
                desc = descricao(c, d, t, link)
                open(os.path.join(pasta, base + ".narracao.txt"), "w", encoding="utf-8").write(narr)
                open(os.path.join(pasta, base + ".youtube.txt"), "w", encoding="utf-8").write(desc)
                n += 1
    print(f"Gerados {n} tópicos (roteiro .narracao.txt + descrição .youtube.txt) em {OUT}/")


if __name__ == "__main__":
    main()
