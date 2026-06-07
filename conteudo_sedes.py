# -*- coding: utf-8 -*-
"""
Conteúdo programático — SEDES-DF (Edital com vários cargos).
Modelagem:
  - GRUPO_SEDES: metadados do concurso "guarda-chuva" (exibido como 1 box que expande).
  - BASE_DISCIPLINAS: conteúdo COMUM (Conhecimentos do DF, SUAS, programas) — vive no
    concurso oculto 'sedes-df-base' e é reaproveitado por todos os cargos via 'reuse'.
  - LP_SEDES: Língua Portuguesa, totalmente reaproveitada de SEFAZ/TCU.
  - CARGOS: 15 cargos (3 TDAS + 12 EDAS), cada um = disciplinas comuns (por reuse) + específicas.
"""

SEFAZ = "sefaz-go"
TCU = "tcu-aufc"
BASE = "sedes-df-base"

GRUPO_SEDES = {
    "id": "sedes-df",
    "nome": "SEDES-DF — Desenvolvimento e Assistência Social",
    "orgao": "SEDES-DF",
    "banca": "",
    "ano": "2026",
    "icone": "🟣",
    "cor": "#7b2d8e",
    "descricao": "Concurso da Secretaria de Desenvolvimento Social do DF, com vários cargos e especialidades. "
                 "Conhecimentos gerais comuns a todos e blocos específicos por especialidade.",
}


# =====================================================================
# LÍNGUA PORTUGUESA — estrutura reaproveitada (SEFAZ + 2 itens do TCU)
# =====================================================================
def lp_sedes():
    return {
        "slug": "lingua-portuguesa",
        "titulo": "Língua Portuguesa",
        "grupo": "Conhecimentos Gerais",
        "icone": "📝",
        "resumo": "Interpretação de textos, ortografia, morfossintaxe, coesão e reescrita (comum a todos os cargos).",
        "topicos": [
            {"titulo": "1. Compreensão e interpretação de textos", "explicacao": "Leitura de gêneros variados: tese, argumentos, inferências e tipologia textual.", "subtopicos": [
                {"titulo": "Compreensão x interpretação", "texto": "O que o texto diz x o que se conclui dele.", "reuse": (SEFAZ, "lingua-portuguesa", 0, 0)},
                {"titulo": "Ideia central e secundárias", "texto": "Tópico frasal, tese e sustentação.", "reuse": (SEFAZ, "lingua-portuguesa", 0, 1)},
                {"titulo": "Inferência e pressuposto", "texto": "Implícitos, pressupostos e subentendidos.", "reuse": (SEFAZ, "lingua-portuguesa", 0, 2)},
                {"titulo": "Tipos e gêneros textuais", "texto": "Reconhecimento de tipologia e gêneros.", "reuse": (TCU, "lingua-portuguesa", 0, 3)},
            ]},
            {"titulo": "2. Ortografia, classes de palavras e crase", "explicacao": "Ortografia oficial, classes de palavras e crase.", "subtopicos": [
                {"titulo": "Ortografia e acentuação", "texto": "Regras do Acordo Ortográfico.", "reuse": (SEFAZ, "lingua-portuguesa", 1, 0)},
                {"titulo": "Emprego da crase", "texto": "Preposição 'a' + artigo 'a'.", "reuse": (SEFAZ, "lingua-portuguesa", 1, 1)},
                {"titulo": "Classes de palavras e pronomes", "texto": "Substantivo, verbo, pronomes, advérbios.", "reuse": (SEFAZ, "lingua-portuguesa", 2, 0)},
                {"titulo": "Conjunções e conectores", "texto": "Relações de coordenação e subordinação.", "reuse": (SEFAZ, "lingua-portuguesa", 2, 1)},
            ]},
            {"titulo": "3. Sintaxe do período", "explicacao": "Concordância, regência, colocação, pontuação e relações entre orações.", "subtopicos": [
                {"titulo": "Concordância verbal e nominal", "texto": "Ajuste do verbo e do nome.", "reuse": (SEFAZ, "lingua-portuguesa", 3, 0)},
                {"titulo": "Regência verbal e nominal", "texto": "Complementos com/sem preposição.", "reuse": (SEFAZ, "lingua-portuguesa", 3, 1)},
                {"titulo": "Colocação pronominal", "texto": "Próclise, mesóclise e ênclise.", "reuse": (SEFAZ, "lingua-portuguesa", 3, 2)},
                {"titulo": "Pontuação e período composto", "texto": "Vírgula, coordenação e subordinação.", "reuse": (SEFAZ, "lingua-portuguesa", 4, 0)},
                {"titulo": "Orações coordenadas e subordinadas", "texto": "Relações entre orações.", "reuse": (SEFAZ, "lingua-portuguesa", 4, 1)},
            ]},
            {"titulo": "4. Semântica, coesão e reescrita", "explicacao": "Significação, coesão e reescrita de frases e parágrafos.", "subtopicos": [
                {"titulo": "Coesão e coerência", "texto": "Referenciação, substituição e conectores.", "reuse": (SEFAZ, "lingua-portuguesa", 5, 0)},
                {"titulo": "Significação e figuras de linguagem", "texto": "Sinonímia, polissemia, conotação.", "reuse": (SEFAZ, "lingua-portuguesa", 5, 1)},
                {"titulo": "Reescrita de frases e parágrafos", "texto": "Reorganizar mantendo o sentido.", "reuse": (TCU, "lingua-portuguesa", 3, 2)},
            ]},
        ],
    }


