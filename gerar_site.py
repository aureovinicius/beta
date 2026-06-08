# -*- coding: utf-8 -*-
"""Gera o site estático multi-concurso (landing + concursos + aprofundamentos)."""
import glob
import html
import json
import math
import os
import shutil
from concursos import AREAS, CONCURSOS, CONCURSO_POR_ID

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "site")
ASSETS_SRC = os.path.join(BASE, "assets")  # fonte versionada do CSS/JS
SITE_URL = "https://aureovinicius.github.io/beta"  # base pública (sem barra final)
GRUPOS = ["Conhecimentos Básicos", "Conhecimentos Específicos"]

# ---- carrega aprofundamentos: (concurso_id, slug, sid) -> item ----
EXP = {}
for c in CONCURSOS:
    for f in glob.glob(os.path.join(BASE, "expandido", c["id"], "*.json")):
        data = json.load(open(f, encoding="utf-8"))
        for it in data["itens"]:
            EXP[(c["id"], data["slug"], it["sid"])] = it


def e(s):
    return html.escape(str(s))


def paras(text):
    blocks = [b.strip() for b in str(text).split("\n\n") if b.strip()]
    return "".join(f"<p>{e(b)}</p>" for b in blocks)


def get_content(cid, slug, s):
    """Retorna (item, origem_concurso_id|None). origem != None => reaproveitado.
    Resolve por sid estável (não por posição)."""
    if "reuse" in s:
        key = tuple(s["reuse"])  # (concurso, slug, sid)
        return EXP.get(key), key[0]
    return EXP.get((cid, slug, s["sid"])), None


# ============================ GRÁFICOS (SVG inline) ============================
def _palette(n):
    """n cores distintas e tema-neutras, distribuídas pelo ângulo áureo (HSL)."""
    return [f"hsl({(i * 137.508) % 360:.0f} 60% 52%)" for i in range(n)]


def svg_pie(dados, legenda_total="questões"):
    """dados = [(label, valor), ...]. Donut SVG inline + legenda (sem dependências)."""
    dados = [(l, v) for l, v in dados if v]
    if not dados:
        return ""
    total = sum(v for _, v in dados)
    cores = _palette(len(dados))
    cx = cy = 90
    r, ri = 80, 50
    segs = ""
    ang = -90.0  # começa no topo
    for (label, valor), cor in zip(dados, cores):
        frac = valor / total
        a0, a1 = math.radians(ang), math.radians(ang + frac * 360)
        ang += frac * 360
        if frac >= 0.999:  # fatia única = anel completo
            segs += (f'<circle cx="{cx}" cy="{cy}" r="{(r + ri) / 2:.1f}" fill="none" '
                     f'stroke="{cor}" stroke-width="{r - ri}"><title>{e(label)}: {valor}</title></circle>')
            continue
        large = 1 if frac > 0.5 else 0
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        xi0, yi0 = cx + ri * math.cos(a1), cy + ri * math.sin(a1)
        xi1, yi1 = cx + ri * math.cos(a0), cy + ri * math.sin(a0)
        segs += (f'<path d="M {x0:.2f} {y0:.2f} A {r} {r} 0 {large} 1 {x1:.2f} {y1:.2f} '
                 f'L {xi0:.2f} {yi0:.2f} A {ri} {ri} 0 {large} 0 {xi1:.2f} {yi1:.2f} Z" '
                 f'fill="{cor}"><title>{e(label)}: {valor}</title></path>')
    centro = (f'<text x="{cx}" y="{cy - 2}" class="pie-num">{total}</text>'
              f'<text x="{cx}" y="{cy + 15}" class="pie-cap">{e(legenda_total)}</text>')
    legenda = "".join(
        f'<li><span class="lg-dot" style="background:{cor}"></span>'
        f'<span class="lg-label">{e(label)}</span>'
        f'<span class="lg-val">{valor} · {round(valor * 100 / total)}%</span></li>'
        for (label, valor), cor in zip(dados, cores))
    return (f'<div class="pie-wrap">'
            f'<svg viewBox="0 0 180 180" class="pie" role="img" aria-label="Gráfico de pizza">'
            f'{segs}{centro}</svg>'
            f'<ul class="pie-legend">{legenda}</ul></div>')


def barras(rows):
    """rows = [(label, valor), ...] já ordenado. Barras horizontais em CSS (responsivas)."""
    rows = [(l, v) for l, v in rows if v]
    if not rows:
        return ""
    maxv = max(v for _, v in rows)
    cores = _palette(len(rows))
    itens = ""
    for (label, valor), cor in zip(rows, cores):
        pct = max(5, round(valor * 100 / maxv))
        itens += (f'<div class="bar-row"><span class="bar-label" title="{e(label)}">{e(label)}</span>'
                  f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%;background:{cor}">'
                  f'</span></span><span class="bar-val">{valor}</span></div>')
    return f'<div class="bars">{itens}</div>'


