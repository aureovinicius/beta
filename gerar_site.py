# -*- coding: utf-8 -*-
"""Gera o site estático a partir do conteúdo programático + aprofundamentos."""
import glob
import html
import json
import os
from conteudo import DISCIPLINAS
from conteudo_especificos import ESPECIFICOS

TODAS = DISCIPLINAS + ESPECIFICOS
BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "site")
CONCURSO = "Auditor-Fiscal da Receita Estadual de Goiás"
SUBT = "SEFAZ-GO · ANEXO II — Conteúdo Programático"
GRUPOS = ["Conhecimentos Básicos", "Conhecimentos Específicos"]

# ---- carrega aprofundamentos: (slug, ti, si) -> item ----
EXP = {}
for f in glob.glob(os.path.join(BASE, "expandido", "*.json")):
    data = json.load(open(f, encoding="utf-8"))
    for it in data["itens"]:
        EXP[(data["slug"], it["ti"], it["si"])] = it


def e(s):
    return html.escape(str(s))


def paras(text):
    """Converte texto com \\n\\n em parágrafos HTML."""
    blocks = [b.strip() for b in str(text).split("\n\n") if b.strip()]
    return "".join(f"<p>{e(b)}</p>" for b in blocks)


def head(title, css_path, depth_script):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{css_path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>"""


def topbar(home):
    return f"""
<header class="topbar">
  <a class="brand" href="{home}">
    <span class="brand-mark">GO</span>
    <span class="brand-text"><strong>Guia de Estudos</strong><small>{e(CONCURSO)}</small></span>
  </a>
  <button id="theme-toggle" class="theme-toggle" aria-label="Alternar tema">🌙</button>
</header>"""


def foot(script_path):
    return f"""
<footer class="foot">
  <p>{e(CONCURSO)} — material de estudo de apoio. Confira sempre o edital oficial.</p>
</footer>
<script src="{script_path}"></script>
</body></html>"""


# =============================== HOME ===============================
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
    total_sub = sum(len(t["subtopicos"]) for d in TODAS for t in d["topicos"])

    doc = head(f"Guia de Estudos — {CONCURSO}", "assets/style.css", "")
    doc += topbar("index.html")
    doc += f"""
<main>
  <section class="hero">
    <p class="eyebrow">{e(SUBT)}</p>
    <h1>Guia de Estudos para o Concurso</h1>
    <p class="lead">Explicações didáticas de todas as disciplinas e subtópicos do conteúdo programático,
    com páginas de aprofundamento para cada assunto.</p>
    <div class="stats">
      <div class="stat"><strong>{total_disc}</strong><span>disciplinas</span></div>
      <div class="stat"><strong>{total_top}</strong><span>tópicos</span></div>
      <div class="stat"><strong>{total_sub}</strong><span>subtópicos</span></div>
    </div>
    <div class="search-wrap">
      <input id="search" type="search" placeholder="🔎 Buscar disciplina (ex.: ICMS, auditoria, lógica)…" autocomplete="off">
    </div>
  </section>
  {sections}
  <p id="no-results" class="no-results" hidden>Nenhuma disciplina encontrada.</p>
</main>"""
    doc += foot("assets/script.js")
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(doc)


# =========================== PÁGINA DISCIPLINA ===========================
def build_disciplina(d, idx):
    prev_d = TODAS[idx - 1] if idx > 0 else None
    next_d = TODAS[idx + 1] if idx < len(TODAS) - 1 else None
    toc_items = "".join(
        f'<li><a href="#t{i}">{e(t["titulo"])}</a></li>' for i, t in enumerate(d["topicos"])
    )

    topicos_html = ""
    for ti, t in enumerate(d["topicos"]):
        subs = ""
        for si, s in enumerate(t["subtopicos"]):
            vermais = ""
            if (d["slug"], ti, si) in EXP:
                href = f"../ampliado/{d['slug']}/t{ti}-s{si}.html"
                vermais = f'<a class="vermais" href="{href}">Ver mais <span>→</span></a>'
            subs += f"""
        <div class="sub">
          <h4>{e(s['titulo'])}</h4>
          <p>{e(s['texto'])}</p>
          {vermais}
        </div>"""
        topicos_html += f"""
      <article class="topico" id="t{ti}">
        <h2>{e(t['titulo'])}</h2>
        <p class="explica">{e(t['explicacao'])}</p>
        <div class="subs">{subs}</div>
      </article>"""

    nav_prev = f'<a class="pager prev" href="{prev_d["slug"]}.html">← {e(prev_d["titulo"])}</a>' if prev_d else "<span></span>"
    nav_next = f'<a class="pager next" href="{next_d["slug"]}.html">{e(next_d["titulo"])} →</a>' if next_d else "<span></span>"

    doc = head(f"{d['titulo']} — Guia de Estudos", "../assets/style.css", "")
    doc += topbar("../index.html")
    doc += f"""
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
</main>"""
    doc += foot("../assets/script.js")
    open(os.path.join(SITE, "disciplinas", f"{d['slug']}.html"), "w", encoding="utf-8").write(doc)


# ======================= PÁGINA DE APROFUNDAMENTO =======================
def build_ampliado(d):
    # ordem linear dos subtópicos da disciplina
    ordem = []
    for ti, t in enumerate(d["topicos"]):
        for si, s in enumerate(t["subtopicos"]):
            if (d["slug"], ti, si) in EXP:
                ordem.append((ti, si, t["titulo"], s["titulo"]))

    out_dir = os.path.join(SITE, "ampliado", d["slug"])
    os.makedirs(out_dir, exist_ok=True)

    for pos, (ti, si, top_titulo, sub_titulo) in enumerate(ordem):
        it = EXP[(d["slug"], ti, si)]

        secoes_html = "".join(
            f"""
        <section class="amp-sec">
          <h2>{e(sec['h'])}</h2>
          {paras(sec['p'])}
        </section>""" for sec in it["secoes"]
        )
        chave_html = "".join(f"<li>{e(p)}</li>" for p in it["pontos_chave"])

        prev_l = next_l = ""
        if pos > 0:
            p = ordem[pos - 1]
            prev_l = f'<a class="pager prev" href="t{p[0]}-s{p[1]}.html">← {e(p[3])}</a>'
        else:
            prev_l = "<span></span>"
        if pos < len(ordem) - 1:
            n = ordem[pos + 1]
            next_l = f'<a class="pager next" href="t{n[0]}-s{n[1]}.html">{e(n[3])} →</a>'
        else:
            next_l = "<span></span>"

        doc = head(f"{sub_titulo} — {d['titulo']}", "../../assets/style.css", "")
        doc += topbar("../../index.html")
        doc += f"""
<main class="amp-page">
  <nav class="crumbs">
    <a href="../../index.html">Início</a> ›
    <a href="../../disciplinas/{d['slug']}.html">{d['icone']} {e(d['titulo'])}</a> ›
    <span>{e(sub_titulo)}</span>
  </nav>
  <header class="amp-head">
    <p class="amp-eyebrow">{e(top_titulo)}</p>
    <h1>{e(sub_titulo)}</h1>
    {paras(it['intro'])}
  </header>

  <div class="amp-grid">
    <article class="amp-body">
      {secoes_html}
      <section class="amp-exemplo">
        <h2>💡 Exemplo aplicado</h2>
        {paras(it['exemplo'])}
      </section>
      <section class="amp-dica">
        <h2>🎯 Na prova</h2>
        {paras(it['dica_prova'])}
      </section>
      <div class="pager-row">{prev_l}{next_l}</div>
    </article>
    <aside class="amp-aside">
      <div class="amp-card">
        <h3>Pontos-chave</h3>
        <ul class="amp-chave">{chave_html}</ul>
      </div>
      <a class="back" href="../../disciplinas/{d['slug']}.html">↩ Voltar à disciplina</a>
    </aside>
  </div>
</main>"""
        doc += foot("../../assets/script.js")
        open(os.path.join(out_dir, f"t{ti}-s{si}.html"), "w", encoding="utf-8").write(doc)
    return len(ordem)


def main():
    os.makedirs(os.path.join(SITE, "disciplinas"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    build_index()
    n_amp = 0
    for i, d in enumerate(TODAS):
        build_disciplina(d, i)
        n_amp += build_ampliado(d)
    print(f"Gerado: index + {len(TODAS)} disciplinas + {n_amp} páginas de aprofundamento")


if __name__ == "__main__":
    main()