# =====================================================================
# BASE — conteúdo COMUM (conteúdo próprio; gerado pelos agentes)
# =====================================================================
BASE_DISCIPLINAS = [
    {
        "slug": "conhecimentos-df",
        "titulo": "Conhecimentos do DF, Política para Mulheres, Legislação e Primeiros Socorros",
        "grupo": "Conhecimentos Gerais",
        "icone": "🏙️",
        "resumo": "Realidade do DF e RIDE, política para mulheres, Lei Orgânica e LC 840/2011, Maria da Penha e primeiros socorros.",
        "topicos": [
            {"titulo": "1. Realidade do DF e a RIDE", "explicacao": "Aspectos étnicos, sociais, históricos, geográficos, culturais, políticos e econômicos do DF e a Região Integrada de Desenvolvimento (RIDE).", "subtopicos": [
                {"titulo": "Realidade do Distrito Federal", "texto": "Formação, geografia, sociedade e economia do DF."},
                {"titulo": "RIDE (LC 94/1998 e Decreto 7.469/2011)", "texto": "Região integrada de desenvolvimento do DF e entorno."},
            ]},
            {"titulo": "2. Política para mulheres e Lei Maria da Penha", "explicacao": "Plano Distrital de Política para Mulheres e o enfrentamento à violência doméstica (mínimo de 3 questões na prova).", "subtopicos": [
                {"titulo": "Plano Distrital de Política para Mulheres (PDPM)", "texto": "Diretrizes e eixos da política para mulheres no DF."},
                {"titulo": "Lei Maria da Penha (Lei 11.340/2006)", "texto": "Formas de violência, medidas protetivas de urgência e rede de atendimento."},
            ]},
            {"titulo": "3. Lei Orgânica do DF", "explicacao": "Título VI da LODF — Da Ordem Social e do Meio Ambiente.", "subtopicos": [
                {"titulo": "LODF — Ordem Social e Meio Ambiente", "texto": "Direitos sociais, assistência, saúde, educação e meio ambiente na LODF."},
            ]},
            {"titulo": "4. Regime jurídico dos servidores do DF (LC 840/2011)", "explicacao": "Disposições preliminares, deveres, regime disciplinar e processos de apuração de infração disciplinar.", "subtopicos": [
                {"titulo": "Deveres e regime disciplinar", "texto": "Deveres, proibições, penalidades e responsabilidades do servidor."},
                {"titulo": "Processo de apuração de infração disciplinar", "texto": "Sindicância e processo administrativo disciplinar (PAD) na LC 840/2011."},
            ]},
            {"titulo": "5. Legislação distrital específica", "explicacao": "Lei Distrital nº 7.484/2024 aplicável ao certame.", "subtopicos": [
                {"titulo": "Lei Distrital nº 7.484/2024", "texto": "Disposições da norma distrital cobrada no edital."},
            ]},
            {"titulo": "6. Noções de primeiros socorros", "explicacao": "Cuidados iniciais, reconhecimento de urgência/emergência e condutas básicas.", "subtopicos": [
                {"titulo": "Reconhecimento de urgência e acionamento do socorro", "texto": "Avaliação da vítima e acionamento do SAMU/serviço especializado."},
                {"titulo": "Condutas básicas de primeiros socorros", "texto": "Engasgo, sangramento, fratura, queimadura, desmaio, convulsão e intoxicação."},
            ]},
        ],
    },
    {
        "slug": "fundamentos-suas-tdas",
        "titulo": "Fundamentos, Organização e Gestão do SUAS (TDAS)",
        "grupo": "Conhecimentos Específicos Comuns",
        "icone": "🤝",
        "resumo": "PNAS/2004, organização do SUAS, seguranças socioassistenciais e NOB/SUAS — comum às especialidades do TDAS.",
        "topicos": [
            {"titulo": "1. PNAS/2004 e organização da assistência social", "explicacao": "Princípios, diretrizes, objetivos, proteções afiançadas e organização da assistência social.", "subtopicos": [
                {"titulo": "PNAS/2004: princípios, proteções e territorialização", "texto": "Proteção Social Básica e Especial, matricialidade sociofamiliar e descentralização."},
            ]},
            {"titulo": "2. SUAS e seguranças socioassistenciais", "explicacao": "Princípios, diretrizes e organização do SUAS, com foco nas seguranças afiançadas.", "subtopicos": [
                {"titulo": "Seguranças socioassistenciais", "texto": "Acolhida, convívio, renda e autonomia."},
            ]},
            {"titulo": "3. NOB/SUAS (2012)", "explicacao": "Norma Operacional Básica do SUAS: pacto federativo e gestão.", "subtopicos": [
                {"titulo": "Responsabilidades, cofinanciamento e vigilância", "texto": "Responsabilidades dos entes, cofinanciamento, gestão do trabalho e vigilância socioassistencial."},
            ]},
        ],
    },
    {
        "slug": "fundamentos-suas-edas",
        "titulo": "Fundamentos e Marcos Normativos da Assistência Social (EDAS)",
        "grupo": "Conhecimentos Específicos Comuns",
        "icone": "🤝",
        "resumo": "LOAS, PNAS, SUAS, NOB e NOB-RH, tipificação, instâncias de controle social, CadÚnico e MROSC.",
        "topicos": [
            {"titulo": "1. LOAS, PNAS e SUAS", "explicacao": "Marcos estruturantes da assistência social como política pública.", "subtopicos": [
                {"titulo": "Princípios, proteções e seguranças", "texto": "LOAS, PNAS/2004, PSB e PSE, seguranças socioassistenciais."},
                {"titulo": "Matricialidade, territorialização e intersetorialidade", "texto": "Centralidade da família e organização territorial dos serviços."},
            ]},
            {"titulo": "2. Normas operacionais", "explicacao": "NOB/SUAS e NOB-RH/SUAS.", "subtopicos": [
                {"titulo": "NOB/SUAS", "texto": "Responsabilidades dos entes, cofinanciamento e estruturação da rede."},
                {"titulo": "NOB-RH/SUAS (Resolução CNAS 269/2006)", "texto": "Gestão do trabalho e equipes de referência no SUAS."},
            ]},
            {"titulo": "3. Tipificação e controle social", "explicacao": "Tipificação Nacional de Serviços e instâncias de pactuação/deliberação.", "subtopicos": [
                {"titulo": "Tipificação Nacional de Serviços Socioassistenciais", "texto": "Serviços de PSB e de PSE de média e alta complexidade."},
                {"titulo": "Instâncias de pactuação e controle social", "texto": "CIT, CIB, Conselhos e Conferências de Assistência Social."},
            ]},
            {"titulo": "4. Gestão integrada e parcerias", "explicacao": "CadÚnico, gestão integrada de benefícios e parcerias com a sociedade civil.", "subtopicos": [
                {"titulo": "CadÚnico e Protocolo de Gestão Integrada", "texto": "Cadastro Único e integração de serviços, benefícios e transferência de renda."},
                {"titulo": "MROSC (Lei 13.019/2014)", "texto": "Parcerias com OSCs: chamamento público, execução e prestação de contas."},
            ]},
        ],
    },
    {
        "slug": "direitos-vulnerabilidades",
        "titulo": "Direitos, Violações de Direitos e Vulnerabilidades Sociais (EDAS)",
        "grupo": "Conhecimentos Específicos Comuns",
        "icone": "🛡️",
        "resumo": "ECA/SINASE, violência de gênero, pessoa idosa e PCD, população de rua e diversidade étnico-racial.",
        "topicos": [
            {"titulo": "1. Crianças, adolescentes e juventude", "explicacao": "ECA e proteção integral.", "subtopicos": [
                {"titulo": "ECA, convivência familiar, acolhimento e adoção", "texto": "Doutrina da proteção integral; medidas de proteção."},
                {"titulo": "SINASE e violência contra crianças e adolescentes", "texto": "Medidas socioeducativas e enfrentamento à violência."},
            ]},
            {"titulo": "2. Mulheres e violência de gênero", "explicacao": "Enfrentamento à violência doméstica e familiar contra a mulher.", "subtopicos": [
                {"titulo": "Violência de gênero, medidas protetivas e rede", "texto": "Lei Maria da Penha e Política Nacional de Enfrentamento à Violência contra as Mulheres."},
            ]},
            {"titulo": "3. Pessoa idosa e pessoa com deficiência", "explicacao": "Proteção da pessoa idosa e da pessoa com deficiência.", "subtopicos": [
                {"titulo": "Estatuto da Pessoa Idosa e LBI", "texto": "Estatuto da Pessoa Idosa, Política Nacional do Idoso e Lei Brasileira de Inclusão."},
            ]},
            {"titulo": "4. População de rua, pobreza e diversidade", "explicacao": "Desproteção social, população em situação de rua e relações étnico-raciais.", "subtopicos": [
                {"titulo": "População em situação de rua e pobreza", "texto": "Política Nacional para a População em Situação de Rua e exclusão social."},
                {"titulo": "Diversidade, equidade e relações étnico-raciais", "texto": "Diversidade sexual/de gênero, racismo e entendimento do STF sobre homotransfobia."},
            ]},
        ],
    },
    {
        "slug": "programas-beneficios-df",
        "titulo": "Programas, Benefícios e Instrumentos Socioassistenciais do DF",
        "grupo": "Conhecimentos Específicos Comuns",
        "icone": "🎫",
        "resumo": "Cartão Prato Cheio, Cartão Gás, Plano DF Social, Benefícios Eventuais e Restaurante Comunitário (SISAN).",
        "topicos": [
            {"titulo": "1. Transferência de renda e provimento alimentar", "explicacao": "Programas distritais de provimento alimentar e auxílio.", "subtopicos": [
                {"titulo": "Cartão Prato Cheio (Lei 7.009/2021)", "texto": "Provimento alimentar direto em caráter emergencial."},
                {"titulo": "Cartão Gás (Lei 6.938/2021)", "texto": "Auxílio para aquisição de gás de cozinha."},
            ]},
            {"titulo": "2. Planos e benefícios eventuais", "explicacao": "Plano estruturante e benefícios eventuais da assistência social do DF.", "subtopicos": [
                {"titulo": "Plano DF Social (Lei 7.008/2021)", "texto": "Plano de combate à pobreza e à desigualdade no DF."},
                {"titulo": "Benefícios Eventuais (Lei 5.165/2013)", "texto": "Provisões suplementares e provisórias em situações de vulnerabilidade."},
            ]},
            {"titulo": "3. Segurança alimentar e nutricional", "explicacao": "Equipamentos públicos de segurança alimentar.", "subtopicos": [
                {"titulo": "SISAN / Restaurante Comunitário", "texto": "Decreto 33.329/2011: restaurantes comunitários e SISAN."},
            ]},
        ],
    },
]