# ===================== AGREGAÇÃO ESTATÍSTICA (entre provas) =====================
def coletar_estatisticas():
    """Agrega, por tópico e por área, em quantas provas e questões cada um foi cobrado.
    Devolve uma estrutura JSON-serializável (gravada também em site/estatisticas.json)."""
    topicos, areas, provas = {}, {}, []
    nome_area = {a["id"]: a["nome"] for a in AREAS}
    for c in CONCURSOS:
        if c.get("oculto") or not c.get("prova"):
            continue
        provas.append({"id": c["id"], "nome": c["nome"], "orgao": c.get("orgao", ""),
                       "banca": c["prova"].get("banca") or c.get("banca", ""),
                       "n_questoes": len(c["prova"].get("questoes") or {})})
        for d in c["disciplinas"]:
            for t in d["topicos"]:
                nums = t.get("prova") or []
                if not nums:
                    continue
                reg = topicos.setdefault((d["slug"], t["titulo"]), {
                    "area": d["area"], "area_nome": nome_area.get(d["area"], d["area"]),
                    "disciplina": d["titulo"], "disciplina_slug": d["slug"],
                    "topico": t["titulo"], "n_questoes": 0, "provas": []})
                reg["n_questoes"] += len(nums)
                reg["provas"].append({"concurso": c["id"], "orgao": c.get("orgao", ""),
                                      "questoes": list(nums)})
                a = areas.setdefault(d["area"], {"q": 0, "provas": set(), "disc": set()})
                a["q"] += len(nums)
                a["provas"].add(c["id"])
                a["disc"].add(d["titulo"])
    rank = []
    for reg in topicos.values():
        reg["n_provas"] = len({p["concurso"] for p in reg["provas"]})
        rank.append(reg)
    rank.sort(key=lambda r: (-r["n_questoes"], -r["n_provas"], r["disciplina"].lower()))
    areas_rank = sorted(
        ({"area": aid, "nome": nome_area.get(aid, aid), "n_questoes": a["q"],
          "n_provas": len(a["provas"]), "n_disciplinas": len(a["disc"])}
         for aid, a in areas.items()),
        key=lambda r: -r["n_questoes"])
    return {"gerado_de": [p["id"] for p in provas], "provas": provas,
            "areas": areas_rank, "topicos": rank}


KATEX_VER = "0.16.11"


def head(title, up, katex=False):
    css = "../" * up + "assets/style.css"
    katex_css = (f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX_VER}/dist/katex.min.css">'
                 if katex else "")
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{css}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{katex_css}
</head>
<body>"""


def topbar(up, sub=""):
    base = "../" * up
    home = base + "index.html"
    subhtml = f"<small>{e(sub)}</small>" if sub else "<small>Guia de Estudos para Concursos</small>"
    return f"""
<header class="topbar">
  <a class="brand" href="{home}">
    <span class="brand-mark">GE</span>
    <span class="brand-text"><strong>Guia de Estudos</strong>{subhtml}</span>
  </a>
  <nav class="topnav">
    <a href="{base}areas/index.html">🧭 <span class="nav-txt">Áreas</span></a>
    <a href="{base}estatisticas.html">📊 <span class="nav-txt">Estatísticas</span></a>
  </nav>
  <button id="theme-toggle" class="theme-toggle" aria-label="Alternar tema">🌙</button>
</header>"""


def foot(up, rodape="", katex=False):
    script = "../" * up + "assets/script.js"
    txt = rodape or "Material de estudo de apoio. Confira sempre o edital oficial."
    katex_js = ""
    if katex:
        b = f"https://cdn.jsdelivr.net/npm/katex@{KATEX_VER}/dist"
        katex_js = f"""
<script defer src="{b}/katex.min.js"></script>
<script defer src="{b}/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'$$',right:'$$',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}],throwOnError:false}});"></script>"""
    return f"""
