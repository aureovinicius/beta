# Guia de Estudos — Auditor-Fiscal da Receita Estadual de Goiás (SEFAZ-GO)

Site estático com explicações didáticas de todas as disciplinas e subtópicos do
**ANEXO II — Conteúdo Programático** do edital.

## Conteúdo

- **15 disciplinas** divididas em Conhecimentos Básicos e Conhecimentos Específicos
- Explicação de cada tópico e subtópico do edital
- Página inicial com busca, índice lateral por disciplina, tema claro/escuro e navegação responsiva

## Estrutura

| Arquivo | Descrição |
|---|---|
| `site/` | Site gerado (abra `site/index.html`) |
| `conteudo.py` | Conteúdo das disciplinas básicas |
| `conteudo_especificos.py` | Conteúdo das disciplinas específicas |
| `gerar_site.py` | Gera o site a partir do conteúdo |

## Como rodar

```bash
# Servir localmente
python3 -m http.server 8753 --directory site
# Acesse http://localhost:8753

# Regenerar o site após editar o conteúdo
python3 gerar_site.py
```

> Material de estudo de apoio. Sempre confira o texto oficial do edital e a legislação citada.
