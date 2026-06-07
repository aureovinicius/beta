# Guia de Estudos para Concursos

Plataforma de estudos em **site estático** com explicações de todas as disciplinas e
subtópicos do conteúdo programático de cada concurso, com páginas de aprofundamento e
reaproveitamento de conteúdo entre concursos.

Concursos atuais: **SEFAZ-GO**, **TCU/AUFC-TI** e **SEDES-DF** (15 cargos/especialidades).

No ar: https://aureovinicius.github.io/beta/

## Arquitetura

- **Conteúdo como dado** (YAML), separado da lógica de geração.
- **IDs estáveis (sid)** por subtópico — reuso por ID, não por posição.
- **Geração estática** + deploy automático por GitHub Actions (nada de HTML versionado).

| Caminho | Descrição |
|---|---|
| `dados/*.yaml` | Conteúdo de cada concurso (estrutura: disciplinas, tópicos, subtópicos, reuso) |
| `dados/_grupos.yaml` | Metadados de grupos (ex.: SEDES-DF, que agrupa vários cargos) |
| `expandido/<concurso>/<disciplina>.json` | Conteúdo aprofundado (intro, seções, exemplo, pontos-chave) por subtópico (`sid`) |
| `schema.py` | Validação dos dados (campos, sids únicos, reuso que resolve) |
| `dados.py` | Carrega os YAML, resolve `incluir`, atribui `sid` e valida |
| `idutil.py` | Geração dos IDs estáveis (slug do título) |
| `gerar_site.py` | Gera o site estático em `site/` (não versionado) |
| `assets/` | CSS/JS (fonte; copiados para `site/assets/` no build) |
| `.github/workflows/pages.yml` | CI: build + deploy no GitHub Pages |

## Como rodar

```bash
pip install -r requirements.txt        # PyYAML
python3 gerar_site.py                   # gera site/
python3 -m http.server 8753 --directory site   # http://localhost:8753
```

Editar conteúdo = editar os `dados/*.yaml` (ou os `expandido/*.json`); o build valida e
publica sozinho a cada push na `master`.

> Material de estudo de apoio. Sempre confira o texto oficial dos editais e a legislação citada.