<footer class="foot"><p>{e(txt)}</p></footer>
<script src="{script}"></script>{katex_js}
</body></html>"""


def counts(c):
    disc = len(c["disciplinas"])
    top = sum(len(d["topicos"]) for d in c["disciplinas"])
    sub = sum(len(t["subtopicos"]) for d in c["disciplinas"] for t in d["topicos"])
    return disc, top, sub


def _meta_line(c):
    partes = []
    if c.get("banca"):
        partes.append(f"🏛️ {e(c['banca'])}")
    if c.get("ano"):
        partes.append(f"📅 {e(c['ano'])}")
    return "".join(f"<span>{p}</span>" for p in partes)


# ================================ LANDING ================================
def build_landing():
    visiveis = [c for c in CONCURSOS if not c.get("oculto")]
    avulsos = [c for c in visiveis if not c.get("grupo")]
    # agrupa cargos por grupo, preservando ordem de aparição
    grupos = {}
    for c in visiveis:
        g = c.get("grupo")
        if g:
            grupos.setdefault(g["id"], {"meta": g, "cargos": []})["cargos"].append(c)

    # bancas distintas (para os chips de filtro)
    bancas = sorted({c.get("banca", "") for c in avulsos if c.get("banca")} |
                    {info["meta"].get("banca", "") for info in grupos.values() if info["meta"].get("banca")})

    cards = ""
    for c in avulsos:
        disc, top, sub = counts(c)
        busca = e(" ".join(str(c.get(k, "")) for k in ("nome", "orgao", "banca", "cargo", "descricao")).lower())
        cards += f"""
      <a class="concurso-card" href="{c['id']}/index.html" style="--accent:{c['cor']}" data-search="{busca}" data-banca="{e(c.get('banca','').lower())}">
        <div class="cc-top"><span class="cc-icon">{c['icone']}</span><span class="cc-orgao">{e(c['orgao'])}</span></div>
        <h3>{e(c['nome'])}</h3>
        <p class="cc-cargo">{e(c['cargo'])}</p>
        <p class="cc-desc">{e(c['descricao'])}</p>
        <div class="cc-meta">{_meta_line(c)}</div>
        <div class="cc-stats"><span><strong>{disc}</strong> disciplinas</span>
          <span><strong>{sub}</strong> subtópicos</span></div>
        <span class="cc-go">Estudar →</span>
      </a>"""

    # boxes de grupo (expansíveis)
    for gid, info in grupos.items():
        g = info["meta"]
        cargos = info["cargos"]
        sub_cards = ""
        cargos_busca = []
        for c in cargos:
            disc, top, sub = counts(c)
            cbusca = e(" ".join(str(c.get(k, "")) for k in ("nome", "cargo", "especialidade", "codigo")).lower())
            cargos_busca.append(cbusca)
            sub_cards += f"""
          <a class="cargo-card" href="{c['id']}/index.html" data-search="{cbusca}">
            <span class="cargo-icon">{c['icone']}</span>
            <span class="cargo-body"><strong>{e(c['nome'])}</strong>
              <small>{e(c['cargo'])} · cód. {e(c.get('codigo',''))} · {sub} subtópicos</small></span>
            <span class="cargo-go">→</span>
          </a>"""
        gbusca = e((" ".join([g["nome"], g["orgao"], g.get("descricao", "")]).lower())) + " " + " ".join(cargos_busca)
        cards += f"""
      <div class="concurso-card grupo-card" style="--accent:{g['cor']}" data-search="{gbusca}" data-banca="{e(g.get('banca','').lower())}">
        <button class="grupo-head" aria-expanded="false">
          <div class="cc-top"><span class="cc-icon">{g['icone']}</span><span class="cc-orgao">{e(g['orgao'])}</span></div>
          <h3>{e(g['nome'])}</h3>
          <p class="cc-desc">{e(g['descricao'])}</p>
          <div class="cc-meta">{_meta_line(g)}</div>
          <div class="cc-stats"><span><strong>{len(cargos)}</strong> cargos/especialidades</span></div>
          <span class="cc-go grupo-toggle">Ver cargos <span class="chevron">▾</span></span>
        </button>
        <div class="grupo-cargos" hidden>{sub_cards}</div>
      </div>"""

    doc = head("Guia de Estudos para Concursos", 0)
    doc += topbar(0)
    doc += f"""
<main>
  <section class="hero">
    <p class="eyebrow">Plataforma de estudos</p>
    <h1>Escolha o seu concurso</h1>
    <p class="lead">Conteúdo programático explicado, disciplina por disciplina, com páginas de
    aprofundamento para cada subtópico. Selecione um concurso para começar.</p>
    <div class="search-wrap">
      <input id="busca-concursos" type="search" placeholder="🔎 Buscar concurso, órgão, banca ou cargo…" autocomplete="off">
    </div>
    <div class="filtros" id="filtros-banca">
      <span class="filtros-label">Banca:</span>
      <button class="chip ativo" data-banca="">Todas</button>
      {''.join(f'<button class="chip" data-banca="{e(b.lower())}">{e(b)}</button>' for b in bancas)}
    </div>
  </section>
  <section class="group">
    <h2 class="group-title">Concursos disponíveis</h2>
    <div class="concurso-grid">{cards}</div>
    <p id="sem-concursos" class="no-results" hidden>Nenhum concurso encontrado.</p>
  </section>
