![](_page_0_Picture_0.jpeg)

# UNIVERSIDADE FEDERAL DO CEARÁ CAMPUS DE CRATEÚS CURSO DE GRADUAÇÃO EM SISTEMAS DE INFORMAÇÃO

#### FRANCISCO DAS CHAGAS ALVES DA SILVA CHAVES

EQUILIBRANDO ANONIMATO E AUTENTICIDADE EM PESQUISAS DE LEVANTAMENTO: EXPLORANDO ASSINATURAS EM ANEL VINCULÁVEIS COMO SOLUÇÃO

#### FRANCISCO DAS CHAGAS ALVES DA SILVA CHAVES

# EQUILIBRANDO ANONIMATO E AUTENTICIDADE EM PESQUISAS DE LEVANTAMENTO: EXPLORANDO ASSINATURAS EM ANEL VINCULÁVEIS COMO SOLUÇÃO

Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em Sistemas de Informação do Campus de Crateús da Universidade Federal do Ceará, como requisito parcial à obtenção do grau de bacharel em Sistemas de Informação.

Orientador: Prof. Dr. Emerson B. Tomaz

Coorientador: Prof. Dr. Allysson Allex Araújo

#### Dados Internacionais de Catalogação na Publicação Universidade Federal do Ceará Sistema de Bibliotecas

Gerada automaticamente pelo módulo Catalog, mediante os dados fornecidos pelo(a) autor(a)

C438e Chaves, Francisco das Chagas Alves Da Silva.

 Equilibrando Anonimato e Autenticidade em Pesquisas de Levantamento: Explorando Assinaturas em Anel Vinculáveis como Solução / Francisco das Chagas Alves Da Silva Chaves. – 2025.

65 f. : il. color.

 Trabalho de Conclusão de Curso (graduação) – Universidade Federal do Ceará, Campus de Crateús, Curso de Sistemas de Informação, Crateús, 2025.

Orientação: Prof. Dr. Antônio Emerson Barros Tomaz.

Coorientação: Prof. Dr. Allysson Allex de Paula Araújo.

 1. Pesquisas de Levantamento. 2. Assinaturas de Anéis Vinculáveis. 3. Anonimato. 4. Autenticidade . I. Título.

CDD 005

#### FRANCISCO DAS CHAGAS ALVES DA SILVA CHAVES

# EQUILIBRANDO ANONIMATO E AUTENTICIDADE EM PESQUISAS DE LEVANTAMENTO: EXPLORANDO ASSINATURAS EM ANEL VINCULÁVEIS COMO SOLUÇÃO

Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em Sistemas de Informação do Campus de Crateús da Universidade Federal do Ceará, como requisito parcial à obtenção do grau de bacharel em Sistemas de Informação.

Aprovada em:

#### BANCA EXAMINADORA

Prof. Dr. Emerson B. Tomaz (Orientador) Universidade Federal do Ceará (UFC)

Prof. Dr. Allysson Allex Araújo (Coorientador) Universidade Federal do Cariri (UFCA)

Prof. Dr. José Wellington Franco da Silva Universidade Federal do Ceará (UFC)

Prof. Dr. Ricardo Ferreira Vilela Universidade Federal do Cariri (UFCA)

#### AGRADECIMENTOS

Inicialmente, gostaria de agradecer à minha mãe, Krislene, e à minha avó, Maria Alves, por todo o amor, cuidado, paciência e apoio. Agradeço também por todas as batalhas que elas enfrentaram em prol da minha educação.

Agradeço também à minha namorada, Edulene, pelo carinho, compreensão e apoio constante. Sua presença ao meu lado, especialmente nos momentos mais difíceis, foi uma grande força para que eu mantivesse a motivação e concentração necessárias para concluir este trabalho.

Por fim, agradeço aos professores da UFC-Crateús, em especial aos professores Emerson, Allysson e José Wellington. Agradeço por todos os ensinamentos e inspirações ao longo da minha trajetória acadêmica.

![](_page_5_Picture_0.jpeg)

#### RESUMO

Pesquisa de levantamento (em inglês, *survey*) é um método sistemático para coletar dados e informações de uma amostra representativa de uma população. No entanto, equilibrar anonimato e autenticidade dos participantes representa um desafio significativo. A presente pesquisa aborda a dificuldade de garantir simultaneamente o anonimato e a autenticidade dos participantes em pesquisas de levantamento. O anonimato sem autenticação pode levar à participação indevida, enquanto a autenticação sem anonimato pode desencorajar respostas sinceras devido ao medo de exposição. Diante disso, respaldado numa estratégia multimetodo baseado *Design Science Research* (DSR) este trabalho visa desenvolver um modelo para pesquisas de levantamento utilizando o esquema de Assinatura em Anel Vinculável, que assegure simultaneamente o anonimato e a autenticidade dos participantes em pesquisas de levantamento. A avaliação foi estruturada em duas perspectivas analíticas complementares, abrangendo, respectivamente, uma análise qualitativa e uma análise quantitativa. Inicialmente, a análise qualitativa foi conduzida por meio de uma abordagem baseada em cenários representativos, enquanto que a quantitativa foi conduzida uma análise baseada em simulações computacionais com intuito de examinar o desempenho da solução e verificar sua viabilidade prática. De forma geral, a análise qualitativa evidenciou que o modelo atende aos requisitos de anonimato e autenticidade. Já a análise quantitativa evidenciam que os algoritmos apresentam tempos compatíveis com aplicações em larga escala. Em termos de contribuições, destaca-se a aplicação inovadora do esquema de assinaturas em anel vinculáveis, originalmente usado em votação eletrônica, para resolver o conflito entre anonimato e autenticidade em pesquisas de levantamento, garantindo respostas honestas e eliminando participação indevida. Além disso, este modelo avança no campo da cibersegurança ao responder à crescente demanda por mecanismos que protejam a privacidade e integridade dos dados em pesquisas de levantamento, beneficiando tanto o meio acadêmico quanto a indústria de software.

Keywords: Pesquisas de Levantamento. Assinaturas de Anéis Vinculáveis. Anonimato. Autenticidade

#### ABSTRACT

Survey research is a systematic method for collecting data and information from a representative sample of a population. However, balancing anonymity and authenticity of participants represents a significant challenge. This research addresses the difficulty of simultaneously ensuring anonymity and authenticity of participants in survey research. Anonymity without authentication can lead to unauthorized participation, while authentication without anonymity can discourage honest responses due to fear of exposure. In light of this, supported by a multi-method strategy based on *Design Science Research* (DSR), this work aims to develop a model for survey research using the Linkable Ring Signature scheme, which ensures both anonymity and authenticity of participants in survey research. The evaluation was structured into two complementary analytical perspectives, encompassing qualitative and quantitative analyses, respectively. Initially, the qualitative analysis was conducted through a scenario-based approach using representative cases, while the quantitative analysis involved simulations aimed at examining the solution's performance and verifying its practical feasibility. Overall, the qualitative analysis demonstrated that the model meets the requirements of anonymity and authenticity. Meanwhile, the quantitative analysis showed that the algorithms deliver execution times compatible with large-scale applications. In terms of contributions, the innovative application of the Linkable Ring Signature scheme, originally used in electronic voting, stands out as a solution to the conflict between anonymity and authenticity in survey research, ensuring honest responses and eliminating unauthorized participation. Additionally, this model advances the field of cybersecurity by addressing the growing demand for mechanisms that protect privacy and data integrity in survey research, benefiting both academia and the software industry.

Keywords: Survey Research; Linkable Ring Signatures; Anonymity; Authenticity

### LISTA DE ILUSTRAÇÕES

| Figura 1<br>–<br>Criptografia de chave pública para confidencialidade .                     | 20 |
|---------------------------------------------------------------------------------------------|----|
| Figura 2<br>–<br>Criptografia de chave pública para autenticação                            | 20 |
| Figura 3<br>–<br>Fluxo para verificar a duplicidade de assinatura.                          | 22 |
| Figura 4<br>–<br>Método baseado em DSR                                                      | 27 |
| Figura 5<br>–<br>Arquitetura do modelo proposto.                                            | 32 |
| Figura 6<br>–<br>Fluxo da solução proposta.                                                 | 35 |
| Figura 7<br>–<br>Diagrama de sequência do fluxo principal da solução                        | 38 |
| Figura 8<br>–<br>Valor da ordem dos número inteiros utilizados nos cálculos.                | 41 |
| Figura 9<br>–<br>Resposta da API quando o participante responde a pesquisa mais de uma vez. | 45 |
| Figura 10 – Visualização do Link Expirado                                                   | 48 |
| Figura 11 – Visualização das Chaves geradas                                                 | 48 |
| Tempo médio do algoritmo de<br>por número de chaves públicas (em<br>Figura 12 –<br>Sig      |    |
| segundos).                                                                                  | 50 |
| Figura 13 –<br>Tempo médio do algoritmo de<br>por número de chaves públicas (em<br>Ver      |    |
| segundos).                                                                                  | 51 |
| Figura 14 – Configuração do experimento no JMeter                                           | 53 |
| Figura 15 – Tempo de Resposta para o Algoritmo<br>Gen<br>(em segundos)                      | 54 |
| Figura 16 – Tempo de resposta para o Algoritmo<br>(em segundos) .<br>Ver                    | 54 |
| Figura 17 – Tempo de resposta para o Algoritmo<br>(em segundos) .<br>Sig                    | 55 |
| Figura 18 – Tempo de resposta para o Algoritmo<br>Link<br>(em segundos)                     | 56 |

#### LISTA DE ABREVIATURAS E SIGLAS

<span id="page-9-2"></span>DSR *Design Science Research*

<span id="page-9-4"></span>GNFS *General Number Field Sieve*

<span id="page-9-5"></span>LGPD *Lei Geral de Proteção de Dados Pessoais*

<span id="page-9-1"></span>LRS *Linkable Ring Signatures*

<span id="page-9-6"></span>RGPD *Regulamento Geral sobre a Proteção de Dados*

<span id="page-9-0"></span>VPN *Virtual Private Network*

<span id="page-9-3"></span>WSGI *Web Server Gateway Interface*

## SUMÁRIO

| 1       | INTRODUÇÃO .                                                              | 12 |
|---------|---------------------------------------------------------------------------|----|
| 1.1     | Declaração do problema e questões de pesquisa                             | 13 |
| 1.2     | Objetivo geral                                                            | 14 |
| 1.3     | Objetivos específicos                                                     | 14 |
| 1.4     | Contribuições                                                             | 14 |
| 1.5     | Estrutura do trabalho                                                     | 15 |
| 2       | FUNDAMENTAÇÃO TEÓRICA                                                     | 16 |
| 2.1     | Pesquisas de levantamento                                                 | 16 |
| 2.2     | Anonimato digital como uma ferramenta para alcançar a privacidade         | 17 |
| 2.3     | Criptografia como ferramenta para garantir autenticidade de mensagens     |    |
|         | digitais                                                                  | 19 |
| 2.4     | Assinatura em anel vinculável                                             | 21 |
| 3       | TRABALHOS RELACIONADOS                                                    | 23 |
| 4       | PROCEDIMENTOS METODOLÓGICOS                                               | 27 |
| 5       | PROPOSTA .                                                                | 32 |
| 5.1     | Modelo arquitetural                                                       | 32 |
| 5.2     | Implementação da API e estrutura dos dados                                | 34 |
| 5.3     | Fluxo da solução proposta                                                 | 35 |
| 6       | RESULTADOS E ANÁLISES                                                     | 39 |
| 6.1     | Análise qualitativa                                                       | 39 |
| 6.1.1   | Cenário #1 – Solução atinge seu objetivo conforme especificado            | 39 |
| 6.1.2   | Cenário #2 – Pesquisador tenta descobrir quem foi responsável por determi |    |
|         | nada resposta                                                             | 40 |
| 6.1.3   | Cenário #3 – Pessoas que tentam responder à pesquisa mais de uma vez      | 43 |
| 6.1.4   | Cenário #4 – Pessoas não autorizadas tentam responder à pesquisa          | 45 |
| 6.2     | Análise quantitativa                                                      | 49 |
| 6.2.1   | Análise do tempo dos algoritmos LRS                                       | 49 |
| 6.2.2   | Análise de escalabilidade na nuvem                                        | 51 |
| 6.2.2.1 | Análise do tempo de resposta                                              | 52 |
| 7       | DISCUSSÃO                                                                 | 57 |

| 8 | CONSIDERAÇÕES FINAIS | 60 |
|---|----------------------|----|
|   | REFERÊNCIAS          | 61 |

## <span id="page-12-0"></span>1 INTRODUÇÃO

