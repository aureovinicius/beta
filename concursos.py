# -*- coding: utf-8 -*-
"""Registro de concursos disponíveis no site."""
from conteudo import DISCIPLINAS
from conteudo_especificos import ESPECIFICOS
from conteudo_tcu import TCU
from conteudo_sedes import CARGOS as SEDES_CARGOS, BASE_CONCURSO as SEDES_BASE

CONCURSOS = [
    {
        "id": "sefaz-go",
        "nome": "Auditor-Fiscal da Receita Estadual de Goiás",
        "orgao": "SEFAZ-GO",
        "cargo": "Auditor-Fiscal da Receita Estadual",
        "banca": "FGV",
        "ano": "2025",
        "icone": "🟢",
        "cor": "#1f6f54",
        "descricao": "Tributação estadual (ICMS, ITCD, IPVA), direito, contabilidade e tecnologia da informação.",
        "disciplinas": DISCIPLINAS + ESPECIFICOS,
    },
    {
        "id": "tcu-aufc",
        "nome": "Auditor Federal de Controle Externo — TI",
        "orgao": "TCU",
        "cargo": "Auditor Federal de Controle Externo (AUFC)",
        "banca": "Cebraspe",
        "ano": "2025",
        "icone": "🔵",
        "cor": "#1f4e79",
        "descricao": "Controle externo, auditoria governamental, direito e especialidade em Tecnologia da Informação.",
        "disciplinas": TCU,
    },
    SEDES_BASE,        # concurso oculto (base de reaproveitamento da SEDES)
    *SEDES_CARGOS,     # 15 cargos da SEDES-DF (agrupados na landing)
]

# Atribui IDs estáveis (sid) a todo subtópico — base da resolução de reuso e das URLs.
from idutil import assign_sids

for _c in CONCURSOS:
    for _d in _c["disciplinas"]:
        assign_sids(_d)

CONCURSO_POR_ID = {c["id"]: c for c in CONCURSOS}