</main>"""
    doc += foot(0, "Guia de Estudos para Concursos — material de apoio. Confira sempre o edital oficial.")
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(doc)


# ============================= HOME DO CONCURSO =============================
def panorama_bloco(c):
    """Seção 'Panorama da prova' na home do concurso: resumo + pizza (questões por
    disciplina) + tabelas de conteúdos fora do edital e não cobrados. Vazio se não há prova."""
    prova = c.get("prova")
    if not prova:
        return ""
    pan = prova.get("panorama") or {}
    por_disc, nao_cairam, total_q = [], {}, set()
    for d in c["disciplinas"]:
        qs, faltantes = set(), []
        for t in d["topicos"]:
            nums = t.get("prova") or []
            (qs.update(nums) if nums else faltantes.append(t["titulo"]))
        if qs:
            por_disc.append((d["titulo"], len(qs)))
            total_q.update(qs)
        if faltantes:
            nao_cairam[d["titulo"]] = faltantes
    if not por_disc:
        return ""
    por_disc.sort(key=lambda x: -x[1])
    n_q = len(prova.get("questoes") or {})
    pie = svg_pie(por_disc, legenda_total="questões")

    resumo_html = f'<div class="pan-resumo">{paras(pan["resumo"])}</div>' if pan.get("resumo") else ""

    fora = pan.get("fora_edital") or []
    fora_html = ""
    if fora:
        linhas = ""
        for it in fora:
            qstr = ", ".join(f"Q{n}" for n in (it.get("questoes") or []))
            badge = f'<span class="prova-badge fora">{e(qstr)}</span> ' if qstr else ""
            linhas += (f'<tr><td class="td-disc">{e(it.get("tema", ""))}</td>'
                       f'<td>{badge}{e(it.get("nota", ""))}</td></tr>')
        fora_html = (f'<div class="pan-tabela"><h3>⚠️ Caíram, mas não estavam claros no edital</h3>'
                     f'<table class="tabela-prova"><thead><tr><th>Tema</th>'
                     f'<th>Questões e observação</th></tr></thead><tbody>{linhas}</tbody></table></div>')

    nao_html = ""
    if nao_cairam:
        linhas = "".join(
            f'<tr><td class="td-disc">{e(disc)}</td>'
            f'<td>{", ".join(e(x) for x in tops)}</td></tr>'
            for disc, tops in nao_cairam.items())
        nao_html = (f'<details class="pan-tabela"><summary>📉 Conteúdos que não caíram '
                    f'({len(nao_cairam)} disciplinas)</summary>'
                    f'<table class="tabela-prova"><thead><tr><th>Disciplina</th>'
                    f'<th>Tópicos não cobrados nesta prova</th></tr></thead><tbody>{linhas}</tbody></table></details>')

    return f"""
  <section class="panorama">
    <h2 class="group-title">📊 Panorama da prova</h2>
    <p class="pan-sub">{e(prova.get('titulo', ''))}</p>
    {resumo_html}
    <div class="panorama-grid">
      <div class="pan-grafico">
        <h3>Questões por disciplina</h3>
        {pie}
        <p class="pan-nota">{len(total_q)} de {n_q} questões mapeadas a {len(por_disc)} disciplinas cobradas.</p>
      </div>
      <div class="pan-tabelas">
        {fora_html}
        {nao_html}
      </div>
    </div>
  </section>"""


def build_concurso_home(c):
    cid = c["id"]
    cards_by_group = {g: [] for g in GRUPOS}
    for d in c["disciplinas"]:
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
        cards_by_group.setdefault(d["grupo"], []).append(card)

    ordem = ["Conhecimentos Gerais", "Conhecimentos Básicos",
             "Conhecimentos Específicos Comuns", "Conhecimentos Específicos"]
    ordem += [g for g in cards_by_group if g not in ordem]
    sections = ""
    for g in ordem:
        if not cards_by_group.get(g):
            continue
        sections += f"""
    <section class="group">
      <h2 class="group-title">{e(g)}</h2>
      <div class="grid">{''.join(cards_by_group[g])}</div>
    </section>"""

    disc, top, sub = counts(c)
    g = c.get("grupo")
    if g:
        crumb = f'<a href="../index.html">Concursos</a> › <span>{e(g["nome"])}</span> › <span>{e(c["nome"])}</span>'
        eyebrow = " · ".join(x for x in [e(g["orgao"]), e(g.get("banca", "")), c.get("cargo", ""), e(c.get("ano", ""))] if x)
        titulo = f"{c['icone']} {e(c['nome'])}"
    else:
        crumb = f'<a href="../index.html">Concursos</a> › <span>{e(c["orgao"])}</span>'
        eyebrow = " · ".join(x for x in [e(c["orgao"]), e(c.get("banca", "")), e(c.get("ano", ""))] if x)
        titulo = e(c["nome"])
    doc = head(f"{c['nome']} — Guia de Estudos", 1)
    doc += topbar(1, g["orgao"] if g else c["orgao"])
    doc += f"""