BASE_MAP = {d["slug"]: d for d in BASE_DISCIPLINAS}


def comp(slug):
    """Inclui uma disciplina-base num cargo, marcando cada subtópico como reaproveitado da base."""
    d = BASE_MAP[slug]
    nd = {k: v for k, v in d.items() if k != "topicos"}
    nd["topicos"] = []
    for ti, t in enumerate(d["topicos"]):
        nt = {k: v for k, v in t.items() if k != "subtopicos"}
        nt["subtopicos"] = [
            {"titulo": s["titulo"], "texto": s["texto"], "reuse": (BASE, slug, ti, si)}
            for si, s in enumerate(t["subtopicos"])
        ]
        nd["topicos"].append(nt)
    return nd


# =====================================================================
# Helpers para disciplinas específicas
# =====================================================================
def S(titulo, texto, reuse=None):
    d = {"titulo": titulo, "texto": texto}
    if reuse:
        d["reuse"] = reuse
    return d


def T(titulo, explicacao, subs):
    return {"titulo": titulo, "explicacao": explicacao, "subtopicos": subs}


def D(slug, titulo, icone, resumo, topicos, grupo="Conhecimentos Específicos"):
    return {"slug": slug, "titulo": titulo, "grupo": grupo, "icone": icone, "resumo": resumo, "topicos": topicos}


def cargo(cid, especialidade, codigo, cargo_nome, icone, descricao, especificas):
    comuns = [lp_sedes(), comp("conhecimentos-df")]
    if cargo_nome == "TDAS":
        comuns += [comp("fundamentos-suas-tdas"), comp("programas-beneficios-df")]
    else:
        comuns += [comp("fundamentos-suas-edas"), comp("direitos-vulnerabilidades"), comp("programas-beneficios-df")]
    return {
        "id": cid,
        "nome": especialidade,
        "orgao": "SEDES-DF",
        "cargo": cargo_nome,
        "especialidade": especialidade,
        "codigo": codigo,
        "banca": "",
        "ano": "2026",
        "icone": icone,
        "cor": GRUPO_SEDES["cor"],
        "descricao": descricao,
        "grupo": GRUPO_SEDES,
        "disciplinas": comuns + especificas,
    }


# =====================================================================
# CARGO TDAS — Técnico em Desenvolvimento e Assistência Social
# =====================================================================
AG = "sedes-tdas-agente-social"

