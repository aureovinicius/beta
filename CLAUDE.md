# Guia de Estudos para Concursos — memória do projeto

Site estático multi-concurso gerado por Python a partir de **dados YAML**. Ver `README.md`
para a arquitetura. Deploy automático por GitHub Actions a cada push na `master`
(o `site/` NÃO é versionado). Conteúdo: `dados/*.yaml` (estrutura) + `expandido/<id>/*.json`
(aprofundamentos, indexados por `sid`).

## Princípios sempre válidos
- **Fontes reais primeiro:** ao gerar/alterar conteúdo com leis, normas, súmulas, CPC etc.,
  os agentes DEVEM conferir na internet (planalto, cpc.org.br, STF/STJ, sites oficiais) e
  sinalizar o que não puderam confirmar. Nunca inventar número de lei/artigo/súmula.
- **Reaproveitar conteúdo** entre concursos via ponteiros `reuse: [concurso, slug, sid]`.
- **Fórmulas em formato matemático** (KaTeX, delimitadores `\( \)` / `\[ \]`; no JSON, barras
  duplicadas `\\(`, `\\dfrac`).
- **Material de prova/gabarito (PDFs, prints) NÃO vai para o git** — `.gitignore` com `/provas/`,
  `/gabaritos/` (âncora `/` para não pegar `dados/provas/`). Já `dados/provas/<id>.yaml`
  (banco de questões) **É versionado**.

---

## FLUXO: trabalhar com um arquivo de PROVA
Quando o usuário fornecer a prova de um concurso (ex.: pasta `provas/`), executar nesta ordem.
Cada etapa abaixo foi validada na prática (SEFAZ-GO/FCC 2026).

### 1. Preparar
- Ignorar no git a pasta da prova: `.gitignore` → `/provas/` (e `/gabaritos/`, `/prova *.../`).
- Extrair o texto: `fitz` (PyMuPDF) → `provas/_prova_texto.txt`. OCR costuma vir com **ruído**
  (símbolos de estatística/matemática e ordem de alternativas podem corromper).
- Mapear seções por disciplina (grep nos cabeçalhos) e numeração das questões.

### 2. Analisar a prova SÓ com o conteúdo do site (subagentes, 1-2 disciplinas cada)
Para cada questão produzir: assunto; `coberto` (sim/parcial/não); `topico_site` que ajudou;
`suficiente` (sim/não); o que `faltou`; o que `adicionar`. Além disso: tópicos NÃO cobrados.
Entregar 4 listas: (a) tópicos que ajudaram, (b) tópicos que não caíram, (c) tópicos
insuficientes, (d) o que adicionar para responder tudo.

### 3. Infra do indicador + banco de questões (uma vez)
- Tópico no YAML ganha campo opcional `prova: [nums]` (questões que caíram nele).
- Banco `dados/provas/<id>.yaml`: `banca`, `titulo`, `questoes: {num: {enunciado, alternativas, [gabarito], [comentario]}}`.
- `dados.py` carrega o banco e anexa `c["prova"]` (normalizar chaves para `str`).
- `gerar_site.py` (`prova_bloco`): badge **"📝 Caiu na prova · Qxx"** / **"○ Não caiu"** por tópico;
  bloco `<details>` "Ver questões desta prova" com enunciado/alternativas; e, por questão,
  `<details>` **"Ver gabarito comentado"** que só revela a letra (`Resposta: X`) + comentário ao abrir.

### 4. Preencher lacunas (conteúdo novo)
- Acrescentar disciplinas/tópicos novos ao `dados/<id>.yaml` (preferir script idempotente que
  injeta tópicos por título e novas disciplinas; marcar `prova:` nelas). Reaproveitar com `reuse`.
- Gerar `expandido/_todo/gap-<slug>.json` (sid, titulo, contexto) só dos subtópicos novos.
- Subagentes (com WEB) **apêndam** os itens ao `expandido/<id>/<slug>.json` existente
  (preservando os itens atuais), no schema `{sid,titulo,intro,secoes,exemplo,pontos_chave,dica_prova}`.
  Validar cada arquivo com `python3 -m json.tool`.

### 5. Aprofundar itens insuficientes
- Subagentes EDITAM itens existentes acrescentando uma seção com **dispositivo legal/súmula exato**
  e/ou **exemplo numérico resolvido passo a passo** — sem remover o que já existe.

### 6. Banco de questões (enunciados)
- Subagente extrai as ~80 questões do OCR para `dados/provas/<id>.yaml` (limpar ruído; resumir
  textos-base longos entre colchetes; NÃO copiar textos inteiros). Conferir cobertura: cada questão
  mapeada a algum tópico via `prova:[nums]` (união deve cobrir todas as questões).

### 7. Gabarito comentado (gabarito OFICIAL do PDF da banca)
- Extrair o PDF do gabarito. **CUIDADO: o PDF tem vários TIPOS** — isolar o Tipo correto
  (ex.: "Tipo de Gabarito: 5" = caderno "Tipo 005") e **validar contra uma amostra conhecida**
  do início (1→C, 2→D…) antes de usar. Pegar a 1ª ocorrência de cada questão na seção do tipo certo.
- Injetar o gabarito oficial no banco (`gabarito: "X"`).
- Comentários: subagentes (1 disciplina cada) gravam **arquivos parciais separados**
  (`dados/provas/_gab/<bloco>.yaml`, só `{num: {comentario}}`) — NUNCA editar o mesmo arquivo em
  paralelo. Justificar pelo conteúdo do site (citar dispositivo/cálculo).
- **Merge:** normalizar chaves para `int` nos dois lados; **validar 80/80 antes de apagar os parciais**.
- Onde o OCR embaralhou alternativas/enunciado (ex.: estatística, tabelas), comentar pelo
  método/conceito e acrescentar a ressalva "(ordem das alternativas pode estar embaralhada no OCR)".

### 8. Regenerar, verificar, publicar
- `python gerar_site.py`; conferir no preview: badges, bloco de questões, gabarito revelando só ao
  clicar, KaTeX sem `.katex-error`. Validar JSON/cobertura. Commit + push (Actions publica sozinho).

## Armadilhas registradas (não repetir)
- Não apagar arquivos intermediários (parciais, _todo) **antes** de validar o merge/uso.
- `git add -A` arrasta lixo (PDFs, prints, `.DS_Store`, htmls soltos) — conferir o stage e
  `git reset HEAD` o que não for do projeto; ajustar `.gitignore`.
- Ao quebrar uma f-string grande no gerador, não fechar `"""` no meio (quebra o HTML seguinte).
- `prova:[nums]` é só no TÓPICO (subtópico não tem o campo); cada questão deve cair em 1 tópico.