<main>
  <nav class="crumbs">{crumb}</nav>
  <section class="hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{titulo}</h1>
    <p class="lead">{e(c['descricao'])}</p>
    <div class="stats">
      <div class="stat"><strong>{disc}</strong><span>disciplinas</span></div>
      <div class="stat"><strong>{top}</strong><span>tópicos</span></div>
      <div class="stat"><strong>{sub}</strong><span>subtópicos</span></div>
    </div>
    <div class="search-wrap">
      <input id="search" type="search" placeholder="🔎 Buscar disciplina…" autocomplete="off">
    </div>
  </section>
  {panorama_bloco(c)}
  {sections}
  <p id="no-results" class="no-results" hidden>Nenhuma disciplina encontrada.</p>
</main>"""
    doc += foot(1, f"{c['nome']} ({c['orgao']}) — material de estudo de apoio.")
    open(os.path.join(SITE, cid, "index.html"), "w", encoding="utf-8").write(doc)


def prova_bloco(t, prova):
    """Retorna (badge_html, questoes_html) para um tópico, dado o banco da prova."""
    if not prova:
        return "", ""
    nums = t.get("prova") or []
    if not nums:
        badge = '<span class="prova-badge naocaiu" title="Não foi cobrado na última prova">○ Não caiu</span>'
        return badge, ""
    qs = ", ".join(f"Q{n}" for n in nums)
    badge = f'<span class="prova-badge caiu" title="Cobrado na última prova">📝 Caiu na prova · {e(qs)}</span>'
    cards = ""
    for n in nums:
        q = prova["questoes"].get(str(n)) or prova["questoes"].get(n)
        if not q:
            continue
        alts = "".join(f"<li>{e(a)}</li>" for a in q.get("alternativas", []))
        alts_html = f"<ol class='q-alts' type='A'>{alts}</ol>" if alts else ""
        if q.get("gabarito"):
            com = f"<span class='q-com'>{e(q['comentario'])}</span>" if q.get("comentario") else ""
            gab = (f"<details class='q-gab'><summary>Ver gabarito comentado</summary>"
                   f"<p class='q-resp'>Resposta: <strong>{e(q['gabarito'])}</strong></p>{com}</details>")
        else:
            gab = ""
        cards += f"""
        <div class="questao">
          <p class="q-num">Questão {n} — {e(prova.get('banca',''))}</p>
          <p class="q-enun">{e(q.get('enunciado',''))}</p>
          {alts_html}{gab}
        </div>"""
    questoes_html = (f'<details class="prova-questoes"><summary>📄 Ver {len(nums)} questão(ões) '
                     f'desta prova</summary>{cards}</details>') if cards else ""
    return badge, questoes_html


# ============================= PÁGINA DISCIPLINA =============================
def build_disciplina(c, d, idx):
    cid = c["id"]
    discs = c["disciplinas"]
    prev_d = discs[idx - 1] if idx > 0 else None
    next_d = discs[idx + 1] if idx < len(discs) - 1 else None
    toc_items = "".join(
        f'<li><a href="#t{i}">{e(t["titulo"])}</a></li>' for i, t in enumerate(d["topicos"])
    )

    prova = c.get("prova")  # {"titulo":..., "questoes":{num:{enunciado,alternativas}}}
    topicos_html = ""
    for ti, t in enumerate(d["topicos"]):
        subs = ""
        for s in t["subtopicos"]:
            item, origem = get_content(cid, d["slug"], s)
            vermais = ""
            if item:
                href = f"../ampliado/{d['slug']}/{s['sid']}.html"
                tag = '<span class="tag-reuse" title="Conteúdo compartilhado entre concursos">♻</span>' if origem else ""
                vermais = f'<a class="vermais" href="{href}">Ver mais <span>→</span></a>{tag}'
            texto_html = f"<p>{e(s['texto'])}</p>" if s.get("texto") else ""
            subs += f"""
        <div class="sub">
          <h4>{e(s['titulo'])}</h4>
          {texto_html}
          {vermais}
        </div>"""
        badge, questoes_html = prova_bloco(t, prova)
        topicos_html += f"""
      <article class="topico" id="t{ti}">
        <h2>{e(t['titulo'])}{badge}</h2>
        <p class="explica">{e(t['explicacao'])}</p>
        <div class="subs">{subs}</div>
        {questoes_html}
      </article>"""

    nav_prev = f'<a class="pager prev" href="{prev_d["slug"]}.html">← {e(prev_d["titulo"])}</a>' if prev_d else "<span></span>"
    nav_next = f'<a class="pager next" href="{next_d["slug"]}.html">{e(next_d["titulo"])} →</a>' if next_d else "<span></span>"

    doc = head(f"{d['titulo']} — {c['orgao']}", 2, katex=True)
    doc += topbar(2, c["orgao"])
    doc += f"""