CARGOS = [
    cargo(AG, "Agente Social", "200", "TDAS", "🧑‍🤝‍🧑",
          "Trabalho social no território: CRAS/CREAS, proteção social básica e especial, abordagem de rua e saúde mental.",
          [
        D("rede-territorio", "Rede Socioassistencial e Trabalho no Território", "🗺️",
          "CRAS, CREAS, Unidades de Acolhimento, territorialização e fluxos de referência.", [
            T("1. Rede e território", "Organização da rede e atuação territorial.", [
                S("CRAS, CREAS e Unidades de Acolhimento", "Funcionamento e atribuições dos equipamentos."),
                S("Territorialização e fluxos de referência/contrarreferência", "Diagnóstico socioterritorial e encaminhamentos no SUAS."),
            ]),
        ]),
        D("psb-familias", "Proteção Social Básica e Trabalho com Famílias", "👨‍👩‍👧",
          "PAIF, SCFV e prevenção de vulnerabilidades.", [
            T("1. PSB e famílias", "Serviços e ações da proteção social básica.", [
                S("Serviço de Atendimento Integral à Família (PAIF)", "Trabalho social com famílias na PSB."),
                S("SCFV e prevenção de vulnerabilidades", "Convivência, fortalecimento de vínculos e mobilização comunitária."),
            ]),
        ]),
        D("pse-as", "Proteção Social Especial", "🆘",
          "Risco pessoal e social, CREAS e acolhimento.", [
            T("1. PSE — média e alta complexidade", "Violação de direitos e acompanhamento especializado.", [
                S("Risco, violação de direitos e o CREAS", "Acompanhamento especializado em situações de violação."),
                S("Acolhimento institucional e familiar", "Serviços de acolhimento e continuidade do atendimento."),
            ]),
        ]),
        D("abordagem-rua", "Abordagem Social e População em Situação de Rua", "🛣️",
          "Política Nacional para População em Situação de Rua, Centros POP e construção de vínculo.", [
            T("1. Abordagem social", "Atuação no território com a população de rua.", [
                S("Política Nacional (Decreto 7.053/2009) e Centros POP", "Diretrizes e equipamentos de atendimento."),
                S("Abordagem social: princípios, estratégias e vínculo", "Postura profissional e respeito à autonomia."),
            ]),
        ]),
        D("saude-mental-drogas", "Saúde Mental e Uso de Álcool e Outras Drogas", "🧠",
          "Sofrimento psíquico, redução de danos e rede de atenção psicossocial.", [
            T("1. Saúde mental e redução de danos", "Abordagem humanizada e não estigmatizante.", [
                S("Redução de danos e articulação psicossocial", "Sofrimento psíquico, vulnerabilidade e rede de saúde."),
            ]),
        ]),
    ]),

    cargo("sedes-tdas-cuidador-social", "Cuidador Social", "201", "TDAS", "🫶",
          "Cuidado e acolhimento: rotinas humanizadas, trabalho em equipe e proteção social especial de alta complexidade.",
          [
        D("rede-intersetorialidade", "Rede Socioassistencial e Intersetorialidade", "🔗",
          "Articulação entre CRAS, CREAS e Unidades de Acolhimento e trabalho em rede.", [
            T("1. Rede e território", "Articulação intersetorial e fluxos no SUAS.", [
                S("CRAS, CREAS e Unidades de Acolhimento", "Funcionamento e atribuições dos equipamentos.", (AG, "rede-territorio", 0, 0)),
                S("Territorialização e fluxos de referência/contrarreferência", "Diagnóstico socioterritorial e encaminhamentos.", (AG, "rede-territorio", 0, 1)),
            ]),
        ]),
        D("rotinas-acolhimento", "Rotinas de Acolhimento, Cuidado e Trabalho em Equipe", "🛏️",
          "Resolução CNAS/CONANDA 1/2009, rotinas humanizadas e trabalho interdisciplinar.", [
            T("1. Acolhimento e equipe", "Orientações técnicas e rotinas de cuidado.", [
                S("Orientações de acolhimento (Res. CNAS/CONANDA 1/2009)", "Serviços de acolhimento para crianças e adolescentes e Plano Nacional de Convivência."),
                S("Rotinas humanizadas e trabalho em equipe", "Higiene, alimentação, autonomia, mediação de conflitos e vínculos."),
            ]),
        ]),
        D("pse-alta-complexidade", "Proteção Social Especial de Alta Complexidade", "🏠",
          "Serviços de acolhimento e seus princípios.", [
            T("1. Acolhimento de alta complexidade", "Princípios e organização do acolhimento.", [
                S("Princípios do acolhimento", "Excepcionalidade, provisoriedade e preservação de vínculos."),
            ]),
        ]),
        D("pop-rua-cuidador", "População em Situação de Rua e Acolhimento", "🛣️",
          "Abordagem e acolhimento da população em situação de rua.", [
            T("1. Abordagem e acolhimento", "Atuação com a população de rua.", [
                S("Política Nacional (Decreto 7.053/2009) e acolhimento", "Diretrizes e equipamentos de atendimento.", (AG, "abordagem-rua", 0, 0)),
            ]),
        ]),
        D("saude-mental-cuidador", "Saúde Mental e Redução de Danos", "🧠",
          "Abordagem humanizada em saúde mental.", [
            T("1. Saúde mental", "Sofrimento psíquico e rede psicossocial.", [
                S("Redução de danos e articulação psicossocial", "Abordagem humanizada e rede de saúde.", (AG, "saude-mental-drogas", 0, 0)),
            ]),
        ]),
    ]),

    cargo("sedes-tdas-tec-administrativo", "Técnico Administrativo", "202", "TDAS", "🗂️",
          "Direito constitucional e administrativo (noções), regime dos servidores do DF, atendimento, arquivologia e compras.",
          [
        D("nocoes-dir-constitucional", "Noções de Direito Constitucional", "⚖️",
          "Princípios fundamentais, direitos e garantias e Administração Pública.", [
            T("1. Constituição e direitos", "Base constitucional aplicada ao serviço público.", [
                S("Princípios fundamentais", "Arts. 1º a 4º da CF/88.", (SEFAZ, "direito-constitucional", 0, 1)),
                S("Direitos e garantias fundamentais", "Direitos individuais, coletivos e sociais.", (SEFAZ, "direito-constitucional", 1, 0)),
                S("Organização do Estado e Administração Pública", "Disposições gerais e servidores públicos.", (SEFAZ, "direito-constitucional", 2, 1)),
            ]),
        ]),
        D("nocoes-dir-administrativo", "Noções de Direito Administrativo e Legislação", "🏛️",
          "Estado e administração, atos, poderes e regime dos servidores do DF.", [
            T("1. Fundamentos e atos", "Conceitos centrais do Direito Administrativo.", [
                S("Estado, governo e administração pública", "Conceitos e princípios.", (SEFAZ, "direito-administrativo", 0, 0)),
                S("Ato administrativo", "Conceito, requisitos, atributos e extinção.", (SEFAZ, "direito-administrativo", 2, 0)),
                S("Poderes da Administração", "Hierárquico, disciplinar, regulamentar e de polícia.", (SEFAZ, "direito-administrativo", 3, 1)),
                S("Regime dos servidores do DF (LC 840/2011)", "Deveres, regime disciplinar e PAD.", (BASE, "conhecimentos-df", 3, 0)),
            ]),
        ]),
        D("atendimento-arquivologia", "Atendimento, Rotinas Administrativas e Arquivologia", "📇",
          "Atendimento ao público, redação oficial, arquivologia e protocolo.", [
            T("1. Atendimento e documentos", "Qualidade no atendimento e gestão documental.", [
                S("Qualidade no atendimento e redação oficial", "Atendimento ao público e comunicações administrativas.", (SEFAZ, "lingua-portuguesa", 6, 0)),
                S("Arquivologia e protocolo", "Tipos de arquivo, métodos de arquivamento, protocolo e digitalização."),
            ]),
        ]),
        D("recursos-materiais-compras", "Recursos Materiais, Patrimônio e Compras", "📦",
          "Administração de materiais, gestão patrimonial e noções de licitação.", [
            T("1. Materiais e compras", "Gestão de materiais, patrimônio e compras públicas.", [
                S("Administração de materiais e patrimônio", "Estoques, armazenagem, tombamento e inventário.", (TCU, "administracao-publica", 4, 0)),
                S("Noções de licitação (Lei 14.133/2021)", "Etapas do processo e modalidades.", (SEFAZ, "direito-administrativo", 5, 0)),
            ]),
        ]),
    ]),
]


