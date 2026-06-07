# Tarefa: gerar conteúdo APROFUNDADO (SEDES-DF) — subtópicos novos de um concurso

Contexto: concurso da **Secretaria de Desenvolvimento Social do DF (SEDES-DF)**, com vários
cargos/especialidades (banca estilo Cebraspe — itens certo/errado). Você recebe a lista exata
dos subtópicos NOVOS de UM concurso (cargo) e deve produzir a página de aprofundamento de cada um.

## Entrada
Você receberá o caminho de um arquivo `expandido/_todo/<concurso_id>.json` com:
```json
{ "concurso_id":"...", "concurso_nome":"...",
  "itens":[ {"disc_slug":"...","disc_titulo":"...","ti":0,"si":1,"topico":"...","titulo":"...","texto":"..."} ] }
```
Cada item é um subtópico a aprofundar. Os itens estão agrupados por `disc_slug` (disciplina).

## Saída — UM arquivo JSON por disciplina
Para CADA `disc_slug` distinto presente na lista, crie
`expandido/<concurso_id>/<disc_slug>.json` com ESTE schema EXATO:
```json
{
  "slug": "<disc_slug>",
  "itens": [
    {
      "ti": 0, "si": 1,
      "titulo": "<igual ao titulo do item>",
      "intro": "1 a 3 parágrafos. \\n\\n entre parágrafos.",
      "secoes": [ { "h": "Título da seção", "p": "Parágrafo(s). \\n\\n entre parágrafos." } ],
      "exemplo": "Exemplo prático ou item de prova comentado (estilo Cebraspe).",
      "pontos_chave": ["frase curta 1", "..."],
      "dica_prova": "Como cai e pegadinhas."
    }
  ]
}
```
Regras: inclua um objeto por item daquela disciplina, com `ti`/`si` exatamente como na entrada;
`secoes` 3 a 6; `pontos_chave` 4 a 8; todos os campos não vazios; texto puro (sem HTML); JSON válido.

## Padrão de qualidade (ESFORCE-SE)
- Português, didático, tecnicamente preciso. Use o `topico` e o `texto` do item como escopo.
- Cite leis/normas concretas quando pertinente e com confiança (LOAS 8.742/93, PNAS/2004,
  NOB/SUAS, ECA 8.069/90, LBI 13.146/15, Lei 11.340/06, LC 840/2011-DF, Lei 14.133/21, LGPD,
  MCASP, Lei 4.320/64, LRF, etc.). Em dúvida sobre um número, descreva o instituto sem citá-lo.
- Inclua um exemplo aplicado (cenário do SUAS/assistência social ou item de prova comentado).
- Aponte pegadinhas típicas de prova.

Ao final, confirme quantos itens e quantos arquivos gravou.