<main class="disc-page">
  <aside class="toc">
    <nav class="crumbs"><a href="../../index.html">Concursos</a> ›
      <a href="../index.html">{e(c['orgao'])}</a></nav>
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
    doc += foot(2, f"{c['nome']} ({c['orgao']}) — material de estudo de apoio.", katex=True)
    open(os.path.join(SITE, cid, "disciplinas", f"{d['slug']}.html"), "w", encoding="utf-8").write(doc)


# ========================= PÁGINA DE APROFUNDAMENTO =========================
def build_ampliado(c, d):
    cid = c["id"]
    ordem = []
    for t in d["topicos"]:
        for s in t["subtopicos"]:
            item, origem = get_content(cid, d["slug"], s)
            if item:
                ordem.append((s["sid"], t["titulo"], s["titulo"], item, origem))

    out_dir = os.path.join(SITE, cid, "ampliado", d["slug"])
    os.makedirs(out_dir, exist_ok=True)

    for pos, (sid, top_titulo, sub_titulo, it, origem) in enumerate(ordem):
        secoes_html = "".join(
            f'<section class="amp-sec"><h2>{e(sec["h"])}</h2>{paras(sec["p"])}</section>'
            for sec in it["secoes"]
        )
        chave_html = "".join(f"<li>{e(p)}</li>" for p in it["pontos_chave"])

        if pos > 0:
            p = ordem[pos - 1]
            prev_l = f'<a class="pager prev" href="{p[0]}.html">← {e(p[2])}</a>'
        else:
            prev_l = "<span></span>"
        if pos < len(ordem) - 1:
            n = ordem[pos + 1]
            next_l = f'<a class="pager next" href="{n[0]}.html">{e(n[2])} →</a>'
        else:
            next_l = "<span></span>"

        banner = ""
        if origem:
            banner = ('<div class="reuse-banner">♻ Conteúdo compartilhado entre concursos '
                      '— mesmo assunto cobrado em mais de um certame.</div>')

        doc = head(f"{sub_titulo} — {c['orgao']}", 3, katex=True)
        doc += topbar(3, c["orgao"])
        doc += f"""
<main class="amp-page">
  <nav class="crumbs">
    <a href="../../../index.html">Concursos</a> ›
    <a href="../../index.html">{e(c['orgao'])}</a> ›
    <a href="../../disciplinas/{d['slug']}.html">{d['icone']} {e(d['titulo'])}</a> ›
    <span>{e(sub_titulo)}</span>
  </nav>
  <header class="amp-head">
    <p class="amp-eyebrow">{e(top_titulo)}</p>
    <h1>{e(sub_titulo)}</h1>
    {banner}
    {paras(it['intro'])}
  </header>
  <div class="amp-grid">
    <article class="amp-body">
      {secoes_html}
      <section class="amp-exemplo"><h2>💡 Exemplo aplicado</h2>{paras(it['exemplo'])}</section>
      <section class="amp-dica"><h2>🎯 Na prova</h2>{paras(it['dica_prova'])}</section>
      <div class="pager-row">{prev_l}{next_l}</div>
    </article>
    <aside class="amp-aside">
      <div class="amp-card"><h3>Pontos-chave</h3><ul class="amp-chave">{chave_html}</ul></div>
      <a class="back" href="../../disciplinas/{d['slug']}.html">↩ Voltar à disciplina</a>
    </aside>
  </div>
</main>"""
        doc += foot(3, f"{c['nome']} ({c['orgao']}) — material de estudo de apoio.", katex=True)
        open(os.path.join(out_dir, f"{sid}.html"), "w", encoding="utf-8").write(doc)
    return len(ordem)


