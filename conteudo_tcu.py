# -*- coding: utf-8 -*-
"""
Conteúdo programático — TCU / Auditor Federal de Controle Externo (AUFC) — TI.
Banca: Cebraspe. Cada subtópico pode ter "reuse": (concurso_id, slug, sid)
apontando, por ID estável, para um aprofundamento já existente em outro concurso.
"""

R = "sefaz-go"  # concurso de origem dos reaproveitamentos

TCU = [
    # ============================ LÍNGUA PORTUGUESA ============================
    {
        "slug": "lingua-portuguesa",
        "titulo": "Língua Portuguesa",
        "grupo": "Conhecimentos Básicos",
        "icone": "📝",
        "resumo": "Interpretação de textos, ortografia, morfossintaxe, coesão e reescrita de frases e parágrafos.",
        "topicos": [
            {
                "titulo": "1. Compreensão e interpretação de textos",
                "explicacao": "Leitura de gêneros variados: identificar tese, argumentos, intenção, relações lógicas e inferências, distinguindo o explícito do implícito.",
                "subtopicos": [
                    {"titulo": "Compreensão x interpretação", "texto": "O que o texto diz x o que se pode concluir dele.", "reuse": (R, "lingua-portuguesa", "compreensao-x-interpretacao")},
                    {"titulo": "Ideia central e secundárias", "texto": "Tópico frasal, tese e ideias de sustentação.", "reuse": (R, "lingua-portuguesa", "ideia-central-e-secundarias")},
                    {"titulo": "Inferência e pressuposto", "texto": "Implícitos, pressupostos e subentendidos.", "reuse": (R, "lingua-portuguesa", "inferencia-e-pressuposto")},
                    {"titulo": "Tipos e gêneros textuais", "texto": "Reconhecimento de tipologia (narração, descrição, dissertação, injunção) e gêneros."},
                ],
            },
            {
                "titulo": "2. Ortografia, classes de palavras e crase",
                "explicacao": "Domínio da ortografia oficial, emprego das classes de palavras e do sinal indicativo de crase.",
                "subtopicos": [
                    {"titulo": "Ortografia e acentuação", "texto": "Regras do Acordo Ortográfico vigente.", "reuse": (R, "lingua-portuguesa", "acentuacao-grafica")},
                    {"titulo": "Emprego da crase", "texto": "Fusão da preposição 'a' com o artigo 'a'.", "reuse": (R, "lingua-portuguesa", "emprego-da-crase")},
                    {"titulo": "Classes de palavras e pronomes", "texto": "Substantivo, adjetivo, verbo, pronomes, advérbios.", "reuse": (R, "lingua-portuguesa", "pronomes")},
                    {"titulo": "Conjunções e conectores", "texto": "Relações lógicas de coordenação e subordinação.", "reuse": (R, "lingua-portuguesa", "conjuncoes")},
                ],
            },
            {
                "titulo": "3. Sintaxe do período",
                "explicacao": "Estrutura morfossintática: concordância, regência, colocação pronominal, pontuação e relações entre orações.",
                "subtopicos": [
                    {"titulo": "Concordância verbal e nominal", "texto": "Ajuste do verbo ao sujeito e do nome a seus determinantes.", "reuse": (R, "lingua-portuguesa", "concordancia-verbal-e-nominal")},
                    {"titulo": "Regência verbal e nominal", "texto": "Complementos com e sem preposição.", "reuse": (R, "lingua-portuguesa", "regencia-verbal-e-nominal")},
                    {"titulo": "Colocação pronominal", "texto": "Próclise, mesóclise e ênclise.", "reuse": (R, "lingua-portuguesa", "colocacao-pronominal")},
                    {"titulo": "Pontuação e período composto", "texto": "Vírgula, ponto e vírgula; coordenação e subordinação.", "reuse": (R, "lingua-portuguesa", "periodo-composto")},
                    {"titulo": "Orações coordenadas e subordinadas", "texto": "Relações entre orações e entre termos da oração.", "reuse": (R, "lingua-portuguesa", "oracoes-adjetivas")},
                ],
            },
            {
                "titulo": "4. Semântica, coesão e reescrita",
                "explicacao": "Significação das palavras, mecanismos de coesão e reescrita de frases e parágrafos preservando o sentido.",
                "subtopicos": [
                    {"titulo": "Coesão e coerência", "texto": "Referenciação, substituição, repetição e conectores.", "reuse": (R, "lingua-portuguesa", "coesao-e-coerencia")},
                    {"titulo": "Significação e figuras de linguagem", "texto": "Sinonímia, polissemia, conotação/denotação.", "reuse": (R, "lingua-portuguesa", "figuras-de-linguagem")},
                    {"titulo": "Reescrita de frases e parágrafos", "texto": "Reorganizar período e trocar palavras/trechos mantendo o sentido — clássico do Cebraspe."},
                ],
            },
        ],
    },

    # ============================== LÍNGUA INGLESA ==============================
    {
        "slug": "lingua-inglesa",
        "titulo": "Língua Inglesa",
        "grupo": "Conhecimentos Básicos",
        "icone": "🌎",
        "resumo": "Compreensão de textos: vocabulário, estrutura, ideias explícitas e implícitas e itens gramaticais.",
        "topicos": [
            {
                "titulo": "1. Compreensão de textos variados",
                "explicacao": "Leitura estratégica em inglês: domínio de vocabulário e estrutura, ideias principais e secundárias, relações intratextuais e intertextuais.",
                "subtopicos": [
                    {"titulo": "Estratégias de leitura (skimming e scanning)", "texto": "Leitura global e localizada para responder sem traduzir tudo."},
                    {"titulo": "Ideias explícitas e implícitas", "texto": "Identificar tese, detalhes e inferências; relações entre textos."},
                ],
            },
            {
                "titulo": "2. Itens gramaticais relevantes",
                "explicacao": "Estruturas gramaticais necessárias para compreender o conteúdo semântico do texto.",
                "subtopicos": [
                    {"titulo": "Gramática aplicada à compreensão", "texto": "Tempos verbais, conectivos, voz passiva, modais e referência."},
                ],
            },
            {
                "titulo": "3. Linguagem contemporânea",
                "explicacao": "Conhecimento e uso das formas contemporâneas da língua inglesa em contextos atuais.",
                "subtopicos": [
                    {"titulo": "Formas contemporâneas do inglês", "texto": "Expressões, vocabulário técnico e registro atual."},
                ],
            },
        ],
    },

    # ============================ RACIOCÍNIO ANALÍTICO ============================
    {
        "slug": "raciocinio-analitico",
        "titulo": "Raciocínio Analítico",
        "grupo": "Conhecimentos Básicos",
        "icone": "🧩",
        "resumo": "Argumentação, senso crítico, tipos de argumentos, falácias e comunicação eficiente de argumentos.",
        "topicos": [
            {
                "titulo": "1. Raciocínio analítico e argumentação",
                "explicacao": "Avaliar e construir argumentos: distinguir argumentos válidos de falaciosos e comunicar raciocínios com clareza e senso crítico.",
                "subtopicos": [
                    {"titulo": "Senso crítico na argumentação", "texto": "Avaliar premissas, evidências e qualidade do raciocínio."},
                    {"titulo": "Validade dos argumentos", "texto": "Quando a conclusão decorre necessariamente das premissas.", "reuse": (R, "raciocinio-logico", "argumentos-validos")},
                    {"titulo": "Argumentos falaciosos e apelativos", "texto": "Falácias formais e informais; apelos à emoção, autoridade e ad hominem."},
                    {"titulo": "Comunicação eficiente de argumentos", "texto": "Estruturar e expor argumentos de forma clara e persuasiva."},
                ],
            },
        ],
    },

    # ============================== CONTROLE EXTERNO ==============================
    {
        "slug": "controle-externo",
        "titulo": "Controle Externo",
        "grupo": "Conhecimentos Básicos",
        "icone": "🏛️",
        "resumo": "Tipos e formas de controle, Tribunais de Contas, controle jurisdicional e improbidade administrativa.",
        "topicos": [
            {
                "titulo": "1. Conceito, tipos e formas de controle",
                "explicacao": "Controle da Administração: interno e externo, prévio/concomitante/posterior, de legalidade/mérito, e seus titulares.",
                "subtopicos": [
                    {"titulo": "Controle interno e externo", "texto": "Quem controla, quando e com que finalidade; sistema de controle interno (art. 74 CF)."},
                    {"titulo": "Controle parlamentar, administrativo e jurisdicional", "texto": "Espécies de controle e o sistema de jurisdição una no Brasil."},
                ],
            },
            {
                "titulo": "2. Tribunais de Contas",
                "explicacao": "O TCU e os TCs dos Estados/DF como órgãos de controle externo, auxiliando o Legislativo (arts. 70 a 75 da CF).",
                "subtopicos": [
                    {"titulo": "TCU, TCEs e TCDF", "texto": "Competências, composição, natureza das decisões e jurisprudência."},
                    {"titulo": "Controle pelos tribunais de contas", "texto": "Julgamento de contas, fiscalização, sustação de atos e contratos."},
                ],
            },
            {
                "titulo": "3. Improbidade e controle da atividade financeira",
                "explicacao": "Responsabilização por improbidade e o controle da atividade financeira do Estado em suas espécies e sistemas.",
                "subtopicos": [
                    {"titulo": "Lei de Improbidade (Lei 8.429/1992)", "texto": "Atos de improbidade e sanções, com as alterações da Lei 14.230/21.", "reuse": (R, "direito-administrativo", "improbidade-administrativa")},
                    {"titulo": "Controle da atividade financeira do Estado", "texto": "Espécies e sistemas de controle das finanças públicas."},
                ],
            },
        ],
    },

    # ============================ ADMINISTRAÇÃO PÚBLICA ============================
    {
        "slug": "administracao-publica",
        "titulo": "Administração Pública (Gestão)",
        "grupo": "Conhecimentos Básicos",
        "icone": "📋",
        "resumo": "Teorias da administração, processo organizacional, gestão de pessoas, processos, projetos e ESG.",
        "topicos": [
            {
                "titulo": "1. Teorias e evolução da administração",
                "explicacao": "Abordagens clássica, burocrática e sistêmica; evolução da administração pública brasileira e os modelos patrimonialista, burocrático e gerencial.",
                "subtopicos": [
                    {"titulo": "Abordagens clássica, burocrática e sistêmica", "texto": "Taylor/Fayol, Weber e a visão sistêmica das organizações."},
                    {"titulo": "Evolução da AP no Brasil e nova gestão pública", "texto": "Reformas administrativas após 1930; DASP, Dec.-Lei 200/67, reforma gerencial de 1995."},
                ],
            },
            {
                "titulo": "2. Processo e estrutura organizacional",
                "explicacao": "As funções administrativas (planejar, organizar, dirigir, controlar) e como a estrutura e a cultura moldam a organização.",
                "subtopicos": [
                    {"titulo": "Funções da administração (PODC)", "texto": "Planejamento, organização, direção e controle."},
                    {"titulo": "Estrutura e cultura organizacional", "texto": "Departamentalização, centralização x descentralização; valores e clima."},
                ],
            },
            {
                "titulo": "3. Gestão de pessoas",
                "explicacao": "Equilíbrio organizacional e comportamento humano no trabalho: motivação, liderança e desempenho.",
                "subtopicos": [
                    {"titulo": "Comportamento organizacional", "texto": "Teorias de motivação (Maslow, Herzberg), liderança e desempenho."},
                    {"titulo": "Objetivos e desafios da gestão de pessoas", "texto": "Relação indivíduo/organização e equilíbrio organizacional."},
                ],
            },
            {
                "titulo": "4. Gestão de processos e projetos",
                "explicacao": "Mapeamento, análise e melhoria de processos; gestão de projetos e métodos ágeis.",
                "subtopicos": [
                    {"titulo": "Mapeamento e melhoria de processos", "texto": "Notação BPMN, cadeia de valor, análise e otimização."},
                    {"titulo": "Gestão de projetos e metodologia ágil", "texto": "Ciclo de vida, etapas, modelos de gestão e abordagem ágil."},
                ],
            },
            {
                "titulo": "5. Recursos materiais e ESG",
                "explicacao": "Administração de recursos materiais e a agenda ESG (ambiental, social e governança) aplicada à gestão pública.",
                "subtopicos": [
                    {"titulo": "Administração de recursos materiais", "texto": "Gestão de estoques, compras e patrimônio."},
                    {"titulo": "ESG na gestão pública", "texto": "Critérios ambientais, sociais e de governança nas decisões."},
                ],
            },
        ],
    },

    # ============================ DIREITO CONSTITUCIONAL ============================
    {
        "slug": "direito-constitucional",
        "titulo": "Direito Constitucional",
        "grupo": "Conhecimentos Básicos",
        "icone": "⚖️",
        "resumo": "Teoria da Constituição, direitos fundamentais, organização do Estado e dos Poderes, controle de constitucionalidade e ordem econômica/social.",
        "topicos": [
            {
                "titulo": "1. Teoria da Constituição e poder constituinte",
                "explicacao": "Conceito, classificações e supremacia da Constituição; aplicabilidade e interpretação das normas; poder constituinte e mutação constitucional.",
                "subtopicos": [
                    {"titulo": "Aplicabilidade e interpretação das normas", "texto": "Eficácia plena, contida e limitada; mutação constitucional.", "reuse": (R, "direito-constitucional", "aplicabilidade-das-normas")},
                    {"titulo": "Poder constituinte (originário e derivado)", "texto": "Características do poder constituinte originário e dos limites ao derivado (reformador/decorrente)."},
                ],
            },
            {
                "titulo": "2. Princípios e direitos fundamentais",
                "explicacao": "Princípios fundamentais (arts. 1º a 4º) e direitos e garantias: individuais, coletivos, sociais, de nacionalidade e políticos, com seus remédios constitucionais.",
                "subtopicos": [
                    {"titulo": "Princípios fundamentais", "texto": "Fundamentos, objetivos e princípios das relações internacionais.", "reuse": (R, "direito-constitucional", "principios-fundamentais-arts-1o-a-4o")},
                    {"titulo": "Direitos individuais e remédios constitucionais", "texto": "Art. 5º, HC, MS, MI e habeas data.", "reuse": (R, "direito-constitucional", "direitos-individuais-e-coletivos")},
                    {"titulo": "Direitos sociais, nacionalidade e políticos", "texto": "Arts. 6º a 17; partidos políticos.", "reuse": (R, "direito-constitucional", "direitos-sociais-nacionalidade-e-politicos")},
                ],
            },
            {
                "titulo": "3. Organização do Estado e dos Poderes",
                "explicacao": "Federação e repartição de competências, Administração Pública na CF, organização dos Poderes com freios e contrapesos e funções essenciais à justiça.",
                "subtopicos": [
                    {"titulo": "Federação e repartição de competências", "texto": "Competências privativas, comuns, concorrentes; intervenção.", "reuse": (R, "direito-constitucional", "reparticao-de-competencias")},
                    {"titulo": "Administração pública na Constituição", "texto": "Arts. 37 a 41; princípios e servidores públicos.", "reuse": (R, "direito-constitucional", "administracao-publica-arts-37-a-41")},
                    {"titulo": "Poderes e processo legislativo", "texto": "Legislativo, Executivo, Judiciário; espécies normativas.", "reuse": (R, "direito-constitucional", "processo-legislativo")},
                    {"titulo": "Funções essenciais à justiça", "texto": "MP, Advocacia Pública e Defensoria.", "reuse": (R, "direito-constitucional", "poder-judiciario-e-funcoes-essenciais")},
                ],
            },
            {
                "titulo": "4. Controle de constitucionalidade",
                "explicacao": "Sistemas de controle e o modelo brasileiro: controle difuso/incidental e concentrado/abstrato, com suas ações típicas.",
                "subtopicos": [
                    {"titulo": "Sistemas e controle difuso (incidental)", "texto": "Controle concreto, cláusula de reserva de plenário, efeitos e papel do Senado (art. 52, X)."},
                    {"titulo": "Controle concentrado (ADI, ADC, ADPF, ADO)", "texto": "Ações do controle abstrato, legitimados (art. 103) e efeitos erga omnes/vinculante."},
                ],
            },
            {
                "titulo": "5. Tributação, finanças e ordem econômica e social",
                "explicacao": "Sistema Tributário Nacional, finanças públicas e orçamentos, ordem econômica e ordem social, incluindo a Reforma da Previdência.",
                "subtopicos": [
                    {"titulo": "Sistema Tributário Nacional", "texto": "Princípios, limitações ao poder de tributar e repartição de receitas.", "reuse": (R, "direito-constitucional", "sistema-tributario-nacional")},
                    {"titulo": "Ordem econômica e financeira", "texto": "Princípios da atividade econômica (art. 170).", "reuse": (R, "direito-constitucional", "ordem-economica-e-financeira")},
                    {"titulo": "Finanças públicas e orçamentos", "texto": "PPA, LDO e LOA; normas gerais de finanças (arts. 163-169).", "reuse": (R, "direito-financeiro", "ppa-ldo-e-loa")},
                    {"titulo": "Ordem social e Reforma da Previdência (EC 103/2019)", "texto": "Seguridade social e principais mudanças da EC 103/2019."},
                ],
            },
            {
                "titulo": "6. Defesa do Estado e comunidades tradicionais",
                "explicacao": "Defesa do Estado e das instituições democráticas e direitos de populações indígenas e quilombolas.",
                "subtopicos": [
                    {"titulo": "Estado de defesa, de sítio e segurança pública", "texto": "Sistema constitucional de crises e órgãos de segurança pública (art. 144)."},
                    {"titulo": "Populações indígenas e quilombolas", "texto": "Direitos dos índios (arts. 231-232) e das comunidades remanescentes de quilombos."},
                ],
            },
        ],
    },

    # ============================ DIREITO ADMINISTRATIVO ============================
    {
        "slug": "direito-administrativo",
        "titulo": "Direito Administrativo",
        "grupo": "Conhecimentos Básicos",
        "icone": "🏢",
        "resumo": "Regime jurídico-administrativo, atos, poderes, agentes (Lei 8.112/90), serviços públicos, organização, responsabilidade, controle e licitações.",
        "topicos": [
            {
                "titulo": "1. Estado, governo e regime jurídico-administrativo",
                "explicacao": "Conceitos de Estado, governo e Administração; objeto e fontes do Direito Administrativo; princípios expressos e implícitos.",
                "subtopicos": [
                    {"titulo": "Conceitos e princípios da administração", "texto": "Sentidos de Administração e princípios (LIMPE e implícitos).", "reuse": (R, "direito-administrativo", "principios-administrativos")},
                    {"titulo": "Objeto, fontes e regime jurídico-administrativo", "texto": "Conceito e objeto do Direito Administrativo, suas fontes (lei, doutrina, jurisprudência, costume) e o regime de prerrogativas e sujeições."},
                ],
            },
            {
                "titulo": "2. Atos administrativos",
                "explicacao": "Conceito, requisitos, atributos, classificação, espécies e formas de extinção do ato administrativo.",
                "subtopicos": [
                    {"titulo": "Requisitos e atributos", "texto": "Competência, finalidade, forma, motivo, objeto; presunção, imperatividade, autoexecutoriedade.", "reuse": (R, "direito-administrativo", "requisitos-e-atributos")},
                    {"titulo": "Classificação e extinção", "texto": "Anulação, revogação, cassação e convalidação.", "reuse": (R, "direito-administrativo", "classificacao-e-extincao")},
                ],
            },
            {
                "titulo": "3. Poderes da administração",
                "explicacao": "Poderes hierárquico, disciplinar, regulamentar e de polícia; uso e abuso do poder.",
                "subtopicos": [
                    {"titulo": "Poder de polícia", "texto": "Limitação de direitos em favor da coletividade; atributos.", "reuse": (R, "direito-administrativo", "poder-de-policia")},
                    {"titulo": "Hierárquico, disciplinar e abuso de poder", "texto": "Poderes internos e os vícios de excesso e desvio de poder.", "reuse": (R, "direito-administrativo", "poder-disciplinar-e-hierarquico")},
                ],
            },
            {
                "titulo": "4. Agentes públicos",
                "explicacao": "Espécies de agentes, regime constitucional e o estatuto dos servidores federais (Lei 8.112/1990).",
                "subtopicos": [
                    {"titulo": "Lei 8.112/1990 (servidores federais)", "texto": "Provimento, vacância, posse, exercício, direitos, deveres e processo administrativo disciplinar (PAD) no regime federal."},
                    {"titulo": "Regime, direitos, deveres e responsabilidade", "texto": "Responsabilidade civil, penal e administrativa do agente.", "reuse": (R, "direito-administrativo", "regime-e-responsabilidade")},
                ],
            },
            {
                "titulo": "5. Organização administrativa",
                "explicacao": "Centralização e descentralização, desconcentração, Administração direta e indireta e o terceiro setor.",
                "subtopicos": [
                    {"titulo": "Centralização e descentralização", "texto": "Desconcentração (hierarquia) x descentralização (tutela).", "reuse": (R, "direito-administrativo", "desconcentracao-x-descentralizacao")},
                    {"titulo": "Administração indireta e terceiro setor", "texto": "Autarquias, fundações, EP, SEM; OS, OSCIP, serviços sociais autônomos.", "reuse": (R, "direito-administrativo", "entidades-da-administracao-indireta")},
                ],
            },
            {
                "titulo": "6. Serviços públicos",
                "explicacao": "Conceito, elementos, princípios, classificação e formas de delegação dos serviços públicos.",
                "subtopicos": [
                    {"titulo": "Conceito, princípios e classificação", "texto": "Serviço público e princípios (continuidade, modicidade, generalidade)."},
                    {"titulo": "Delegação: concessão, permissão e autorização", "texto": "Formas de prestação e meios de execução; Lei 8.987/95 e equilíbrio econômico-financeiro."},
                ],
            },
            {
                "titulo": "7. Responsabilidade civil do Estado",
                "explicacao": "Evolução, teoria do risco administrativo, responsabilidade por ação e omissão, excludentes e direito de regresso.",
                "subtopicos": [
                    {"titulo": "Responsabilidade civil do Estado", "texto": "Regra objetiva (risco administrativo); art. 37, §6º.", "reuse": (R, "direito-administrativo", "responsabilidade-civil-do-estado")},
                    {"titulo": "Excludentes, atenuantes e direito de regresso", "texto": "Caso fortuito/força maior, culpa da vítima; ação de regresso contra o agente (dolo/culpa)."},
                ],
            },
            {
                "titulo": "8. Controle, improbidade, processo e licitações",
                "explicacao": "Controle da Administração, improbidade administrativa, processo administrativo federal e o regime de licitações e contratos.",
                "subtopicos": [
                    {"titulo": "Controle da administração pública", "texto": "Controle administrativo, legislativo e judicial; tutela e autotutela (Súmulas 346 e 473 do STF)."},
                    {"titulo": "Improbidade administrativa (Lei 8.429/1992)", "texto": "Modalidades e sanções; exigência de dolo após a Lei 14.230/21.", "reuse": (R, "direito-administrativo", "improbidade-administrativa")},
                    {"titulo": "Processo administrativo (Lei 9.784/1999)", "texto": "Princípios, fases, prazos e o dever de motivação no processo administrativo federal."},
                    {"titulo": "Licitações e contratos (Lei 14.133/2021)", "texto": "Modalidades, fases e contratação direta.", "reuse": (R, "direito-administrativo", "modalidades-e-fases")},
                ],
            },
        ],
    },

    # ============================ AUDITORIA GOVERNAMENTAL ============================
    {
        "slug": "auditoria-governamental",
        "titulo": "Auditoria Governamental",
        "grupo": "Conhecimentos Básicos",
        "icone": "🔍",
        "resumo": "Conceito e tipos de auditoria, instrumentos de fiscalização, normas (TCU/INTOSAI/NBASP), planejamento, execução, achados e relatórios.",
        "topicos": [
            {
                "titulo": "1. Conceito, finalidade e tipos de auditoria",
                "explicacao": "Conceito, finalidade, abrangência e atuação da auditoria; papéis da auditoria interna e externa e os tipos de auditoria no setor público.",
                "subtopicos": [
                    {"titulo": "Conceito, abrangência e papéis (interna x externa)", "texto": "Finalidade e atuação da auditoria; diferença entre auditoria interna e externa no controle."},
                    {"titulo": "Tipos: conformidade, operacional e financeira", "texto": "Auditoria de conformidade (legalidade), operacional (desempenho) e financeira (demonstrações)."},
                ],
            },
            {
                "titulo": "2. Instrumentos de fiscalização",
                "explicacao": "Os instrumentos usados pelo controle externo para fiscalizar a gestão pública.",
                "subtopicos": [
                    {"titulo": "Auditoria, levantamento, monitoramento, acompanhamento e inspeção", "texto": "Finalidade e diferenças entre cada instrumento de fiscalização do TCU."},
                ],
            },
            {
                "titulo": "3. Normas de auditoria",
                "explicacao": "Normas que regem a auditoria governamental: do TCU, da INTOSAI (ISSAIs) e as Normas Brasileiras de Auditoria do Setor Público.",
                "subtopicos": [
                    {"titulo": "Normas do TCU, INTOSAI/ISSAI e NBASP", "texto": "Código de ética e princípios fundamentais (ISSAI 100, 200, 300 e 400) e as NBASP."},
                ],
            },
            {
                "titulo": "4. Planejamento de auditoria",
                "explicacao": "Determinação de escopo, avaliação de materialidade, risco e relevância, amostragem e a matriz de planejamento.",
                "subtopicos": [
                    {"titulo": "Materialidade, risco e relevância", "texto": "Patamar de relevância que orienta a profundidade dos exames.", "reuse": (R, "auditoria", "materialidade")},
                    {"titulo": "Amostragem estatística em auditoria", "texto": "Exame de parte da população para concluir sobre o todo.", "reuse": (R, "auditoria", "metodos-de-selecao")},
                    {"titulo": "Matriz de planejamento e escopo", "texto": "Instrumento que estrutura questões, informações, fontes e procedimentos da auditoria."},
                ],
            },
            {
                "titulo": "5. Controles internos e execução",
                "explicacao": "Avaliação de controles internos e a execução da auditoria: programas, papéis de trabalho, testes e técnicas.",
                "subtopicos": [
                    {"titulo": "Controles internos (COSO)", "texto": "Componentes do controle interno e segregação de funções.", "reuse": (R, "auditoria", "componentes-coso")},
                    {"titulo": "Programas, papéis de trabalho e testes", "texto": "Testes de observância e substantivos.", "reuse": (R, "auditoria", "tipos-de-procedimentos")},
                    {"titulo": "Técnicas e procedimentos", "texto": "Exame documental, circularização, revisão analítica.", "reuse": (R, "auditoria", "procedimentos-analiticos")},
                ],
            },
            {
                "titulo": "6. Evidências e achados",
                "explicacao": "Obtenção de evidências e caracterização de achados de auditoria, com as matrizes de achados e de responsabilização.",
                "subtopicos": [
                    {"titulo": "Evidência e caracterização de achados", "texto": "Atributos do achado (situação, critério, causa, efeito) e suficiência/adequação da evidência."},
                    {"titulo": "Matriz de achados e de responsabilização", "texto": "Instrumentos que consolidam achados e identificam responsáveis."},
                ],
            },
            {
                "titulo": "7. Comunicação dos resultados",
                "explicacao": "Elaboração e comunicação dos relatórios de auditoria e a opinião do auditor.",
                "subtopicos": [
                    {"titulo": "Relatórios de auditoria e opinião", "texto": "Tipos de opinião e estrutura do relatório.", "reuse": (R, "auditoria", "tipos-de-opiniao")},
                ],
            },
        ],
    },

    # ============================ INFRAESTRUTURA DE TI ============================
    {
        "slug": "infraestrutura-ti",
        "titulo": "Infraestrutura de TI",
        "grupo": "Conhecimentos Específicos",
        "icone": "🖧",
        "resumo": "Arquitetura de data center, redes, sistemas operacionais, armazenamento, segurança, monitoramento e alta disponibilidade.",
        "topicos": [
            {
                "titulo": "1. Arquitetura de infraestrutura",
                "explicacao": "Topologias físicas e lógicas, arquiteturas de data center (on-premises, cloud, híbrida) e infraestrutura projetada para escala, redundância e tolerância a falhas.",
                "subtopicos": [
                    {"titulo": "Topologias e arquiteturas de data center", "texto": "On-premises, cloud e híbrida; topologias físicas e lógicas de redes corporativas."},
                    {"titulo": "Hiperconvergência, escalabilidade e redundância", "texto": "Infraestrutura hiperconvergente; arquitetura escalável, tolerante a falhas e redundante."},
                ],
            },
            {
                "titulo": "2. Redes e comunicação de dados",
                "explicacao": "Protocolos de comunicação, comutação e roteamento em ambientes corporativos, redes definidas por software e wireless corporativo.",
                "subtopicos": [
                    {"titulo": "Protocolos de comunicação", "texto": "TCP, UDP, SCTP, ARP, TLS/SSL, OSPF, BGP, DNS, DHCP, ICMP, FTP/SFTP, SSH, HTTP/HTTPS, SMTP/IMAP/POP3."},
                    {"titulo": "Switching, roteamento, SDN e wireless", "texto": "VLANs, STP, QoS, roteamento/switching; SDN e redes programáveis; Wi-Fi 6, WPA3, mesh."},
                ],
            },
            {
                "titulo": "3. Sistemas operacionais e servidores",
                "explicacao": "Administração avançada de Linux e Windows Server, virtualização e serviços de diretório.",
                "subtopicos": [
                    {"titulo": "Linux e Windows Server", "texto": "Administração avançada, gerenciamento de usuários, permissões e GPOs."},
                    {"titulo": "Virtualização e serviços de diretório", "texto": "KVM, VMware vSphere/ESXi; Active Directory e LDAP."},
                ],
            },
            {
                "titulo": "4. Armazenamento e backup",
                "explicacao": "Arquiteturas de armazenamento (SAN, NAS, DAS), RAID e estratégias de backup e recuperação.",
                "subtopicos": [
                    {"titulo": "SAN, NAS, DAS e RAID", "texto": "Protocolos iSCSI, NFS, SMB; níveis de RAID, vantagens e hot-spare."},
                    {"titulo": "Backup e recuperação (RPO/RTO)", "texto": "Snapshots, deduplicação, RPO/RTO e Oracle RMAN."},
                ],
            },
            {
                "titulo": "5. Segurança de infraestrutura",
                "explicacao": "Hardening, defesa de perímetro e proteção de dados em redes corporativas.",
                "subtopicos": [
                    {"titulo": "Hardening, firewalls e IDS/IPS", "texto": "Hardening de servidores/rede; NGFW, IDS/IPS, proxies e NAC."},
                    {"titulo": "VPNs, PKI e segmentação de rede", "texto": "VPNs, SSL/TLS, PKI, criptografia; segmentação e zonas de segurança."},
                ],
            },
            {
                "titulo": "6. Monitoramento, gestão e automação",
                "explicacao": "Ferramentas de monitoramento, gerência de capacidade/disponibilidade, ITIL v4 e automação.",
                "subtopicos": [
                    {"titulo": "Monitoramento e ITIL v4", "texto": "Zabbix, New Relic, Grafana; incidentes, problemas, mudanças e configurações (CMDB)."},
                    {"titulo": "Automação (PowerShell, Bash, Puppet)", "texto": "Scripts e automação de infraestrutura; gerência de capacidade e desempenho."},
                ],
            },
            {
                "titulo": "7. Alta disponibilidade e recuperação de desastres",
                "explicacao": "Clusters de alta disponibilidade, balanceamento de carga e planos de continuidade e recuperação de desastres.",
                "subtopicos": [
                    {"titulo": "Clusters e balanceamento de carga", "texto": "Alta disponibilidade, failover, heartbeat e fencing."},
                    {"titulo": "Continuidade de negócios e testes de DR", "texto": "Planos de continuidade (BCP) e testes de recuperação de desastres."},
                ],
            },
        ],
    },

    # ============================ ENGENHARIA DE DADOS ============================
    {
        "slug": "engenharia-dados",
        "titulo": "Engenharia de Dados",
        "grupo": "Conhecimentos Específicos",
        "icone": "🗄️",
        "resumo": "Bancos relacionais e NoSQL, modelagem, BI/DW, integração, ETL/pipelines, governança e qualidade de dados e integração com nuvem.",
        "topicos": [
            {
                "titulo": "1. Bancos de dados",
                "explicacao": "Bancos relacionais (Oracle, SQL Server) e não relacionais (MongoDB, Elasticsearch), modelagens de dados e SQL.",
                "subtopicos": [
                    {"titulo": "Modelo relacional e chaves", "texto": "Tabelas, chaves primária/estrangeira e integridade referencial.", "reuse": (R, "tecnologia-da-informacao", "modelo-relacional-e-chaves")},
                    {"titulo": "SQL (DDL, DML, DCL)", "texto": "Linguagem de consulta e manipulação de dados.", "reuse": (R, "tecnologia-da-informacao", "linguagens-sql")},
                    {"titulo": "Bancos NoSQL (MongoDB, Elasticsearch)", "texto": "Modelos de documento e de busca; quando usar NoSQL x relacional; teorema CAP."},
                ],
            },
            {
                "titulo": "2. Arquitetura de inteligência de negócio",
                "explicacao": "Repositórios analíticos (Data Warehouse, Data Mart, Data Lake, Data Mesh) e Business Intelligence.",
                "subtopicos": [
                    {"titulo": "DW, Data Mart, Data Lake e Data Mesh", "texto": "Modelagem dimensional, esquema estrela e OLAP.", "reuse": (R, "tecnologia-da-informacao", "esquema-estrela-e-olap")},
                    {"titulo": "Business Intelligence", "texto": "Indicadores, dashboards e apoio à decisão.", "reuse": (R, "tecnologia-da-informacao", "indicadores-e-visualizacao")},
                ],
            },
            {
                "titulo": "3. Conectores e integração",
                "explicacao": "Integração com fontes de dados via APIs, arquivos e mensageria, com controle de integridade e segurança na captação.",
                "subtopicos": [
                    {"titulo": "APIs, arquivos e mensageria", "texto": "REST/SOAP, Web Services; CSV, JSON, XML, Parquet; mensageria e eventos."},
                    {"titulo": "Integridade e segurança na captação", "texto": "Integridade dos dados, TLS, autenticação e mascaramento.", "reuse": (R, "tecnologia-da-informacao", "integridade-e-seguranca")},
                ],
            },
            {
                "titulo": "4. Fluxo de manipulação (ETL e pipelines)",
                "explicacao": "Processos de ETL e pipelines de dados com versionamento, logging, tolerância a falhas e integração com CI/CD.",
                "subtopicos": [
                    {"titulo": "ETL e pipeline de dados", "texto": "Extração, transformação e carga de dados.", "reuse": (R, "tecnologia-da-informacao", "etl")},
                    {"titulo": "Versionamento, logging e CI/CD", "texto": "Auditoria, retries, checkpoints e integração contínua nos pipelines."},
                ],
            },
            {
                "titulo": "5. Governança e qualidade de dados",
                "explicacao": "Linhagem, catalogação, metadados e controle de qualidade dos dados.",
                "subtopicos": [
                    {"titulo": "Linhagem, catalogação e metadados", "texto": "Rastreamento da origem dos dados, glossários e políticas de acesso."},
                    {"titulo": "Qualidade de dados", "texto": "Validação, conformidade e deduplicação de dados."},
                ],
            },
            {
                "titulo": "6. Integração com nuvem",
                "explicacao": "Serviços gerenciados de dados em nuvem e integração com armazenamento e IA.",
                "subtopicos": [
                    {"titulo": "Serviços gerenciados (Azure Data Factory, Databricks)", "texto": "Orquestração e processamento de dados em nuvem."},
                    {"titulo": "Armazenamento em nuvem e IA", "texto": "S3, Azure Blob, GCS; integração com serviços de IA e análise."},
                ],
            },
        ],
    },

    # ============================ ENGENHARIA DE SOFTWARE ============================
    {
        "slug": "engenharia-software",
        "titulo": "Engenharia de Software",
        "grupo": "Conhecimentos Específicos",
        "icone": "💾",
        "resumo": "Arquitetura, padrões de projeto, APIs, persistência, DevOps/CI-CD, testes e desenvolvimento seguro.",
        "topicos": [
            {
                "titulo": "1. Arquitetura de software",
                "explicacao": "Padrões arquiteturais (monolito, microsserviços, serverless), arquitetura orientada a eventos e padrões de integração.",
                "subtopicos": [
                    {"titulo": "Monolito, microsserviços e serverless", "texto": "Trade-offs entre os estilos e arquitetura orientada a eventos/mensageria."},
                    {"titulo": "Padrões de integração (API Gateway, Service Mesh, CQRS)", "texto": "Padrões para comunicação e escalabilidade de sistemas distribuídos."},
                ],
            },
            {
                "titulo": "2. Design e programação",
                "explicacao": "Padrões de projeto (GoF e GRASP) e técnicas de concorrência e programação assíncrona.",
                "subtopicos": [
                    {"titulo": "Padrões de projeto (GoF e GRASP)", "texto": "Padrões criacionais, estruturais e comportamentais; coesão e acoplamento."},
                    {"titulo": "Concorrência e programação assíncrona", "texto": "Paralelismo, multithreading e modelos assíncronos."},
                ],
            },
            {
                "titulo": "3. APIs e integrações",
                "explicacao": "Design e versionamento de APIs RESTful e boas práticas de autenticação/autorização.",
                "subtopicos": [
                    {"titulo": "Design e versionamento de APIs REST", "texto": "Boas práticas REST, idempotência e versionamento."},
                    {"titulo": "Autenticação e autorização (OAuth2, JWT, OpenID)", "texto": "Fluxos OAuth2, tokens JWT e OpenID Connect."},
                ],
            },
            {
                "titulo": "4. Persistência de dados",
                "explicacao": "Modelagem relacional e normalização, bancos NoSQL e versionamento/migração de esquemas.",
                "subtopicos": [
                    {"titulo": "Modelagem relacional e normalização", "texto": "Formas normais e redução de redundância.", "reuse": (R, "tecnologia-da-informacao", "normalizacao")},
                    {"titulo": "NoSQL e migração de esquemas", "texto": "MongoDB, Elasticsearch; versionamento e migração de schema."},
                ],
            },
            {
                "titulo": "5. DevOps e integração contínua",
                "explicacao": "Pipelines de CI/CD, build/teste/deploy automatizados e orquestração de contêineres.",
                "subtopicos": [
                    {"titulo": "Pipelines de CI/CD", "texto": "GitHub Actions; build, testes e deploy automatizados."},
                    {"titulo": "Docker e Kubernetes", "texto": "Contêineres, orquestração, observabilidade (Grafana, New Relic)."},
                ],
            },
            {
                "titulo": "6. Testes e desenvolvimento seguro",
                "explicacao": "Testes automatizados, análise de qualidade de código e práticas de DevSecOps.",
                "subtopicos": [
                    {"titulo": "Testes automatizados e qualidade", "texto": "Unitários, integração, contrato; análise estática e cobertura (SonarQube)."},
                    {"titulo": "Desenvolvimento seguro (DevSecOps)", "texto": "Segurança integrada ao ciclo de desenvolvimento; linguagem Java."},
                ],
            },
        ],
    },

    # ============================ SEGURANÇA DA INFORMAÇÃO ============================
    {
        "slug": "seguranca-informacao",
        "titulo": "Segurança da Informação",
        "grupo": "Conhecimentos Específicos",
        "icone": "🔐",
        "resumo": "Gestão de identidade, malware e ataques, soluções de defesa, frameworks, criptografia e segurança em nuvem.",
        "topicos": [
            {
                "titulo": "1. Gestão de identidade e acesso",
                "explicacao": "Autenticação, autorização e gestão de identidades, incluindo SSO e múltiplos fatores.",
                "subtopicos": [
                    {"titulo": "Autenticação, autorização e SSO", "texto": "SSO, SAML, OAuth2 e OpenID Connect."},
                    {"titulo": "MFA, IAM e PAM", "texto": "Múltiplos fatores; Identity e Privileged Access Management."},
                ],
            },
            {
                "titulo": "2. Malware e ataques a redes",
                "explicacao": "Tipos de código malicioso e os principais ataques a redes e aplicações.",
                "subtopicos": [
                    {"titulo": "Tipos de malware", "texto": "Vírus, worm, trojan, ransomware, rootkit, spyware, keylogger, fileless, adware, backdoor."},
                    {"titulo": "Ataques a redes e aplicações", "texto": "DoS/DDoS, phishing, zero-day, IP/ARP spoofing, buffer overflow, SQL injection, XSS, DNS poisoning."},
                ],
            },
            {
                "titulo": "3. Soluções de segurança",
                "explicacao": "Tecnologias de proteção e controles para aplicações web e serviços.",
                "subtopicos": [
                    {"titulo": "Firewall, IDS/IPS, SIEM e proxy", "texto": "Defesa em camadas; IAM, PAM, antivírus e antispam."},
                    {"titulo": "Controles para aplicações web", "texto": "Controles e testes de segurança para aplicações web e Web Services."},
                ],
            },
            {
                "titulo": "4. Frameworks e tratamento de incidentes",
                "explicacao": "Frameworks de segurança e o processo de tratamento de incidentes cibernéticos.",
                "subtopicos": [
                    {"titulo": "Frameworks (MITRE ATT&CK, CIS, NIST CSF)", "texto": "Modelos de referência para segurança e segurança cibernética."},
                    {"titulo": "Tratamento de incidentes cibernéticos", "texto": "Detecção, contenção, erradicação, recuperação e lições aprendidas."},
                ],
            },
            {
                "titulo": "5. Criptografia e proteção de dados",
                "explicacao": "Criptografia, assinatura/certificação digital e proteção de dados em trânsito e em repouso, incluindo nuvem e contêineres.",
                "subtopicos": [
                    {"titulo": "Criptografia e certificação digital", "texto": "Simétrica/assimétrica, assinatura e certificação digital; dados em trânsito e em repouso."},
                    {"titulo": "Segurança em nuvem e contêineres", "texto": "Privacidade por padrão e segurança de ambientes em nuvem e contêineres."},
                ],
            },
        ],
    },

    # ============================ COMPUTAÇÃO EM NUVEM ============================
    {
        "slug": "computacao-nuvem",
        "titulo": "Computação em Nuvem",
        "grupo": "Conhecimentos Específicos",
        "icone": "☁️",
        "resumo": "Modelos de serviço/implantação, plataformas, arquitetura, segurança, DevOps/IaC, governança, dados e multicloud.",
        "topicos": [
            {
                "titulo": "1. Fundamentos de computação em nuvem",
                "explicacao": "Modelos de serviço (IaaS, PaaS, SaaS) e de implantação, com elasticidade, escalabilidade e alta disponibilidade.",
                "subtopicos": [
                    {"titulo": "Modelos de serviço e de implantação", "texto": "IaaS/PaaS/SaaS; nuvem pública, privada e híbrida."},
                    {"titulo": "Elasticidade, escalabilidade e SOA", "texto": "Arquitetura orientada a serviços, microsserviços e alta disponibilidade."},
                ],
            },
            {
                "titulo": "2. Plataformas e arquitetura de soluções",
                "explicacao": "Principais provedores e o design de soluções distribuídas, serverless e baseadas em contêineres.",
                "subtopicos": [
                    {"titulo": "AWS, Azure e Google Cloud", "texto": "Plataformas e serviços de nuvem dos principais provedores."},
                    {"titulo": "Sistemas distribuídos, serverless e contêineres", "texto": "Design resiliente, event-driven, balanceamento e orquestração (Docker, Kubernetes)."},
                ],
            },
            {
                "titulo": "3. Redes e segurança em nuvem",
                "explicacao": "Conectividade, gestão de identidade, criptografia e arquitetura Zero Trust em nuvem.",
                "subtopicos": [
                    {"titulo": "IAM, RBAC e criptografia (KMS)", "texto": "Gestão de identidade/acesso, MFA e criptografia em trânsito e repouso."},
                    {"titulo": "Zero Trust e conectividade", "texto": "Zero Trust em nuvem; VPNs, sub-redes, gateways, Direct Connect/ExpressRoute."},
                ],
            },
            {
                "titulo": "4. DevOps, CI/CD e IaC",
                "explicacao": "Automação de infraestrutura como código, pipelines de entrega contínua e observabilidade.",
                "subtopicos": [
                    {"titulo": "Infraestrutura como código (Terraform)", "texto": "IaC e pipelines (Jenkins, GitHub Actions)."},
                    {"titulo": "Observabilidade em nuvem", "texto": "Monitoramento, logging e tracing (CloudWatch, Azure Monitor, GCloud Monitoring)."},
                ],
            },
            {
                "titulo": "5. Governança, custos, dados e multicloud",
                "explicacao": "Governança, compliance, FinOps, armazenamento e processamento de dados, migração e estratégias multicloud.",
                "subtopicos": [
                    {"titulo": "Governança, compliance e FinOps", "texto": "Tagueamento, cotas, ISO/IEC 27001, NIST 800-53, LGPD e gestão de custos."},
                    {"titulo": "Dados, migração e multicloud", "texto": "Data lakes, migração de aplicações, multicloud e soberania de dados."},
                ],
            },
        ],
    },

    # ============================ INTELIGÊNCIA ARTIFICIAL ============================
    {
        "slug": "inteligencia-artificial",
        "titulo": "Inteligência Artificial",
        "grupo": "Conhecimentos Específicos",
        "icone": "🤖",
        "resumo": "Aprendizado de máquina, redes neurais e deep learning, PLN, IA generativa, MLOps e ética em IA.",
        "topicos": [
            {
                "titulo": "1. Aprendizado de máquina",
                "explicacao": "Paradigmas de aprendizado (supervisionado, não supervisionado, semissupervisionado e por reforço) e análise preditiva.",
                "subtopicos": [
                    {"titulo": "Supervisionado, não supervisionado e por reforço", "texto": "Algoritmos com dados rotulados, agrupamento e aprendizado por recompensa.", "reuse": (R, "tecnologia-da-informacao", "aprendizado-de-maquina")},
                    {"titulo": "Análise preditiva e avaliação de modelos", "texto": "Métricas como acurácia, precisão, recall e curva ROC.", "reuse": (R, "tecnologia-da-informacao", "avaliacao-de-modelos")},
                ],
            },
            {
                "titulo": "2. Redes neurais e deep learning",
                "explicacao": "Arquiteturas de redes neurais, frameworks, técnicas de treinamento e aplicações.",
                "subtopicos": [
                    {"titulo": "Arquiteturas e frameworks", "texto": "Redes densas, CNN, RNN, transformers; TensorFlow e PyTorch."},
                    {"titulo": "Treinamento e aplicações", "texto": "Backpropagation, overfitting/regularização e casos de uso."},
                ],
            },
            {
                "titulo": "3. PLN e IA generativa",
                "explicacao": "Processamento de linguagem natural, agentes inteligentes e modelos generativos.",
                "subtopicos": [
                    {"titulo": "Processamento de linguagem natural e agentes", "texto": "Pré-processamento, modelos de linguagem e sistemas multiagentes."},
                    {"titulo": "IA generativa", "texto": "Modelos generativos (LLMs), prompts e aplicações."},
                ],
            },
            {
                "titulo": "4. Engenharia e ética de IA",
                "explicacao": "Operacionalização de modelos (MLOps), deploy e os princípios éticos e regulatórios da IA.",
                "subtopicos": [
                    {"titulo": "MLOps e deploy de modelos", "texto": "Ciclo de vida, versionamento e integração com nuvem."},
                    {"titulo": "Ética, viés e LGPD", "texto": "Explicabilidade, viés algorítmico, discriminação e impactos regulatórios."},
                ],
            },
        ],
    },

    # ============================ CONTRATAÇÕES DE TI ============================
    {
        "slug": "contratacoes-ti",
        "titulo": "Contratações de TI",
        "grupo": "Conhecimentos Específicos",
        "icone": "📑",
        "resumo": "Etapas da contratação, modelos de serviço, governança e fiscalização de contratos, riscos e legislação aplicável.",
        "topicos": [
            {
                "titulo": "1. Etapas da contratação de soluções de TI",
                "explicacao": "Planejamento da contratação: estudo técnico preliminar, termo de referência, análise de riscos e pesquisa de preços.",
                "subtopicos": [
                    {"titulo": "ETP, Termo de Referência e Projeto Básico", "texto": "Documentos da fase de planejamento da contratação de TI."},
                    {"titulo": "Análise de riscos e pesquisa de preços (RACI)", "texto": "Matriz de riscos, pesquisa de preços e matriz de responsabilidades."},
                ],
            },
            {
                "titulo": "2. Tipos de soluções e modelos de serviço",
                "explicacao": "Formas de contratar TI: software sob demanda, licenciamento, nuvem e serviços gerenciados.",
                "subtopicos": [
                    {"titulo": "Software, licenciamento e nuvem (SaaS/IaaS/PaaS)", "texto": "Modelos de serviço e contratação de soluções de TI."},
                    {"titulo": "Fábrica de software e serviços gerenciados", "texto": "Sustentação de sistemas, outsourcing e serviços de infraestrutura."},
                ],
            },
            {
                "titulo": "3. Governança e fiscalização de contratos",
                "explicacao": "Papéis e responsabilidades na gestão de contratos, indicadores de nível de serviço e gestão de mudanças.",
                "subtopicos": [
                    {"titulo": "Papéis (gestor e fiscais) e SLAs", "texto": "Gestor, fiscal técnico e administrativo; níveis de serviço e penalidades."},
                    {"titulo": "Mudanças contratuais e reequilíbrio", "texto": "Gestão de alterações e reequilíbrio econômico-financeiro."},
                ],
            },
            {
                "titulo": "4. Riscos, controles e legislação",
                "explicacao": "Riscos e controles internos nas contratações de TI e os normativos aplicáveis.",
                "subtopicos": [
                    {"titulo": "Riscos e controles em contratações", "texto": "Identificação, análise e resposta a riscos; auditoria e responsabilização."},
                    {"titulo": "Legislação e normativos (14.133, LGPD, INs)", "texto": "Lei 14.133/21, Decreto 10.024/19, LGPD; INs SGD/ME 01/2019 e 94/2022 e SEGES."},
                ],
            },
        ],
    },

    # ============================ GESTÃO DE TI ============================
    {
        "slug": "gestao-ti",
        "titulo": "Gestão de Tecnologia da Informação",
        "grupo": "Conhecimentos Específicos",
        "icone": "⚙️",
        "resumo": "Gerenciamento de serviços (ITIL v4), governança de TI (COBIT 2019) e metodologias ágeis.",
        "topicos": [
            {
                "titulo": "1. Gerenciamento de serviços (ITIL v4)",
                "explicacao": "Conceitos básicos, estrutura e objetivos do ITIL v4 para o gerenciamento de serviços de TI.",
                "subtopicos": [
                    {"titulo": "ITIL v4: conceitos, estrutura e objetivos", "texto": "Sistema de valor de serviço, cadeia de valor, práticas e princípios orientadores."},
                ],
            },
            {
                "titulo": "2. Governança de TI (COBIT 2019)",
                "explicacao": "Conceitos básicos, estrutura e objetivos do COBIT 2019 como framework de governança de TI.",
                "subtopicos": [
                    {"titulo": "COBIT 2019: conceitos, estrutura e objetivos", "texto": "Objetivos de governança/gestão, componentes e fatores de design."},
                ],
            },
            {
                "titulo": "3. Metodologias ágeis",
                "explicacao": "Frameworks e práticas ágeis para desenvolvimento e entrega de produtos de TI.",
                "subtopicos": [
                    {"titulo": "Scrum, XP e Kanban", "texto": "Papéis, eventos e artefatos do Scrum; práticas de XP e fluxo Kanban."},
                    {"titulo": "TDD, BDD e DDD", "texto": "Test/Behavior-Driven Development e Domain-Driven Design."},
                ],
            },
        ],
    },
]

