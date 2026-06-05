# -*- coding: utf-8 -*-
"""Gera o site estático a partir do conteúdo programático."""
import html
import os
from conteudo import DISCIPLINAS
from conteudo_especificos import ESPECIFICOS

TODAS = DISCIPLINAS + ESPECIFICOS
BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "site")
CONCURSO = "Auditor-Fiscal da Receita Estadual de Goiás"
SUBT = "SEFAZ-GO · ANEXO II — Conteúdo Programático"

GRUPOS = ["Conhecimentos Básicos", "Conhecimentos Específicos"]


def e(s):
    return html.escape(str(s))


def head(title, css_path, extra=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{css_path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{extra}
</head>
<body>"""


def topbar(home="index.html"):
    return f"""
<header class="topbar">
  <a class="brand" href="{home}">
    <span class="brand-mark">GO</span>
    <span class="brand-text"><strong>Guia de Estudos</strong><small>{e(CONCURSO)}</small></span>
  </a>
  <button id="theme-toggle" class="theme-toggle" aria-label="Alternar tema">🌙</button>
</header>"""


def build_index():
    cards_by_group = {g: [] for g in GRUPOS}
    for d in TODAS:
        n_top = len(d["topicos"])
        n_sub = sum(len(t["subtopicos"]) for t in d["topicos"])
        card = f"""
      <a class="card" href="disciplinas/{d['slug']}.html" data-name="{e(d['titulo'].lower())}">
        <div class="card-icon">{d['icone']}</div>
        <div class="card-body">
          <h3>{e(d['titulo'])}</h3>
          <p>{e(d['resumo'])}</p>
          <div class="card-meta"><span>{n_top} tópicos</span><span>{n_sub} subtópicos</span></div>
        </div>
      </a>"""
        cards_by_group[d["grupo"]].append(card)

    sections = ""
    for g in GRUPOS:
        sections += f"""
    <section class="group">
      <h2 class="group-title">{e(g)}</h2>
      <div class="grid">{''.join(cards_by_group[g])}</div>
    </section>"""

    total_disc = len(TODAS)
    total_top = sum(len(d["topicos"]) for d in TODAS)

    html_doc = head(f"Guia de Estudos — {CONCURSO}", "assets/style.css")
    html_doc += topbar()
    html_doc += f"""
<main>
  <section class="hero">
    <p class="eyebrow">{e(SUBT)}</p>
    <h1>Guia de Estudos para o Concurso</h1>
    <p class="lead">Explicações didáticas de todas as disciplinas e subtópicos do conteúdo programático,
    organizadas para orientar a sua preparação.</p>
    <div class="stats">
      <div class="stat"><strong>{total_disc}</strong><span>disciplinas</span></div>
      <div class="stat"><strong>{total_top}</strong><span>tópicos</span></div>
      <div class="stat"><strong>2</strong><span>blocos de prova</span></div>
    </div>
    <div class="search-wrap">
      <input id="search" type="search" placeholder="🔎 Buscar disciplina (ex.: ICMS, auditoria, lógica)…" autocomplete="off">
    </div>
  </section>
  {sections}
  <p id="no-results" class="no-results" hidden>Nenhuma disciplina encontrada.</p>
</main>
<footer class="foot">
  <p>Conteúdo gerado a partir do edital <em>{e(SUBT)}</em>. Material de estudo de apoio — sempre confira o texto oficial do edital.</p>
</footer>
<script src="assets/script.js"></script>
</body></html>"""
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_doc)


def build_disciplina(d, idx):
    prev_d = TODAS[idx - 1] if idx > 0 else None
    next_d = TODAS[idx + 1] if idx < len(TODAS) - 1 else None

    # sidebar TOC
    toc_items = "".join(
        f'<li><a href="#t{i}">{e(t["titulo"])}</a></li>' for i, t in enumerate(d["topicos"])
    )

    topicos_html = ""
    for i, t in enumerate(d["topicos"]):
        subs = "".join(
            f"""
        <div class="sub">
          <h4>{e(s['titulo'])}</h4>
          <p>{e(s['texto'])}</p>
        </div>""" for s in t["subtopicos"]
        )
        topicos_html += f"""
      <article class="topico" id="t{i}">
        <h2>{e(t['titulo'])}</h2>
        <p class="explica">{e(t['explicacao'])}</p>
        <div class="subs">{subs}</div>
      </article>"""

    nav_prev = f'<a class="pager prev" href="{prev_d["slug"]}.html">← {e(prev_d["titulo"])}</a>' if prev_d else "<span></span>"
    nav_next = f'<a class="pager next" href="{next_d["slug"]}.html">{e(next_d["titulo"])} →</a>' if next_d else "<span></span>"

    html_doc = head(f"{d['titulo']} — Guia de Estudos", "../assets/style.css")
    html_doc += topbar("../index.html")
    html_doc += f"""
<main class="disc-page">
  <aside class="toc">
    <p class="toc-label">{e(d['grupo'])}</p>
    <h1 class="toc-title">{d['icone']} {e(d['titulo'])}</h1>
    <nav><ul>{toc_items}</ul></nav>
    <a class="back" href="../index.html">↩ Todas as disciplinas</a>
  </aside>
  <div class="content">
    <p class="disc-resumo">{e(d['resumo'])}</p>
    {topicos_html}
    <div class="pager-row">{nav_prev}{nav_next}</div>
  </div>
</main>
<footer class="foot">
  <p>{e(CONCURSO)} — material de estudo de apoio. Confira sempre o edital oficial.</p>
</footer>
<script src="../assets/script.js"></script>
</body></html>"""
    with open(os.path.join(SITE, "disciplinas", f"{d['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html_doc)


def main():
    os.makedirs(os.path.join(SITE, "disciplinas"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    build_index()
    for i, d in enumerate(TODAS):
        build_disciplina(d, i)
    print(f"Gerado: {len(TODAS)} disciplinas + index em {SITE}")


if __name__ == "__main__":
    main()