# ============================== ESTATÍSTICAS ==============================
def build_estatisticas(est):
    """Página global de estatísticas: ranking de tópicos mais cobrados + rollup por área.
    O 'arquivo de dados' (estatisticas.json) é gravado em main()."""
    rank, areas, provas = est["topicos"], est["areas"], est["provas"]
    n_provas = len(provas)

    area_bars = barras([(a["nome"], a["n_questoes"]) for a in areas])
    top = rank[:20]
    top_bars = barras([(f'{r["topico"]} — {r["disciplina"]}', r["n_questoes"]) for r in top])

    rank_linhas = "".join(
        f'<tr><td>{e(r["topico"])}</td><td class="td-disc">{e(r["disciplina"])}</td>'
        f'<td>{e(r["area_nome"])}</td>'
        f'<td class="num">{r["n_provas"]}</td><td class="num">{r["n_questoes"]}</td></tr>'
        for r in rank)
    provas_chips = "".join(
        f'<a class="area-chip" href="{p["id"]}/index.html">{e(p["orgao"] or p["nome"])} '
        f'· {e(p["banca"])} · {p["n_questoes"]} questões</a>' for p in provas)

    doc = head("Estatísticas — Guia de Estudos", 0)
    doc += topbar(0)
    doc += f"""
<main>
  <nav class="crumbs"><a href="index.html">Início</a> › <span>Estatísticas</span></nav>
  <section class="hero">
    <p class="eyebrow">O que mais cai</p>
    <h1>📊 Estatísticas das provas</h1>
    <p class="lead">Tópicos ranqueados por incidência nas provas já catalogadas: em quantas
    provas e em quantas questões cada um foi cobrado. A base cresce a cada nova prova analisada.</p>
    <div class="stats">
      <div class="stat"><strong>{n_provas}</strong><span>prova(s)</span></div>
      <div class="stat"><strong>{len(rank)}</strong><span>tópicos cobrados</span></div>
      <div class="stat"><strong>{len(areas)}</strong><span>áreas</span></div>
    </div>
    <p class="pan-nota">Provas catalogadas: {provas_chips or '—'}</p>
  </section>

  <section class="group">
    <h2 class="group-title">Questões por área de conhecimento</h2>
    {area_bars or '<p class="pan-nota">Sem dados ainda.</p>'}
  </section>

  <section class="group">
    <h2 class="group-title">Top 20 tópicos mais cobrados</h2>
    {top_bars or '<p class="pan-nota">Sem dados ainda.</p>'}
  </section>

  <section class="group">
    <h2 class="group-title">Ranking completo de tópicos</h2>
    <div class="rank-wrap"><table class="rank-table">
      <thead><tr><th>Tópico</th><th>Disciplina</th><th>Área</th>
        <th class="num">Provas</th><th class="num">Questões</th></tr></thead>
      <tbody>{rank_linhas}</tbody>
    </table></div>
    <p class="pan-nota">Dados abertos: <a href="estatisticas.json">estatisticas.json</a>.</p>
  </section>
</main>"""
    doc += foot(0, "Estatísticas geradas a partir das provas catalogadas no projeto.")
    open(os.path.join(SITE, "estatisticas.html"), "w", encoding="utf-8").write(doc)


# ========================== ÁREAS DE CONHECIMENTO ==========================
def build_areas():
    """Índice de áreas (site/areas/index.html) com cards que levam a cada área."""
    cards = ""
    for a in AREAS:
        if not a["disciplinas"]:
            continue
        n_conc = len({o["concurso_id"] for d in a["disciplinas"] for o in d["ocorrencias"]})
        cards += f"""
      <a class="card area-card" href="{a['id']}.html" style="--accent:{a['cor']}">
        <div class="card-icon">{a['icone']}</div>
        <div class="card-body">
          <h3>{e(a['nome'])}</h3>
          <p>{e(a['descricao'])}</p>
          <div class="card-meta"><span>{len(a['disciplinas'])} disciplinas</span><span>{n_conc} concursos</span></div>
        </div>
      </a>"""
    doc = head("Áreas de Conhecimento — Guia de Estudos", 1)
    doc += topbar(1)
    doc += f"""
<main>
  <nav class="crumbs"><a href="../index.html">Início</a> › <span>Áreas de Conhecimento</span></nav>
  <section class="hero">
    <p class="eyebrow">Estudo temático</p>
    <h1>🧭 Áreas de Conhecimento</h1>
    <p class="lead">Estude por área, reunindo as disciplinas equivalentes de todos os concursos
    em um só lugar. Cada disciplina aponta para o concurso onde você quer aprofundá-la.</p>
  </section>
  <section class="group"><div class="grid">{cards}</div></section>
</main>"""
    doc += foot(1, "Áreas de Conhecimento — material de estudo de apoio.")
    open(os.path.join(SITE, "areas", "index.html"), "w", encoding="utf-8").write(doc)


