# -*- coding: utf-8 -*-
"""
Conteúdo programático + explicações didáticas.
Concurso: Auditor-Fiscal da Receita Estadual de Goiás (SEFAZ-GO) — ANEXO II.
Cada disciplina possui tópicos; cada tópico tem uma explicação e subtópicos comentados.
"""

DISCIPLINAS = [
    # ============================ LÍNGUA PORTUGUESA ============================
    {
        "slug": "lingua-portuguesa",
        "titulo": "Língua Portuguesa",
        "grupo": "Conhecimentos Básicos",
        "icone": "📝",
        "resumo": "Compreensão e interpretação de textos, gramática aplicada e redação de documentos oficiais.",
        "topicos": [
            {
                "titulo": "1. Interpretação de texto",
                "explicacao": "Interpretar é ir além do que está escrito: identificar tese, argumentos, intenção do autor, relações de causa/consequência e inferências. Em prova, a maior parte dos erros vem de extrapolar (afirmar o que o texto não diz) ou de reduzir (ignorar ressalvas como 'em geral', 'pode', 'salvo').",
                "subtopicos": [
                    {"titulo": "Compreensão x interpretação", "texto": "Compreensão = o que o texto diz explicitamente. Interpretação = o que se pode concluir logicamente a partir dele. Cuidado com inferências que exigem conhecimento externo não autorizado pelo texto."},
                    {"titulo": "Ideia central e secundárias", "texto": "Localize o tópico frasal de cada parágrafo. A ideia central costuma aparecer na introdução ou conclusão; as secundárias dão sustentação (exemplos, dados, contra-argumentos)."},
                    {"titulo": "Inferência e pressuposto", "texto": "Pressuposto está implícito na própria estrutura da frase (ex.: 'continuou estudando' pressupõe que já estudava). Subentendido depende do contexto."},
                ],
            },
            {
                "titulo": "2. Ortografia, acentuação e crase",
                "explicacao": "Domínio das regras do Acordo Ortográfico vigente. A crase (fusão da preposição 'a' com o artigo 'a') é tema recorrente: ocorre diante de palavra feminina que admita artigo e seja regida por preposição 'a'.",
                "subtopicos": [
                    {"titulo": "Acentuação gráfica", "texto": "Oxítonas terminadas em a/e/o, ditongos abertos éi/éu/ói só em oxítonas, hiatos i/u tônicos sozinhos ou com s. Lembre: paroxítonas não recebem acento em ditongos abertos após o Acordo (ex.: ideia, heroico)."},
                    {"titulo": "Emprego da crase", "texto": "Usa-se antes de palavra feminina ('vou à escola'), nas locuções ('às vezes', 'à medida que') e na indicação de horas ('às 8h'). Não se usa antes de verbo, de palavra masculina ou de pronome que rejeita artigo."},
                ],
            },
            {
                "titulo": "3. Classes de palavras",
                "explicacao": "Substantivo, adjetivo, numeral, pronome, verbo, advérbio, preposição, conjunção, interjeição e artigo. Reconhecer a classe e a função é base para concordância, regência e pontuação.",
                "subtopicos": [
                    {"titulo": "Pronomes", "texto": "Pessoais, possessivos, demonstrativos, relativos e indefinidos. Os relativos (que, qual, cujo, onde) ligam orações e exigem atenção à regência do verbo da oração adjetiva."},
                    {"titulo": "Conjunções", "texto": "Coordenativas (aditiva, adversativa, alternativa, conclusiva, explicativa) e subordinativas (causal, condicional, concessiva, consecutiva etc.). Determinam o sentido lógico entre orações."},
                ],
            },
            {
                "titulo": "4. Sintaxe: regência, concordância e colocação",
                "explicacao": "Regência trata da relação entre verbo/nome e seus complementos (com ou sem preposição). Concordância (verbal e nominal) ajusta as palavras em número, pessoa e gênero. Colocação pronominal define próclise, mesóclise e ênclise.",
                "subtopicos": [
                    {"titulo": "Concordância verbal e nominal", "texto": "Verbo concorda com o sujeito; nas estruturas com 'haver' (existir) o verbo é impessoal. Atenção a sujeito composto, partitivos e expressões como 'mais de um'."},
                    {"titulo": "Regência verbal e nominal", "texto": "Ex.: 'assistir a um filme' (ver), 'obedecer a alguém'. A regência justifica o uso ou não da crase e a escolha do pronome relativo (a que, em que, de que)."},
                    {"titulo": "Colocação pronominal", "texto": "Próclise (pronome antes) com palavras atrativas (negação, advérbio, pronomes relativos); mesóclise no futuro do presente/pretérito sem atração; ênclise como regra padrão no início de oração."},
                ],
            },
            {
                "titulo": "5. Pontuação, coordenação e subordinação",
                "explicacao": "A pontuação organiza o período e marca relações sintáticas. Vírgula separa termos de mesma função, isola apostos/vocativos e adjuntos deslocados, mas não separa sujeito de predicado nem verbo de objeto.",
                "subtopicos": [
                    {"titulo": "Período composto", "texto": "Coordenação une orações independentes; subordinação cria dependência (substantivas, adjetivas, adverbiais). Reconhecer o tipo orienta a pontuação."},
                    {"titulo": "Orações adjetivas", "texto": "Explicativas vêm entre vírgulas (informação acessória); restritivas, sem vírgula (delimitam o sentido). Trocar uma pela outra altera o significado."},
                ],
            },
            {
                "titulo": "6. Semântica e estilística",
                "explicacao": "Estuda significado: sinonímia, antonímia, polissemia, ambiguidade, conotação/denotação e figuras de linguagem. Coesão e coerência garantem a articulação textual.",
                "subtopicos": [
                    {"titulo": "Coesão e coerência", "texto": "Coesão é a amarração formal (conectivos, pronomes, elipses); coerência é a unidade de sentido. Substituir um conectivo pode quebrar a lógica argumentativa."},
                    {"titulo": "Figuras de linguagem", "texto": "Metáfora, metonímia, ironia, eufemismo, hipérbole. Em textos oficiais predomina a denotação; figuras aparecem mais na interpretação de textos literários/jornalísticos."},
                ],
            },
            {
                "titulo": "7. Redação oficial",
                "explicacao": "Reconhecimento e produção de correspondências e atos oficiais conforme o padrão do Manual de Redação. Prioriza clareza, concisão, impessoalidade, formalidade e uso do padrão culto.",
                "subtopicos": [
                    {"titulo": "Atributos do texto oficial", "texto": "Impessoalidade, linguagem formal padrão, clareza, concisão, uniformidade. Evita-se rebuscamento e ambiguidade."},
                    {"titulo": "Tipos de documentos", "texto": "Ofício (padrão único de comunicação oficial), memorando, parecer, despacho, ata, relatório. Conhecer o fecho, o vocativo e o pronome de tratamento adequados."},
                ],
            },
        ],
    },

    # ============= RACIOCÍNIO LÓGICO, MAT. FINANCEIRA E ESTATÍSTICA =============
    {
        "slug": "raciocinio-logico",
        "titulo": "Raciocínio Lógico, Matemática Financeira e Estatística",
        "grupo": "Conhecimentos Básicos",
        "icone": "📊",
        "resumo": "Lógica proposicional, sequências, finanças (juros, descontos) e estatística descritiva e probabilidade.",
        "topicos": [
            {
                "titulo": "1. Estrutura lógica de relações",
                "explicacao": "Deduzir informações a partir de relações entre pessoas, lugares, objetos ou eventos fictícios. Inclui problemas de associação lógica (tabelas-verdade de correspondência) e diagramas.",
                "subtopicos": [
                    {"titulo": "Problemas de associação", "texto": "Montar tabela cruzando elementos e eliminar combinações impossíveis a partir das pistas. Técnica do 'verdadeiro/falso' por linha e coluna."},
                ],
            },
            {
                "titulo": "2. Lógica proposicional",
                "explicacao": "Proposições simples e compostas com conectivos: conjunção (e), disjunção (ou), condicional (se...então), bicondicional (se e somente se) e negação. Tabelas-verdade definem o valor lógico.",
                "subtopicos": [
                    {"titulo": "Conectivos e tabela-verdade", "texto": "Conjunção só é V se ambas V; disjunção só é F se ambas F; condicional só é F quando V→F; bicondicional é V quando os valores são iguais."},
                    {"titulo": "Tautologia, contradição e contingência", "texto": "Tautologia é sempre verdadeira; contradição, sempre falsa; contingência depende dos valores. Importante para verificar equivalências."},
                    {"titulo": "Equivalências e negações", "texto": "Leis de De Morgan: ~(p∧q)=~p∨~q. Negação do condicional: ~(p→q)=p∧~q. Equivalência: p→q ≡ ~q→~p (contrapositiva)."},
                ],
            },
            {
                "titulo": "3. Argumentação e quantificadores",
                "explicacao": "Validade de argumentos (premissas → conclusão) e uso dos quantificadores 'todo', 'algum', 'nenhum' com diagramas de Venn. Um argumento é válido quando a conclusão decorre necessariamente das premissas.",
                "subtopicos": [
                    {"titulo": "Argumentos válidos", "texto": "Modus ponens (p→q, p ∴ q), modus tollens (p→q, ~q ∴ ~p), silogismo hipotético. Distinguir validade (forma) de verdade (conteúdo)."},
                    {"titulo": "Quantificadores", "texto": "Negação de 'todo A é B' é 'algum A não é B'. Negação de 'algum' é 'nenhum'. Diagramas ajudam a testar conclusões."},
                ],
            },
            {
                "titulo": "4. Sequências, matrizes e análise combinatória",
                "explicacao": "Padrões numéricos e figurais, progressões aritmética (PA) e geométrica (PG), além de contagem por princípio multiplicativo, permutações, arranjos e combinações.",
                "subtopicos": [
                    {"titulo": "PA e PG", "texto": "PA: an = a1 + (n−1)r; soma Sn = (a1+an)·n/2. PG: an = a1·q^(n−1); soma finita Sn = a1(q^n−1)/(q−1)."},
                    {"titulo": "Análise combinatória", "texto": "Arranjo importa a ordem (A=n!/(n−p)!); combinação não (C=n!/[p!(n−p)!]); permutação é arranjo de todos os elementos."},
                    {"titulo": "Conjuntos", "texto": "Operações de união, interseção e diferença; princípio da inclusão-exclusão para contagem em diagramas de Venn."},
                ],
            },
            {
                "titulo": "5. Probabilidade",
                "explicacao": "Razão entre casos favoráveis e casos possíveis em espaço amostral equiprovável. Inclui probabilidade da união, condicional e independência de eventos.",
                "subtopicos": [
                    {"titulo": "Regras fundamentais", "texto": "P(A∪B)=P(A)+P(B)−P(A∩B). Eventos independentes: P(A∩B)=P(A)·P(B). Probabilidade condicional: P(A|B)=P(A∩B)/P(B)."},
                ],
            },
            {
                "titulo": "6. Matemática Financeira",
                "explicacao": "Juros simples e compostos, descontos, taxas de juros, equivalência de capitais, séries de pagamentos (amortização) e fluxo de caixa. Base para análise tributária e econômica.",
                "subtopicos": [
                    {"titulo": "Juros simples e compostos", "texto": "Simples: J = C·i·t (linear). Compostos: M = C·(1+i)^t (exponencial, juro sobre juro). Diferença cresce com o tempo."},
                    {"titulo": "Descontos", "texto": "Desconto simples comercial (sobre o valor nominal) e racional (sobre o valor atual). Comum em títulos antecipados."},
                    {"titulo": "Taxas e equivalência", "texto": "Taxas nominal, efetiva e equivalente; capitais são equivalentes quando, levados a uma mesma data por uma taxa, têm o mesmo valor."},
                    {"titulo": "Amortização", "texto": "Sistemas SAC (amortização constante) e Price (prestação constante). Compreender a composição juros+amortização de cada parcela."},
                ],
            },
            {
                "titulo": "7. Estatística descritiva",
                "explicacao": "Organização e resumo de dados: tabelas, gráficos, medidas de posição (média, mediana, moda), de dispersão (variância, desvio-padrão) e de assimetria/curtose.",
                "subtopicos": [
                    {"titulo": "Medidas de posição", "texto": "Média (sensível a outliers), mediana (valor central, robusta) e moda (mais frequente). Quartis e percentis localizam pontos da distribuição."},
                    {"titulo": "Medidas de dispersão", "texto": "Amplitude, variância, desvio-padrão e coeficiente de variação. Medem o quanto os dados se afastam da média."},
                    {"titulo": "Distribuições de probabilidade", "texto": "Binomial (eventos discretos com 2 resultados), Poisson (eventos raros), Normal (contínua, simétrica) e t de Student (amostras pequenas)."},
                    {"titulo": "Amostragem e estimação", "texto": "Amostra probabilística representa a população; estimação por ponto e por intervalo de confiança; testes de hipótese para validar afirmações sobre parâmetros."},
                ],
            },
        ],
    },

    # ========================= DIREITO CONSTITUCIONAL =========================
    {
        "slug": "direito-constitucional",
        "titulo": "Direito Constitucional",
        "grupo": "Conhecimentos Básicos",
        "icone": "⚖️",
        "resumo": "Constituição, princípios fundamentais, direitos e garantias, organização do Estado, Poderes e tributação na CF/88.",
        "topicos": [
            {
                "titulo": "1. Constituição da República de 1988",
                "explicacao": "Estudo do texto constitucional como norma suprema. A CF/88 é rígida (exige processo legislativo especial para emendas), analítica (extensa) e dirigente (estabelece programas e metas ao Estado).",
                "subtopicos": [
                    {"titulo": "Aplicabilidade das normas", "texto": "Normas de eficácia plena (aplicação imediata), contida (aplicação imediata, mas restringível por lei) e limitada (dependem de regulamentação para produzir todos os efeitos)."},
                    {"titulo": "Princípios fundamentais (arts. 1º a 4º)", "texto": "Fundamentos da República (soberania, cidadania, dignidade, valores sociais do trabalho e da livre iniciativa, pluralismo político), objetivos e princípios das relações internacionais."},
                ],
            },
            {
                "titulo": "2. Direitos e garantias fundamentais",
                "explicacao": "Direitos individuais e coletivos (art. 5º), sociais, de nacionalidade e políticos. Os remédios constitucionais (habeas corpus, mandado de segurança, habeas data, mandado de injunção, ação popular) protegem esses direitos.",
                "subtopicos": [
                    {"titulo": "Direitos individuais e coletivos", "texto": "Igualdade, legalidade, liberdade de expressão, devido processo legal, contraditório e ampla defesa, inviolabilidade de domicílio e sigilos. São cláusulas pétreas."},
                    {"titulo": "Direitos sociais, nacionalidade e políticos", "texto": "Direitos sociais (art. 6º), regras de aquisição/perda da nacionalidade e dos direitos políticos (alistamento, elegibilidade, inelegibilidades)."},
                ],
            },
            {
                "titulo": "3. Organização do Estado",
                "explicacao": "Federação brasileira: União, Estados, DF e Municípios, todos autônomos. Distribuição de competências (administrativas e legislativas) e repartição de receitas.",
                "subtopicos": [
                    {"titulo": "Repartição de competências", "texto": "Competências privativas da União, comuns (administrativas a todos os entes) e concorrentes (legislação onde a União fixa normas gerais e os Estados suplementam)."},
                    {"titulo": "Administração Pública (arts. 37 a 41)", "texto": "Princípios LIMPE (legalidade, impessoalidade, moralidade, publicidade, eficiência), concursos, servidores públicos, estabilidade e responsabilidade."},
                ],
            },
            {
                "titulo": "4. Organização dos Poderes",
                "explicacao": "Separação e independência entre Legislativo, Executivo e Judiciário, com freios e contrapesos. Inclui processo legislativo, funções de cada Poder e funções essenciais à Justiça.",
                "subtopicos": [
                    {"titulo": "Processo legislativo", "texto": "Espécies normativas (EC, LC, LO, medidas provisórias, leis delegadas), iniciativa, tramitação, sanção/veto e quóruns. Essencial para o Direito Tributário."},
                    {"titulo": "Poder Judiciário e funções essenciais", "texto": "STF como guardião da Constituição, controle de constitucionalidade (difuso e concentrado), Ministério Público, Advocacia Pública e Defensoria."},
                ],
            },
            {
                "titulo": "5. Tributação, orçamento e ordem econômica",
                "explicacao": "O Sistema Tributário Nacional na CF (arts. 145 a 162), as finanças públicas (arts. 163 a 169) e a ordem econômica e financeira (arts. 170 e seguintes) constituem o núcleo de interesse fiscal.",
                "subtopicos": [
                    {"titulo": "Sistema Tributário Nacional", "texto": "Espécies tributárias, limitações ao poder de tributar (princípios e imunidades), competências e repartição de receitas tributárias entre os entes."},
                    {"titulo": "Ordem econômica e financeira", "texto": "Princípios da ordem econômica (livre iniciativa, livre concorrência, função social da propriedade) e atuação do Estado como agente normativo e regulador."},
                ],
            },
        ],
    },

    # ========================= DIREITO ADMINISTRATIVO =========================
    {
        "slug": "direito-administrativo",
        "titulo": "Direito Administrativo",
        "grupo": "Conhecimentos Básicos",
        "icone": "🏛️",
        "resumo": "Regime jurídico-administrativo, atos, poderes, organização, agentes, licitações, controle e responsabilidade do Estado.",
        "topicos": [
            {
                "titulo": "1. Estado, governo e Administração Pública",
                "explicacao": "Conceitos de Estado (elementos: povo, território, governo soberano) e de Administração Pública nos sentidos subjetivo (órgãos/agentes) e objetivo (atividade administrativa).",
                "subtopicos": [
                    {"titulo": "Princípios administrativos", "texto": "Expressos (LIMPE) e implícitos (supremacia e indisponibilidade do interesse público, razoabilidade, proporcionalidade, autotutela, segurança jurídica)."},
                ],
            },
            {
                "titulo": "2. Organização administrativa",
                "explicacao": "Administração direta (entes políticos e seus órgãos) e indireta (autarquias, fundações públicas, empresas públicas e sociedades de economia mista). Estuda desconcentração e descentralização.",
                "subtopicos": [
                    {"titulo": "Desconcentração x descentralização", "texto": "Desconcentração distribui competências dentro da mesma pessoa jurídica (hierarquia). Descentralização transfere a outra pessoa (vínculo de tutela/supervisão)."},
                    {"titulo": "Entidades da Administração indireta", "texto": "Autarquias (regime público), fundações, empresas públicas e sociedades de economia mista (regime predominantemente privado)."},
                ],
            },
            {
                "titulo": "3. Atos administrativos",
                "explicacao": "Manifestação unilateral da Administração que produz efeitos jurídicos. Possuem requisitos (competência, finalidade, forma, motivo, objeto) e atributos (presunção de legitimidade, imperatividade, autoexecutoriedade, tipicidade).",
                "subtopicos": [
                    {"titulo": "Requisitos e atributos", "texto": "Vícios em qualquer requisito podem anular o ato. Competência e finalidade são vinculados; motivo e objeto podem ser discricionários."},
                    {"titulo": "Classificação e extinção", "texto": "Vinculados x discricionários; anulação (por ilegalidade, efeitos ex tunc), revogação (por conveniência, ex nunc) e convalidação de vícios sanáveis."},
                ],
            },
            {
                "titulo": "4. Poderes da Administração",
                "explicacao": "Prerrogativas para atender o interesse público: poder vinculado, discricionário, hierárquico, disciplinar, regulamentar e de polícia.",
                "subtopicos": [
                    {"titulo": "Poder de polícia", "texto": "Limita o exercício de direitos individuais em prol da coletividade (fiscalização tributária, sanitária, ambiental). Atributos: discricionariedade, autoexecutoriedade e coercibilidade."},
                    {"titulo": "Poder disciplinar e hierárquico", "texto": "Hierárquico organiza e ordena; disciplinar apura e pune infrações funcionais por meio do processo administrativo."},
                ],
            },
            {
                "titulo": "5. Agentes públicos",
                "explicacao": "Toda pessoa que exerce função pública, ainda que transitoriamente. Inclui agentes políticos, servidores estatutários, empregados públicos e particulares em colaboração.",
                "subtopicos": [
                    {"titulo": "Regime e responsabilidade", "texto": "Provimento, vacância, direitos e deveres, regime disciplinar. Responsabilidade civil, penal e administrativa, que são independentes entre si."},
                ],
            },
            {
                "titulo": "6. Licitações e contratos (Lei 14.133/2021)",
                "explicacao": "Procedimento para seleção da proposta mais vantajosa, regido pela nova Lei de Licitações. Princípios, modalidades, fases e hipóteses de contratação direta.",
                "subtopicos": [
                    {"titulo": "Modalidades e fases", "texto": "Pregão, concorrência, concurso, leilão e diálogo competitivo. Fase preparatória, divulgação, apresentação de propostas, julgamento, habilitação e homologação."},
                    {"titulo": "Contratação direta", "texto": "Dispensa e inexigibilidade de licitação (quando a competição é inviável). Exige justificativa e formalização adequada."},
                ],
            },
            {
                "titulo": "7. Controle, responsabilidade e improbidade",
                "explicacao": "Controle interno, externo (Tribunais de Contas) e judicial da Administração. Responsabilidade civil do Estado (objetiva) e improbidade administrativa (Lei 8.429/1992).",
                "subtopicos": [
                    {"titulo": "Responsabilidade civil do Estado", "texto": "Regra objetiva (teoria do risco administrativo): basta o nexo entre conduta e dano; admite excludentes (culpa exclusiva da vítima, caso fortuito/força maior)."},
                    {"titulo": "Improbidade administrativa", "texto": "Atos que importam enriquecimento ilícito, prejuízo ao erário ou violação a princípios. A Lei 14.230/2021 alterou o regime, exigindo dolo."},
                ],
            },
            {
                "titulo": "8. Processo administrativo e acesso à informação",
                "explicacao": "Processo administrativo (Lei 9.784/1999) garante contraditório, motivação e razoável duração. A Lei de Acesso à Informação (12.527/2011) assegura transparência.",
                "subtopicos": [
                    {"titulo": "Bens públicos e intervenção na propriedade", "texto": "Bens de uso comum, especial e dominical; desapropriação, servidão, requisição, tombamento e limitações administrativas."},
                ],
            },
        ],
    },

    # ========================== DIREITO FINANCEIRO ==========================
    {
        "slug": "direito-financeiro",
        "titulo": "Direito Financeiro",
        "grupo": "Conhecimentos Básicos",
        "icone": "💰",
        "resumo": "Orçamento público (PPA, LDO, LOA), receita e despesa, créditos adicionais, dívida pública e responsabilidade fiscal.",
        "topicos": [
            {
                "titulo": "1. Orçamento público e leis orçamentárias",
                "explicacao": "O ciclo orçamentário se estrutura em três leis integradas: PPA (planejamento de médio prazo, 4 anos), LDO (metas e prioridades anuais, regras) e LOA (orçamento anual com previsão de receitas e fixação de despesas).",
                "subtopicos": [
                    {"titulo": "PPA, LDO e LOA", "texto": "PPA define diretrizes, objetivos e metas; LDO faz a ponte e orienta a elaboração da LOA; LOA materializa o orçamento do exercício. Princípios: unidade, universalidade, anualidade, exclusividade."},
                ],
            },
            {
                "titulo": "2. Receita pública",
                "explicacao": "Ingressos de recursos aos cofres públicos. Classifica-se em originária (patrimônio do Estado) e derivada (poder de império — tributos). Quanto ao orçamento: corrente e de capital.",
                "subtopicos": [
                    {"titulo": "Estágios da receita", "texto": "Previsão, lançamento, arrecadação e recolhimento. A classificação por categoria econômica separa receitas correntes (tributárias, contribuições) de capital (operações de crédito, alienação de bens)."},
                ],
            },
            {
                "titulo": "3. Despesa pública",
                "explicacao": "Aplicação de recursos públicos. Classifica-se em corrente (manutenção, custeio) e de capital (investimentos, inversões, amortização da dívida). Segue estágios legais de execução.",
                "subtopicos": [
                    {"titulo": "Estágios da despesa", "texto": "Empenho (reserva de dotação), liquidação (verificação do direito do credor) e pagamento. Restos a pagar e despesas de exercícios anteriores são exceções controladas."},
                ],
            },
            {
                "titulo": "4. Créditos adicionais",
                "explicacao": "Autorizações de despesa não computadas ou insuficientes na LOA. Dividem-se em suplementares (reforço), especiais (nova dotação) e extraordinários (urgência imprevisível, como guerra/calamidade).",
                "subtopicos": [
                    {"titulo": "Tipos e fontes", "texto": "Suplementares e especiais dependem de autorização legislativa e indicação de recursos; extraordinários abrem-se por MP ou decreto, dada a urgência."},
                ],
            },
            {
                "titulo": "5. Dívida pública e endividamento",
                "explicacao": "Compromissos financeiros do Estado. Distingue dívida flutuante (curto prazo, restos a pagar) de fundada/consolidada (longo prazo). Operações de crédito captam recursos por endividamento.",
                "subtopicos": [
                    {"titulo": "Limites e controle", "texto": "A LRF e resoluções do Senado fixam limites de endividamento e operações de crédito. A 'regra de ouro' veda crédito que financie despesa corrente além do permitido."},
                ],
            },
            {
                "titulo": "6. Responsabilidade Fiscal (LC 101/2000)",
                "explicacao": "A LRF impõe planejamento, transparência e equilíbrio entre receitas e despesas, com limites para pessoal e endividamento e mecanismos de compensação para renúncias e novas despesas.",
                "subtopicos": [
                    {"titulo": "Gestão fiscal responsável", "texto": "Metas fiscais na LDO, limites de despesa com pessoal, renúncia de receita compensada, vedações em fim de mandato e relatórios de gestão fiscal."},
                ],
            },
        ],
    },

    # ====================== DIREITO CIVIL E EMPRESARIAL ======================
    {
        "slug": "direito-civil-empresarial",
        "titulo": "Direito Civil e Empresarial",
        "grupo": "Conhecimentos Básicos",
        "icone": "📜",
        "resumo": "Pessoas, bens, fatos e negócios jurídicos, obrigações, contratos e o regime do Direito de Empresa.",
        "topicos": [
            {
                "titulo": "1. Lei de Introdução e aplicação das normas",
                "explicacao": "A LINDB (DL 4.657/1942) trata de vigência, eficácia, interpretação e integração das normas (analogia, costumes, princípios gerais). Os arts. 20 a 30 trouxeram regras sobre segurança jurídica na atuação pública.",
                "subtopicos": [
                    {"titulo": "Integração e interpretação", "texto": "Na omissão da lei, o juiz decide por analogia, costumes e princípios gerais do direito. A LINDB também rege a aplicação da lei no tempo e no espaço."},
                ],
            },
            {
                "titulo": "2. Pessoas e bens",
                "explicacao": "Pessoa natural (personalidade, capacidade, direitos da personalidade) e pessoa jurídica (constituição, tipos, desconsideração). Bens classificam-se quanto à mobilidade, divisibilidade e fungibilidade.",
                "subtopicos": [
                    {"titulo": "Pessoa jurídica", "texto": "Início, registro, espécies (direito público e privado) e desconsideração da personalidade jurídica em caso de abuso, desvio de finalidade ou confusão patrimonial."},
                    {"titulo": "Domicílio e bens", "texto": "Bens móveis/imóveis, fungíveis/infungíveis, públicos/particulares. Domicílio é o centro de atividades jurídicas da pessoa."},
                ],
            },
            {
                "titulo": "3. Fatos e negócios jurídicos",
                "explicacao": "O negócio jurídico exige agente capaz, objeto lícito/possível e forma prescrita ou não defesa. Estuda planos de existência, validade e eficácia, além dos defeitos e invalidades.",
                "subtopicos": [
                    {"titulo": "Defeitos do negócio jurídico", "texto": "Vícios de consentimento (erro, dolo, coação, estado de perigo, lesão) e vício social (fraude contra credores, simulação). Geram anulabilidade ou nulidade."},
                    {"titulo": "Prescrição e decadência", "texto": "Prescrição extingue a pretensão; decadência extingue o próprio direito potestativo. Distinção relevante em matéria de crédito tributário."},
                ],
            },
            {
                "titulo": "4. Obrigações e responsabilidade civil",
                "explicacao": "Vínculo jurídico em que o devedor deve uma prestação ao credor. Classes de obrigações (dar, fazer, não fazer), adimplemento, inadimplemento e a responsabilidade civil daí decorrente.",
                "subtopicos": [
                    {"titulo": "Modalidades e extinção", "texto": "Obrigações solidárias, divisíveis/indivisíveis. Extinção por pagamento, compensação, novação, confusão, remissão e dação em pagamento."},
                    {"titulo": "Responsabilidade civil", "texto": "Subjetiva (exige culpa) e objetiva (independe de culpa, baseada no risco). Pressupõe conduta, dano e nexo causal."},
                ],
            },
            {
                "titulo": "5. Contratos",
                "explicacao": "Acordo de vontades que cria, modifica ou extingue obrigações. Princípios: autonomia da vontade, boa-fé objetiva, função social do contrato e força obrigatória (pacta sunt servanda).",
                "subtopicos": [
                    {"titulo": "Teoria geral e espécies", "texto": "Formação, classificação e extinção dos contratos. Espécies típicas: compra e venda, prestação de serviços, locação, fiança, entre outras."},
                ],
            },
            {
                "titulo": "6. Direito de Empresa",
                "explicacao": "Empresário é quem exerce profissionalmente atividade econômica organizada para a produção/circulação de bens ou serviços. Regula-se o registro, o nome, o estabelecimento e as sociedades.",
                "subtopicos": [
                    {"titulo": "Empresário e estabelecimento", "texto": "Inscrição obrigatória no Registro Público de Empresas Mercantis; estabelecimento é o complexo de bens organizados; trespasse é sua transferência."},
                    {"titulo": "Sociedades", "texto": "Personificadas e não personificadas; sociedade simples e empresária; tipos (limitada, anônima, em nome coletivo). A limitada é a mais comum no Brasil."},
                    {"titulo": "Falência e recuperação", "texto": "Recuperação judicial/extrajudicial visa preservar a empresa viável; a falência liquida o patrimônio do insolvente. Lei 11.101/2005."},
                ],
            },
        ],
    },

    # =============================== ECONOMIA ===============================
    {
        "slug": "economia",
        "titulo": "Economia",
        "grupo": "Conhecimentos Básicos",
        "icone": "📈",
        "resumo": "Microeconomia (oferta, demanda, mercados, tributação) e Macroeconomia (PIB, moeda, inflação, política fiscal e monetária).",
        "topicos": [
            {
                "titulo": "1. Conceitos fundamentais",
                "explicacao": "Economia estuda a alocação de recursos escassos entre necessidades ilimitadas. Conceitos centrais: escassez, custo de oportunidade, fatores de produção e a curva de possibilidades de produção (CPP).",
                "subtopicos": [
                    {"titulo": "Escassez e custo de oportunidade", "texto": "Todo recurso tem usos alternativos; escolher um implica abrir mão de outro. A CPP ilustra o trade-off e a eficiência produtiva."},
                ],
            },
            {
                "titulo": "2. Oferta, demanda e equilíbrio de mercado",
                "explicacao": "A demanda relaciona preço e quantidade procurada (inversa); a oferta, preço e quantidade ofertada (direta). O equilíbrio ocorre onde as curvas se cruzam, definindo preço e quantidade de mercado.",
                "subtopicos": [
                    {"titulo": "Deslocamentos x movimentos", "texto": "Variação de preço move-se ao longo da curva; mudanças em renda, gostos, preço de bens relacionados ou expectativas deslocam a curva inteira."},
                    {"titulo": "Bens substitutos e complementares", "texto": "Substitutos: alta no preço de um eleva a demanda do outro. Complementares: alta no preço de um reduz a demanda do outro."},
                ],
            },
            {
                "titulo": "3. Elasticidades",
                "explicacao": "Mede a sensibilidade da quantidade a variações de preço ou renda. Elasticidade-preço da demanda indica se a demanda é elástica (>1), inelástica (<1) ou unitária (=1) — crucial para política tributária.",
                "subtopicos": [
                    {"titulo": "Elasticidade e tributação", "texto": "Quanto mais inelástica a demanda, maior a parcela do imposto repassada ao consumidor e maior a arrecadação com menor perda de bem-estar."},
                ],
            },
            {
                "titulo": "4. Teoria da produção e custos",
                "explicacao": "Relação entre insumos e produto (função de produção), produtividade marginal e lei dos rendimentos decrescentes. Custos fixos, variáveis, totais, médios e marginais.",
                "subtopicos": [
                    {"titulo": "Custos no curto e longo prazo", "texto": "No curto prazo há fator fixo; no longo prazo todos variam, permitindo economias e deseconomias de escala."},
                ],
            },
            {
                "titulo": "5. Estruturas de mercado",
                "explicacao": "Concorrência perfeita (muitos agentes, produto homogêneo, preço dado), monopólio (um vendedor), oligopólio (poucos) e concorrência monopolística (diferenciação de produto).",
                "subtopicos": [
                    {"titulo": "Falhas de mercado", "texto": "Externalidades, bens públicos, assimetria de informação e poder de mercado justificam a intervenção do Estado e a tributação corretiva."},
                ],
            },
            {
                "titulo": "6. Macroeconomia: contas nacionais",
                "explicacao": "Mensuração da atividade econômica: PIB pelas óticas da produção, da renda e da despesa. Diferença entre variáveis nominais e reais e o papel dos agregados macroeconômicos.",
                "subtopicos": [
                    {"titulo": "PIB e agregados", "texto": "PIB = C + I + G + (X − M). Identidades entre poupança e investimento; PIB nominal usa preços correntes, PIB real, preços constantes."},
                ],
            },
            {
                "titulo": "7. Moeda, inflação e sistema financeiro",
                "explicacao": "Funções da moeda, oferta monetária, criação de moeda pelos bancos e o papel do Banco Central. Inflação como elevação contínua do nível geral de preços.",
                "subtopicos": [
                    {"titulo": "Política monetária", "texto": "Instrumentos: taxa de juros (Selic), depósito compulsório e operações de mercado aberto. Controlam liquidez e inflação."},
                    {"titulo": "Inflação", "texto": "Tipos (demanda, custos, inercial) e índices de preços. Afeta a arrecadação real e a correção monetária de tributos."},
                ],
            },
            {
                "titulo": "8. Política fiscal e setor externo",
                "explicacao": "Política fiscal usa receitas (tributos) e despesas públicas para influenciar a economia. O setor externo trata de balança comercial, câmbio e balanço de pagamentos.",
                "subtopicos": [
                    {"titulo": "Política fiscal", "texto": "Expansionista (mais gasto/menos imposto) estimula a demanda; contracionista, o contrário. Relaciona-se diretamente ao orçamento e à tributação."},
                ],
            },
        ],
    },

    # ========================= CONTABILIDADE GERAL =========================
    {
        "slug": "contabilidade-geral",
        "titulo": "Contabilidade Geral",
        "grupo": "Conhecimentos Básicos",
        "icone": "🧾",
        "resumo": "Conceitos, princípios e normas contábeis (CPC), escrituração, demonstrações financeiras e análise de balanços.",
        "topicos": [
            {
                "titulo": "1. Conceitos e princípios contábeis",
                "explicacao": "Contabilidade é o sistema de informação que registra os fatos patrimoniais e gera demonstrações para usuários. Baseia-se em princípios e na estrutura conceitual do CFC e dos Pronunciamentos do CPC.",
                "subtopicos": [
                    {"titulo": "Estrutura conceitual", "texto": "Características qualitativas: relevância e representação fidedigna (fundamentais); comparabilidade, verificabilidade, tempestividade e compreensibilidade (de melhoria)."},
                    {"titulo": "Patrimônio", "texto": "Ativo (bens e direitos), passivo (obrigações) e patrimônio líquido (capital próprio). Equação fundamental: Ativo = Passivo + PL."},
                ],
            },
            {
                "titulo": "2. Escrituração e o método das partidas dobradas",
                "explicacao": "Registro contábil pelo método das partidas dobradas: para todo débito há um crédito de igual valor. Contas patrimoniais e de resultado, livros obrigatórios e plano de contas.",
                "subtopicos": [
                    {"titulo": "Débito e crédito", "texto": "Ativo e despesas aumentam a débito; passivo, PL e receitas aumentam a crédito. O razonete sintetiza a movimentação de cada conta."},
                    {"titulo": "Regime de competência", "texto": "Receitas e despesas são reconhecidas no período em que ocorrem (fato gerador), independentemente do recebimento/pagamento (caixa)."},
                ],
            },
            {
                "titulo": "3. Operações com mercadorias e estoques",
                "explicacao": "Apuração do custo das mercadorias vendidas (CMV), critérios de avaliação de estoques (PEPS, custo médio) e tratamento de tributos sobre compras e vendas.",
                "subtopicos": [
                    {"titulo": "CMV e avaliação de estoques", "texto": "CMV = EI + Compras − EF. Métodos PEPS (primeiro que entra, primeiro que sai) e média ponderada afetam o resultado e os tributos."},
                ],
            },
            {
                "titulo": "4. Ativo imobilizado, intangível e depreciação",
                "explicacao": "Reconhecimento e mensuração de ativos de longo prazo. Depreciação, amortização e exaustão distribuem o custo pela vida útil; teste de recuperabilidade (impairment) ajusta perdas.",
                "subtopicos": [
                    {"titulo": "Depreciação", "texto": "Métodos linear (cotas constantes), soma dos dígitos e unidades produzidas. Reduz o ativo e gera despesa ao longo da vida útil do bem."},
                ],
            },
            {
                "titulo": "5. Demonstrações financeiras",
                "explicacao": "Conjunto exigido pela Lei 6.404/76 e CPCs: Balanço Patrimonial, DRE, DRA, DFC, DMPL e DVA, com notas explicativas. Cada uma evidencia um aspecto da situação econômico-financeira.",
                "subtopicos": [
                    {"titulo": "Balanço Patrimonial e DRE", "texto": "BP é estático (posição em uma data); DRE é dinâmica (resultado do período, do lucro bruto ao lucro líquido)."},
                    {"titulo": "DFC e DVA", "texto": "DFC mostra entradas/saídas de caixa (operacional, investimento, financiamento); DVA evidencia a riqueza gerada e sua distribuição."},
                ],
            },
            {
                "titulo": "6. Análise de balanços",
                "explicacao": "Interpretação das demonstrações por meio de indicadores de liquidez, endividamento, rentabilidade e atividade, além das análises horizontal e vertical.",
                "subtopicos": [
                    {"titulo": "Índices", "texto": "Liquidez (corrente, seca, geral), endividamento, rentabilidade (ROE, ROA, margens) e prazos médios. Avaliam capacidade de pagamento e desempenho."},
                ],
            },
        ],
    },

    # ========================= REALIDADE DE GOIÁS =========================
    {
        "slug": "realidade-de-goias",
        "titulo": "Realidade Étnica, Social, Histórica, Geográfica, Cultural, Política e Econômica de Goiás",
        "grupo": "Conhecimentos Básicos",
        "icone": "🌳",
        "resumo": "Formação, povoamento, geografia, sociedade, política, cultura e economia do Estado de Goiás.",
        "topicos": [
            {
                "titulo": "1. Formação econômica e povoamento",
                "explicacao": "O ciclo da mineração do ouro no século XVIII impulsionou a ocupação de Goiás. Com a decadência aurífera, a economia voltou-se à pecuária e à agricultura de subsistência, marcando longa estagnação.",
                "subtopicos": [
                    {"titulo": "Ciclo do ouro e decadência", "texto": "Bandeirantes fundaram arraiais mineradores; o esgotamento das jazidas levou ao isolamento e à transição para atividades agropastoris."},
                ],
            },
            {
                "titulo": "2. Geografia de Goiás",
                "explicacao": "Localização no Centro-Oeste, relevo de planaltos e chapadas, clima tropical com estações seca e chuvosa, e o bioma Cerrado predominante, com importante rede hidrográfica.",
                "subtopicos": [
                    {"titulo": "Cerrado e recursos naturais", "texto": "O Cerrado, segundo maior bioma brasileiro, sustenta a expansão agrícola; nascentes goianas integram bacias do Araguaia/Tocantins e do Paraná."},
                ],
            },
            {
                "titulo": "3. Sociedade e cultura",
                "explicacao": "Diversidade étnica (indígenas, quilombolas como Kalunga, migrantes) e manifestações culturais como folias, congadas, a culinária e o patrimônio histórico das cidades coloniais.",
                "subtopicos": [
                    {"titulo": "Patrimônio e identidade", "texto": "Cidade de Goiás (Patrimônio da Humanidade pela UNESCO), Pirenópolis e suas festas tradicionais expressam a cultura goiana."},
                ],
            },
            {
                "titulo": "4. Política e modernização",
                "explicacao": "A transferência da capital para Goiânia (planejada nos anos 1930) e a construção de Brasília reposicionaram Goiás, integrando-o à dinâmica nacional e acelerando a urbanização.",
                "subtopicos": [
                    {"titulo": "Goiânia e Brasília", "texto": "A nova capital simbolizou a modernização; a interiorização promovida por Brasília dinamizou a economia e a infraestrutura regional."},
                ],
            },
            {
                "titulo": "5. Economia contemporânea",
                "explicacao": "Agronegócio (grãos, carne), agroindústria, mineração, energia e serviços compõem a economia goiana, com forte inserção no comércio exterior e atração de investimentos.",
                "subtopicos": [
                    {"titulo": "Agronegócio e indústria", "texto": "Goiás é grande produtor de soja, milho, cana e proteína animal; a agroindústria e a logística reforçam sua relevância econômica e fiscal."},
                ],
            },
        ],
    },
]

