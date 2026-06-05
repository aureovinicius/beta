# Tarefa: gerar conteúdo APROFUNDADO por subtópico

Contexto: site de estudos para o concurso de **Auditor-Fiscal da Receita Estadual de
Goiás (SEFAZ-GO)**. Cada disciplina tem tópicos; cada tópico tem subtópicos. Hoje cada
subtópico tem só um resumo curto. Sua tarefa é produzir uma **página de aprofundamento**
para CADA subtópico da disciplina que lhe foi atribuída.

## Como obter os dados
1. Leia `conteudo.py` (disciplinas básicas) e `conteudo_especificos.py` (específicas).
2. Localize a disciplina cujo campo `slug` é o que lhe foi indicado.
3. Para CADA tópico (na ordem da lista, índice `ti` começando em 0) e CADA subtópico
   dentro dele (índice `si` começando em 0), gere um item de conteúdo aprofundado.

## Padrão de qualidade (ESFORCE-SE)
- Escreva em **português**, didático, correto e tecnicamente preciso.
- Vá MUITO além do resumo: explique o conceito do zero, destrinche definições,
  apresente classificações, **cite artigos de lei / súmulas / normas quando pertinente**
  (CF/88, CTN, EC 132/2023, CTE-GO Lei 11.651/91, Lei 14.133/21, CPC, etc.).
- Inclua pelo menos um **exemplo prático/aplicado** ou exercício comentado por subtópico,
  com foco no que cai em prova de Auditor-Fiscal.
- Aponte **pegadinhas de prova** e erros comuns.
- NÃO invente números de lei ou jurisprudência que você não tenha confiança; se incerto,
  fale do instituto sem citar o número exato.

## Saída: escreva um arquivo JSON
Crie o arquivo `expandido/<slug>.json` (o diretório `expandido/` já existe) com ESTE
schema EXATO (JSON válido, UTF-8, sem comentários, sem vírgula sobrando):

```json
{
  "slug": "<slug-da-disciplina>",
  "itens": [
    {
      "ti": 0,
      "si": 0,
      "titulo": "<título do subtópico, igual ao do conteudo.py>",
      "intro": "1 a 3 parágrafos introdutórios. Separe parágrafos com \\n\\n.",
      "secoes": [
        { "h": "Título da seção", "p": "Parágrafo(s) explicativos. Use \\n\\n entre parágrafos." }
      ],
      "exemplo": "Exemplo prático ou questão comentada (texto corrido, pode ter \\n\\n).",
      "pontos_chave": ["frase curta 1", "frase curta 2", "..."],
      "dica_prova": "Como o tema é cobrado e quais pegadinhas evitar."
    }
  ]
}
```

Regras do schema:
- `itens` deve conter **um objeto para cada subtópico** da disciplina, na ordem correta,
  com `ti`/`si` corretos (0-based).
- `secoes`: de **3 a 6** seções por subtópico.
- `pontos_chave`: de **4 a 8** itens curtos.
- Todos os campos são obrigatórios e não vazios.
- Use apenas texto puro nos valores (sem HTML). Quebras de parágrafo via `\n\n`.
- Garanta JSON **válido**: aspas duplas, escape correto de aspas internas, sem trailing comma.

Ao final, confirme quantos itens (subtópicos) você gravou.