def build_area(a):
    """Página de uma área (site/areas/<id>.html): disciplinas e onde estudá-las."""
    blocos = ""
    for d in a["disciplinas"]:
        chips = "".join(
            f'<a class="area-chip" href="../{o["concurso_id"]}/disciplinas/{o["slug"]}.html">'
            f'{e(o["orgao"] or o["concurso_nome"])} · {o["n_subtopicos"]} subtópicos</a>'
            for o in d["ocorrencias"])
        blocos += f"""
      <div class="area-disc">
        <div class="ad-head"><span class="ad-icon">{d['icone']}</span><h3>{e(d['titulo'])}</h3></div>
        <div class="area-chips">{chips}</div>
      </div>"""
    doc = head(f"{a['nome']} — Áreas de Conhecimento", 1)
    doc += topbar(1)
    doc += f"""
<main>
  <nav class="crumbs"><a href="../index.html">Início</a> ›
    <a href="index.html">Áreas</a> › <span>{e(a['nome'])}</span></nav>
  <section class="hero">
    <p class="eyebrow">Área de conhecimento</p>
    <h1>{a['icone']} {e(a['nome'])}</h1>
    <p class="lead">{e(a['descricao'])}</p>
  </section>
  <section class="group area-discs">{blocos}</section>
</main>"""
    doc += foot(1, "Áreas de Conhecimento — material de estudo de apoio.")
    open(os.path.join(SITE, "areas", f"{a['id']}.html"), "w", encoding="utf-8").write(doc)


def copy_assets():
    """Copia os assets de fonte (assets/) para site/assets/ e grava .nojekyll."""
    dst = os.path.join(SITE, "assets")
    os.makedirs(dst, exist_ok=True)
    for f in glob.glob(os.path.join(ASSETS_SRC, "*")):
        if os.path.isfile(f):
            shutil.copy2(f, dst)
    open(os.path.join(SITE, ".nojekyll"), "w").close()


def validar():
    """Falha alto se algum subtópico visível não resolver conteúdo (ex.: reuso quebrado)."""
    erros = []
    for c in CONCURSOS:
        if c.get("oculto"):
            continue
        for d in c["disciplinas"]:
            for t in d["topicos"]:
                for s in t["subtopicos"]:
                    item, _ = get_content(c["id"], d["slug"], s)
                    if item is None:
                        alvo = tuple(s["reuse"]) if "reuse" in s else (c["id"], d["slug"], s.get("sid"))
                        erros.append(f"{c['id']}/{d['slug']}/{s.get('sid')} -> {alvo}")
    if erros:
        raise SystemExit("ERRO: subtópicos sem conteúdo (reuso quebrado?):\n  " + "\n  ".join(erros))


def build_sitemap():
    """Gera sitemap.xml (todas as páginas) e robots.txt apontando para ele."""
    urls = []
    for f in sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(f, SITE).replace(os.sep, "/")
        if rel == "index.html":
            loc = SITE_URL + "/"
        elif rel.endswith("/index.html"):
            loc = f"{SITE_URL}/{rel[:-len('index.html')]}"
        else:
            loc = f"{SITE_URL}/{rel}"
        urls.append(loc)
    body = "".join(f"  <url><loc>{e(u)}</loc></url>\n" for u in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}</urlset>\n")
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    return len(urls)


def main():
    os.makedirs(SITE, exist_ok=True)
    validar()
    copy_assets()
    build_landing()
    n_amp = 0
    publicos = [c for c in CONCURSOS if not c.get("oculto")]
    for c in publicos:
        cid = c["id"]
        os.makedirs(os.path.join(SITE, cid, "disciplinas"), exist_ok=True)
        os.makedirs(os.path.join(SITE, cid, "ampliado"), exist_ok=True)
        build_concurso_home(c)
        for i, d in enumerate(c["disciplinas"]):
            build_disciplina(c, d, i)
            n_amp += build_ampliado(c, d)

    # estatísticas (arquivo de dados + página) e áreas de conhecimento
    est = coletar_estatisticas()
    open(os.path.join(SITE, "estatisticas.json"), "w", encoding="utf-8").write(
        json.dumps(est, ensure_ascii=False, indent=2))
    build_estatisticas(est)
    os.makedirs(os.path.join(SITE, "areas"), exist_ok=True)
    build_areas()
    n_areas = 0
    for a in AREAS:
        if a["disciplinas"]:
            build_area(a)
            n_areas += 1

    n_urls = build_sitemap()
    print(f"Gerado: landing + {len(publicos)} concursos visíveis + {n_amp} páginas de aprofundamento "
          f"+ estatísticas + {n_areas} áreas + sitemap ({n_urls} URLs)")


if __name__ == "__main__":
    main()
