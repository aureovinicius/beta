# -*- coding: utf-8 -*-
"""Conhecimentos Específicos — Auditor-Fiscal da Receita Estadual de Goiás."""

ESPECIFICOS = [
    # ======================= TECNOLOGIAS DA INFORMAÇÃO =======================
    {
        "slug": "tecnologia-da-informacao",
        "titulo": "Tecnologias da Informação",
        "grupo": "Conhecimentos Específicos",
        "icone": "💻",
        "resumo": "Banco de dados, administração de dados, BI, mineração de dados e introdução à ciência de dados aplicadas à fiscalização.",
        "topicos": [
            {
                "titulo": "1. Fundamentos de banco de dados",
                "explicacao": "Banco de dados é uma coleção organizada de dados; o SGBD (Sistema Gerenciador) controla armazenamento, acesso e integridade. O modelo relacional organiza dados em tabelas (relações) com chaves.",
                "subtopicos": [
                    {"titulo": "Modelo relacional e chaves", "texto": "Tabelas, atributos e tuplas; chave primária identifica unicamente um registro; chave estrangeira referencia outra tabela, garantindo integridade referencial."},
                    {"titulo": "Linguagens (SQL)", "texto": "DDL (definição: CREATE, ALTER), DML (manipulação: SELECT, INSERT, UPDATE, DELETE) e DCL (controle de acesso). SQL é a base da consulta a dados fiscais."},
                    {"titulo": "Normalização", "texto": "Processo de organizar tabelas para reduzir redundância e anomalias (1FN, 2FN, 3FN). Equilibra integridade e desempenho das consultas."},
                ],
            },
            {
                "titulo": "2. Administração de dados",
                "explicacao": "Gestão do dado como ativo organizacional: integridade, segurança, disponibilidade e desempenho. Inclui backup, recuperação, controle de acesso e tuning de banco de dados.",
                "subtopicos": [
                    {"titulo": "Integridade e segurança", "texto": "Controle de transações (propriedades ACID), níveis de isolamento, autenticação e autorização. Protege dados sigilosos do contribuinte."},
                    {"titulo": "Backup e recuperação", "texto": "Estratégias de cópia (completo, incremental, diferencial) e planos de recuperação garantem continuidade e auditabilidade dos dados fiscais."},
                ],
            },
            {
                "titulo": "3. Modelagem multidimensional e Data Warehouse",
                "explicacao": "Para análise, dados operacionais são integrados em um Data Warehouse (DW), modelado de forma multidimensional (esquema estrela/floco de neve) com fatos e dimensões, suportando OLAP.",
                "subtopicos": [
                    {"titulo": "Esquema estrela e OLAP", "texto": "Tabela-fato (métricas) cercada por dimensões; OLAP permite slice, dice, drill-down e roll-up para analisar grandes volumes."},
                    {"titulo": "ETL", "texto": "Extração, Transformação e Carga: integra fontes heterogêneas, limpa e padroniza dados antes da carga no DW."},
                ],
            },
            {
                "titulo": "4. Business Intelligence (BI)",
                "explicacao": "Conjunto de técnicas para transformar dados em informação de apoio à decisão: dashboards, KPIs, relatórios e análises que orientam a inteligência fiscal.",
                "subtopicos": [
                    {"titulo": "Indicadores e visualização", "texto": "KPIs (indicadores-chave), painéis interativos e relatórios apoiam o monitoramento de arrecadação e a seleção de contribuintes para fiscalização."},
                ],
            },
            {
                "titulo": "5. Mineração de dados (Data Mining)",
                "explicacao": "Descoberta de padrões úteis em grandes bases. Tarefas principais: classificação, regressão, agrupamento (clustering), associação e detecção de anomalias — essenciais para identificar sonegação.",
                "subtopicos": [
                    {"titulo": "Tarefas de mineração", "texto": "Classificação prevê categorias (ex.: sonegador/não); clustering agrupa por semelhança; associação descobre regras (cesta de compras); anomalias revelam fraudes."},
                    {"titulo": "Avaliação de modelos", "texto": "Métricas como acurácia, precisão, recall, matriz de confusão e curva ROC medem a qualidade dos modelos preditivos."},
                ],
            },
            {
                "titulo": "6. Introdução à ciência de dados",
                "explicacao": "Combina estatística, computação e conhecimento de negócio para extrair valor dos dados, com aprendizado de máquina supervisionado e não supervisionado.",
                "subtopicos": [
                    {"titulo": "Aprendizado de máquina", "texto": "Supervisionado (regressão, árvores de decisão, redes neurais, SVM) usa dados rotulados; não supervisionado (k-means, PCA) descobre estrutura oculta."},
                    {"titulo": "Big Data e fluxos", "texto": "Tratamento de grandes volumes e dados em tempo real; mineração de fluxos e séries temporais apoiam previsão e detecção precoce de irregularidades."},
                ],
            },
        ],
    },

    # ============================== AUDITORIA ==============================
    {
        "slug": "auditoria",
        "titulo": "Auditoria",
        "grupo": "Conhecimentos Específicos",
        "icone": "🔍",
        "resumo": "Planejamento, risco, evidência, procedimentos, controles internos, amostragem, relatórios e parecer.",
        "topicos": [
            {
                "titulo": "1. Planejamento de auditoria",
                "explicacao": "Etapa inicial que define objetivos, natureza, época e extensão dos exames. Considera o conhecimento do negócio, os riscos e a materialidade para direcionar os esforços.",
                "subtopicos": [
                    {"titulo": "Materialidade", "texto": "Patamar de relevância: distorções acima dele influenciam decisões dos usuários. Orienta a profundidade e a seleção de itens a examinar."},
                ],
            },
            {
                "titulo": "2. Risco de auditoria",
                "explicacao": "Probabilidade de o auditor emitir opinião inadequada. Decompõe-se em risco inerente, risco de controle e risco de detecção. Quanto maior o risco, maior a extensão dos procedimentos.",
                "subtopicos": [
                    {"titulo": "Componentes do risco", "texto": "Inerente (suscetibilidade natural a erro), de controle (falha dos controles internos) e de detecção (procedimentos não detectarem a distorção)."},
                ],
            },
            {
                "titulo": "3. Controles internos",
                "explicacao": "Conjunto de políticas e procedimentos que garantem confiabilidade da informação, eficiência operacional e conformidade. Avaliar controles permite reduzir testes substantivos.",
                "subtopicos": [
                    {"titulo": "Componentes (COSO)", "texto": "Ambiente de controle, avaliação de riscos, atividades de controle, informação/comunicação e monitoramento. Segregação de funções é controle-chave."},
                ],
            },
            {
                "titulo": "4. Evidência e procedimentos de auditoria",
                "explicacao": "A evidência fundamenta a opinião do auditor e deve ser suficiente e adequada. Obtém-se por inspeção, observação, indagação, confirmação, recálculo, reexecução e procedimentos analíticos.",
                "subtopicos": [
                    {"titulo": "Tipos de procedimentos", "texto": "Testes de observância (verificam controles) e testes substantivos (de transações e de saldos) detectam distorções relevantes."},
                    {"titulo": "Procedimentos analíticos", "texto": "Comparações e análises de relações entre dados (índices, tendências) para identificar variações incomuns que mereçam investigação."},
                ],
            },
            {
                "titulo": "5. Amostragem em auditoria",
                "explicacao": "Aplicação de procedimentos a menos de 100% dos itens, permitindo concluir sobre toda a população. Pode ser estatística (probabilística) ou não estatística (baseada no julgamento).",
                "subtopicos": [
                    {"titulo": "Métodos de seleção", "texto": "Aleatória, sistemática e por unidade monetária. O risco de amostragem é a chance de a amostra não representar a população."},
                ],
            },
            {
                "titulo": "6. Relatórios e parecer de auditoria",
                "explicacao": "Comunicação do resultado dos trabalhos. A opinião pode ser não modificada (sem ressalva) ou modificada (com ressalva, adversa ou abstenção), conforme as distorções encontradas.",
                "subtopicos": [
                    {"titulo": "Tipos de opinião", "texto": "Sem ressalva (demonstrações fidedignas); com ressalva (distorção relevante mas não generalizada); adversa (relevante e generalizada); abstenção (impossibilidade de obter evidência)."},
                ],
            },
        ],
    },

    # ================= CONTABILIDADE AVANÇADA E DE CUSTOS =================
    {
        "slug": "contabilidade-avancada-custos",
        "titulo": "Contabilidade Avançada e de Custos",
        "grupo": "Conhecimentos Específicos",
        "icone": "📐",
        "resumo": "Investimentos, consolidação, combinação de negócios, tributos diferidos e a contabilidade de custos para decisão.",
        "topicos": [
            {
                "titulo": "1. Contabilidade avançada: investimentos societários",
                "explicacao": "Avaliação de participações em outras empresas. Coligadas e controladas com influência significativa usam o método de equivalência patrimonial (MEP); demais, o custo ou valor justo.",
                "subtopicos": [
                    {"titulo": "Método de equivalência patrimonial", "texto": "A investidora reconhece sua parte no resultado e no PL da investida. Ajusta o valor contábil do investimento conforme o desempenho da participada."},
                ],
            },
            {
                "titulo": "2. Combinação de negócios e consolidação",
                "explicacao": "Aquisição do controle de um negócio (método de aquisição) gera goodwill (ágio por rentabilidade futura). A consolidação reúne as demonstrações da controladora e controladas como entidade única.",
                "subtopicos": [
                    {"titulo": "Goodwill e mais/menos-valia", "texto": "Diferença entre o valor pago e o valor justo dos ativos líquidos; goodwill é testado por impairment e não amortizado."},
                    {"titulo": "Consolidação", "texto": "Soma-se ativo, passivo, receitas e despesas, eliminando-se transações e saldos intragrupo e destacando a participação de não controladores."},
                ],
            },
            {
                "titulo": "3. Reorganização societária e tributos diferidos",
                "explicacao": "Fusão, incorporação e cisão alteram a estrutura das sociedades. Diferenças temporárias entre o lucro contábil e o fiscal geram ativos e passivos fiscais diferidos.",
                "subtopicos": [
                    {"titulo": "Tributos diferidos", "texto": "Diferenças temporárias dedutíveis geram ativo fiscal diferido; tributáveis geram passivo. Refletem o efeito futuro de IRPJ/CSLL."},
                ],
            },
            {
                "titulo": "4. Custos: conceitos e classificação",
                "explicacao": "Custo é o gasto com bens/serviços na produção; despesa é o gasto para gerar receita fora da produção. Classificam-se em diretos/indiretos e fixos/variáveis.",
                "subtopicos": [
                    {"titulo": "Terminologia", "texto": "Gasto, custo, despesa, investimento, perda e desembolso. Diretos são apropriados diretamente; indiretos exigem rateio (CIF)."},
                    {"titulo": "Fixos e variáveis", "texto": "Fixos independem do volume (aluguel da fábrica); variáveis acompanham a produção (matéria-prima). Base da análise custo-volume-lucro."},
                ],
            },
            {
                "titulo": "5. Métodos de custeio",
                "explicacao": "Formas de apropriar custos aos produtos: custeio por absorção (legal e fiscal, inclui custos fixos), variável (apenas variáveis, gerencial) e baseado em atividades (ABC).",
                "subtopicos": [
                    {"titulo": "Absorção x variável", "texto": "Absorção é exigido pela legislação societária e fiscal; o variável apoia decisões gerenciais por isolar a margem de contribuição."},
                    {"titulo": "Custeio ABC", "texto": "Aloca custos indiretos a partir das atividades e seus direcionadores, aprimorando a precisão em estruturas complexas."},
                ],
            },
            {
                "titulo": "6. Análise custo-volume-lucro",
                "explicacao": "Margem de contribuição (receita − custos/despesas variáveis), ponto de equilíbrio (onde a margem cobre os custos fixos) e alavancagem operacional apoiam decisões de preço e produção.",
                "subtopicos": [
                    {"titulo": "Ponto de equilíbrio", "texto": "Contábil, econômico e financeiro. Indica o volume mínimo de vendas para não ter prejuízo; abaixo dele há perda, acima, lucro."},
                ],
            },
        ],
    },

    # =========================== DIREITO TRIBUTÁRIO I ===========================
    {
        "slug": "direito-tributario-1",
        "titulo": "Direito Tributário I",
        "grupo": "Conhecimentos Específicos",
        "icone": "📚",
        "resumo": "Sistema Tributário Nacional, princípios, competência, espécies tributárias, obrigação, crédito e Código Tributário Nacional.",
        "topicos": [
            {
                "titulo": "1. Sistema Tributário Nacional",
                "explicacao": "Conjunto de normas constitucionais e legais que regem a tributação. A CF distribui competências e estabelece limites; o CTN (Lei 5.172/66) traz as normas gerais com status de lei complementar.",
                "subtopicos": [
                    {"titulo": "Princípios constitucionais tributários", "texto": "Legalidade, isonomia, irretroatividade, anterioridade (anual e nonagesimal), vedação ao confisco, capacidade contributiva e uniformidade geográfica."},
                    {"titulo": "Imunidades", "texto": "Limitações constitucionais ao poder de tributar: recíproca entre entes, templos, partidos, sindicatos, entidades sem fins lucrativos, livros e jornais."},
                ],
            },
            {
                "titulo": "2. Espécies tributárias e competência",
                "explicacao": "Tributos são impostos, taxas, contribuições de melhoria, empréstimos compulsórios e contribuições especiais. A competência (poder de instituir) é indelegável e privativa de cada ente.",
                "subtopicos": [
                    {"titulo": "Espécies de tributos", "texto": "Impostos (não vinculados), taxas (serviço/poder de polícia), contribuição de melhoria (valorização imobiliária), empréstimos compulsórios e contribuições especiais."},
                    {"titulo": "Competência tributária", "texto": "Privativa, comum, residual e extraordinária. A capacidade tributária ativa (arrecadar/fiscalizar) pode ser delegada; a competência, não."},
                ],
            },
            {
                "titulo": "3. Obrigação tributária",
                "explicacao": "Vínculo entre Fisco e contribuinte. A obrigação principal (pagar tributo/penalidade) surge com o fato gerador; a acessória impõe deveres instrumentais (escriturar, declarar, emitir nota).",
                "subtopicos": [
                    {"titulo": "Fato gerador e hipótese de incidência", "texto": "A hipótese de incidência é a previsão abstrata na lei; o fato gerador é sua concretização, que faz nascer a obrigação."},
                    {"titulo": "Sujeitos e responsabilidade", "texto": "Sujeito ativo (credor) e passivo (contribuinte ou responsável). Responsabilidade por substituição, transferência, sucessão e de terceiros."},
                ],
            },
            {
                "titulo": "4. Crédito tributário",
                "explicacao": "É a obrigação tributária tornada líquida e exigível pelo lançamento. O lançamento pode ser de ofício, por declaração ou por homologação, conforme a participação do sujeito passivo.",
                "subtopicos": [
                    {"titulo": "Lançamento", "texto": "De ofício (Fisco apura tudo, ex.: IPTU), por declaração (mista) e por homologação (contribuinte calcula e antecipa, ex.: ICMS). Vincula a atividade administrativa."},
                    {"titulo": "Suspensão, extinção e exclusão", "texto": "Suspensão (moratória, parcelamento, liminar); extinção (pagamento, compensação, prescrição, decadência); exclusão (isenção e anistia)."},
                ],
            },
            {
                "titulo": "5. Garantias, privilégios e administração tributária",
                "explicacao": "O crédito tributário goza de garantias e preferências na cobrança. A administração tributária abrange fiscalização, dívida ativa e certidões, com poderes e deveres definidos no CTN.",
                "subtopicos": [
                    {"titulo": "Dívida ativa e CDA", "texto": "Crédito não pago é inscrito em dívida ativa, gerando a Certidão de Dívida Ativa (CDA), título executivo que embasa a execução fiscal."},
                    {"titulo": "Fiscalização e sigilo", "texto": "Poderes de fiscalização, dever de informação de terceiros e proteção ao sigilo fiscal, com exceções legais para troca de informações."},
                ],
            },
        ],
    },

    # ================ DIREITO TRIBUTÁRIO II — REFORMA TRIBUTÁRIA ================
    {
        "slug": "direito-tributario-2-reforma",
        "titulo": "Direito Tributário II — Reforma Tributária",
        "grupo": "Conhecimentos Específicos",
        "icone": "🔄",
        "resumo": "EC 132/2023, IBS, CBS, Imposto Seletivo, transição, comitê gestor e o novo modelo de tributação sobre o consumo.",
        "topicos": [
            {
                "titulo": "1. EC 132/2023 e o novo modelo",
                "explicacao": "A Emenda Constitucional 132/2023 instituiu a reforma da tributação sobre o consumo, substituindo cinco tributos (ICMS, ISS, IPI, PIS e Cofins) por um modelo de IVA dual: IBS, CBS e o Imposto Seletivo.",
                "subtopicos": [
                    {"titulo": "Princípios da reforma", "texto": "Simplicidade, transparência, neutralidade, justiça tributária, cooperação e defesa do meio ambiente. Tributação no destino, não na origem."},
                    {"titulo": "IVA dual", "texto": "Modelo com dois tributos sobre valor agregado: a CBS (federal) e o IBS (estadual/municipal compartilhado), além do Imposto Seletivo."},
                ],
            },
            {
                "titulo": "2. IBS — Imposto sobre Bens e Serviços",
                "explicacao": "Tributo de competência compartilhada entre Estados, DF e Municípios, que substitui o ICMS e o ISS. Incide de forma ampla sobre operações com bens materiais/imateriais e serviços, com não cumulatividade plena.",
                "subtopicos": [
                    {"titulo": "Características do IBS", "texto": "Base ampla, alíquota única por ente (com possibilidade de alíquota de referência), cobrança no destino e crédito amplo (não cumulatividade plena)."},
                    {"titulo": "Não cumulatividade plena", "texto": "Garante crédito sobre praticamente todas as aquisições, eliminando o efeito cascata e desonerando exportações e investimentos."},
                ],
            },
            {
                "titulo": "3. CBS — Contribuição sobre Bens e Serviços",
                "explicacao": "Contribuição federal que substitui PIS e Cofins (e parte do IPI), com a mesma base e regras do IBS, formando o IVA dual. Visa simplificar e dar neutralidade à tributação federal do consumo.",
                "subtopicos": [
                    {"titulo": "Harmonização com o IBS", "texto": "CBS e IBS partilham fato gerador, base de cálculo e regras gerais, facilitando o cumprimento das obrigações pelo contribuinte."},
                ],
            },
            {
                "titulo": "4. Imposto Seletivo",
                "explicacao": "Imposto federal extrafiscal ('imposto do pecado') sobre a produção, extração, comercialização ou importação de bens e serviços prejudiciais à saúde ou ao meio ambiente.",
                "subtopicos": [
                    {"titulo": "Finalidade extrafiscal", "texto": "Desestimula o consumo de produtos nocivos (tabaco, bebidas, alguns combustíveis). Não incide sobre exportações nem sobre bens essenciais."},
                ],
            },
            {
                "titulo": "5. Regimes específicos e diferenciados",
                "explicacao": "A reforma prevê tratamentos próprios para setores específicos (combustíveis, financeiro, imóveis, saúde, educação, agronegócio, Simples Nacional) e regimes diferenciados com redução de alíquota ou cashback.",
                "subtopicos": [
                    {"titulo": "Cesta básica e cashback", "texto": "Cesta básica nacional com alíquota zero; mecanismo de devolução (cashback) de tributo a famílias de baixa renda para reduzir a regressividade."},
                ],
            },
            {
                "titulo": "6. Transição e governança federativa",
                "explicacao": "A migração para o novo sistema é gradual (período de transição até 2033) e a gestão do IBS cabe ao Comitê Gestor, com Fundos de compensação para mitigar perdas de arrecadação dos entes.",
                "subtopicos": [
                    {"titulo": "Período de transição", "texto": "Convivência temporária entre tributos antigos e novos (alíquotas-teste a partir de 2026), com extinção progressiva de ICMS/ISS até 2033."},
                    {"titulo": "Comitê Gestor do IBS", "texto": "Entidade pública que centraliza arrecadação, distribuição e regulamentação do IBS entre Estados, DF e Municípios, assegurando uniformidade."},
                ],
            },
        ],
    },

    # ========================= LEGISLAÇÃO TRIBUTÁRIA =========================
    {
        "slug": "legislacao-tributaria",
        "titulo": "Legislação Tributária (Estado de Goiás)",
        "grupo": "Conhecimentos Específicos",
        "icone": "🏷️",
        "resumo": "ICMS, ITCD, IPVA e taxas estaduais conforme o Código Tributário de Goiás e legislação correlata.",
        "topicos": [
            {
                "titulo": "1. Código Tributário do Estado de Goiás",
                "explicacao": "A Lei 11.651/1991 institui o Código Tributário Estadual (CTE-GO), que disciplina os tributos de competência de Goiás, as obrigações, o lançamento, o contencioso e as penalidades.",
                "subtopicos": [
                    {"titulo": "Estrutura do CTE-GO", "texto": "Disposições gerais, normas sobre cada tributo estadual, obrigações acessórias, infrações e penalidades e o processo administrativo tributário."},
                ],
            },
            {
                "titulo": "2. ICMS — incidência e fato gerador",
                "explicacao": "Principal tributo estadual, incide sobre circulação de mercadorias, prestação de serviços de transporte interestadual/intermunicipal e de comunicação, além de importação. Não cumulativo e seletivo.",
                "subtopicos": [
                    {"titulo": "Hipóteses de incidência", "texto": "Saída de mercadoria, importação, serviços de transporte e comunicação, fornecimento de energia e de mercadoria com serviço não tributado pelo ISS."},
                    {"titulo": "Não cumulatividade", "texto": "Compensa-se o imposto devido com o cobrado nas operações anteriores (crédito), evitando a tributação em cascata ao longo da cadeia."},
                ],
            },
            {
                "titulo": "3. ICMS — base de cálculo, alíquotas e substituição tributária",
                "explicacao": "A base é o valor da operação; as alíquotas variam por produto (seletividade) e por operação (interna/interestadual). A substituição tributária concentra o recolhimento em um responsável.",
                "subtopicos": [
                    {"titulo": "Alíquotas internas e interestaduais", "texto": "Operações internas seguem a alíquota do Estado; interestaduais usam alíquotas fixadas pelo Senado, com partilha do diferencial (DIFAL) ao destino."},
                    {"titulo": "Substituição tributária (ST)", "texto": "Antecipa-se o ICMS de toda a cadeia por meio de um substituto (geralmente o fabricante/importador), simplificando a fiscalização."},
                ],
            },
            {
                "titulo": "4. ICMS — benefícios fiscais e documentos",
                "explicacao": "Isenções, reduções de base e créditos outorgados dependem de convênios no CONFAZ. Obrigações acessórias incluem a emissão de documentos fiscais eletrônicos (NF-e, CT-e) e a EFD.",
                "subtopicos": [
                    {"titulo": "Convênios CONFAZ", "texto": "Benefícios de ICMS exigem deliberação unânime dos Estados via convênio, para evitar a guerra fiscal entre as unidades federadas."},
                    {"titulo": "Documentos fiscais eletrônicos", "texto": "NF-e, NFC-e, CT-e e a Escrituração Fiscal Digital (EFD) integram o SPED e instrumentalizam a fiscalização eletrônica."},
                ],
            },
            {
                "titulo": "5. ITCD — Transmissão Causa Mortis e Doação",
                "explicacao": "Imposto estadual sobre transmissão gratuita de bens e direitos por herança/legado (causa mortis) ou doação. Em Goiás é regido pelo CTE-GO e legislação específica.",
                "subtopicos": [
                    {"titulo": "Incidência e base", "texto": "Incide sobre o valor venal dos bens transmitidos gratuitamente. O contribuinte é o herdeiro, legatário ou donatário, conforme o caso."},
                ],
            },
            {
                "titulo": "6. IPVA — Propriedade de Veículos Automotores",
                "explicacao": "Imposto estadual anual sobre a propriedade de veículos automotores. Fato gerador é a propriedade; base é o valor venal; alíquotas variam por tipo de veículo.",
                "subtopicos": [
                    {"titulo": "Fato gerador e repartição", "texto": "Ocorre anualmente (e na primeira aquisição/importação). 50% da arrecadação pertence ao município de licenciamento do veículo."},
                ],
            },
            {
                "titulo": "7. Taxas estaduais e legislação correlata",
                "explicacao": "Taxas pelo exercício do poder de polícia e pela prestação de serviços públicos específicos e divisíveis, além de leis, decretos e instruções normativas que regulamentam a legislação tributária goiana.",
                "subtopicos": [
                    {"titulo": "Hierarquia normativa", "texto": "Constituição, leis complementares e ordinárias, decretos (RICMS), instruções normativas e atos do CONFAZ compõem a legislação tributária aplicável."},
                ],
            },
        ],
    },
]