# =====================================================================
# CARGO EDAS — Especialista em Desenvolvimento e Assistência Social
# =====================================================================
CARGOS += [
    cargo("sedes-edas-administracao", "Administração", "400", "EDAS", "📊",
          "Teoria administrativa, OS&M e qualidade, projetos, AFO, gestão de pessoas e ética no serviço público.", [
        D("teoria-adm", "Teoria Geral e Processos Administrativos", "📊", "Evolução da administração, funções e planejamento estratégico.", [
            T("1. Teoria e funções", "Pensamento administrativo e planejamento.", [
                S("Evolução do pensamento administrativo", "Da administração na sociedade contemporânea.", (TCU, "administracao-publica", 0, 0)),
                S("Funções administrativas (PODC)", "Planejar, organizar, dirigir e controlar.", (TCU, "administracao-publica", 1, 0)),
                S("Planejamento estratégico (SWOT, APO, BSC)", "Missão, visão, Balanced Scorecard e processo decisório."),
            ]),
        ]),
        D("osm-qualidade", "Organização, Sistemas, Métodos e Qualidade", "🧭", "Arquitetura organizacional e gestão da qualidade.", [
            T("1. OS&M e qualidade", "Processos e qualidade na gestão.", [
                S("Arquitetura organizacional e mapeamento de processos", "Organogramas, fluxogramas e distribuição do trabalho.", (TCU, "administracao-publica", 3, 0)),
                S("Gestão da qualidade e modelos de excelência", "Ferramentas da qualidade e excelência na gestão pública."),
            ]),
        ]),
        D("gestao-projetos-adm", "Gestão de Projetos", "📁", "Elaboração, etapas e modelos de gestão de projetos.", [
            T("1. Projetos", "Ciclo e modelos de gestão.", [
                S("Projetos e modelos de gestão", "Etapas, análise e avaliação de projetos.", (TCU, "administracao-publica", 3, 1)),
            ]),
        ]),
        D("afo-administracao", "Administração Financeira e Orçamentária (AFO)", "💰", "Orçamento, receita, despesa e execução no DF.", [
            T("1. Orçamento e execução", "Processo orçamentário e execução financeira.", [
                S("Orçamento público (PPA, LDO, LOA)", "Princípios e leis orçamentárias.", (SEFAZ, "direito-financeiro", 0, 0)),
                S("Receita pública", "Categorias, fontes, estágios e dívida ativa.", (SEFAZ, "direito-financeiro", 1, 0)),
                S("Despesa pública", "Categorias e estágios da despesa.", (SEFAZ, "direito-financeiro", 2, 0)),
                S("SIAFEM-DF e execução financeira", "Sistemas de planejamento, orçamento e execução no DF."),
            ]),
        ]),
        D("gestao-pessoas-adm", "Gestão de Pessoas", "👥", "Comportamento organizacional e subsistemas de RH.", [
            T("1. Gestão de pessoas", "Pessoas nas organizações públicas.", [
                S("Comportamento organizacional", "Motivação, liderança e conflitos.", (TCU, "administracao-publica", 2, 0)),
                S("Recrutamento, desempenho e competências", "Seleção, gestão de desempenho e por competências; tendências no setor público."),
            ]),
        ]),
        D("etica-servico-publico", "Ética e Conduta Profissional", "⚖️", "Ética no serviço público.", [
            T("1. Ética", "Conduta no serviço público.", [
                S("Ética e conduta no serviço público", "Comportamento profissional e organização do trabalho."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-contabeis", "Ciências Contábeis", "401", "EDAS", "🧾",
          "Contabilidade geral e societária, análise de balanços, CASP, AFO e auditoria.", [
        D("contab-geral-soc", "Contabilidade Geral e Societária", "🧾", "Estrutura conceitual, patrimônio e evidenciação.", [
            T("1. Estrutura e patrimônio", "Fundamentos da contabilidade.", [
                S("Estrutura conceitual da contabilidade", "Características qualitativas e normas.", (SEFAZ, "contabilidade-geral", 0, 0)),
                S("Patrimônio: ativo, passivo e PL", "Equação patrimonial.", (SEFAZ, "contabilidade-geral", 0, 1)),
                S("Mensuração, avaliação e evidenciação", "Conceito de lucro; mensuração de ativo/passivo e evidenciação contábil."),
            ]),
        ]),
        D("afo-analise-balancos", "Administração Financeira e Análise de Balanços", "📈", "Liquidez e capital de giro.", [
            T("1. Análise e capital de giro", "Análise financeira.", [
                S("Análise de balanços e liquidez", "Indicadores de liquidez e desempenho.", (SEFAZ, "contabilidade-geral", 5, 0)),
                S("Capital de giro, caixa e risco x rentabilidade", "Equilíbrio financeiro e necessidade de capital de giro."),
            ]),
        ]),
        D("casp", "Contabilidade Aplicada ao Setor Público (CASP)", "🏛️", "MCASP, PCASP, DCASP e NBC TSP.", [
            T("1. CASP", "Contabilidade pública.", [
                S("MCASP e PCASP", "Manual e plano de contas aplicados ao setor público."),
                S("DCASP, NBC TSP e PCO/PCP", "Demonstrações, normas e procedimentos orçamentários e patrimoniais."),
            ]),
        ]),
        D("orcamento-afo-contab", "Orçamento Público / AFO", "💰", "Lei 4.320, LRF, PPA/LDO/LOA e execução.", [
            T("1. Orçamento", "Normas e execução orçamentária.", [
                S("Lei 4.320/1964 e LRF", "Normas gerais e responsabilidade fiscal.", (SEFAZ, "direito-financeiro", 5, 0)),
                S("PPA, LDO e LOA", "Leis orçamentárias.", (SEFAZ, "direito-financeiro", 0, 0)),
                S("Execução: estágios e créditos adicionais", "Estágios da receita/despesa e créditos.", (SEFAZ, "direito-financeiro", 3, 0)),
            ]),
        ]),
        D("auditoria-contab", "Auditoria Contábil e Governamental", "🔍", "Controles internos, papéis de trabalho e auditoria por ciclos.", [
            T("1. Auditoria", "Auditoria aplicada.", [
                S("Controles internos e papéis de trabalho", "Planejamento, execução e avaliação.", (SEFAZ, "auditoria", 2, 0)),
                S("Auditoria por ciclos", "Receitas, compras, estoques, caixa, ativos e passivos."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-comunicacao", "Comunicação Social", "402", "EDAS", "📡",
          "Teorias da comunicação, comunicação organizacional, assessoria, gestão de crise, digital e ética.", [
        D("fund-comunicacao", "Fundamentos e Teorias da Comunicação", "📡", "Processos e teorias da comunicação.", [
            T("1. Teorias", "Bases da comunicação.", [
                S("Processos e teorias da comunicação", "Escolas, correntes sociológicas e pensadores."),
                S("O comunicador na sociedade de massas", "Dimensão política e cultural da comunicação."),
            ]),
        ]),
        D("comunicacao-organizacional", "Comunicação Organizacional e Relações Públicas", "🏢", "Planejamento, públicos e pesquisa.", [
            T("1. Comunicação organizacional", "Públicos e RP.", [
                S("Planejamento estratégico e públicos", "Públicos internos/externos e comunicação dirigida."),
                S("Pesquisa de opinião e responsabilidade social", "Métodos quali/quanti, grupos focais e cidadania."),
            ]),
        ]),
        D("jornalismo-crise", "Jornalismo, Assessoria de Imprensa e Gestão de Crise", "📰", "Assessoria, release e gestão de crise.", [
            T("1. Assessoria e crise", "Relacionamento com a mídia.", [
                S("Assessoria de imprensa e produção de conteúdo", "Release, press-kit, entrevistas e media training."),
                S("Gestão de crise de imagem no setor público", "Comunicação de risco e clipping."),
            ]),
        ]),
        D("comunicacao-digital", "Comunicação Digital e Novas Tecnologias", "📱", "Mídias sociais, web e métricas.", [
            T("1. Digital", "Comunicação em rede.", [
                S("Mídias sociais, web e métricas", "Cibercultura, redes institucionais, conteúdo e monitoramento."),
            ]),
        ]),
        D("etica-comunicacao", "Ética Profissional", "⚖️", "Códigos de ética em comunicação.", [
            T("1. Ética", "Deontologia da comunicação.", [
                S("Códigos de ética (Jornalismo e RP)", "Moral, ética, deontologia e comunicação pública."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-direito", "Direito e Legislação", "403", "EDAS", "⚖️",
          "Direito civil, processual civil, constitucional, administrativo, financeiro, LGPD e LAI.", [
        D("direito-civil", "Direito Civil", "📜", "LINDB, pessoas, bens, obrigações, contratos e responsabilidade civil.", [
            T("1. LINDB, pessoas e bens", "Parte geral do Direito Civil.", [
                S("LINDB", "Vigência, integração e interpretação das normas.", (SEFAZ, "direito-civil-empresarial", 0, 0)),
                S("Pessoas", "Personalidade, capacidade e pessoa jurídica.", (SEFAZ, "direito-civil-empresarial", 1, 0)),
                S("Bens", "Classificação geral dos bens.", (SEFAZ, "direito-civil-empresarial", 1, 1)),
            ]),
            T("2. Fatos, obrigações e contratos", "Negócios, obrigações e contratos.", [
                S("Negócio jurídico e defeitos", "Planos e defeitos do negócio jurídico.", (SEFAZ, "direito-civil-empresarial", 2, 0)),
                S("Prescrição e decadência", "Distinção e prazos.", (SEFAZ, "direito-civil-empresarial", 2, 1)),
                S("Obrigações", "Modalidades, transmissão e adimplemento.", (SEFAZ, "direito-civil-empresarial", 3, 0)),
                S("Contratos", "Princípios, formação e espécies.", (SEFAZ, "direito-civil-empresarial", 4, 0)),
                S("Responsabilidade civil", "Subjetiva/objetiva, nexo e dano.", (SEFAZ, "direito-civil-empresarial", 3, 1)),
            ]),
        ]),
        D("direito-processual-civil", "Direito Processual Civil", "⚖️", "Jurisdição, ação, tutela provisória e procedimento comum.", [
            T("1. Processo civil", "Teoria e procedimento.", [
                S("Jurisdição, ação e pressupostos processuais", "Normas processuais, sujeitos do processo e litisconsórcio."),
                S("Tutela provisória e procedimento comum", "Tutela de urgência/evidência; petição inicial, contestação e saneamento."),
            ]),
        ]),
        D("direito-constitucional", "Direito Constitucional", "🏛️", "Constituição, direitos, Poderes e controle de constitucionalidade.", [
            T("1. Constituição e direitos", "Teoria e direitos fundamentais.", [
                S("Constituição e aplicabilidade das normas", "Conceito, classificações e eficácia.", (SEFAZ, "direito-constitucional", 0, 0)),
                S("Princípios fundamentais", "Arts. 1º a 4º.", (SEFAZ, "direito-constitucional", 0, 1)),
                S("Direitos e garantias fundamentais", "Individuais, coletivos e sociais.", (SEFAZ, "direito-constitucional", 1, 0)),
            ]),
            T("2. Estado, Poderes e controle", "Organização e controle.", [
                S("Organização do Estado", "Federação e competências.", (SEFAZ, "direito-constitucional", 2, 0)),
                S("Administração Pública na Constituição", "Arts. 37 a 41.", (SEFAZ, "direito-constitucional", 2, 1)),
                S("Organização dos Poderes", "Legislativo, Executivo e Judiciário.", (SEFAZ, "direito-constitucional", 3, 0)),
                S("Controle de constitucionalidade", "Difuso e concentrado.", (TCU, "direito-constitucional", 3, 1)),
            ]),
        ]),
        D("direito-administrativo", "Direito Administrativo", "🏢", "Atos, poderes, controle, improbidade, processo e licitações.", [
            T("1. Atos, poderes e princípios", "Fundamentos.", [
                S("Estado, governo e princípios", "Conceitos e princípios.", (SEFAZ, "direito-administrativo", 0, 0)),
                S("Atos administrativos", "Requisitos, atributos e extinção.", (SEFAZ, "direito-administrativo", 2, 0)),
                S("Poderes administrativos", "Hierárquico, disciplinar e de polícia.", (SEFAZ, "direito-administrativo", 3, 1)),
            ]),
            T("2. Controle, improbidade e contratos", "Controle e contratações.", [
                S("Controle da Administração e Tribunais de Contas", "Controle interno, externo e jurisdicional.", (TCU, "direito-administrativo", 7, 0)),
                S("Processo administrativo (Lei 9.784/1999)", "Princípios, fases e prazos.", (TCU, "direito-administrativo", 7, 2)),
                S("Improbidade administrativa (Lei 8.429/1992)", "Modalidades e sanções.", (SEFAZ, "direito-administrativo", 6, 1)),
                S("Licitações e contratos (Lei 14.133/2021)", "Modalidades e fases.", (SEFAZ, "direito-administrativo", 5, 0)),
                S("MROSC (Lei 13.019/2014)", "Parcerias com OSCs.", (BASE, "fundamentos-suas-edas", 3, 1)),
            ]),
        ]),
        D("direito-financeiro", "Direito Financeiro", "💰", "Finanças públicas, orçamento, Lei 4.320 e LRF.", [
            T("1. Finanças e orçamento", "Direito financeiro.", [
                S("Finanças públicas e orçamento (PPA/LDO/LOA)", "Orçamento na CF e leis orçamentárias.", (SEFAZ, "direito-financeiro", 0, 0)),
                S("Lei 4.320/1964 e LRF", "Normas gerais e responsabilidade fiscal.", (SEFAZ, "direito-financeiro", 5, 0)),
            ]),
        ]),
        D("transparencia-dados", "Transparência e Proteção de Dados", "🔐", "LGPD e LAI.", [
            T("1. LGPD e LAI", "Dados e transparência.", [
                S("LGPD (Lei 13.709/2018)", "Fundamentos, princípios, direitos dos titulares e tratamento pelo Poder Público."),
                S("LAI (Lei 12.527/2011) e regulamentação no DF", "Acesso à informação e Lei Distrital 4.990/2012."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-economia", "Economia", "404", "EDAS", "📈",
          "Teoria econômica, economia do setor público e economia social (pobreza e desigualdade).", [
        D("teoria-economica", "Teoria Econômica", "📈", "Micro e macroeconomia.", [
            T("1. Micro e equilíbrio", "Mercados e equilíbrio.", [
                S("Oferta, demanda e equilíbrio", "Determinação de preço e quantidade.", (SEFAZ, "economia", 1, 0)),
                S("Elasticidades", "Sensibilidade a preço e renda.", (SEFAZ, "economia", 2, 0)),
                S("Estruturas de mercado e falhas", "Monopólio, concorrência e falhas de mercado.", (SEFAZ, "economia", 4, 0)),
            ]),
            T("2. Microeconomia avançada", "Tópicos avançados.", [
                S("Teoria dos jogos e mercado de fatores", "Interação estratégica e fatores de produção."),
                S("Equilíbrio geral e escolha pública", "Economia do bem-estar e teoria da escolha pública."),
            ]),
        ]),
        D("economia-setor-publico", "Economia do Setor Público", "🏛️", "Despesa pública, tributação e federalismo fiscal.", [
            T("1. Setor público", "Atuação do Estado.", [
                S("Despesa pública, orçamento e gastos", "Teoria da despesa pública e gastos governamentais."),
                S("Tributação e federalismo fiscal", "Teoria da tributação e relações federativas."),
            ]),
        ]),
        D("economia-social", "Economia Social: Pobreza e Desigualdade", "🤲", "Distribuição de renda e combate à pobreza.", [
            T("1. Pobreza e desigualdade", "Desigualdade e políticas.", [
                S("Distribuição de renda e desigualdade", "Concentração de renda e métricas (Gini)."),
                S("Pobreza e políticas no DF", "Pobreza multidimensional e políticas de combate."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-educador-social", "Educador Social", "405", "EDAS", "📚",
          "Política social e família, prática socioeducativa no SUAS, metodologia e diretrizes internacionais.", [
        D("fund-politica-social", "Fundamentos da Política Social e Dinâmica Familiar", "🏛️", "Seguridade social e família contemporânea.", [
            T("1. Política social e família", "Bases da política social.", [
                S("Seguridade social no Brasil", "Conceito, organização e financiamento."),
                S("Família contemporânea e políticas públicas", "Configurações familiares e ciclo de políticas."),
            ]),
        ]),
        D("pratica-socioeducativa", "A Prática Socioeducativa no SUAS", "📚", "Educador na PSB e PSE.", [
            T("1. Educador no SUAS", "Atuação socioeducativa.", [
                S("Educador na Proteção Social Básica (PAIF, SCFV)", "Inserção e papel na PSB."),
                S("Educador na Proteção Social Especial (PAEFI)", "Abordagem social e acolhimento."),
            ]),
        ]),
        D("metodologia-trabalho-social", "Metodologia do Trabalho Social", "🛠️", "Trabalho social e escuta qualificada.", [
            T("1. Metodologia", "Trabalho com famílias e grupos.", [
                S("Trabalho social com famílias e grupos", "Escuta qualificada, vínculos e interdisciplinaridade."),
            ]),
        ]),
        D("temas-diretrizes-internacionais", "Temas Contemporâneos e Diretrizes Internacionais", "🌐", "Drogas, redução de danos e diretrizes da ONU.", [
            T("1. Drogas e diretrizes", "Temas atuais.", [
                S("Drogas, redução de danos e diretrizes internacionais", "Política sobre drogas; Regras de Beijing, RIAD e DUDH."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-estatistica", "Estatística", "406", "EDAS", "📊",
          "Estatística descritiva, probabilidade e inferência, modelagem multivariada e bancos de dados.", [
        D("estatistica-descritiva", "Estatística Descritiva e Análise Exploratória", "📊", "Medidas resumo e indicadores sociais.", [
            T("1. Descritiva", "Resumo de dados.", [
                S("Medidas de posição", "Média, mediana e moda.", (SEFAZ, "raciocinio-logico", 6, 0)),
                S("Medidas de dispersão", "Variância, desvio-padrão e CV.", (SEFAZ, "raciocinio-logico", 6, 1)),
                S("Indicadores, representação e associação", "Números índices, contingência, risco relativo e odds ratio."),
            ]),
        ]),
        D("probabilidade-inferencia", "Probabilidade e Inferência Estatística", "🎲", "Amostragem, testes e inferência bayesiana.", [
            T("1. Inferência", "Estimação e testes.", [
                S("Amostragem e estimação", "Distribuições amostrais, TLC e intervalos de confiança.", (SEFAZ, "raciocinio-logico", 6, 3)),
                S("Testes de hipóteses e qui-quadrado", "Testes para médias/variâncias e qui-quadrado."),
                S("Inferência bayesiana e não paramétricos", "Probabilidade subjetiva e testes não paramétricos."),
            ]),
        ]),
        D("modelagem-multivariada", "Modelagem Estatística e Análise Multivariada", "📐", "Regressão, ANOVA e multivariada.", [
            T("1. Modelagem", "Modelos estatísticos.", [
                S("Regressão e correlação", "Linear simples/múltipla e logística."),
                S("ANOVA e análise multivariada", "PCA, fatorial, cluster e equações estruturais."),
            ]),
        ]),
        D("bancos-dados-estat", "Gestão e Exploração de Bancos de Dados", "🗄️", "Modelagem, SQL e multidimensional.", [
            T("1. Bancos de dados", "Dados para análise.", [
                S("Modelo ER e relacional", "Projeto conceitual, lógico e físico.", (SEFAZ, "tecnologia-da-informacao", 0, 0)),
                S("SQL", "Definição e manipulação de dados.", (SEFAZ, "tecnologia-da-informacao", 0, 1)),
                S("Bancos multidimensionais", "OLAP e apoio à análise estatística.", (SEFAZ, "tecnologia-da-informacao", 2, 0)),
            ]),
        ]),
    ]),

    cargo("sedes-edas-nutricao", "Nutrição", "407", "EDAS", "🥗",
          "Segurança alimentar, nutrição em saúde pública, gestão de UAN, EAN e dietoterapia.", [
        D("san-politicas", "Segurança Alimentar e Nutricional e Políticas Públicas", "🍲", "DHAA, SISAN, PNAN e equipamentos públicos.", [
            T("1. SAN", "Segurança alimentar.", [
                S("DHAA, soberania e SISAN", "Direito humano à alimentação e sistema de SAN."),
                S("PNAN e equipamentos públicos", "Política de alimentação e restaurantes comunitários."),
            ]),
        ]),
        D("nutricao-saude-publica", "Nutrição em Saúde Pública e Epidemiologia", "🩺", "Epidemiologia nutricional e ciclos da vida.", [
            T("1. Saúde pública", "Nutrição populacional.", [
                S("Epidemiologia nutricional", "Desnutrição, obesidade e anemia em vulneráveis."),
                S("Nutrição nos ciclos da vida", "Gestação, infância, idoso e aleitamento materno."),
            ]),
        ]),
        D("gestao-uan", "Gestão de Unidades de Alimentação e Nutrição (UAN)", "🍽️", "Administração de UAN e controle sanitário.", [
            T("1. UAN", "Gestão de serviços de alimentação.", [
                S("Administração de UAN", "Planejamento, organização e controle."),
                S("Higiene e controle sanitário (BPF)", "Contaminação, toxinfecções e boas práticas."),
            ]),
        ]),
        D("ean-programas", "Educação Alimentar e Programas Institucionais", "🎓", "EAN e PNAE.", [
            T("1. EAN", "Educação alimentar.", [
                S("Educação alimentar e PNAE", "Estratégias educativas e alimentação escolar."),
            ]),
        ]),
        D("dietoterapia", "Fundamentos de Nutrição e Dietoterapia Básica", "🥦", "Nutrição básica e DCNTs.", [
            T("1. Nutrição básica", "Nutrientes e dietoterapia.", [
                S("Nutrição básica e DCNTs", "Macro/micronutrientes e dietoterapia (diabetes, hipertensão, obesidade)."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-pedagogia", "Pedagogia", "408", "EDAS", "📚",
          "Pedagogia social, direito educacional, pedagogo no SUAS e intervenção em vulnerabilidade.", [
        D("fund-pedagogia-social", "Fundamentos da Educação e Pedagogia Social", "📚", "Concepções de educação e pedagogia social.", [
            T("1. Fundamentos", "Bases da educação.", [
                S("Concepções de educação e educação popular", "Abordagens críticas e emancipatórias."),
                S("Educação formal, não formal e pedagogo não escolar", "Atuação social do pedagogo."),
            ]),
        ]),
        D("direito-educacional", "Direito Educacional", "⚖️", "Educação na CF e LDB.", [
            T("1. Direito educacional", "Marco legal da educação.", [
                S("Educação na CF e LDB", "Princípios e gestão democrática (Lei 9.394/1996)."),
            ]),
        ]),
        D("pedagogo-suas", "O Pedagogo no SUAS", "🤝", "Atuação e planejamento socioeducativo.", [
            T("1. Atuação no SUAS", "Dimensão pedagógica.", [
                S("Dimensão pedagógica no SUAS", "Atuação em CRAS/CREAS e planejamento socioeducativo."),
                S("Metodologias participativas e território", "Oficinas, grupos e fortalecimento de vínculos."),
            ]),
        ]),
        D("intervencao-pedagogica", "Intervenção Pedagógica em Vulnerabilidade", "🛡️", "Violências e direitos humanos.", [
            T("1. Intervenção", "Atuação em contextos de risco.", [
                S("Violências, direitos humanos e cidadania", "Prevenção de violências e educação em direitos humanos (Res. CNE/CP 1/2012)."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-psicologia", "Psicologia", "409", "EDAS", "🧠",
          "Psicologia social, prática psicossocial no SUAS, avaliação e ética profissional.", [
        D("fund-psicologia-social", "Fundamentos da Psicologia e Psicologia Social", "🧠", "Abordagens teóricas e psicologia social.", [
            T("1. Fundamentos", "Bases da psicologia.", [
                S("Abordagens teóricas da Psicologia", "Psicanálise, TCC, humanista e sócio-histórica."),
                S("Psicologia social crítica e desenvolvimento", "Compromisso social e psicologia do desenvolvimento."),
            ]),
        ]),
        D("pratica-psicossocial-suas", "A Prática Psicossocial no SUAS", "🤝", "Atuação do psicólogo no SUAS.", [
            T("1. Prática no SUAS", "Atuação psicossocial.", [
                S("Atuação nas equipes (CRAS, CREAS, Pop)", "Dimensão socioeducativa do psicólogo."),
                S("Escuta qualificada em violações de direitos", "Intervenção psicossocial e matricialidade familiar."),
            ]),
        ]),
        D("avaliacao-instrumentos-psi", "Avaliação e Instrumentos Técnico-Operativos", "📋", "Avaliação psicológica e técnicas.", [
            T("1. Avaliação", "Instrumentos.", [
                S("Avaliação psicológica e técnicas", "Entrevista, anamnese, observação e visita domiciliar."),
            ]),
        ]),
        D("etica-documentos-psi", "Ética Profissional e Documentos", "⚖️", "Código de ética e documentos psicológicos.", [
            T("1. Ética", "Ética e documentos.", [
                S("Código de ética e documentos psicológicos", "Sigilo e documentos (relatórios, laudos) do CFP."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-servico-social", "Serviço Social", "410", "EDAS", "📖",
          "Fundamentos histórico-metodológicos, ética profissional, dimensão técnico-operativa e políticas sociais.", [
        D("fund-servico-social", "Fundamentos Históricos e Teórico-Metodológicos", "📖", "Constituição da profissão e questão social.", [
            T("1. Fundamentos", "História e teoria.", [
                S("Constituição da profissão e questão social", "Significado social e expressões da questão social."),
                S("Perspectivas teórico-metodológicas", "Conservadorismo, reconceituação e crítico-dialética."),
            ]),
        ]),
        D("etica-servico-social", "Ética e Legislação Profissional", "⚖️", "Projeto ético-político e código de ética.", [
            T("1. Ética", "Ética profissional.", [
                S("Projeto ético-político e Lei 8.662/1993", "Regulamentação da profissão."),
                S("Código de Ética e sigilo (CFESS)", "Princípios, direitos e deveres."),
            ]),
        ]),
        D("tecnico-operativo-ss", "Dimensão Técnico-Operativa e Pesquisa Social", "🛠️", "Instrumentos e pesquisa social.", [
            T("1. Instrumentos", "Práxis profissional.", [
                S("Instrumentos (entrevista, visita, estudo social)", "Técnicas de intervenção do Serviço Social."),
                S("Documentos técnicos e pesquisa social", "Relatórios, laudos e pesquisa quali/quanti."),
            ]),
        ]),
        D("estado-politicas-ss", "Estado, Políticas Sociais, Planejamento e Gestão", "🏛️", "Políticas sociais e seguridade.", [
            T("1. Políticas sociais", "Estado e políticas.", [
                S("Políticas sociais e Welfare State", "Paradigmas e crise do Estado de Bem-Estar."),
                S("Seguridade social, orçamento e controle social", "Seguridade na CF/88, PPA/LDO/LOA e conselhos."),
            ]),
        ]),
    ]),

    cargo("sedes-edas-sociologia", "Sociologia", "411", "EDAS", "🌐",
          "Teoria sociológica, relações étnico-raciais, sociologia urbana e metodologia de pesquisa social.", [
        D("teoria-sociologica", "Teoria Sociológica e Conceitos Fundamentais", "📚", "Clássicos e contemporâneos.", [
            T("1. Teoria", "Pensadores.", [
                S("Clássicos: Marx, Durkheim e Weber", "Fundadores da sociologia."),
                S("Contemporâneos: Bourdieu, Bauman, Foucault e Butler", "Habitus, modernidade líquida, poder e gênero."),
            ]),
        ]),
        D("pensamento-social-etnico", "Pensamento Social e Relações Étnico-Raciais", "✊", "Formação brasileira e decolonialidade.", [
            T("1. Brasil e decolonialidade", "Raça e sociedade.", [
                S("Formação brasileira e decolonialidade", "Fanon e epistemologias do Sul."),
                S("Racismo estrutural e interseccionalidade", "Mito da democracia racial; raça, classe e gênero."),
            ]),
        ]),
        D("sociologia-urbana", "Sociologia Urbana, Desigualdades e Movimentos Sociais", "🏙️", "Cidade, violência e movimentos sociais.", [
            T("1. Urbano e movimentos", "Cidade e ação coletiva.", [
                S("Direito à cidade e violência urbana", "Segregação, gentrificação e criminalização da pobreza."),
                S("Movimentos sociais e controle social", "Ação coletiva e participação cidadã."),
            ]),
        ]),
        D("metodologia-pesquisa-social", "Metodologia de Pesquisa Social e Avaliação", "🔬", "Métodos e indicadores sociais.", [
            T("1. Pesquisa social", "Métodos de pesquisa.", [
                S("Métodos quali/quanti e indicadores sociais", "Etnografia, entrevistas e avaliação de políticas."),
            ]),
        ]),
    ]),
]


# Concurso oculto que detém o conteúdo comum (base de reaproveitamento da SEDES)
BASE_CONCURSO = {
    "id": BASE,
    "nome": "SEDES-DF — Base comum",
    "orgao": "SEDES-DF",
    "cargo": "Base",
    "banca": "",
    "ano": "2026",
    "icone": "🟣",
    "cor": GRUPO_SEDES["cor"],
    "descricao": "Conteúdo comum reaproveitado pelos cargos da SEDES-DF.",
    "oculto": True,
    "disciplinas": BASE_DISCIPLINAS,
}