Pesquisas de levantamento (em inglês, *surveys*) são investigações descritivas usadas para coletar dados de uma amostra representativa da população-alvo [\(MATHIYAZHAGAN;](#page-62-0) [NANDAN, 2010\)](#page-62-0). Dado seu emprego frequente na descrição e exploração do comportamento humano, essas pesquisas são amplamente utilizadas em estudos sociais e psicológicos [\(SINGLE-](#page-63-0)[TON](#page-63-0) *et al.*, [1988\)](#page-63-0). Empresas, universidades, hospitais e agências governamentais frequentemente utilizam pesquisas de levantamento para coletar dados e avaliar suas operações. De acordo com [Johnson e Smith](#page-62-1) [\(2017\)](#page-62-1), as pesquisas de levantamento apresentam vários benefícios, como facilidade na análise de dados, transparência nos métodos utilizados e cobertura da população em estudo. Dessa forma, a pesquisa de levantamento revela-se uma abordagem bastante útil e legítima, proporcionando benefícios claros ao descrever e explorar variáveis e aspectos de interesse relacionados ao tema em estudo [\(PONTO, 2015\)](#page-63-1).

No entanto, a manipulação de dados sensíveis e opiniões privadas levanta preocupações sobre privacidade e segurança, exigindo garantias de que tais informações não serão compartilhadas ou expostas a terceiros não autorizados. É comum, nesse cenário, que os participantes desejem responder à pesquisa de forma anônima. O anonimato é um estado de não ser identificado individualmente em um grupo de participantes, de modo que as informações fornecidas não possam ser vinculadas à identidade da pessoa [\(PFITZMANN; HANSEN, 2000\)](#page-63-2). A garantia do anonimato dos participantes é um requisito fundamental, pois protege suas informações e assegura que serão tratadas com discrição. Além disso, a preservação do anonimato incentiva os participantes a responderem abertamente às perguntas da pesquisa.

Outro aspecto relevante das pesquisas de levantamento é assegurar que elas representem com precisão a população-alvo, garantindo a confiabilidade e validade dos dados, bem como a autenticação dos participantes. Conforme definido por [Gaharana e Anand](#page-61-1) [\(2015\)](#page-61-1), a autenticação refere-se ao processo de verificação da identidade de um usuário para acessar um sistema ou serviço. Sem esse processo, participantes indesejados de outros grupos podem se envolver na pesquisa, o que pode comprometer a precisão dos dados. Portanto, a autenticação não só reforça a credibilidade dos resultados, como também aprimora a qualidade dos dados, garantindo uma utilização mais eficiente e confiável das informações coletadas.

Entretanto, conciliar o anonimato e a autenticidade dos participantes é um desafio considerável. O anonimato visa garantir que o participante não seja identificado, mantendo em segredo sua identidade. Já a autenticidade busca verificar a identidade do participante. Surge, consequentemente, a necessidade de encontrar um ponto de equilíbrio entre esses dois princípios aparentemente opostos. Diante desse desafio, uma proposta inicial para resolver o conflito entre autenticidade e anonimato foi proposta por [Rivest](#page-63-3) *et al.* [\(2001\)](#page-63-3), que propuseram um esquema conhecido como assinatura em anel. Nesse esquema, um signatário, pertencente a um grupo específico (o anel), pode assinar uma mensagem de forma que a autenticidade da assinatura seja verificável como proveniente de alguém do grupo. A assinatura em anel é construída de forma que o verificador pode confirmar que a mensagem foi assinada por alguém do grupo, mas não consegue determinar qual membro específico produziu a assinatura.

No entanto, a assinatura em anel pode não ser adequado para pesquisas de levantamento, pois não permite determinar se duas assinaturas foram emitidas pelo mesmo participante, o que pode resultar na submissão de respostas múltiplas por um único participante. Para lidar com essa limitação, [Liu e Wong](#page-62-2) [\(2005\)](#page-62-2) propuseram um esquema de assinatura em anel vinculável, que permite verificar se duas assinaturas foram emitidas pelo mesmo membro do grupo. Essa solução apresenta potencial para resolver o conflito entre anonimato e autenticidade em pesquisas de levantamento, além de prevenir a duplicação de participações por um mesmo indivíduo.

#### <span id="page-13-0"></span>1.1 Declaração do problema e questões de pesquisa

A preocupação com a privacidade pode levar os participantes a hesitarem em compartilhar dados sensíveis ou opiniões privadas, resultando em respostas enviesadas que comprometem os resultados da pesquisa [\(HOHENBERGER](#page-62-3) *et al.*, [2014\)](#page-62-3). Nesse sentido, a anonimização dos participantes em pesquisas de levantamento é um aspecto crítico para preservar a privacidade. Todavia, essa prática pode eventualmente permitir que pessoas fora do grupo estudado se insiram como participantes indesejados. Essa inclusão indevida pode distorcer os resultados e afetar a validade da pesquisa. Logo, é fundamental confirmar a participação apenas de membros legítimos e autorizados na pesquisa, garantindo assim a autenticidade dos participantes e a qualidade dos dados coletados.

Diante do conflito intrínseco entre o anonimato e a autenticidade dos participantes em pesquisas de levantamento, surge a seguinte questão de pesquisa: *Como o esquema de assinatura em anel vinculável pode ser implementado em pesquisas de levantamento para aprimorar a preservação da privacidade, garantindo simultaneamente a autenticidade dos participantes e o anonimato de suas identidades?*

#### <span id="page-14-0"></span>1.2 Objetivo geral

Desenvolver um modelo arquitetural baseado assinaturas em anel vinculáveis para pesquisas de levantamento que garanta simultaneamente o anonimato e a autenticidade dos participantes, promovendo, assim, a integridade dos dados coletados e fortalecendo a confiança nos resultados obtidos.

#### <span id="page-14-1"></span>1.3 Objetivos específicos

- Descrever o modelo baseado no esquema de assinatura de anel vinculável, explicando como seus componentes interagem para garantir anonimato e autenticidade em pesquisas de levantamento;
- Implementar o modelo e avaliar seu desempenho considerando a eficiência computacional e a escalabilidade;
- Validar a eficácia do modelo em ambiente simulado demonstrando sua aplicabilidade e benefícios em pesquisas de levantamento;

#### <span id="page-14-2"></span>1.4 Contribuições

Este trabalho apresenta contribuições importantes para o campo das pesquisas de levantamento, focando no desafio de assegurar simultaneamente o anonimato e a autenticidade dos participantes por meio de um esquema criptográfico de assinatura em anel vinculável. Embora esse esquema criptográfico tenha sido proposto inicialmente para sistemas de votação eletrônica [\(LIU; WONG, 2005\)](#page-62-2), sua aplicação para garantir anonimato e autenticidade em pesquisas de levantamento representa uma abordagem inovadora e promissora. A integração dos benefícios do anonimato com a autenticação dos participantes oferece um novo caminho para a condução ética e confiável de pesquisas que envolvem dados sensíveis.

Este trabalho destaca a importância da autenticação para a validade dos dados em pesquisas de levantamento. Ao implementar assinaturas em anel vinculáveis, assegura-se que somente membros legítimos da população-alvo participem, eliminando a influência de participantes não autorizados e aumentando a credibilidade dos resultados. Adicionalmente, a garantia do anonimato, possibilitada pelo modelo proposto, tem o potencial de incentivar respostas mais sinceras e honestas, especialmente em pesquisas que envolvem dados sensíveis ou opiniões privadas.

Por fim, o modelo proposto avança no campo da cibersegurança ao atender à crescente demanda por mecanismos que protejam a privacidade e integridade dos dados coletados em pesquisas com dados sensíveis. As implicações práticas abrangem os contextos acadêmico e corporativo. Ao demonstrar a eficácia das assinaturas em anel vinculáveis, esta pesquisa pode orientar futuros projetos na adoção de práticas avançadas de segurança de dados e proteção de privacidade em pesquisa de levantamento.

#### <span id="page-15-0"></span>1.5 Estrutura do trabalho

O presente trabalho está estruturado em cinco capítulos, incluindo esta Introdução. O [Capítulo 2](#page-16-0) abrange todo o embasamento teórico para a compreensão desta pesquisa. Em seguida, no [Capítulo 3,](#page-23-0) são apresentados os trabalhos relacionados. No [Capítulo 4,](#page-27-1) é explicado o procedimento metodológico adotado neste estudo. No [Capítulo 5](#page-32-1) é apresentado a proposta do modelo em conjunto com a arquitetura e fluxo da solução. O [Capítulo 6](#page-39-0) tem como objetivo discutir e apresentar os resultados obtidos acerca da solução proposta. Já o [Capítulo 7](#page-57-0) promove uma discussão a luz da literatura sobre os principais resultados obtidos. Por fim, no [Capítulo 8,](#page-60-0) o trabalho é concluído e são apresentados os trabalhos futuros.

## <span id="page-16-0"></span>2 FUNDAMENTAÇÃO TEÓRICA

Este capítulo visa fornecer o embasamento teórico essencial para a compreensão desta pesquisa. Inicialmente, será abordada a importância das pesquisas de levantamento (Seção [2.1\)](#page-16-1). Em seguida, será explicado o conceito de anonimato (Seção [2.2\)](#page-17-0). Posteriormente, será discutido o conceito de criptografia de chave pública (Seção [2.3\)](#page-19-0). Por fim, serão apresentados os algoritmos e a relevância da assinatura em anel vinculável (Seção [2.4\)](#page-21-0).

#### <span id="page-16-1"></span>2.1 Pesquisas de levantamento

Pesquisas de levantamento são definidas como a coleta de informações de uma amostra de indivíduos por meio de suas respostas às perguntas [\(CHECK; SCHUTT, 2011\)](#page-61-2). Segundo Lee *[et al.](#page-62-4)* [\(2012\)](#page-62-4), a pesquisa por levantamento é um método sistemático de coleta de dados no qual amostras são selecionadas, entrevistados são questionados, e os dados são analisados para extrapolar para uma população de interesse. Estas podem utilizar tanto a população total (censo populacional) como amostras da população para recolher estes dados [\(COUGHLAN](#page-61-3) *et al.*, [2009\)](#page-61-3). Assim, as pesquisas de levantamento desempenham um papel fundamental, oferecendo muitas vantagens na coleta e análise de dados.

Uma das principais vantagens da pesquisa de levantamento reside em sua capacidade de acumular rapidamente dados de um grande número de entrevistados em um espaço de tempo relativamente curto [\(ANWAR](#page-61-4) *et al.*, [2021\)](#page-61-4). Essa eficiência facilita a obtenção de dados de diversos grupos. Outra vantagem, destacada por [Shreya](#page-63-4) [\(2022\)](#page-63-4), é a capacidade de generalização, na qual uma amostra de alguns indivíduos de uma população pode representar os dados de uma população total. Logo, o entrevistador não tem a necessidade de realizar o questionário com toda a população.

No entanto, para aproveitar integralmente das vantagens e conveniências das pesquisas de levantamento em determinados contextos, a garantia do anonimato dos participantes é fundamental. [Kang e Hwang](#page-62-5) [\(2023\)](#page-62-5) salientam que, ao garantir o anonimato dos participantes, estes têm maior probabilidade de oferecer respostas genuínas às perguntas, contribuindo para resultados mais fidedignos e de alta qualidade. [Robertson](#page-63-5) *et al.* [\(2018\)](#page-63-5) realizaram uma pesquisa, na qual comprovaram que pessoas se sentem mais confortáveis a responder questões sensíveis, como aquelas envolvendo orientação sexual, quando o questionário é anônimo, principalmente quando este é *online*. No entanto, conforme citado por [Edman e Yener](#page-61-5) [\(2009\)](#page-61-5), a infraestrutura

de comunicações moderna é capaz de identificar e registrar ações realizadas, destinos de dados e até mesmo o conteúdo das comunicações na Internet. Essa capacidade levanta preocupações não apenas técnicas, mas também éticas, pois, mesmo quando os dados são coletados sob a premissa do anonimato, não há garantia de que serão utilizados de maneira ética e em conformidade com o propósito originalmente declarado. Assim, garantir o anonimato em pesquisas de levantamento *online* torna-se um desafio técnico significativo.

Outro desafio a ser abordado é a identificação de participantes aptos a responderem à pesquisa, na qual um mecanismo de autenticação tem um papel fundamental. A autenticidade, neste contexto de autenticação de usuário, refere-se ao processo de verificação da identidade de um usuário para acessar um sistema ou serviço [\(GAHARANA; ANAND, 2015\)](#page-61-1). Assim, manter a autenticidade dos participantes em pesquisas de levantamento é essencial. Um exemplo é a pesquisa de levantamento realizada por [Pratt-Chapman](#page-63-6) *et al.* [\(2021\)](#page-63-6), na qual mais da metade dos participantes eram *bots* (robôs automatizados). Portanto, a falta de autenticação pode resultar na participação de usuários não autorizados, comprometendo a integridade dos dados da pesquisa.

Portanto, apesar das inúmeras vantagens que tornam as pesquisas de levantamento uma ferramenta valiosa na coleta e análise de dados, sua aplicação eficaz exige atenção cuidadosa a desafios técnicos e éticos. A garantia simultânea do anonimato e da autenticidade dos participantes representa uma dualidade complexa, mas essencial para a credibilidade e a integridade dos resultados obtidos. Somente ao enfrentar esses desafios de maneira sistemática será possível explorar todo o potencial das pesquisas de levantamento, assegurando que seus dados reflitam, com precisão e confiabilidade, as populações que pretendem representar

#### <span id="page-17-0"></span>2.2 Anonimato digital como uma ferramenta para alcançar a privacidade

Anonimato e privacidade são conceitos distintos que muitas vezes são equivocadamente utilizados como termos intercambiáveis [\(BRADBURY, 2014\)](#page-61-6). O anonimato é a propriedade de manter em segredo a identidade do usuário que realiza determinada ação [\(YANG;](#page-64-0) [XIAO, 2022\)](#page-64-0). Assim, a ideia central do anonimato é assegurar aos usuários de uma atividade ou serviço específico que sua identificação permanecerá protegida e que terceiros não poderão descobrir sua identidade, mesmo em ambientes *online*. Já a privacidade diz respeito à garantia de que os indivíduos possam controlar ou influenciar quais informações pessoais relacionadas a eles são coletadas e armazenadas, bem como a maneira, por quem e para quem tais informações podem ser divulgadas [\(STALLINGS, 2014\)](#page-63-7). Portanto, enquanto o anonimato se concentra na

proteção da identidade do usuário, a privacidade abrange um aspecto mais amplo de informações pessoais e controle sobre elas.

É importante notar que, conforme argumentado por [Novak](#page-62-6) [\(2014\)](#page-62-6), o conceito de anonimato está intrinsecamente ligado ao de privacidade, pois envolve a capacidade de realizar atividades ou transmitir informações sem revelar sua identidade pessoal. No entanto, [Waldo](#page-64-1) *et [al.](#page-64-1)* [\(2010\)](#page-64-1) ressaltam que o anonimato é apenas um subconjunto da privacidade, já que é uma forma específica de proteger a privacidade. Além disso, o anonimato assegura privacidade até certo ponto, prevenindo a identificação direta da pessoa. Contudo, outras informações podem ser coletadas e usadas para desanonimizar o indivíduo, o que significa que o anonimato não oferece uma privacidade absoluta, mas sim em relação à identidade pessoal. Mesmo assim, o anonimato desempenha um papel fundamental na preservação da privacidade, tornando necessária a busca por mecanismos eficazes para garantir a proteção da identidade e das informações pessoais.

[Hoang e Pishva](#page-61-7) [\(2014\)](#page-61-7) citam algumas ferramentas comumente utilizadas para garantir o anonimato *online*, como: *proxies*, redes privadas virtuais, do inglês *[Virtual Private](#page-9-0) [Network](#page-9-0)* (VPN) e a rede Tor, uma aplicação que emprega múltiplas camadas de roteamento que torna difícil rastrear a origem e o destino das comunicações. O Tor, em particular, é destacado por [Bradbury](#page-61-6) [\(2014\)](#page-61-6) como uma das ferramentas de anonimato mais robustas disponíveis. No entanto, mesmo com suas medidas de segurança, o Tor ainda apresenta algumas vulnerabilidades, principalmente relacionadas à análise de tráfego em pontos de entrada e saída da rede, além de possíveis comprometimentos por meio de falhas em navegadores e pulins. Além disso, diversos serviços *online* e plataformas corporativas implementam bloqueios sistemáticos aos usuários do Tor, prejudicando sua utilidade para navegação cotidiana.

Mesmo diante de técnicas conhecidas para preservar o anonimato, a privacidade ainda pode ser ameaçada. [Farrall](#page-61-8) [\(2008\)](#page-61-8) destaca que o anonimato, como mencionado anteriormente, especialmente no contexto das interações na Internet, não garante necessariamente a privacidade. Um exemplo é explicado por [Chakravarty](#page-61-9) *et al.* [\(2011\)](#page-61-9), no qual até mesmo sistemas de comunicação anônima como a rede Tor podem expor dados sigilosos, caso estes não sejam adequadamente cifrados. Isso ocorre porque, quando o tráfego retransmitido atinge os limites da rede de sobreposição em direção ao seu destino real, o tráfego do usuário original é inevitavelmente exposto, comprometendo a confidencialidade das informações.

#### <span id="page-19-0"></span>2.3 Criptografia como ferramenta para garantir autenticidade de mensagens digitais

A criptografia é o estudo de técnicas matemáticas relacionadas a aspectos de segurança da informação, como confidencialidade, integridade e autenticidade [\(MENEZES](#page-62-7) *et al.*, [2018\)](#page-62-7). Segundo [Stallings](#page-63-7) [\(2014\)](#page-63-7), até os anos 1970, o único método existente de criptografia era o simétrico, até a criação da criptografia de chave pública. A criptografia simétrica consiste na utilização da mesma chave para cifrar e decifrar uma mensagem [\(LIGUORI, 2022\)](#page-62-8). Assim, de acordo com [Zhang](#page-64-2) [\(2021\)](#page-64-2), tanto o emissor quanto o receptor precisam se encontrar em um momento anterior para compartilhar as suas chaves secretas. Caso alguém consiga descobrir a chave e o algoritmo utilizado, toda a comunicação poderá ser lida facilmente.

Um dos problemas da criptografia simétrica é que ela não garante autenticidade [\(OLIVEIRA, 2012\)](#page-62-9). O principal desafio aqui é que, em certos cenários, pode ser necessário identificar o autor da mensagem. No entanto, quando remetente e destinatário usam a mesma chave, torna-se impossível validar essa informação. Para resolver esse problema, [Diffie e Hellman](#page-61-10) [\(1976\)](#page-61-10) introduziram o conceito de criptografia de chave pública.

Ao contrário da criptografia simétrica, a criptografia de chave pública (ou criptografia assimétrica) permite enviar e receber mensagens sem a necessidade de trocar uma chave secreta com a outra parte [\(KRZYWORZEKA, 2016\)](#page-62-10). Como definido por [Stallings](#page-63-7) [\(2014\)](#page-63-7), a criptografia de chave pública envolve o uso de um par de chaves, sendo uma delas privada e a outra pública. A chave privada é mantida estritamente em segredo pelo proprietário, enquanto a chave pública pode ser divulgada livremente para permitir a transferência segura de dados. Dessa forma, este método pode ser utilizado em dois cenários, um para garantir confidencialidade e outro para autenticidade [\(BRAGA; DAHAB, 2018\)](#page-61-11).

A Figura [1](#page-20-0) exemplifica o processo de criptografia de chave pública para garantir confidencialidade. Esse cenário ocorre quando alguém deseja enviar uma mensagem de modo que apenas o destinatário possa acessá-la. Inicialmente, o remetente cifra a mensagem usando a chave pública do destinatário, podendo então enviá-la por qualquer canal, mesmo que inseguro. Quando o destinatário recebe a mensagem, ele decifra usando sua chave privada. Dessa forma, como somente a chave privada do destinatário é capaz de decifrar a mensagem, apenas ele irá ter acesso ao seu conteúdo.

O outro cenário garantido pela criptografia de chave pública é o da autenticidade. Neste contexto, a autenticidade refere-se à capacidade de cada destinatário de uma mensagem verificar a identidade do remetente e a integridade das mensagens emitidas por ele [\(ALAGHE-](#page-61-12)

Chave pública do receptor

Chave pública do receptor

Chave privada do receptor

Texto claro

Algoritmo de cifração

Texto claro

Receptor

Chave privada do receptor

Algoritmo de decifração

<span id="page-20-0"></span>Figura 1 – Criptografia de chave pública para confidencialidade

Fonte: adaptada de Stallings (2014).

BAND; MASHATAN, 2022). Garantir a autenticidade de documentos digitais é fundamental quando estes devem ser aceitos como oficiais em qualquer tipo de acordo (TANWAR; KUMAR, 2019). Nesse cenário, a criptografia de chave pública surge como uma ferramenta essencial para assegurar a autenticidade de mensagens digitais.

Remetente Receptor Chave pública Chave privada do remetente do remetente Algoritmo de Algoritmo de Texto claro Texto cifrado Texto claro cifração decifração (texto assinado) (assinatura) (verificação)

<span id="page-20-1"></span>Figura 2 – Criptografia de chave pública para autenticação

Fonte: adaptada de Stallings (2014).

A Figura 2 demonstra como a criptografia de chave pública garante a autenticidade dos dados. Este cenário ocorre quando uma pessoa deseja assinar digitalmente uma mensagem, o que envolve cifrar a mensagem com sua própria chave privada. Com isso, apenas a chave

pública desse usuário irá conseguir decifrar a mensagem, garantido que foi ele quem assinou a mensagem.

#### <span id="page-21-0"></span>2.4 Assinatura em anel vinculável

Assinaturas em anel vinculáveis, do inglês *[Linkable Ring Signatures](#page-9-1)* (LRS), é uma variante da assinatura em anel tradicional desenvolvida por [Liu e Wong](#page-62-2) [\(2005\)](#page-62-2) que permite que uma pessoa assine uma mensagem como parte de um grupo (anel), mantendo seu anonimato dentro do grupo, mas com uma característica adicional importante: é possível detectar quando a mesma chave secreta é usada mais de uma vez para assinar, ou seja, quando a mesma pessoa realiza múltiplas assinaturas.

A ideia principal da [LRS,](#page-9-1) conforme [Liu e Wong](#page-62-2) [\(2005\)](#page-62-2), é fornecer anonimato ao signatário, mas ao mesmo tempo determinar se duas assinaturas foram emitidas pelo mesmo membro de um grupo. Ela pode se mostrar extremamente útil para a implementação de sistemas de votação eletrônica. Para votar, o eleitor gera uma assinatura vinculável para seu voto. O anonimato é mantido e a vinculação ajuda a detectar o voto duplo se um eleitor fizer dois votos. Além disso, as assinaturas em anel vinculáveis eliminam o envolvimento dos eleitores na fase de registro de cada evento de votação e, ao mesmo tempo, evitam o vazamento de informações sobre quais eleitores votaram e quais não votaram.

Formalmente, uma [LRS](#page-9-1) é uma quádrupla (Gen,Sig,Ver,Link), em que:

- (*x*, *y*) ← Gen(1 *k* ) é um algoritmo de geração de chaves que recebe um parâmetro de segurança *k* e gera um par de chaves — a chave privada *x* e a chave pública *y*.
- σ ← Sig(1 *k* ,1 *n* , *x*,*L*,*m*) é um algoritmo que gera uma assinatura. Ele recebe como entrada um parâmetro de segurança *k*, o tamanho do grupo *n*, a chave privada *x* do signatário, uma lista *L* de *n* chaves públicas (incluindo a do signatário) e uma mensagem *m*. O algoritmo então produz uma assinatura σ para essa mensagem.
- 1/0 ← Ver(1 *k* ,1 *n* ,*L*,*m*,σ) é um algoritmo booleano para verificar uma assinatura. Ele aceita como entrada o parâmetro de segurança *k*, o tamanho do grupo *n*, uma lista *L* de *n* chaves públicas, a mensagem *m* e a assinatura σ, e retorna 1 ou 0 para aceitar ou rejeitar, respectivamente. É exigido isso para qualquer mensagem *m*, qualquer (*x*, *y*) ← Gen(1 *k* ) e qualquer *L* que inclua *y*.
- 1/0 ← Link(1 *k* ,1 *n* ,*L*,*m*1,*m*2,σ1,σ2) é um algoritmo booleano para verificar se

duas assinaturas foram emitidas pela mesma pessoa. Ele aceita como entrada um parâmetro de segurança k, o tamanho do grupo n, uma lista L de n chaves públicas, mensagens  $m_1$  e  $m_2$  e assinaturas  $\sigma_1$  e  $\sigma_2$  de tal modo que ele retorna 1 caso as duas assinaturas tenham sido geradas pela mesma pessoa (assinatura vinculada), e 0 caso contrário (assinatura desvinculada).

<span id="page-22-0"></span>Figura 3 – Fluxo para verificar a duplicidade de assinatura.

![](_page_22_Picture_3.jpeg)

Fonte: elaborado pelo autor.

A Figura 3 exemplifica o processo para verificação se duas assinaturas foram emitidas pelo mesmo signatário. Inicialmente, cada signatário gera um par de chaves (uma pública e uma privada), usando o algoritmo  $Gen(1^k)$ . Cada signatário deve assinar a mensagem utilizando sua chave privada x no algoritmo de assinatura  $Sig(1^k, 1^n, x, L, m)$ . O algoritmo de assinatura emprega as chaves públicas de todos os membros signatários do grupo, o que equivale a uma assinatura coletiva do grupo. O verificador pode utilizar o algoritmo  $Link(1^k, 1^n, L, m_1, m_2, \sigma_1, \sigma_2)$  para confirmar se duas assinaturas foram feitas pelo mesmo signatário.

A partir desses algoritmos, Liu e Wong (2005) apresentam três aspectos referentes a segurança do sistema: *impossibilidades de falsificação*, *anonimato do signatário* e *vinculabilidade*. O primeiro refere-se a incapacidade de um invasor forjar uma assinatura para qualquer mensagem que não seja assinada por um signatário legítimo, isso ocorre devido a dificuldade de gerar uma assinatura que satisfaça  $Ver(1^k, 1^n, L, m, \sigma) = 1$ . O segundo aspecto é o anonimato, no qual significa a impossibilidade da identificação de um assinante a partir de um grupo de n usuários. A LRS dificulta a descoberta, isto significa que mesmo que um atacante conheça t chaves privadas, ele não conseguirá descobrir o signatário real com probabilidade maior que 1/(n-t). Por fim, a vinculabilidade refere-se à dificuldade de duas assinaturas feitas por participantes diferentes utilizando o algoritmo  $Sig(1^k, 1^n, x, L, m)$  gerarem 1.

#### <span id="page-23-0"></span>3 TRABALHOS RELACIONADOS

Este capítulo revisa trabalhos relacionados ao problema de garantir anonimato e autenticidade em pesquisas de levantamento, com foco em abordagens criptográficas. Os trabalhos serão apresentados em ordem cronológica, do mais antigo para o mais recente, para demonstrar a evolução das ideias e pesquisas na área, oferecendo uma visão geral das diferentes abordagens e estratégias adotadas para lidar com essas questões-chave.

[Kapis e Korojelo](#page-62-11) [\(2012\)](#page-62-11) apresentam um sistema para pesquisas de levantamento *online* com foco em reforçar a autenticação dos participantes. O sistema distingue entre dois tipos de pesquisas: pesquisas abertas, acessíveis a qualquer pessoa, e pesquisas fechadas, onde o acesso é restrito a participantes convidados. Para pesquisas fechadas, cada participante é previamente cadastrado e recebe um convite por e-mail contendo um link único para a pesquisa. O usuário, então, autentica-se usando seu e-mail e senha previamente cadastrados. As credenciais são armazenadas no banco de dados com hash MD5. Os autores afirmam que o sistema impede múltiplas submissões, bloqueando novas respostas após a primeira submissão bem-sucedida. Embora o uso de hash MD5 proteja as credenciais de acesso, ele não garante o anonimato do participante em relação ao conteúdo das respostas, uma vez que o sistema mantém registro de quem respondeu a cada pesquisa, sendo possível, portanto, relacionar as respostas com a identificação do participante. O anonimato, neste caso, é limitado e depende da confiança no administrador do sistema, que tem acesso a essas informações. Além disso, o uso de MD5 sem *salt* é criticável, pois, conforme apontado por [Rathod](#page-63-8) *et al.* [\(2020\)](#page-63-8), pode ser vulnerável a ataques de dicionário. Um ataque de dicionário é uma técnica de adivinhação de senha na qual o invasor tenta determinar a senha de um usuário tentando sucessivamente palavras de um dicionário (uma lista compilada de senhas prováveis) na expectativa de que uma dessas tentativas de senha seja a senha real do usuário [\(ADAMS, 2019\)](#page-61-13).

[Hohenberger](#page-62-3) *et al.* [\(2014\)](#page-62-3) propõem o ANONIZE, um sistema baseado em *tokens* para garantir anonimato e autenticidade em pesquisas *ad-hoc*. Após a seleção dos participantes autorizados pelo pesquisador, cada pesquisa recebe um identificador (ID) e uma chave pública da pesquisa gerada com base nas identidades dos participantes autorizados. Para que um usuário autorizado participe, é necessário que ele combine a chave pública da pesquisa com sua credencial (*master user token*), gerando assim um token de uso exclusivo usando a função pseudoaleatória. Este token possibilita o acesso e a submissão anônima da pesquisa. Como o *token* é de uso único, ele expira quando o participante submete a pesquisa, garantindo assim que não existam múltiplas

respostas do mesmo usuário. Em termos de resultados, os autores destacam a preservação do anonimato e a autenticidade dos participantes nas pesquisas, além de impedir a submissão de múltiplas respostas. No entanto, o esquema proposto apresenta uma arquitetura complexa, que se baseia em uma intrincada combinação de primitivas criptográficas para a geração do token único, tais como o compromisso de Pedersen, a assinatura de Boneh-Boyen e a função pseudoaleatória de Dodis-Yampolskiy, e na construção de uma prova de conhecimento zero do tipo cSE-NIZK com uma testemunha de múltiplos elementos. Essa complexidade, embora matematicamente sólida, dificulta a implementação e pode comprometer a viabilidade prática do esquema no mundo real, principalmente devido à interação intrincada entre essas primitivas e à estrutura complexa da testemunha da prova de conhecimento zero.

[Lu Li Yuxi](#page-62-12) [\(2016\)](#page-62-12) propõem um sistema para garantir anonimato e autenticidade em pesquisas eletrônicas. Assim como [Hohenberger](#page-62-3) *et al.* [\(2014\)](#page-62-3) no ANONIZE, os autores usam uma combinação de primitivas criptográficas, incluindo NIZK (*Non-Interactive Zero-Knowledge*), esquema de assinatura de Boneh-Boyen, compromisso de Pedersen e funções pseudoaleatórias, para ocultar a identidade do usuário e autenticá-lo. Embora as primitivas sejam semelhantes, a arquitetura do sistema e a forma como essas primitivas são combinadas e aplicadas no protocolo diferem significativamente do ANONIZE. Em termos de resultados, o sistema proposto permite a condução completa de uma pesquisa eletrônica, desde a inicialização até a publicação dos resultados estatísticos, mantendo o anonimato dos participantes e a autenticidade de suas respostas. No entanto, um ponto crucial que não é abordado no artigo é a prevenção de múltiplas respostas por um mesmo usuário, uma limitação significativa em comparação a outros trabalhos na área.

[Ripper](#page-63-9) *et al.* [\(2017\)](#page-63-9) propõem um método para reduzir o viés de desejabilidade social e potencialmente obter respostas mais honestas de participantes adolescentes em pesquisas de levantamento. O viés de desejabilidade social é a tendência dos participantes de responderem a perguntas de uma maneira que eles acreditam ser vista favoravelmente por outros, mesmo que isso signifique relatar informações imprecisas, especialmente em tópicos sensíveis. O método de [Ripper](#page-63-9) *et al.* [\(2017\)](#page-63-9) se baseia na criação de um código secreto gerado pelo próprio participante, com base em oito perguntas cujas respostas, presume-se, não mudam ao longo do tempo. Esse código é então usado como um identificador anônimo, permitindo a ligação de respostas da mesma pessoa em pesquisas repetidas ao longo do tempo, permitindo acompanhar as respostas dos mesmos indivíduos em diferentes momentos, sem a necessidade de coletar informações

pessoalmente identificáveis. Os autores relatam uma alta taxa de correspondência entre as pesquisas, indicando que o método é eficaz para rastrear as respostas do mesmo indivíduo ao longo do tempo, mantendo o anonimato. Os dados foram coletados e gerenciados usando o REDCap, uma plataforma eletrônica projetada para suportar a captura de dados de forma segura para pesquisas. Embora eficaz para o anonimato, o artigo não aborda a questão da autenticidade dos participantes nem oferece mecanismos para impedir a submissão de múltiplas respostas.

[Ardalan](#page-61-14) *et al.* [\(2019\)](#page-61-14) apresentam a arquitetura de um sistema de informação projetado para garantir o anonimato dos respondentes em uma pesquisa online sobre ensino docente. Os autores afirmam que o sistema alcança esse objetivo dissociando a identidade dos respondentes de suas respostas, mantendo as duas partes em bancos de dados distintos e sem qualquer vínculo direto entre elas. O processo ocorre da seguinte maneira: quando um respondente submete a pesquisa, o sistema simultaneamente envia sua identidade para um banco de dados de registro e acompanhamento do curso, enquanto suas respostas são direcionadas para o banco de dados específico da pesquisa. Após a submissão, o sistema elimina os links de acesso à pesquisa de todos os locais onde o respondente poderia clicar para iniciá-la, impedindo assim múltiplas respostas. O artigo assume que a autenticação é realizada por um sistema de login da universidade, mas não esclarece como esse sistema garante a autenticidade dos respondente, ou seja, como verifica se o respondente é elegível para a pesquisa. Além disso, o artigo não discute a possibilidade de conluio entre administradores de banco de dados e pesquisadores desonestos, que poderiam combinar informações dos dois bancos de dados para desanonimizar os respondentes. Essa é uma ameaça significativa à privacidade, considerando que o administrador do banco de dados de registro teria acesso às informações de identificação dos alunos e o pesquisador teria acesso às respostas.

Esta revisão da literatura apresenta diferentes abordagens para o desafio de garantir anonimato e autenticidade em pesquisas de levantamento *online*, porém revela uma série de limitações nas propostas existentes. Essas limitações incluem a complexidade das arquiteturas e das primitivas criptográficas, a dependência da segurança de múltiplos componentes e a necessidade de maior clareza sobre a autenticação. Além disso, a possibilidade de conluio entre agentes internos e a ausência de mecanismos para impedir a submissão de múltiplas respostas também se mostram como pontos fracos em alguns desses trabalhos, conforme sumarizado na Tabela [1.](#page-26-0) Diante dessas lacunas, o presente trabalho propõe um novo esquema para pesquisas de levantamento *online*, baseado em uma arquitetura mais simples e que utiliza assinaturas em anel vinculáveis para garantir, simultaneamente, o anonimato e a autenticidade. Além disso, o esquema proposto permite a distinção de grupos de respondentes, possibilitando análises segmentadas e mantendo o anonimato individual, uma funcionalidade não contemplada em todos os trabalhos analisados. O objetivo é desenvolver um sistema seguro, fácil de implementar e que incentive a participação honesta dos respondentes, contribuindo para a coleta de dados mais confiáveis e válidos. As principais diferenças entre o esquema proposto e os trabalhos relacionados, incluindo as primitivas criptográficas utilizadas, a abordagem para autenticação e a capacidade de impedir múltiplas respostas, estão sumarizadas na Tabela 1.

<span id="page-26-0"></span>Tabela 1 – Comparação dos trabalhos relacionados

| Autores                   | Solução utilizada                     | Anonimato | Autenticidade | Impede<br>múltiplas<br>respostas |  |
|---------------------------|---------------------------------------|-----------|---------------|----------------------------------|--|
| Kapis e Korojelo (2012)   | Hash MD5                              | Limitado  | Sim           | Sim                              |  |
| Hohenberger et al. (2014) | Tokens,<br>cSE-NIZK,<br>entre outras. | Sim       | Sim           | Sim                              |  |
| Liu Li Yuxi (2016)        | NIZK, Boneh-Boyen,<br>Pedersen        | Sim       | Sim           | Não                              |  |
| Ripper et al. (2017)      | Códigos secretos                      | Sim       | Não           | Não                              |  |
| Ardalan et al. (2019)     | Arquitetura de SI                     | Limitado  | Não           | Sim                              |  |
| Trabalho proposto         | LRS                                   | Sim       | Sim           | Sim                              |  |

Fonte: elaborada pelo autor.

# <span id="page-27-1"></span>4 PROCEDIMENTOS METODOLÓGICOS

Este trabalho caracteriza-se como uma pesquisa de natureza aplicada que visa apresentar um modelo que garanta a autenticidade e o anonimato dos participantes em pesquisas de levantamento. A pesquisa se enquadra na forma experimental com uma abordagem qualitativa e quantitativa. O desenho metodológico adotado segue os princípios da *[Design Science](#page-9-2) [Research](#page-9-2)* (DSR). O uso da DSR se justifica pela capacidade em orientar o desenvolvimento de artefatos tecnológicos e a avaliação de sua aplicabilidade em contextos práticos, garantindo que os resultados obtidos sejam tanto teoricamente fundamentados quanto úteis para a prática profissional [\(PEFFERS](#page-63-10) *et al.*, [2007\)](#page-63-10). A Figura [4](#page-27-0) fornece uma visão geral do desenho metodológico, estruturado em cinco estágios sugeridos por Vaishavi e Kuechler (2004).

<span id="page-27-0"></span>Figura 4 – Método baseado em DSR

![](_page_27_Picture_4.jpeg)

Fonte: elaborada pelo autor.

Durante a Conscientização do Problema, foi realizado um levantamento bibliográfico abrangente, incluindo artigos acadêmicos para identificar práticas que garantam a privacidade no contexto de pesquisas de levantamento. Esse levantamento foi feito via Google Scholar durante o mês de abril de 2024, utilizando palavras-chave relacionadas ao escopo deste trabalho, como "anonymous survey system", "non-identifiable survey", "privacy" ,"authenticity", e "authentication". Tal processo resultou em uma amostra de cinco trabalhos relacionados à presente pesquisa, discutidos no Capítulo [3.](#page-23-0) Assim, foi possível constatar que, embora existam trabalhos que abordem anonimato e autenticidade em pesquisas de levantamento, a quantidade de soluções desenvolvidas até o momento é limitada e não aborda integralmente os desafios desse equilíbrio. Além disso, foram identificadas abordagens que, apesar de apresentarem avanços, não discutem em profundidade os desafios dessa dualidade, como a prevenção de múltiplas submissões e a autenticação sem comprometer o anonimato. Logo, esse levantamento bibliográfico permitiu consolidar o entendimento do problema e direcionar o desenvolvimento de uma solução, baseada em assinaturas em anel vinculáveis, que busca lidar com a lacuna identificadas na literatura.

Durante a fase de Sugestão, foi concebido um *tentative design* sob a forma de um modelo arquitetural que seria posteriormente instanciado como artefato em uma aplicação web. Baseando-se no conhecimento obtido na fase anterior, o modelo foi idealizado com foco nos requisitos de três elementos fundamentais: anonimato, autenticidade e prevenção de múltiplas respostas. Nesse contexto, optou-se por adotar o padrão arquitetural *Model-View-Controller* (MVC), amplamente reconhecido por sua capacidade de organizar aplicações complexas em camadas principais. Em particular, a escolha pelo padrão MVC foi motivada por sua capacidade de separar claramente a lógica de negócio, o gerenciamento de dados e a interface do usuário. O modelo arquitetural foi idealizado para ser genérico o suficiente para permitir instâncias em diferentes contextos de pesquisa, mantendo a flexibilidade para adaptações específicas.

A fase de Desenvolvimento consistiu na implementação do modelo arquitetural com foco na construção e a integração dos principais módulos do artefato. Realizada ao longo de aproximadamente 3 meses, essa fase foi estruturada em etapas interdependentes. Inicialmente, foi desenvolvida a *Interface de Programação de Aplicações* (API), que incorporou o esquema de assinatura de anel vinculável, garantindo anonimato e prevenção de múltiplas respostas. Em seguida, procedeu-se à estruturação do banco de dados, projetado para armazenar com segurança tanto os dados da pesquisa quanto as chaves públicas dos participantes. Por fim, todos os módulos foram integrados, promovendo a interoperabilidade entre as camadas e validando o alinhamento com o modelo arquitetural.

A Avaliação foi estruturada em duas perspectivas analíticas complementares, abrangendo, respectivamente, uma análise qualitativa e uma análise quantitativa. Inicialmente, a análise qualitativa foi conduzida por meio de uma abordagem baseada em cenários representativos. A avaliação baseada em cenários segundo [Rodrigues](#page-63-11) [\(2018\)](#page-63-11), consiste em uma técnica metodológica que utiliza situações hipotéticas, porém plausíveis, construídas em torno do artefato, para demonstrar sua utilidade. Nesse caso, os cenários foram projetados para refletir situações críticas que podem ocorrer em pesquisas baseadas em levantamento. Essa abordagem permite explorar, de forma fundamentada, como a solução proposta responde a diferentes desafios e limitações inerentes ao contexto. Os cenários qualitativos definidos para esta avaliação estão descritos a seguir:

> • Cenário #1 – Solução atinge seu objetivo conforme especificado. Neste cenário, todo o fluxo funcional da solução ocorrerá conforme esperado. Ou seja, o pesquisador será capaz de coletar e analisar os dados sem nenhuma intercorrên-

- cia, e os participantes responderão à pesquisa sem intenções maliciosas e com consciência das respostas.
- Cenário #2 Pesquisador tenta descobrir quem foi responsável por determinada resposta. Nesse cenário, o esquema de assinatura em anel vinculável dificulta a descoberta do responsável por determinada resposta. Isso ocorre devido ao conceito de anonimato do signatário, no qual, mesmo que um pesquisador tenha conhecimento de *t* chaves privadas em um grupo de *n* indivíduos, ele não será capaz de identificar o usuário com uma probabilidade maior que 1/(*n*−*t*) [\(LIU; WONG, 2005\)](#page-62-2).
- Cenário #3 Pessoas que tentam responder à pesquisa mais de uma vez. Nesse cenário, a aplicação deve permitir apenas uma resposta à pesquisa e, após isso, o formulário deve ser expirado. Mesmo que o usuário consiga burlar esse sistema, é possível verificar por meio do esquema de assinatura em anel vinculável se um usuário submeteu a pesquisa mais de uma vez.
- Cenário #4 Pessoas não autorizadas tentam responder à pesquisa. Antes de descrever este cenário, é importante destacar que o modelo proposto utiliza um esquema baseado em chaves criptográficas para garantir a autenticação e o anonimato dos participantes. Cada participante autorizado gera um par de chaves — uma chave pública, armazenada no sistema, e uma chave privada, mantida pelo participante — que serão utilizadas para assinar as respostas da pesquisa de maneira anônima e verificar sua autenticidade. O cenário em que pessoas não autorizadas tentam respondem à pesquisa ocorre quando um ou mais usuários autorizados compartilham o *link* de criação de chaves com outros indivíduos, permitindo que eles criem suas próprias chaves de acesso ao formulário da pesquisa. Para prevenir essa situação, a aplicação deve enviar *links* de uso único exclusivamente para os indivíduos autorizados. Dessa forma, cada *link* possibilita a criação de apenas um par de chaves. Portanto, se um usuário autorizado clicar no *link* e criar suas chaves, mesmo que ele compartilhe o *link*, o usuário não autorizado não conseguirá criar o par de chaves necessário para acessar o formulário.

Os cenários descritos acima serviram como base para a realização de uma análise qualitativa, detalhada no Capítulo [6,](#page-39-0) cujo objetivo foi avaliar o comportamento e a eficácia da solução proposta em situações hipotéticas. De forma complementar, foi conduzida uma análise quantitativa baseada em simulações computacionais, com o intuito de examinar o desempenho da solução e verificar sua viabilidade em condições práticas. A simulação computacional refere-se a métodos para estudar uma ampla variedade de modelos de sistemas do mundo real por meio de avaliação numérica, utilizando software projetado para imitar as operações ou características dos sistemas, frequentemente ao longo do tempo [\(KELTON](#page-62-13) *et al.*, [2002\)](#page-62-13). O foco da análise quantitativa foi avaliar dois aspectos principais:

- Tempo de execução dos algoritmos do esquema [LRS:](#page-9-1) o tempo de execução é um aspecto fundamental para avaliar o desempenho do esquema de assinatura de anel vinculável (LRS) em contextos práticos. Analisar os tempos médios de operações, como geração de chaves (Gen), assinatura (Sig), verificação (Ver) e vinculabilidade (Link), permite identificar gargalos e determinar a eficiência da solução em termos de processamento. Essa análise fornece um indicador importante para avaliar se a solução pode ser empregada em contextos com diferentes requisitos de desempenho.
- Escalabilidade da solução em um ambiente computacional na nuvem: A escalabilidade é fundamental para garantir que a solução seja capaz de atender a cenários de grande escala, com um número crescente de participantes simultâneos e volumes elevados de dados. Assim, a análise dessa dimensão busca verificar a capacidade da solução de manter seu desempenho e a integridade dos dados mesmo sob alta demanda. Testes realizados com a ferramenta JMeter[1](#page-30-0) simulam cargas reais, permitindo avaliar o tempo médio de resposta, o consumo de recursos computacionais (CPU, memória, largura de banda) e a estabilidade do sistema. Dessa forma, torna-se possível investigar se a solução se mostra robusta e adequada para implementações em diferentes contextos operacionais.

Por fim, na Conclusão, realizou-se uma discussão sobre os principais achados e resultados obtidos ao longo deste trabalho. Essa etapa destacou como os objetivos propostos foram alcançados, os desafios enfrentados durante o desenvolvimento, bem como as possíveis limitações e sugestões para trabalhos futuros. A comunicação dos resultados tem envolvido três canais principais: este Trabalho de Conclusão de Curso (TCC), que inclui toda a fundamentação teórica, metodologia, análises e resultados deste projeto; a publicação de um artigo[2](#page-30-1) na forma

<span id="page-30-0"></span><sup>1</sup> https://jmeter.apache.org/

<span id="page-30-1"></span><sup>2</sup> https://sol.sbc.org.br/index.php/sbsi\_estendido/article/view/28640

de resumo expandido no XX Simpósio Brasileiro de Sistemas de Informação (SBSI 2024), que sintetizou os aspectos mais relevantes da pesquisa; e, por fim, o código-fonte[3](#page-31-0) em um repositório aberto no GitHub, promovendo a transparência e a reprodutibilidade científica, permitindo que outros pesquisadores da área utilizem, analisem e modifiquem o código.

<span id="page-31-0"></span><sup>3</sup> https://github.com/Chagas823/lrs\_survey

#### <span id="page-32-1"></span>5 PROPOSTA

Este capítulo visa descrever a arquitetura do modelo proposto, detalhando sua estrutura e os principais componentes envolvidos na implementação (Seção [5.1\)](#page-32-2). Serão também apresentados as tecnologias utilizadas no desenvolvimento e outras ferramentas relevantes para a solução (Seção [5.2\)](#page-34-0). Por fim, será abordado o fluxo da solução, explicando como ocorrerá todo o processo para a realização de uma pesquisa de levantamento garantindo o anonimato dos participantes, a autenticidade das respostas e a prevenção de submissão de múltiplas respostas (Seção [5.3\)](#page-35-1).

#### <span id="page-32-2"></span>5.1 Modelo arquitetural

O modelo arquitetural proposto neste trabalho é estruturado para ser implementado como uma aplicação web baseada no padrão *Model-View-Controller* (MVC). A arquitetura é composta por dois módulos principais: uma interface para interação do usuário com a aplicação e uma API responsável por toda a lógica e conectividade com o banco de dados. Consequentemente, todas as regras de negócio estão contidas no *back-end* da aplicação, sendo a interface responsável por apresentar o aspecto visual e intuitivo da solução.

<span id="page-32-0"></span>![](_page_32_Figure_5.jpeg)

Figura 5 – Arquitetura do modelo proposto.

A camada Interface, por não ser o foco desta pesquisa, é mais simples nesta aplicação, não possuindo nenhuma lógica complexa ou regra de negócio. Neste contexto, esta camada representa o *front-end* da aplicação, onde fica toda a parte visual e intuitiva do sistema. É esta camada que é responsável por realizar chamadas solicitando o processamento de dados na API e, em seguida, mostrar o resultado para o usuário. Este processamento é feito utilizando solicitações HTTPS que são recebidas pela camada Controller.

Por sua vez, a camada Controller é responsável por lidar diretamente com as requisições do usuário. Ela processa os dados recebidas e encaminha para as camadas seguintes, podendo ser a Model em caso de alteração de dados ou a Interface na necessidade da visualização de uma página. No contexto desta aplicação, a Controller possui três componentes principais: gerenciador de formulários, gerenciador de *links* e gerenciador de assinaturas.

O componente Gerenciador de Formulários lida diretamente com a criação do formulário pelo pesquisador. Uma vez que o pesquisador tenha criado as perguntas da pesquisa, este componente enviará os dados para a camada Model, que os direcionará para o banco de dados. Adicionalmente, o componente Gerenciador de *Links* é responsável pelo envio dos *links* aos participantes. Assim que o pesquisador criar o formulário, poderá enviar um *link* de uso único para que cada participante gere sua chave. Quando todos estiverem de posse de suas chaves, o pesquisador pode enviar o *link* do formulário para o participante. Portanto, todas essas ações estão diretamente relacionadas ao componente Gerenciador de *Links*. Finalmente, o componente Gerenciador de Assinaturas possui três responsabilidades: gerar o par de chaves, assinar as respostas do formulário e verificar se o formulário foi preenchido mais de uma vez pelo mesmo participante. Cada um desses processos faz uso dos conceitos propostos por [Liu e](#page-62-2) [Wong](#page-62-2) [\(2005\)](#page-62-2), conforme descrito a seguir:

- A criação de chaves utiliza o algoritmo (*x*, *y*) ← Gen(1 *k* ) que recebe um parâmetro de segurança *k* e gera a chave privada *x* e a chave pública *y*;
- Para a assinatura, é usado o algoritmo σ ← Sig(1 *k* ,1 *n* , *x*,*L*,*m*), que utiliza um parâmetro de segurança *k*, o tamanho do grupo de participantes *n*, a chave privada *x* do respondente, uma lista *L* das *n* chaves públicas dos participantes, incluindo a do respondente, e as respostas *m* da pesquisa.
- Para verificar se uma determinada assinatura é válida, é utilizado o algoritmo 1/0 ← Ver(1 *k* ,1 *n* ,*L*,*m*,σ), que recebe como entradas o parâmetro de segurança *k*, o tamanho do grupo *n*, uma lista *L* de *n* chaves públicas, a mensagem *m* e a assinatura σ. O algoritmo retorna 1 para aceitar ou 0 para rejeitar. Isso é exigido para qualquer mensagem *m*, qualquer (*x*, *y*) ← Gen(1 *k* ) e qualquer *L* que inclua *y*.
- Após o envio das respostas, o algoritmo 1/0 ← Link(1 *k* ,1 *n* ,*L*,*m*1,*m*2,σ1,σ2) é executado. Esse algoritmo utiliza um parâmetro de segurança *k*, o tamanho do grupo de participantes *n*, uma lista de chaves públicas *L*, um par de respostas

da pesquisa *m*<sup>1</sup> e *m*<sup>2</sup> e um par de assinaturas σ<sup>1</sup> e σ<sup>2</sup> para verificar se o par de respostas foi assinado pelo mesmo participante. O algoritmo retorna 1 se as respostas foram assinadas pelo mesmo participante, e 0 caso contrário, garantindo a integridade e autenticidade das respostas.

Finalmente, a camada Model engloba dois componentes principais: Gerenciador de Banco de Dados e Gerenciador de Entidades. O Gerenciador de Banco de Dados é responsável pelas operações no banco de dados, incluindo consultas e modificações de dados. Por exemplo, recuperar chaves públicas a serem utilizadas pelo componente Gerenciador de Assinaturas na assinatura de uma pesquisa, salvar a chave pública de um participante e armazenar respostas de pesquisa. Cada uma dessas operações constitui uma solicitação originada na camada Controller. O componente Gerenciador de Entidades é responsável por organizar e estruturar os elementos do sistema como abstrações, facilitando sua manipulação e validação. Por exemplo, o Formulário é representado como uma entidade que contém perguntas e respostas. Além de armazenar esses dados, ele incorpora regras de validação específicas, como verificar se o formulário possui pelo menos uma pergunta antes de ser salvo ou utilizado no sistema.

#### <span id="page-34-0"></span>5.2 Implementação da API e estrutura dos dados

O artefato desenvolvido inclui uma *Application Programming Interface* (API), projetada como o núcleo da solução para integrar e gerenciar o processo de pesquisa. Tanto a API quanto o esquema [LRS](#page-9-1) foram implementadas utilizando a linguagem *Python*. Essa escolha foi motivada pela ampla coleção de bibliotecas de criptografia disponíveis, como cryptography, PyCryptodome e hashlib, que facilitam a implementação de algoritmos criptográficos.

Para a implementação da API, optou-se pelo *framework* Flask, que se destaca pela sua simplicidade e flexibilidade. Essas características permitem uma rápida prototipação e implementação de soluções web. O Flask segue o padrão de desenvolvimento *[Web Server](#page-9-3) [Gateway Interface](#page-9-3)* (WSGI), facilitando a criação de APIs e a integração com outros componentes do sistema.

Para gerenciar os dados da pesquisa e as chaves públicas dos participantes, utilizouse a biblioteca Flask-SQLAlchemy, que fornece uma interface de alto nível para trabalhar com bancos de dados SQL em Flask. A estrutura do banco de dados foi projetada para incluir as seguintes entidades principais:

• Participante: armazena informações sobre os participantes da pesquisa, in-

cluindo ID, chaves públicas e dados de autenticação.

- Pesquisa: armazena informações sobre a pesquisa, como título e descrição.
- Grupo: armazena informações sobre um grupo e seus participantes associados.
- Perguntas: armazena informações sobre as perguntas, incluindo a pesquisa associada, o tipo de pergunta e o texto.
- Respostas: registra as respostas fornecidas pelos participantes, junto com a assinatura, sem associar ao ID do participante.

#### <span id="page-35-1"></span>5.3 Fluxo da solução proposta

Mediante a compreensão do modelo arquitetural, tem-se abaixo uma visão geral do fluxo funcional da solução proposta (conforme sintetizado na Figura [6\)](#page-35-0):

<span id="page-35-0"></span>Figura 6 – Fluxo da solução proposta.

![](_page_35_Picture_9.jpeg)

Na Etapa 1, o pesquisador, já familiarizado com os participantes que integrarão a pesquisa, encaminha individualmente o *link* a cada um deles. Esse *link* conduzirá a uma página que será responsável por gerar as chaves privada e pública do participante. A partir disso, o participante irá guardar sua chave privada e sua chave pública será guardada em um banco de dados. Após esse procedimento, o *link* será expirado, podendo ser utilizado uma única vez. Essa medida é adotada para evitar que participantes mal-intencionados compartilhem o *link* com outras pessoas, possibilitando a criação de chaves adicionais e, consequentemente, a participação não autorizada na pesquisa. A Etapa 2 irá ocorrer em um momento posterior, quando os participantes já estiverem de posse de suas respectivas chaves privadas. Nesse contexto, o pesquisador encaminha o *link* que contém o formulário da pesquisa. Logo, na Etapa 3, o participante recebe o link da pesquisa e insere sua chave privada. Por fim, na Etapa 4, o participante preencherá o formulário da pesquisa e, em seguida, enviará o formulário. Após o envio, o modelo verificará se o participante já respondeu à pesquisa. Caso não tenha respondido, as respostas serão enviadas para o banco de dados.

Assim, o cenário demonstra que o fluxo garante a autenticidade e o anonimato das

respostas sem comprometer a integridade da pesquisa. De forma complementar e mais detalhada, apresenta-se na Figura [7](#page-38-0) um diagrama de sequência estruturando o funcionamento básico da proposta.

- 1. Criação da pesquisa: o pesquisador inicia o processo criando uma pesquisa por meio de uma requisição POST para o *endpoint create-survey*, onde insere o título e a descrição da pesquisa. Após a submissão, ele recebe um identificador único (ID) vinculado à pesquisa.
- 2. Criação das perguntas: com o ID da pesquisa em mãos, o pesquisador cria as perguntas por meio de uma requisição POST para o *endpoint create-question*. Nesta etapa, ele informa a pergunta, o tipo da pergunta (por exemplo, múltipla escolha, aberta, etc.) e o ID associado à pesquisa.
- 3. Envio do *link* para criação de chaves: em seguida, o pesquisador envia um *link* pro e-mail dos participantes através do *endpoint send-link*, informando o ID do grupo e o ID da pesquisa. Este *link* redireciona para uma página que fornece a chave privada e pública do participante gerada pelo algoritmo Gen. Essas chaves serão utilizadas no processo de assinatura da pesquisa. A chave pública é armazenada no banco de dados. Este *link* também contém um *token* de uso único, que é armazenado em um dicionário do *Python* quando o pesquisador envia o *link* para os participantes. Quando o participante acessa o link, o *token* é invalidado e excluído do dicionário, impedindo que ele seja reutilizado. Dessa forma, garantese que cada participante crie suas chaves apenas uma vez, prevenindo acessos repetidos ou duplicados.
- 4. Envio do formulário para resposta da pesquisa: com suas chaves privada e pública em mãos, cada participante recebe a pesquisa enviada pelo pesquisador por meio do *endpoint send-survey*, utilizando uma requisição GET. Ao receber o formulário, o participante responde utilizando sua chave privada para o processo de assinatura. Durante esse processo, o sistema recupera as chaves públicas de todos os participantes do grupo a partir do banco de dados, recebe a resposta do participante atual e utiliza o algoritmo Sig para gerar a assinatura digital da resposta, garantindo anonimato e autenticidade. Após a assinatura, o algoritmo Link verifica se existem duplicidade de resposta. Para quaisquer duas assinaturas válidas, σ = (*y*0,...) e σ ′ = (*y* ′ 0 ,...) emitidas por um mesmo grupo na mesma

pesquisa, Link compara os valores iniciais *y*<sup>0</sup> e *y* ′ 0 . Se *y*<sup>0</sup> é igual ao *y* ′ 0 , isso indica que ambas as assinaturas foram geradas pelo mesmo participante. Neste caso, a nova resposta é descartada para evitar duplicidade. Caso contrário, a assinatura e as respostas são armazenadas no banco de dados, garantindo que não haja vínculo direto entre a resposta/assinatura e a identidade do participante.

5. Coleta de dados e finalização da pesquisa: após as respostas dos participantes, o pesquisador finaliza a pesquisa. Neste estágio, o algoritmo Ver é utilizado para verificar a autenticidade das respostas da pesquisa, confirmando sua autenticidade. Com as respostas válidas, o pesquisador pode coletar e analisar os dados da pesquisa.

<span id="page-38-0"></span>![](_page_38_Figure_1.jpeg)

Figura 7 – Diagrama de sequência do fluxo principal da solução

### <span id="page-39-0"></span>6 RESULTADOS E ANÁLISES

Este capítulo tem como objetivo apresentar e realizar uma análise abrangente dos resultados obtidos neste estudo, com foco na avaliação da eficácia e da viabilidade do modelo proposto para garantir o anonimato e a autenticidade em pesquisas de levantamento. Na seção [6.1](#page-39-1) é realizado uma análise qualitativa, explorando cenários específicos que simulam situações reais que podem ocorrer em pesquisas de levantamento. Por fim, na Seção [6.2](#page-49-0) é realizada uma análise quantitativa, dividida em duas etapas: a primeira mediu o tempo de execução dos algoritmos do [LRS](#page-9-1) em segundos; a segunda analisou o tempo de resposta da aplicação em segundos durante múltiplos acessos simultâneos de usuários.

#### <span id="page-39-1"></span>6.1 Análise qualitativa

Esta seção realiza uma análise qualitativa baseada em cenários, conforme explicado no Capítulo [4.](#page-27-1) A escolha do método baseado em cenários para a análise qualitativa fundamentase em sua capacidade de simular situações críticas que podem surgir no uso do modelo proposto. O uso de cenários permite criar condições específicas que refletem desafios previamente identificados, assegurando uma avaliação detalhada da solução em condições hipotéticas, porém plausíveis.

Essa abordagem é particularmente útil em projetos que envolvem sistemas tecnológicos inovadores, onde o foco é testar a robustez do artefato antes de sua aplicação em larga escala. Além disso, cenários são ferramentas metodológicas que possibilitam um grau de flexibilidade ao explorar tanto os aspectos funcionais do sistema quanto limitações potenciais. Por exemplo, eles permitem avaliar o impacto de tentativas de quebra de anonimato, a detecção de múltiplas respostas e a atuação de usuários não autorizados, sem os riscos e custos associados a experimentos em condições reais.

#### <span id="page-39-2"></span>*6.1.1 Cenário #1 – Solução atinge seu objetivo conforme especificado*

Neste cenário, todo o fluxo funcional da solução ocorre conforme o esperado, representando o padrão ideal para o modelo proposto. As operações são realizadas sem interrupções ou falhas, garantindo a coerência de todas as etapas do processo. O pesquisador consegue criar o formulário, enviar os links de acesso aos participantes e coletar as respostas sem qualquer necessidade de ajustes adicionais.

Por sua vez, os participantes realizam todas as etapas do processo de maneira honesta e conforme instruído. Eles geram suas chaves privadas e públicas, utilizam essas chaves para responder ao formulário e enviam as respostas, assegurando que o anonimato seja preservado. Não há qualquer tentativa de burlar o sistema, como responder mais de uma vez ou compartilhar links para acesso indevido.

Portanto, o sistema deve atingir os seus objetivos principais em condições ideais, garantindo:

- Anonimato: as respostas são submetidas de forma que a identidade dos participantes não pode ser associada aos dados fornecidos.
- Autenticidade: Todas as respostas são validadas como provenientes de participantes legítimos, utilizando o esquema de assinaturas em anel vinculáveis.
- Prevenção de múltiplas respostas: O sistema impede que um mesmo participante envie respostas duplicadas, verificando eventuais tentativas de uso repetido de chaves.

Este cenário serve como uma referência para a solução proposta, definindo o padrão de funcionamento que o sistema deve atingir.

# <span id="page-40-0"></span>*6.1.2 Cenário #2 – Pesquisador tenta descobrir quem foi responsável por determinada resposta*

Este cenário examina a capacidade do sistema de preservar o anonimato dos participantes, mesmo diante de tentativas deliberadas de um pesquisador de identificar o autor de uma resposta específica. O objetivo é garantir que, mesmo com acesso às respostas coletadas, chaves públicas e assinaturas geradas, não seja possível associar uma resposta a uma chave privada e, consequentemente, ao seu autor.

No esquema de Assinaturas em Anel Vinculáveis (LRS), a proteção do anonimato está fundamentada em uma combinação de fatores, sendo o problema do logaritmo discreto (PLD) um dos elementos centrais. O PLD é amplamente reconhecido como intratável quando aplicado a grupos finitos de ordem suficientemente grande, o que assegura que, mesmo com informações avançadas disponíveis ao pesquisador, a identificação dos participantes seja inviável.

#### *Mecanismo de proteção*

A segurança do modelo implementado é baseada em fundamentos matemáticos bem estabelecidos. A operação de exponenciação modular, denotada como *h <sup>x</sup>*<sup>π</sup> mod *q*, é utilizada para gerar assinaturas seguras. Nessa construção:

*h*: é derivado do hash das chaves públicas no anel, garantindo um valor único para cada conjunto de participantes.

*x*π: representa a chave privada do participante, sendo o elemento secreto que determina o resultado da operação.

Essa operação é computacionalmente eficiente para gerar assinaturas, mas a operação inversa — determinar *x*<sup>π</sup> a partir *h <sup>x</sup>*<sup>π</sup> mod *q* — é equivalente a resolver o problema do logaritmo discreto. Tal problema é considerado inviável para valores grandes de *q*, devido à sua complexidade exponencial. Neste trabalho, foi utiliza uma ordem *q* de 617 dígitos (aproximadamente 2048 bits), como ilustrado na Figura [8,](#page-41-0) garantindo uma resistência substancial contra ataques, incluindo:

<span id="page-41-0"></span>Figura 8 – Valor da ordem dos número inteiros utilizados nos cálculos.

Fonte: elaborado pelo autor.

- Ataques de força bruta: o espaço de busca para *x*<sup>π</sup> é tão vasto que, mesmo com o poder computacional atual, levaria milhões de anos para encontrar a chave correta.
- Algoritmos avançados de logaritmo discreto: métodos como o *[General Num](#page-9-4)[ber Field Sieve](#page-9-4)* (GNFS), conhecidos por sua eficiência em resolver problemas de logaritmo discreto, tornam-se impraticáveis com grupos inteiros dessa magnitude. [Weber](#page-64-4) [\(1996\)](#page-64-4) demonstrou que, ao utilizar uma ordem *q* de 69 dígitos, o problema levou 5 anos, 116 dias, 15 horas e 36 minutos para ser resolver o problema do logaritmo discreto utilizando esta técnica. Ou seja, para um grupo de ordem 617

se torna impraticável.

A escolha de *q* com 617 dígitos oferece um nível de segurança elevado, suficiente para proteger a privacidade dos participantes e garantir o anonimato da pesquisa. Portanto, mesmo com acesso às chaves públicas e à assinatura, o pesquisador não consegue determinar quem foi o responsável pela resposta, devido à dificuldade de solucionar o problema do logaritmo discreto.

#### *Associação entre chaves privadas e identidades*

Caso a chave privada *x*<sup>π</sup> de um participante pudesse ser descoberta, o anonimato seria comprometido. Isso ocorre porque:

- A chave privada *x*<sup>π</sup> está vinculada à chave pública correspondente, que é utilizada para assinar respostas.
- As respostas assinadas com uma chave pública podem ser associadas diretamente ao seu autor, caso a chave privada correspondente seja revelada.
- Em cenários reais, a chave pública geralmente está vinculada a uma identidade digital ou a informações do participante no sistema, possibilitando a identificação direta.

Portanto, garantir a inviolabilidade de *x*<sup>π</sup> é essencial para manter a segurança e anonimato dos participantes, protegendo não apenas contra identificações individuais, mas também contra explorações maliciosas do sistema.

#### *Resultados esperados para este cenário*

Este cenário demonstra que o modelo proposto é robusto o suficiente para proteger o anonimato dos participantes contra tentativas de identificação, mesmo por agentes com acesso privilegiado ao sistema. A integração de diversos fatores, como a dificuldade computacional do PLD e as propriedades do LRS, assegura que nenhuma associação direta ou indireta entre respostas e participantes possa ser estabelecida. Além disso, o esquema apresenta resistente a ataques de força bruta contra a chave privada, dados a dificuldade computacional de resolver o PLD. Este cenário reflete não apenas a eficiência do modelo criptográfico, mas também a importância de sua implementação cuidadosa para garantir segurança e anonimato em ambientes práticos.

#### <span id="page-43-0"></span>*6.1.3 Cenário #3 – Pessoas que tentam responder à pesquisa mais de uma vez*

Este cenário aborda o comportamento de participantes que tentam responder à pesquisa várias vezes, seja por erro ou por intenção de manipular os resultados. O sistema deve ser capaz de impedir múltiplas submissões por um mesmo participante, preservando a integridade do levantamento.

#### *Mecanismo de proteção*

A proteção contra múltiplas respostas é garantida por duas estratégias principais integradas ao esquema LRS:

#### • Expiração do formulário após submissão:

Cada participante recebe um *link* exclusivo para responder à pesquisa. Após a submissão da resposta, o formulário associado a esse *link* é automaticamente expirado, impedindo qualquer tentativa de reutilização.

#### • Verificação de duplicidade de assinaturas:

O algoritmo Link compara para quaisquer duas assinaturas válidas, σ = (*y*0,...) e σ ′ = (*y* ′ 0 ,...) emitidas por um mesmo grupo na mesma pesquisa, os valores iniciais *y*<sup>0</sup> e *y* ′ 0 . Estes valores são calculados no momento da assinatura utilizando o conjunto de chaves públicas *L* = {*y*1,..., *yn*} do grupo do participante, uma função hash *H*<sup>2</sup> e a chave privada *x*<sup>π</sup> do participante.

- 1. Inicialmente é aplicado um hash no conjunto de chaves públicas do grupo do participante: *h* ← *H*2(*L*) mod *q*
- 2. Após isso, *y*<sup>0</sup> é calculado elevando o valor hash *h* a chave privada do participante: *y*<sup>0</sup> ← *h <sup>x</sup>*<sup>π</sup> mod *q*.

Imagine o seguinte cenário ilustrativo:

- 1. *h* (valor das hash das chaves públicas) é 5
- 2. *x*<sup>π</sup> (valor da chave privada do participante) é 3
- 3. *q* é 7

O cálculo do *y*<sup>0</sup> será da seguinte maneira: *y*0 = *h <sup>x</sup>*<sup>π</sup> mod *q* = 5 <sup>3</sup> mod 7 = 6. Perceba que se o mesmo participante tentar responder a pesquisa novamente, utilizando a mesma chave privada *x*π, o valor do *y*<sup>0</sup> será idêntico em ambas as assinaturas. Ou seja, o algoritmo Link detectará essa igualdade, sinalizando a

tentativa de múltipla resposta.

Na implementação do sistema, foi utilizado a função hash *SHA256* (ver linha 2 do Código-fonte [1\)](#page-44-0), escolhida por sua forte resistência a ataques de colisão (situação em que duas entradas produzem o mesmo hash) e sua rápida eficiência.

```
1 def calculate_h (self , L):
2 hash_obj = SHA256 . new ()
3 for key in L:
4 hash_obj . update ( number . long_to_bytes ( key ))
5 return self . hash_to_int ( hash_obj )
6
7 def calculate_y0 (self , h, private_key ):
8 return pow (h, private_key , self .q)
9
10 def generate_signature (self , public_keys , message ,
         private_key ) :
12 r = number . getRandomRange (1 , self .q - 1)
13 pi = 0
14 h = self . calculate_h ( public_keys )
15 y0 = self . calculate_y0 (h, private_key )
```

Código-fonte 1 – Código utilizado para o cálculo do y0

O Código-Fonte [2](#page-44-1) abaixo demonstra a simplicidade do algoritmo Link. Ele compara diretamente os valores y0 das duas assinaturas recebidas como entrada. Se os valores forem iguais, a função retorna "True", indicando que as assinaturas são vinculadas, ou seja, foram geradas pelo mesmo participante.

```
1 def link (self , sig1 , sig2 ) :
2 return sig1 .y0 == sig2 .y0
```

Código-fonte 2 – Código utilizado para o algoritmo Link

#### *Resultados esperados para este cenário*

Os resultados esperados para este cenário incluem a garantia de que os participantes enviem apenas uma única resposta à pesquisa, assegurando a integridade e a confiabilidade dos dados coletados. O algoritmo Link desempenha um papel central nesse processo, pois permite identificar e descartar respostas múltiplas realizadas pelo mesmo participante. Essa funcionalidade mitiga riscos de manipulação mal-intencionada, garantindo que as respostas registradas sejam únicas e autênticas.

Além disso, a implementação com o algoritmo SHA256 contribui significativamente para a robustez do sistema, oferecendo um cálculo eficiente e resistência a ataques de colisão. A verificação de duplicidade ocorre de maneira a preservar o anonimato dos participantes, de forma que nenhuma informação pessoal seja comprometida durante o processo. Dessa forma, o sistema assegura que os dados finais sejam representativos, confiáveis e condizentes com o propósito do levantamento realizado. A Figura [9](#page-45-0) exemplifica a resposta da API quando o participante tenta responder à pesquisa mais de uma vez.

<span id="page-45-0"></span>Figura 9 – Resposta da API quando o participante responde a pesquisa mais de uma vez.

![](_page_45_Picture_4.jpeg)

Fonte: elaborado pelo autor.

#### <span id="page-45-1"></span>*6.1.4 Cenário #4 – Pessoas não autorizadas tentam responder à pesquisa*

Este cenário trata da tentativa de participação de pessoas não autorizadas na pesquisa, utilizando links ou chaves privadas de usuários legítimos. O objetivo principal é prevenir o

acesso indevido e garantir que apenas participantes autorizados possam responder à pesquisa.

#### *Mecanismo de proteção*

O sistema proposto adota duas estratégias fundamentais para evitar o uso indevido por pessoas não autorizadas:

#### • Links de uso único:

Cada participante autorizado recebe um *link* exclusivo que expira automaticamente após o primeiro uso. Este mecanismo impede que o *link* seja reutilizado ou compartilhado com terceiros. O sistema valida o estado do *link* e, caso já tenha sido utilizado, exibe uma mensagem informando sua expiração, reforçando a segurança contra acessos repetidos.

#### • Gerenciamento de tokens e chaves:

Durante o acesso ao *link*, o sistema gera um par de chaves (privada e pública) associado exclusivamente ao participante. O token correspondente é marcado como utilizado, impedindo novos registros com o mesmo *link*. A abordagem de *links* de uso único implementada neste código baseia-se na geração de tokens exclusivos (ver Código-fonte [3\)](#page-47-0), utilizando a função uuid.uuid4() da biblioteca uuid, e no gerenciamento do seu estado por meio de um dicionário denominado tokens. Cada *link* é associado a um token único e a um identificador de participante. Ao acessar o *link*, o sistema valida a existência e o estado do token: se já utilizado, uma mensagem de expiração é exibida (ver Figura [10\)](#page-48-0); caso contrário, o token é marcado como utilizado, e um par de chaves (privada e pública) é gerado e associado ao participante correspondente (ver Figura [11\)](#page-48-1). Essa abordagem promove a segurança ao garantir que cada *link* seja acessado apenas uma vez, evitando tentativas de reutilização ou compartilhamento indevido, além de assegurar a transparência no processo de geração de chaves.

```
1 tokens = {}
2 @app . route ('/ generate - link ', methods =[ 'GET '])
3 def generate_link ( participante_id ):
4 token = str ( uuid . uuid4 () )
5 tokens [ token ] = False
6 link = f'http :// localhost :5000/ use - link /{ token }/{
           participante_id } '
7 return f'Link gerado : <a href ="{ link }" >{ link } </a> '
8
9 @app . route ('/use - link /<token >/ < participante_id > ', methods =[ '
        GET '])
10 def use_link (token , participante_id ):
11 if token in tokens :
12 if tokens [ token ]:
13 expired_html = "
14 <h1 > Este link ja foi utilizado ! </h1 >
15 <p>Por favor , gere um novo link para acessar a
                  chave . </p>
16 "
17 return render_template_string ( expired_html )
18 else :
19 tokens [ token ] = True
20 config_keypair = KeyPair (q,g)
21 private_key , public_key = config_keypair .
                  generate_key_pair ()
22
23 success_html = f"
24 <div class =" key " >{ public_key } </div >
25 <p> Chave privada : </p>
26 <div class =" key " >{ private_key } </div >
27 "
28 return render_template_string ( success_html )
29 else :
30 return 'Link invalido ou expirado . ', 404
```

Código-fonte 3 – Código utilizado para geração do par de chaves

#### *Resultados esperados para este cenário*

Com o mecanismo de proteção implementado, o sistema deve garantir que apenas pessoas autorizadas tenham acesso à pesquisa e possam enviar suas respostas. O sistema deve impedir que *links* de acesso sejam compartilhados ou reutilizados, garantindo que cada *link* exclusivo funcione apenas uma vez e expire após o primeiro uso. Dessa forma, mesmo que um participante autorizado compartilhe seu *link* com terceiros, o sistema não permitirá novos

<span id="page-48-0"></span>Figura 10 – Visualização do Link Expirado

![](_page_48_Picture_2.jpeg)

Fonte: elaborado pelo autor.

<span id="page-48-1"></span>Figura 11 – Visualização das Chaves geradas

![](_page_48_Picture_5.jpeg)

Fonte: elaborado pelo autor.

acessos ou envios de respostas. Além disso, a utilização de tokens únicos e a validação de chaves públicas e privadas asseguram que apenas os participantes legítimos possam interagir com o sistema, reforçando a integridade do levantamento. Como consequência, o sistema deve preservar a confiabilidade dos dados coletados e garantir que os resultados da pesquisa representem fielmente os participantes previstos, sem interferências ou acessos indevidos.

Entretanto, pode ocorrer o caso em que um usuário não autorizado tenha acesso ao e-mail do usuário autorizado. Neste caso, é importante ressaltar que a segurança do sistema proposto depende da confidencialidade do e-mail do participante e também da sua chave privada. Logo, assumimos que o participante não irá compartilhar com terceiros estes dados confidenciais. Para minimizar este tipo de risco, recomenda-se para os participantes não compartilhar seu e-mail e manter sua chave privada em um local seguro e difícil acesso a terceiros não autorizados.

#### <span id="page-49-0"></span>6.2 Análise quantitativa

Nesta seção, busca-se avaliar o desempenho da solução em termos quantitativos, analisando tanto os tempos dos algoritmos do [LRS](#page-9-1) (conforme detalhado na Subseção [6.2.1\)](#page-49-1) quanto sua escalabilidade em um ambiente real na nuvem (explorado na Seção [6.2.2\)](#page-51-1). Na nuvem são explorados os tempos de respostas de cada um dos algoritmos do [LRS](#page-9-1) com base em um número variado de usuários simultâneos.

#### <span id="page-49-1"></span>*6.2.1 Análise do tempo dos algoritmos LRS*

Nesta subseção, são realizados experimentos computacionais para avaliar o tempo de execução de cada um dos algoritmos do [LRS.](#page-9-1) Os testes foram conduzidos em uma máquina de 16 GB de memória RAM, um SSD de 500 GB e um processador *AMD Ryzen* 7. Além disso, para os algoritmos de assinatura (Sig) e verificação de assinatura (Ver), analisou-se o comportamento em função do aumento no número de chaves públicas. Os resultados apresentados correspondem à média, em segundos, calculada a partir de múltiplas execuções.

Diferentemente dos algoritmos Sig e Ver, os algoritmos de Geração de Par de Chaves (Gen) e Link não dependem de parâmetros relacionados à quantidade de chaves públicas, já que apenas Sig e Ver necessitam das chaves públicas do grupo para sua execução. Para os algoritmos Gen e Link, foram realizadas 30 execuções com o objetivo de calcular a média do tempo de execução. O algoritmo Gen apresentou um tempo médio de 0,02214 segundos, enquanto o algoritmo Link demonstrou ser ainda mais rápido, com uma média de 0,00095 segundos. Esses resultados evidenciam que ambos os algoritmos são extremamente eficientes, mesmo sob condições de uso intensivo, sendo adequados para aplicações que exigem alta

performance e baixa latência, como sistemas em tempo real e aplicações móveis. Na subseção [6.2.2](#page-51-1) realizamos testes de escalabilidade no algoritmo de Gen e Link, os quais demonstraram que, mesmo em cenários com múltiplos usuários, eles mantiveram um desempenho satisfatório.

Para os algoritmos de Sig e Ver, foi analisada a relação entre o número de chaves públicas do grupo e o tempo de execução. Como mostrado na Figura [12,](#page-50-0) o algoritmo Sig demonstrou que a relação entre o número de chaves públicas e o tempo de execução é aproximadamente linear, já que o tempo cresce proporcionalmente à quantidade de chaves. Por exemplo, ao dobrar o número de chaves de 500 para 1000, o tempo também quase dobra, passando de 20,64 segundos para 37,67 segundos. Isso sugere que o algoritmo possui uma complexidade *O*(*n*), o que é considerado eficiente para algoritmos que lidam com grandes volumes de dados. Neste caso, a complexidade linear não apenas facilita o uso do algoritmo em cenários de alta demanda, mas também o torna uma escolha vantajosa em comparação com outros algoritmos que apresentam comportamento polinomial de grau maior ou até mesmo complexidade exponencial.

![](_page_50_Figure_3.jpeg)

<span id="page-50-0"></span>Figura 12 – Tempo médio do algoritmo de Sig por número de chaves públicas (em segundos).

Fonte: elaborado pelo autor.

De forma similar, o algoritmo de Ver, demonstrou assim como o algoritmo anterior, um tempo linear (ver Figura [13\)](#page-51-0). Nota-se que ao dobrar a quantidade de chaves públicas, o tempo de execução também aproximadamente dobra. Por exemplo, de 500 para 1000 chaves, o tempo aumenta de 19,69 segundos para 37,90 segundos. Observa-se também, que o algoritmo Ver possui tempos bem próximos do algoritmo Sig. Isso também sugere que o algoritmo de Ver possui uma complexidade *O*(*n*), o que o torna também eficiente em relação a outros algoritmos. Essa característica destaca tanto Sig quanto Ver como soluções eficientes, especialmente em cenários que exigem altos número de participantes.

número de chaves públicas tempo em segundos 0 10 20 30 40 200 400 600 800 1000

<span id="page-51-0"></span>Figura 13 – Tempo médio do algoritmo de Ver por número de chaves públicas (em segundos).

Fonte: elaborado pelo autor.

Em resumo, os experimentos realizados demonstraram que os algoritmos analisados possuem bons desempenho em termos de tempo de execução. Os algoritmos Gen e Link apresentaram tempos médios extremamente baixos, sendo adequados para aplicações que exigem alta performance e baixa latência. Já os algoritmos de Sig e Ver mostraram um comportamento linear em relação ao número de chaves públicas, o que confirma sua eficiência e escalabilidade mesmo em cenários com grandes volumes de dados.

#### <span id="page-51-1"></span>*6.2.2 Análise de escalabilidade na nuvem*

Visando compreender como a solução proposta se comporta em um cenário com diversos usuários em um ambiente computacional na nuvem, nesta seção são realizados *benchmarks* com diferentes volumes de usuários, avaliando o desempenho, a escalabilidade e a eficiência da solução em condições variadas de carga. São realizados testes de Tempo de Resposta nos principais algoritmos do sistema: Geração do par de chaves, Assinatura, Verificação da Assinatura e Link.

Para a realização do experimento computacional optou-se por utilizar a Ferramenta JMeter. JMeter é uma aplicação desktop projetada para a realização de testes de desempenho e estresse em aplicações cliente/servidor, tais como aplicações Web [\(SANTOS; NETO, 2008\)](#page-63-12). Sua flexibilidade permite a criação de cenários personalizados, adequados para testar as capacidades de escalabilidade e robustez do sistema sob diferentes condições de carga, sendo uma escolha adequada para avaliar o comportamento da solução proposta.

O serviço de nuvem escolhido para a realização dos testes foi a Google Cloud, que oferece recursos escaláveis e flexíveis, ideais para a execução de experimentos computacionais. A máquina virtual utilizada foi configurada com as seguintes especificações: 4 vCPUs, 16 GB de memória RAM, Disco de inicialização de 20 GB do tipo Disco Permanente Equilibrado (Balanced Persistent Disk), com interface SCSI e criptografia gerenciada pelo Google e sistema operacional Debian 12. Essas configurações foram escolhidas para garantir um ambiente de teste robusto e capaz de suportar a carga gerada pelos cenários simulados no JMeter.

Por fim, os testes foram feitos com um número *n* de 5, 10, 30, 50 e 100 usuários simultâneos ver Figura [14.](#page-53-0) Para cada teste foi realizado 10 execuções com o objetivo de evitar *outliers*. Para os experimentos envolvendo as funcionalidades de assinatura e verificação de assinatura, foram alocadas uma quantidade equivalente de chaves públicas ao número de acessos simultâneos, simulando assim um cenário em que todos os usuários do mesmo grupo tentam realizar a assinatura de forma simultânea.

#### <span id="page-52-0"></span>*6.2.2.1 Análise do tempo de resposta*

O Tempo de Resposta é o tempo desde o momento em que a solicitação é enviada até o momento em que a última parte da resposta é recebida [\(JMETER, 2025\)](#page-62-14). Vale destacar que fatores como latência de rede, capacidade de processamento do servidor, complexidade da solicitação e tamanho da resposta podem impactar significativamente o tempo de resposta.

Na Figura [15,](#page-54-0) apresenta-se o gráfico referente ao tempo de resposta no contexto de uma solicitação de geração de par de chaves, ou seja, quando o participante realiza uma requisição GET para solicita seu par de chaves (Gen). A Figura [16](#page-54-1) apresenta o gráfico referente ao tempo de resposta no contexto de verificação de assinatura (Ver) com uma requisição POST e envio de arquivo de tamanho *s* = 241 KB, representando o momento em que o pesquisador finaliza a análise da pesquisa e verifica a autenticidade das respostas. Já a Figura [18](#page-56-0) ilustra o tempo de resposta no contexto de uma solicitação GET, utilizada para verificar se o participante já respondeu à pesquisa ao finalizar o envio de suas respostas (Link). Por fim, a Figura [17](#page-55-0) ilustra o tempo de resposta no contexto do algoritmo de assinatura (Sig), considerando o envio de

<span id="page-53-0"></span>![](_page_53_Picture_1.jpeg)

Figura 14 – Configuração do experimento no JMeter

Fonte: elaborado pelo autor.

um arquivo com tamanho *s* = 1088 KB. Nesse caso, o participante conclui o preenchimento do formulário e, em seguida, assina o conteúdo utilizando sua chave privada por meio de uma requisição POST.

A menor média de tempo de resposta para a geração do par de chaves (Figura [15\)](#page-54-0) é de 0,43414 segundos, registrada em uma requisição com 10 usuários simultâneos, enquanto a maior média, de 2,570589 segundos, foi observada em uma requisição com 100 usuários simultâneos. Além disso, nota-se que, à medida que a quantidade de usuários aumenta, o tempo médio também tende a crescer. Contudo, há dois casos em que diferentes quantidades de usuários resultaram em tempos próximos. Esse comportamento pode ser explicado por conta do baixo número de usuários simultâneos nesses dois casos. Ademais, pode-se verificar que ocorreu uma oscilação na segunda rodada de 100 usuários, com esse comportamento podendo ser explicado por conta de oscilações na rede. Em geral, esses resultados indicam que o algoritmo mantém desempenho consistente e eficiente, mesmo com um número crescente de usuários simultâneos.

Observando a Figura [16,](#page-54-1) constata-se que o tempo médio de resposta do algoritmo Ver aumenta proporcionalmente com o número de usuários enviando requisições simultaneamente, sugerindo um comportamento linear. Por exemplo, ao chegar na caso dos 50 usuários, o tempo

![](_page_54_Figure_1.jpeg)

<span id="page-54-0"></span>Figura 15 – Tempo de Resposta para o Algoritmo Gen (em segundos)

Fonte: elaborado pelo autor.

médio foi de 6,82773 segundos e ao dobrar o valor de usuários, o valor médio aproximadamente dobra também, chegando na casa dos 12,90258 segundos.

![](_page_54_Figure_5.jpeg)

<span id="page-54-1"></span>Figura 16 – Tempo de resposta para o Algoritmo Ver (em segundos)

Fonte: elaborado pelo autor.

Por sua vez, na Figura [17,](#page-55-0) observa-se um aumento progressivo no tempo médio do algoritmo Sig à medida que cresce o número de usuários simultâneos. Embora a diferença entre 5 e 10 usuários seja mínima, o aumento torna-se considerável ao atingir 30 usuários. O maior tempo médio registrado foi de 115,41773 segundos, correspondente às requisições realizadas por 100 usuários simultâneos. Apesar do aumento expressivo no tempo de resposta para 100 usuários, o desempenho pode ser considerado aceitável em cenários com carga moderada. Contudo, para aplicações que demandam alta disponibilidade e tempos de resposta baixos, seria recomendável explorar técnicas como balanceamento de carga ou alocação dinâmica de recursos. Vale destacar que a operação pode ocorrer de forma assíncrona, para não impactar a experiência do usuário.

![](_page_55_Figure_2.jpeg)

<span id="page-55-0"></span>Figura 17 – Tempo de resposta para o Algoritmo Sig (em segundos)

Fonte: elaborado pelo autor.

Pode-se verificar na Figura [18](#page-56-0) que o algoritmo Link apresenta um desempenho extremamente satisfatório. O tempo de resposta médio varia pouco, mesmo com o aumento no número de usuários. Por exemplo, para 5 usuários simultâneos, o tempo médio de resposta foi de 0,39902 segundos. Notou-se uma pequeno oscilação isolada de 0,5798 segundos em uma das rodadas, sugerindo uma possível oscilação na rede. Com o aumento da quantidade de usuários simultâneos, o tempo médio cresce de maneira controlada. Para 30 usuários o tempo médio foi de 0,39082 segundos, enquanto para 50 usuários chegou a 0,618236 segundos. Finalmente, para 100 usuários simultâneos, o tempo médio de resposta foi de 1,290457 segundos. Nota-se, portanto que o desempenho observado confirma que o algoritmo Link atende adequadamente aos requisitos de escalabilidade e confiabilidade para cenários de altas demandas.

Por fim, os resultados apresentados permitem concluir que os tempos de resposta observados nos algoritmos de Gen, Ver e Link são compatíveis com cenários de uso moderado a intenso, demonstrando a robustez e a escalabilidade dos serviços oferecidos pela API. Em particular, o algoritmo Link apresentou um desempenho extremamente satisfatório, refletindo

![](_page_56_Figure_1.jpeg)

<span id="page-56-0"></span>Figura 18 – Tempo de resposta para o Algoritmo Link (em segundos)

Fonte: elaborado pelo autor.

sua eficácia e alinhamento com complexidade baixa. Esse comportamento é ideal para sistemas que exigem operações rápidas e frequentes. No entanto, para cenários com altas demandas por desempenho em tempo real, o algoritmo Sig pode apresentar gargalos, sendo necessários estratégias de otimização, como aquelas mencionadas anteriormente. Esses achados destacam a importância de monitorar e ajustar a infraestrutura de acordo com as necessidades específicas de cada aplicação.

### <span id="page-57-0"></span>7 DISCUSSÃO

Este estudo teve como objetivo investigar o uso do esquema de assinatura em anel vinculável [\(LRS\)](#page-9-1) proposto por [Liu e Wong](#page-62-2) [\(2005\)](#page-62-2) no contexto de pesquisas de levantamento, abordando desafios relacionados a preservação simultânea do anonimato e da autenticidade dos participantes. Embora [LRS](#page-9-1) já tenha sido incorporado em muitas aplicações, como o de votação eletrônica por [Tsang e Wei](#page-64-5) [\(2005\)](#page-64-5) e criptomoedas por [Torres](#page-64-6) *et al.* [\(2018\)](#page-64-6), [Noether](#page-62-15) *et al.* [\(2016\)](#page-62-15), Sun *[et al.](#page-63-13)* [\(2017\)](#page-63-13), o diferencial deste trabalho consiste em trazer uma adaptação para o contexto específico de pesquisas de levantamento. A análise dos resultados permite reflexões importantes acerca da eficácia do modelo proposto, sua contribuição teórica e suas limitações.

Os resultados qualitativos (ver Seção [6.1\)](#page-39-1) demonstram que o modelo atinge seus objetivos centrais, garantindo que os participantes permaneçam anônimos e que suas respostas sejam autênticas. A robustez do esquema [LRS](#page-9-1) foi corroborada pelo cenário #2, que evidencia a dificuldade prática de um pesquisador identificar os respondentes devido à dificuldade computacional do logaritmo discreto. Outro ponto a se destacar, conforme explicado no cenário #3 (discutido na Seção [6.1.3\)](#page-43-0), é a capacidade do modelo em prevenir múltiplas respostas de um mesmo participante, essencial para garantir a integridade da pesquisa. O algoritmo Link, um componente fundamental do [LRS,](#page-9-1) demonstrou eficiência na detecção de assinaturas duplicadas. Por outro lado, o cenário #4 destacou uma limitação do modelo: a dependência do comportamento seguro dos usuários. Logo, a eficácia do sistema pode ser comprometida se os participantes compartilharem suas chaves privadas e e-mails. Esse questão reforça a necessidade de medidas complementares, como a necessidade do não compartilhamento de senhas.

Os algoritmos de geração do par de chaves (Gen), assinatura (Sig), verificação da assinatura (Ver) e Link demonstraram um bom desempenho em termos de tempo de execução, como evidenciado na Seção [6.2.1.](#page-49-1) As Figuras [12](#page-50-0) e [13](#page-51-0) ilustraram a escalabilidade dos algoritmos, mostrando como o seu tempo cresce simultaneamente com o aumento de chaves públicas, o que garante a viabilidade da solução mesmo em cenários com um grande número de participantes.

A análise de escalabilidade na nuvem, discutida na seção [6.2.2,](#page-51-1) evidenciou a viabilidade da solução em um ambiente simulado na nuvem com diferentes números de usuários simultâneos, mostrando que o sistema mantém um desempenho razoável, mesmo sob condições de alta demanda. Os tempos de resposta, para os algoritmo de Gen, Ver e Link se mostraram bastante eficientes. Ademais, o algoritmo de Sig apresentou tempos de execução mais elevados em cenários de alta demanda, mas é importante destacar que esse tempo não impacta diretamente

a experiência do usuário final. Isso ocorre porque o processo de assinatura pode ser realizado de forma assíncrona, permitindo que o participante envie sua resposta e saia do sistema enquanto o servidor processa essa operação em segundo plano. O sistema pode melhorar em termos de desempenho utilizando algumas abordagens como:

- Dividir as operações de assinatura em múltiplas threads ou nós na nuvem para acelerar o processamento.
- Reduzir a complexidade computacional do algoritmo, diminuindo o seu tempo de processamento.
- Utilizar uma infraestrutura com máquinas virtuais que tenha um maior poder de processamento

Em termos de contribuição, esta pesquisa avança para o campo acadêmico, sobretudo na área de cibersegurança e privacidade em sistemas computacionais. A principal contribuição consiste na aplicação inovadora do assinaturas em anel vinculáveis [\(LRS\)](#page-9-1) no contexto de pesquisas de levantamento, uma abordagem até em então pouco explorada fora do contexto de sistemas de votação e criptomoedas. Portanto, este trabalho evidencia que o modelo é viável como solução para o desafio de equilibrar o anonimato e autenticidade. Ademais, esta pesquisa contribui para a literatura ao superar limitações enfrentadas trabalhos anteriores, como a complexidade arquitetural de [Hohenberger](#page-62-3) *et al.* [\(2014\)](#page-62-3) e a falta de mecanismos eficazes para impedir submissão de múltiplas respostas de [Lu Li Yuxi](#page-62-12) [\(2016\)](#page-62-12) e [Ripper](#page-63-9) *et al.* [\(2017\)](#page-63-9) . O modelo proposto combina simplicidade, viabilidade prática e segurança, oferecendo uma base sólida para futuras pesquisas e investigações sobre privacidade e autenticação em sistemas de pesquisas de levantamento.

Na esfera prática, esta pesquisa traz contribuições para a indústria de software, especialmente quanto ao desenvolvimento de aplicações que envolvem a coleta de dados sensíveis. O modelo oferece uma proposta factível para empresas que necessitam garantir o anonimato e autenticidade de suas pesquisas, como avaliação de desempenho, pesquisas organizacional e *feedback* anônimo. Em particular, o uso de assinatura em anel vinculável garante a integridade e autenticidade das respostas sem comprometer o anonimato dos participantes. Dessa forma, tornase possível contribuir com empresas a atender regulamentações como a *[Lei Geral de Proteção](#page-9-5) [de Dados Pessoais](#page-9-5)* (LGPD) e o *[Regulamento Geral sobre a Proteção de Dados](#page-9-6)* (RGPD), por exemplo. Outra contribuição relevante é a adaptabilidade do modelo a diferentes contextos corporativos. A arquitetura permite que a solução seja personalizada para atender demandas

especificas, como controle de acesso a formulários, prevenção de duplicidade de respostas e auditoria de participação.

Mesmo atingindo os objetivos de pesquisa previamente estabelecidos, este estudo também enfrenta limitações e oferece oportunidades de melhorias para o futuro:

- O modelo é totalmente dependente do comportamento seguro e da confidencialidade do e-mail dos usuários conforme destacado no cenário #4, a eficácia da solução pode ser comprometida caso o usuário compartilhe seu e-mail, chave privada e link da pesquisas com terceiros não autorizados. Embora medidas como links de uso único sejam utilizadas, esse problema não é totalmente eliminável apenas por meio de soluções técnicas.
- Apesar da maioria dos algoritmos do [LRS](#page-9-1) terem demonstrado desempenhos satisfatórios em contextos com altas demandas, o algoritmo Sig se mostrou mais elevados em cenários com múltiplos participantes simultâneos. Embora isso não impacte diretamente a experiência do usuário devido ao processamento assíncrono, isso pode representar um desafio em aplicações que exigem respostas em tempo real. Melhoria futuras podem incluir otimizações no algoritmo e o maior uso de infraestrutura de processamento paralelo.
- Os testes foram focados em ambientes simulados, o que possibilita avaliar o sistema em diferentes condições controladas. No entanto, o comportamento do modelo em cenários reais, onde fatores como conexões de rede instáveis e uso de participantes inexperientes, podem interferir na eficácia do modelo. Isso representa uma área importante para experimentação prática em projetos futuros.

### <span id="page-60-0"></span>8 CONSIDERAÇÕES FINAIS

O presente trabalho teve como objetivo investigar como o esquema de assinaturas em anel vinculáveis pode ser implementado em pesquisas de levantamento, garantindo simultaneamente o anonimato dos participantes e a autenticidade de suas respostas. A questão de pesquisa, formulada na introdução, é retomada aqui à luz dos resultados obtidos, com o intuito de oferecer uma resposta clara e fundamentada.

A partir da implementação do modelo proposto, descrito detalhadamente no Capítulo [5,](#page-32-1) foi possível desenvolver um sistema que equilibra, de maneira eficaz, os princípios de anonimato e autenticidade. O uso de assinaturas em anel vinculáveis mostrou-se uma solução robusta, prevenindo a ocorrência de múltiplas respostas de um mesmo participante, sem comprometer sua identidade e evitando a submissão indevida de dados. Esses resultados foram validados tanto qualitativamente, por meio de cenários simulados, quanto quantitativamente, por análises de desempenho computacional, as quais confirmaram a eficiência e escalabilidade da solução.

Os resultados qualitativos indicam que o modelo atende aos requisitos previamente definidos, incluindo a garantia de anonimato mesmo em cenários de tentativas maliciosas de identificação dos participantes. Já os testes quantitativos evidenciam que os algoritmos do esquema LRS apresentam tempos de execução compatíveis com aplicações em larga escala, o que reforça a aplicabilidade do sistema em contextos diversos. Com base nas evidências apresentadas, conclui-se que o modelo proposto oferece uma resposta satisfatória à questão de pesquisa inicialmente formulada.

Em termos de contribuição, destaca-se a aplicação inovadora da assinatura em anel vinculável em pesquisas de levantamento, resolvendo o conflito entre anonimato e autenticidade nesse tipo de pesquisa, viabilizando a coleta de dados sensíveis de forma ética, segura e confiável. Além disso, a combinação da abordagem descritiva com o uso da DSR reforça a conexão entre teoria e prática, oferecendo uma metodologia replicável para o desenvolvimento de soluções tecnológicas e ampliação do modelo em outros contextos.

Em termos de trabalhos futuros, tem-se a oportunidade de explorar a integração do modelo com tecnologias emergentes, como blockchain, para garantir imutabilidade dos dados coletados.

# REFERÊNCIAS

- <span id="page-61-13"></span><span id="page-61-0"></span>ADAMS, C. Dictionary Attack. Berlin, Heidelberg: Springer Berlin Heidelberg, 2019. 1–2 p. Disponível em: [<https://doi.org/10.1007/978-3-642-27739-9\\_74-2>.](https://doi.org/10.1007/978-3-642-27739-9_74-2)
- <span id="page-61-12"></span>ALAGHEBAND, M. R.; MASHATAN, A. Advanced digital signatures for preserving privacy and trust management in hierarchical heterogeneous iot: Taxonomy, capabilities, and objectives. Internet of Things, v. 18, p. 100492, 2022. ISSN 2542-6605. Disponível em: [<https://www.sciencedirect.com/science/article/pii/S2542660521001311>.](https://www.sciencedirect.com/science/article/pii/S2542660521001311)
- <span id="page-61-4"></span>ANWAR, K.; NURZANAH, M.; MUNAWAROH, M.; LAYA, A. P. Questionnaire design challenges in research methodology courses: A call for educational enhancements. Indonesian EFL Research and Practices, v. 1, n. 2, p. 15–22, Jun. 2021. Disponível em: [<https://journal.iaima.ac.id/i-efl/article/view/68>.](https://journal.iaima.ac.id/i-efl/article/view/68)
- <span id="page-61-14"></span>ARDALAN, A.; ARDALAN, R. K.; RAO, S.; ALEXANDER, K. B. An information system architecture for ensuring anonymity of student survey responses. The International Journal of Information and Learning Technology, Emerald Publishing Limited, v. 36, n. 1, p. 52–65, 2019.
- <span id="page-61-6"></span>BRADBURY, D. Anonymity and privacy: a guide for the perplexed. Network Security, v. 2014, n. 10, p. 10–14, 2014. ISSN 1353-4858. Disponível em: [<https:](https://www.sciencedirect.com/science/article/pii/S1353485814701023) [//www.sciencedirect.com/science/article/pii/S1353485814701023>.](https://www.sciencedirect.com/science/article/pii/S1353485814701023)
- <span id="page-61-11"></span>BRAGA, A.; DAHAB, R. Criptografia assimétrica para programadores–evitando outros maus usos da criptografia em sistemas de software. Sociedade Brasileira de Computação, 2018.
- <span id="page-61-9"></span>CHAKRAVARTY, S.; PORTOKALIDIS, G.; POLYCHRONAKIS, M.; KEROMYTIS, A. D. Detecting traffic snooping in tor using decoys. p. 222–241, 2011.
- <span id="page-61-2"></span>CHECK, J.; SCHUTT, R. Research Methods in Education. SAGE Publications, 2011. ISBN 9781483342092. Disponível em: [<https://books.google.com.br/books?id=nSWYAAAAQBAJ>.](https://books.google.com.br/books?id=nSWYAAAAQBAJ)
- <span id="page-61-3"></span>COUGHLAN, M.; CRONIN, P.; RYAN, F. Survey research: Process and limitations. International Journal of Therapy and Rehabilitation, MA Healthcare London, v. 16, n. 1, p. 9–15, 2009.
- <span id="page-61-10"></span>DIFFIE, W.; HELLMAN, M. New directions in cryptography (1976). 1976.
- <span id="page-61-5"></span>EDMAN, M.; YENER, B. On anonymity in an electronic society: A survey of anonymous communication systems. ACM Comput. Surv., Association for Computing Machinery, New York, NY, USA, v. 42, n. 1, dec 2009. ISSN 0360-0300. Disponível em: [<https://doi.org/10.1145/1592451.1592456>.](https://doi.org/10.1145/1592451.1592456)
- <span id="page-61-8"></span>FARRALL, K. N. Global privacy in flux: Illuminating privacy across cultures in china and the us. International Journal of Communication, v. 2, p. 38, 2008.
- <span id="page-61-1"></span>GAHARANA, S.; ANAND, D. Dynamic id based remote user authentication in multi server environment using smart cards: A review. 2015 International Conference on Computational Intelligence and Communication Networks (CICN), p. 1081–1084, 2015.
- <span id="page-61-7"></span>HOANG, N. P.; PISHVA, D. Anonymous communication and its importance in social networking. In: IEEE. 16th international conference on advanced communication technology. [S.l.], 2014. p. 34–39.

<span id="page-62-3"></span>HOHENBERGER, S.; MYERS, S.; PASS, R. *et al.* Anonize: A large-scale anonymous survey system. In: IEEE. 2014 IEEE Symposium on Security and Privacy. [S.l.], 2014. p. 375–389.

<span id="page-62-14"></span>JMETER. Apache JMeter. 2025. [<https://jmeter.apache.org/>.](https://jmeter.apache.org/) Acesso em: 5 jan. 2025.

<span id="page-62-1"></span>JOHNSON, T. P.; SMITH, T. W. Big data and survey research: Supplement or substitute? Seeing cities through big data: Research, methods and applications in urban informatics, Springer, p. 113–125, 2017.

<span id="page-62-5"></span>KANG, E.; HWANG, H.-J. The importance of anonymity and confidentiality for conducting survey research. Journal of Research and Publication Ethics, v. 4, n. 1, p. 1–7, 2023.

<span id="page-62-11"></span>KAPIS, K.; KOROJELO, S. P. Online surveys system with enhanced authentication intelligence: a case of online course evaluation system. International Journal on New Computer Architectures and Their Applications (IJNCAA), v. 2, n. 1, p. 81–90, 2012.

<span id="page-62-13"></span>KELTON, W. D.; SADOWSKI, R. P.; SADOWSKI, D. A. Simulation with Arena. 2. ed. USA: McGraw-Hill, Inc., 2002. ISBN 0071122397.

<span id="page-62-10"></span>KRZYWORZEKA, N. Asymmetric cryptography and trapdoor one-way functions. Automatyka/Automatics, v. 20, n. 2, 2016.

<span id="page-62-4"></span>LEE, G.; BENOIT-BRYAN, J.; JOHNSON, T. P. Survey research in public administration: Assessing mainstream journals with a total survey error framework. Public Administration Review, Wiley Online Library, v. 72, n. 1, p. 87–97, 2012.

<span id="page-62-8"></span>LIGUORI, C. Direito e criptografia. Saraiva Jur, 2022. ISBN 9786553623446. Disponível em: [<https://books.google.com.br/books?id=PahYEAAAQBAJ>.](https://books.google.com.br/books?id=PahYEAAAQBAJ)

<span id="page-62-2"></span>LIU, J. K.; WONG, D. S. Linkable ring signatures: Security models and new schemes. In: GERVASI, O.; GAVRILOVA, M. L.; KUMAR, V.; LAGANÀ, A.; LEE, H. P.; MUN, Y.; TANIAR, D.; TAN, C. J. K. (Ed.). Computational Science and Its Applications – ICCSA 2005. Berlin, Heidelberg: Springer Berlin Heidelberg, 2005. p. 614–623. ISBN 978-3-540-32044-9.

<span id="page-62-12"></span>LU LI YUXI, Z. F. L. Anonymous electronic survey system based on non-interactive zero-knowledge proof. Journal of Network and Information Security, Journal of Network and Information Security, v. 2, n. 12, p. 39, 2016.

<span id="page-62-0"></span>MATHIYAZHAGAN, T.; NANDAN, D. Survey research method. Media Mimansa, v. 4, n. 1, p. 34–45, 2010.

<span id="page-62-7"></span>MENEZES, A. J.; OORSCHOT, P. C. V.; VANSTONE, S. A. Handbook of applied cryptography. 1st. ed. CRC press, 2018. Disponível em: [<https://doi.org/10.1201/](https://doi.org/10.1201/9780429466335) [9780429466335>.](https://doi.org/10.1201/9780429466335)

<span id="page-62-15"></span>NOETHER, S.; MACKENZIE, A.; LAB, t. M. R. Ring confidential transactions. Ledger, v. 1, p. 1–18, Dec. 2016. Disponível em: [<https://ledger.pitt.edu/ojs/ledger/article/view/34>.](https://ledger.pitt.edu/ojs/ledger/article/view/34)

<span id="page-62-6"></span>NOVAK, A. Anonymity, confidentiality, privacy, and identity: The ties that bind and break in communication research. Review of communication, Taylor & Francis, v. 14, n. 1, p. 36–48, 2014.

<span id="page-62-9"></span>OLIVEIRA, R. R. Criptografia simétrica e assimétrica-os principais algoritmos de cifragem. Segurança Digital [Revista online], v. 31, p. 11–15, 2012.

- <span id="page-63-10"></span>PEFFERS, K.; TUUNANEN, T.; ROTHENBERGER, M. A.; CHATTERJEE, S. A design science research methodology for information systems research. Journal of management information systems, Taylor & Francis, v. 24, n. 3, p. 45–77, 2007.
- <span id="page-63-2"></span>PFITZMANN, A.; HANSEN, M. Anonymity, unobservability, and pseudonymity: A consolidated proposal for terminology. draft, July, 2000.
- <span id="page-63-1"></span>PONTO, J. Understanding and evaluating survey research. Journal of the advanced practitioner in oncology, Harborside Press, v. 6, n. 2, p. 168, 2015.
- <span id="page-63-6"></span>PRATT-CHAPMAN, M.; MOSES, J.; AREM, H. Strategies for the identification and prevention of survey fraud: Data analysis of a web-based survey. JMIR Cancer, v. 7, n. 3, p. e30730, Jul 2021. ISSN 2369-1999. Disponível em: [<https://cancer.jmir.org/2021/3/e30730>.](https://cancer.jmir.org/2021/3/e30730)
- <span id="page-63-8"></span>RATHOD, U.; SONKAR, M.; CHANDAVARKAR, B. An experimental evaluation on the dependency between one-way hash functions and salt. In: IEEE. 2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT). [S.l.], 2020. p. 1–7.
- <span id="page-63-9"></span>RIPPER, L.; CIARAVINO, S.; JONES, K.; JAIME, M. C. D.; MILLER, E. Use of a respondent-generated personal code for matching anonymous adolescent surveys in longitudinal studies. Journal of Adolescent Health, v. 60, n. 6, p. 751–753, 2017. ISSN 1054-139X.
- <span id="page-63-3"></span>RIVEST, R. L.; SHAMIR, A.; TAUMAN, Y. How to leak a secret. In: SPRINGER. Advances in Cryptology—ASIACRYPT 2001: 7th International Conference on the Theory and Application of Cryptology and Information Security Gold Coast, Australia, December 9–13, 2001 Proceedings 7. [S.l.], 2001. p. 552–565.
- <span id="page-63-5"></span>ROBERTSON, R. E.; TRAN, F. W.; LEWARK, L. N.; EPSTEIN, R. Estimates of non-heterosexual prevalence: The roles of anonymity and privacy in survey methodology. Archives of sexual behavior, Springer, v. 47, n. 4, p. 1069–1084, 2018.
- <span id="page-63-11"></span>RODRIGUES, D. D. Design science research como caminho metodológico para disciplinas e projetos de design da informação | design science research as methodological path for information design subjects and projects. InfoDesign - Journal of Information Design, v. 15, n. 1, p. 111–124, Aug. 2018. Disponível em: [<https://infodesign.emnuvens.com.br/infodesign/](https://infodesign.emnuvens.com.br/infodesign/article/view/564) [article/view/564>.](https://infodesign.emnuvens.com.br/infodesign/article/view/564)
- <span id="page-63-12"></span>SANTOS, I. de S.; NETO, P. d. A. dos S. Automaçao de testes de desempenho e estresse com o jmeter. 2008.
- <span id="page-63-4"></span>SHREYA, A. Bridging gap in research during medical training. SBV Journal of Basic, Clinical and Applied Health Science, v. 6, n. 1, p. 18–20, 2022.
- <span id="page-63-0"></span>SINGLETON, R.; STRAITS, B. C.; STRAITS, M. M.; MCALLISTER, R. J. Approaches to social research. [S.l.]: Oxford University Press, 1988.
- <span id="page-63-7"></span>STALLINGS, W. Cryptography and network security, 6/E. [S.l.]: Pearson Education Brasil, 2014.
- <span id="page-63-13"></span>SUN, S.-F.; AU, M. H.; LIU, J. K.; YUEN, T. H. Ringct 2.0: A compact accumulator-based (linkable ring signature) protocol for blockchain cryptocurrency monero. In: FOLEY, S. N.; GOLLMANN, D.; SNEKKENES, E. (Ed.). Computer Security – ESORICS 2017. Cham: Springer International Publishing, 2017. p. 456–474. ISBN 978-3-319-66399-9.

- <span id="page-64-3"></span>TANWAR, S.; KUMAR, A. An efficient and secure identity based multiple signatures scheme based on rsa. Journal of Discrete Mathematical Sciences and Cryptography, Taylor & Francis, v. 22, n. 6, p. 953–971, 2019.
- <span id="page-64-6"></span>TORRES, W. A. A.; STEINFELD, R.; SAKZAD, A.; LIU, J. K.; KUCHTA, V.; BHATTACHARJEE, N.; AU, M. H.; CHENG, J. Post-quantum one-time linkable ring signature and application to ring confidential transactions in blockchain (lattice ringct v1.0). In: SUSILO, W.; YANG, G. (Ed.). Information Security and Privacy. Cham: Springer International Publishing, 2018. p. 558–576. ISBN 978-3-319-93638-3.
- <span id="page-64-5"></span>TSANG, P. P.; WEI, V. K. Short linkable ring signatures for e-voting, e-cash and attestation. In: DENG, R. H.; BAO, F.; PANG, H.; ZHOU, J. (Ed.). Information Security Practice and Experience. Berlin, Heidelberg: Springer Berlin Heidelberg, 2005. p. 48–60. ISBN 978-3-540-31979-5.
- VAISHNAVI, V.; KUECHLER, W. Design science research in information systems. Association for Information Systems. Available at http://desrist.org/design-research-in-informationsystems, 2004.
- <span id="page-64-1"></span>WALDO, J.; LIN, H. S.; COX, L. H. Thinking about privacy: Chapter 1 of "engaging privacy and information technology in a digital age". Journal of Privacy and Confidentiality, v. 2, n. 1, Sep. 2010. Disponível em: [<https://journalprivacyconfidentiality.org/index.php/jpc/article/view/581>.](https://journalprivacyconfidentiality.org/index.php/jpc/article/view/581)
- <span id="page-64-4"></span>WEBER, D. Computing discrete logarithms with the general number field sieve. In: COHEN, H. (Ed.). Algorithmic Number Theory. Berlin, Heidelberg: Springer Berlin Heidelberg, 1996. p. 391–403. ISBN 978-3-540-70632-8.
- <span id="page-64-0"></span>YANG, K.; XIAO, M. A framework for formal analysis of anonymous communication protocols. Security and Communication Networks, 2022.
- <span id="page-64-2"></span>ZHANG, Q. An overview and analysis of hybrid encryption: The combination of symmetric encryption and asymmetric encryption. In: 2021 2nd International Conference on Computing and Data Science (CDS). [S.l.: s.n.], 2021. p. 616–622.