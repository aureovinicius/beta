# Tarefa: gerar conteúdo APROFUNDADO (TCU/AUFC-TI) — apenas subtópicos NOVOS

Contexto: site de estudos para o concurso de **Auditor Federal de Controle Externo (AUFC) —
Tecnologia da Informação, do TCU (banca Cebraspe)**. Cada disciplina tem tópicos e subtópicos.
Alguns subtópicos são reaproveitados de outro concurso (têm a chave `reuse`) e NÃO devem ser
gerados por você. Sua tarefa é produzir a página de aprofundamento para CADA subtópico que
**NÃO** tem a chave `reuse`.

## Como obter os dados
1. Leia `conteudo_tcu.py`. Localize a disciplina cujo `slug` foi indicado a você.
2. Percorra os tópicos (índice `ti`, 0-based) e subtópicos (índice `si`, 0-based).
3. Gere um item APENAS para os subtópicos que **não** possuem a chave `reuse`.

## Padrão de qualidade (ESFORCE-SE)
- Português, didático, tecnicamente preciso, nível de prova Cebraspe (itens certo/errado).
- Explique do zero: definições, classificações, comparações. Para TI, cite tecnologias,
  protocolos, padrões e normas concretas (ex.: RFCs, ISO/IEC 27001, NIST, ITIL v4, COBIT 2019,
  Lei 14.133/21, LGPD, ISSAI/NBASP) quando pertinente e com confiança.
- Inclua um **exemplo prático/aplicado** por subtópico (cenário de auditoria de TI, item de prova
  comentado, ou caso real).
- Aponte **pegadinhas de prova** e confusões comuns (especialmente o estilo Cebraspe).
- NÃO invente números de norma/lei sem confiança; em dúvida, descreva o conceito sem o número.

## Saída: escreva um arquivo JSON
Crie `expandido/tcu-aufc/<slug>.json` com ESTE schema EXATO (JSON válido, UTF-8, sem comentários,
sem vírgula sobrando):

```json
{
  "slug": "<slug-da-disciplina>",
  "itens": [
    {
      "ti": 0,
      "si": 1,
      "titulo": "<título do subtópico, igual ao do conteudo_tcu.py>",
      "intro": "1 a 3 parágrafos. Separe parágrafos com \\n\\n.",
      "secoes": [ { "h": "Título da seção", "p": "Parágrafo(s). \\n\\n entre parágrafos." } ],
      "exemplo": "Exemplo prático ou item de prova comentado.",
      "pontos_chave": ["frase curta 1", "frase curta 2", "..."],
      "dica_prova": "Como o tema cai (Cebraspe) e pegadinhas."
    }
  ]
}
```

Regras do schema:
- Inclua um objeto para **cada subtópico SEM `reuse`**, na ordem, com `ti`/`si` corretos (0-based).
  Os `si` podem não ser contíguos (pule os reaproveitados) — use o índice real do subtópico na lista.
- `secoes`: 3 a 6. `pontos_chave`: 4 a 8. Todos os campos obrigatórios e não vazios.
- Apenas texto puro (sem HTML). Quebras de parágrafo via `\n\n`. JSON válido.

Ao final, confirme quantos itens gravou.
