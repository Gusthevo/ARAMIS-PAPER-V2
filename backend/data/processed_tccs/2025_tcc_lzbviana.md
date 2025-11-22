# PREVISÃO DE SÉRIES TEMPORAIS ORIENTADA POR PROMPT COM MODELOS DE LINGUAGEM DE GRANDE ESCALA

# AGRADECIMENTOS

À Universidade Federal do Ceará, pelo apoio e incentivo ao longo de toda a minha formação.

Aos meus estimados colegas de turma, pelas valiosas trocas de conhecimento e pelos momentos de amizade que tornaram essa jornada ainda mais especial.

Aos professores que, com dedicação, orientaram este trabalho.

Ao EngineLab, por oferecer um ambiente acolhedor e inspirador.

Aos meus colegas e amigos de laboratório, por todas as risadas, aprendizados e experiências compartilhadas.

A todos os funcionários terceirizados, pelo respeito, gentileza e pelo excelente tratamento que sempre me proporcionaram.

Ao Fluminense Football Club, por tornar minha graduação ainda mais memorável com um ano inesquecível em 2023.

E ao meu Deus.

"Eu perdi o vestibular de medicina Minha mãe ficou zangada E eu nem um pouco Eu não sei Mas talvez seja muito louco" (Santanna o Cantador)

## RESUMO

A previsão de séries temporais é uma ferramenta essencial para a tomada de decisões em diversos setores, como o varejo e a mobilidade urbana. Este trabalho apresenta uma abordagem comparativa entre métodos tradicionais – representados pelo *Random Forest* e pela Rede Neural *LSTM* (Long Short-Term Memory) – e uma metodologia inovadora que utiliza Modelo de Linguagem de Grande Escala (LLM) orientados por engenharia de prompt. Para a realização deste estudo, foram utilizados dois conjuntos de dados reais: um relativo às vendas de produtos em um supermercado de Fortaleza e outro composto pelos registros de embarques em linhas de ônibus da mesma cidade. Enquanto os métodos clássicos empregaram a técnica de janelas deslizantes para estruturar os dados históricos, o método baseado em LLM foi desenvolvido por meio de um prompt especificamente elaborado para o modelo Gemini-1.5-pro, de forma a captar padrões sazonais e tendências de forma integrada. A avaliação dos modelos foi realizada por meio das métricas SMAPE (Symmetric Mean Absolute Percentage Error) e SEM (Standard Error of the Mean), permitindo uma análise comparativa de desempenho entre as abordagens.

Palavras-chave: Previsão de Séries Temporais; LLM; Random Forest; LSTM; Engenharia de Prompt.

# ABSTRACT

Time series forecasting is an essential tool for decision-making in various sectors, such as retail and urban mobility. This paper presents a comparative approach between traditional methods – represented by *Random Forest* and *LSTM* Neural Network (Long Short-Term Memory) – and an innovative methodology that uses Prompt Engineering-driven Large Language Model (LLM). For this study, two real datasets were used: one relating to product sales in a supermarket in Fortaleza and the other composed of boarding records on bus lines in the same city. While the classical methods employed the sliding window technique to structure historical data, the LLM-based method was developed through a prompt specifically designed for the Gemini-1.5-pro model, in order to capture seasonal patterns and trends in an integrated way. The evaluation of the models was carried out using the SMAPE (Symmetric Mean Absolute Percentage Error) and SEM (Standard Error of the Mean), metrics, allowing a comparative performance analysis between the approaches.

Keywords: Time Series Forecasting; Large Language Model (LLM); Random Forest; Long Short-Term Memory (LSTM); Prompt Engineering.

# LISTA DE ABREVIATURAS E SIGLAS

IA Inteligência Artificial

LLM Modelo de Linguagem de Grande Escala - Large Language Models

LSTM Long Short-Term Memory

ML Machine Learning (Aprendizado de Máquina)

PE Engenharia de Prompt - Prompting Engineering

PLN Processamento de Linguagem Natural

RF Random Forest

RNN Redes Neurais Recorrentes

SEM Erro Padrão da Média

SMAPE Erro Percentual Médio Simétrico

# SUMÁRIO

| 1     | INTRODUÇÃO .                                                          | 13 |
|-------|-----------------------------------------------------------------------|----|
| 1.1   | Justificativa                                                         | 14 |
| 1.2   | Objetivo Geral                                                        | 14 |
| 1.3   | Objetivos Específicos                                                 | 15 |
| 1.4   | Organização do Trabalho                                               | 15 |
| 2     | FUNDAMENTAÇÃO TEÓRICA                                                 | 16 |
| 2.1   | Séries Temporais                                                      | 16 |
| 2.2   | Inteligência Artificial                                               | 17 |
| 2.3   | Aprendizado de Máquina                                                | 20 |
| 2.3.1 | Aprendizado Supervisionado                                            | 20 |
| 2.3.2 | Aprendizado Não Supervisionado                                        | 21 |
| 2.3.3 | Aprendizado Por Reforço                                               | 21 |
| 2.4   | LSTM                                                                  | 21 |
| 2.5   | Random Forest                                                         | 23 |
| 2.6   | Processamento de Linguagem Natural                                    | 23 |
| 2.7   | Modelos de Linguagem de Grande Escala                                 | 25 |
| 2.8   | Gemini                                                                | 25 |
| 2.8.1 | Características Principais                                            | 26 |
| 2.8.2 | Aplicações                                                            | 26 |
| 2.9   | Engenharia de Prompt                                                  | 26 |
| 2.9.1 | Zero-shot e Few-shot Prompting                                        | 27 |
| 2.9.2 | COSTAR                                                                | 28 |
| 3     | TRABALHOS RELACIONADOS                                                | 29 |
| 3.1   | Spatial-temporal large language model for traffic prediction          | 29 |
| 3.2   | Large language models are zero-shot time series forecasters           | 30 |
| 3.3   | PromptCast: A New Prompt-based Learning Paradigm for Time Series      |    |
|       | Forecasting                                                           | 31 |
| 3.4   | The impact of window size on univariate time series forecasting using |    |
|       | machine learning                                                      | 32 |
| 3.5   | Análise Comparativa                                                   | 33 |

| 3.5.1 | Abordagens Baseadas em LLMs                 | 33 |
|-------|---------------------------------------------|----|
| 3.5.2 | Abordagens Baseadas em Algoritmos Clássicos | 34 |
| 3.5.3 | Comparativo de Desempenho e Aplicabilidade  | 34 |
| 3.5.4 | Preliminar                                  | 35 |
| 4     | METODOLOGIA                                 | 36 |
| 4.1   | Visão Geral                                 | 36 |
| 4.2   | Conjunto de Dados                           | 37 |
| 4.3   | Ajustes de Dados                            | 39 |
| 4.4   | Modelagem e Treinamento de Modelos          | 39 |
| 4.5   | Prompt desenvolvido                         | 41 |
| 4.6   | Ambiente de execução dos experimentos       | 44 |
| 4.7   | Avaliação                                   | 44 |
| 4.8   | Cronograma                                  | 45 |
| 5     | RESULTADOS                                  | 46 |
| 6     | CONCLUSÕES E TRABALHOS FUTUROS              | 48 |
|       | REFERÊNCIAS                                 | 49 |

# 1 INTRODUÇÃO

A previsão de séries temporais é uma ferramenta essencial para a tomada de decisão em diversos setores, como o varejo e a mobilidade urbana. A capacidade de antecipar comportamentos futuros a partir de dados históricos permite não apenas a otimização de processos, mas também a identificação de padrões que podem influenciar estratégias operacionais e comerciais. Tradicionalmente, métodos como *Random Forest (RF)* e Redes Neurais *Long Short-Term Memory (LSTM)* têm sido amplamente utilizados para essa finalidade, empregando a técnica de janelas deslizantes que transforma os dados históricos em conjuntos de treinamento para algoritmos de aprendizado supervisionado Kane *et al.* (2014).

Nos últimos anos, contudo, o surgimento dos Modelo de Linguagem de Grande Escala - Large Language Models (LLM) e a evolução das técnicas de Engenharia de Prompt - Prompting Engineering (PE) têm ampliado o leque de abordagens disponíveis para a previsão de séries temporais. Estudos recentes demonstram o potencial desses modelos para capturar, de forma integrada, padrões sazonais e tendências Freitas *et al.* (2023b). Por exemplo, o trabalho de Liu *et al.* (2024) propõe um modelo espaço-temporal que incorpora embeddings específicos para representar as dependências entre dados de tráfego, enquanto Gruver *et al.* (2024) exploram a capacidade dos LLM em configurações *zero-shot* para realizar previsões sem a necessidade de ajustes finos. Além disso, o paradigma introduzido pelo PromptCast, conforme apresentado por Xue e Salim (2023), reformula a previsão de séries temporais como uma tarefa de transformação de sentenças, utilizando prompts — instruções textuais que guiam a resposta do modelo — para orientar a modelagem dos dados.

Diante desse cenário, o presente trabalho propõe uma abordagem comparativa entre métodos tradicionais – representados pelo RF e pela Rede Neural LSTM – e uma metodologia inovadora baseada em LLM, utilizando o modelo Gemini-1.5-pro orientado por um prompt desenvolvido especificamente para a tarefa de previsão. Para tanto, foram utilizados dois conjuntos de dados reais: um referente às vendas de produtos de um supermercado em Fortaleza e outro composto pelos registros de embarques em linhas de ônibus na mesma cidade. Essa escolha permite avaliar o desempenho dos modelos em cenários com padrões sazonais distintos, possibilitando uma análise robusta das técnicas empregadas.

A metodologia adotada envolve etapas fundamentais que garantem a qualidade e a consistência dos dados. Inicialmente, os conjuntos de dados são submetidos a um rigoroso processo de pré-processamento – que inclui a correção de valores ausentes, a remoção de registros duplicados e a normalização – a fim de preparar as séries temporais para a modelagem. Para os métodos tradicionais, a aplicação da técnica de janelas deslizantes possibilita a extração de características relevantes dos dados históricos, transformando-os em amostras rotuladas para o treinamento dos algoritmos. Em contrapartida, a abordagem baseada em LLM utiliza um prompt estruturado que direciona o modelo a identificar e extrapolar padrões temporais sem a necessidade de fragmentar os dados em blocos, permitindo uma análise mais holística da série.

A avaliação dos modelos é realizada por meio de métricas como o Erro Percentual Médio Simétrico (SMAPE) Makridakis (1993) e o Erro Padrão da Média (SEM) Altman e Bland (2005), as quais fornecem uma base quantitativa para a comparação do desempenho preditivo entre as abordagens tradicionais e a inovadora metodologia proposta. Assim, este trabalho não só busca evidenciar as vantagens e limitações inerentes a cada técnica, mas também contribuir para o avanço das práticas de previsão de séries temporais, integrando métodos clássicos com as inovações proporcionadas pelos LLM e pela PE.

# 1.1 Justificativa

A previsão de séries temporais é essencial para setores como varejo, mobilidade urbana, saúde, energia, agronegócio, finanças e entretenimento, auxiliando na demanda, consumo e tendências. A capacidade de antecipar tendências e padrões comportamentais permite a otimização de processos e a redução de custos operacionais. Embora métodos tradicionais, como RF e Redes Neurais LSTM, tenham obtido sucesso na modelagem desses dados, eles apresentam limitações na captura de padrões mais complexos e na adaptação a cenários com dados escassos ou altamente variáveis. Recentemente, o surgimento dos LLM e o avanço na PE têm demonstrado um potencial promissor para superar essas limitações, oferecendo uma abordagem inovadora que integra o contexto global dos dados sem a necessidade de fragmentação em janelas. Dessa forma, este trabalho justifica-se pela necessidade de investigar e comparar as abordagens tradicionais com a metodologia baseada em LLM, contribuindo para o avanço do conhecimento na previsão de séries temporais e ampliando as possibilidades de aplicação prática dessa tecnologia.

#### 1.2 Objetivo Geral

Comparar o desempenho de métodos tradicionais de previsão de séries temporais, como RF e LSTM, com uma abordagem inovadora baseada em LLM orientados por PE, utilizando o modelo Gemini-1.5-pro.

#### 1.3 Objetivos Específicos

- Realizar a coleta e o pré-processamento dos dados de séries temporais oriundos dos domínios de varejo e mobilidade urbana;
- Implementar os modelos tradicionais de previsão, aplicando a técnica de janelas deslizantes para a estruturação dos dados;
- Desenvolver um prompt específico para o LLM, a fim de orientar a previsão dos valores futuros da série;
- Treinar e ajustar os modelos RF, LSTM e o modelo LLM com base nos conjuntos de dados selecionados;
- Avaliar o desempenho preditivo dos modelos utilizando métricas quantitativas, como o SMAPE e o SEM;
- Analisar e comparar os resultados obtidos, identificando as vantagens, limitações e potenciais aplicações de cada abordagem.

#### 1.4 Organização do Trabalho

Este trabalho está organizado em seis capítulos. O Capítulo 1 apresenta a introdução, contextualizando o problema, a relevância da previsão de séries temporais e a motivação para o uso de LLMs. No Capítulo 2, são revisados os principais conceitos e técnicas relacionadas à previsão de séries temporais, incluindo Inteligência Artificial (IA), Machine Learning (Aprendizado de Máquina) (ML), Processamento de Linguagem Natural (PLN) e LLMs. O Capítulo 3 discute trabalhos relacionados, comparando métodos tradicionais e abordagens baseadas em LLMs. No Capítulo 4, é detalhada a metodologia adotada, abrangendo desde a coleta e pré-processamento dos dados até a modelagem e elaboração do prompt. O Capítulo 5 apresenta e analisa os resultados obtidos a partir dos experimentos realizados, avaliando o desempenho dos modelos e comparando-os com abordagens clássicas. Por fim, o Capítulo 6 discute as conclusões do estudo, destacando as contribuições, limitações e possíveis direções para trabalhos futuros.

# 2 FUNDAMENTAÇÃO TEÓRICA

Neste capítulo exploramos os alicerces que sustentam o desenvolvimento de soluções inteligentes, iniciando com uma análise da Inteligência Artificial e suas aplicações práticas por meio do Aprendizado de Máquina, tanto na vertente supervisionada quanto na não supervisionada. Em paralelo, o Processamento de Linguagem Natural (PLN) é examinado como ferramenta essencial para a compreensão e manipulação de conteúdos textuais, destacando a importância dos Large Language Models (LLMs) nesse contexto. E por fim, a Engenharia de Prompt é abordada, enfatizando métodos inovadores como o few-shot e o COSTAR.

## 2.1 Séries Temporais

As séries temporais representam conjuntos de observações ordenadas no tempo, permitindo a análise da evolução de uma determinada variável ao longo de períodos sucessivos DOWNING e CLARK (2012). Essas observações podem ser coletadas em intervalos regulares ou irregulares, caracterizando a série como discreta ou contínua, respectivamente. Para ilustrar, a Figura 1 apresenta um exemplo de séries temporais:

Os principais objetivos do estudo de séries temporais incluem a descrição, explicação, predição e controle de processos EHLERS (2009). Para entender a dinâmica dessas séries, é essencial considerar suas componentes fundamentais: tendência, sazonalidade, ciclo e erro Mendenhall e McClave (1993). A tendência refere-se a mudanças graduais e sistemáticas ao longo do tempo, podendo ser crescente ou decrescente. A sazonalidade está associada a

padrões periódicos previsíveis dentro de intervalos fixos, enquanto os ciclos ocorrem em períodos mais longos e de forma menos regular. Por fim, o erro representa as flutuações aleatórias não explicadas por tendências, sazonalidade ou ciclos.

A classificação das séries temporais também pode se basear em sua estacionariedade. Segundo Morettin e Toloi (1985), uma série é considerada estacionária quando se desenvolve no tempo aleatoriamente ao redor de uma média constante, refletindo alguma forma de equilíbrio. A estacionariedade fraca é um critério frequentemente adotado em modelos empíricos e ocorre quando a média e a variância são constantes ao longo do tempo, e a covariância entre dois períodos depende apenas da defasagem entre eles, e não do instante em que são computadas. Em contrapartida, uma série não estacionária apresenta variações em sua média ou variância ao longo do tempo.

Além disso, a ordem dos dados é um aspecto fundamental em séries temporais, pois a sequência das observações afeta diretamente a análise e os modelos preditivos Morettin e Toloi (1985). Esses modelos são utilizados para inferir padrões e tendências, contribuindo para a tomada de decisões em diversas áreas, como econometria, meteorologia e análise de poluição ambiental.

A literatura também distingue as séries temporais de acordo com sua classificação em contínuas ou discretas Fischer (1982). Uma série é considerada discreta quando suas observações são realizadas em intervalos de tempo finitos e enumeráveis, enquanto as séries contínuas possuem um conjunto infinito e não enumerável de observações. Exemplos comuns incluem medições diárias da poluição do ar, temperaturas mensais, índices da bolsa de valores e registros de marés.

Em resumo, a análise de séries temporais oferece um conjunto de ferramentas poderosas para entender a dinâmica de dados sequenciais, permitindo a extração de insights valiosos para a tomada de decisões em diversas áreas.

#### 2.2 Inteligência Artificial

A Inteligência Artificial (IA) emergiu como um campo interdisciplinar que busca desenvolver sistemas computacionais capazes de simular a capacidade humana de raciocinar, aprender e tomar decisões. O termo "Inteligência Artificial" foi formalmente introduzido por John McCarthy na Conferência de Dartmouth em 1956, marcando o início do estudo sistemático dessa área McCarthy *et al.* (2006). Entretanto, as primeiras discussões sobre a possibilidade

de construir máquinas inteligentes remontam à década de 1930, com as contribuições de Alan Turing e suas Máquinas de Turing, que forneceram a base teórica para a computação moderna Copeland (2015).

Desde então, a IA tem se expandido, englobando diferentes subcampos, como Aprendizado de Máquina (Machine Learning), Redes Neurais Artificiais, Processamento de Linguagem Natural e Visão Computacional. Essas abordagens permitiram avanços significativos em diversas áreas, tornando a IA uma ferramenta fundamental na atualidade Xu *et al.* (2021).

Apesar de seu amplo reconhecimento, não há consenso sobre uma definição única de IA. Russell e Norvig (2016)categorizam as definições da área em quatro abordagens principais: (i) sistemas que pensam como humanos, (ii) sistemas que agem como humanos, (iii) sistemas que pensam racionalmente e (iv) sistemas que agem racionalmente. Essas perspectivas refletem a diversidade do campo e suas aplicações.

- Sistemas que pensam como humanos (Teste de Turing): Criado por Alan Turing, esse teste avalia se um computador pode ser considerado inteligente ao enganar uma pessoa, fazendo-a acreditar que está conversando com outro humano. Para isso, a máquina precisa entender e responder perguntas de forma natural, raciocinar e aprender.
- Sistemas que agem como humanos (Modelagem Cognitiva): Essa abordagem tenta replicar o pensamento humano em máquinas. Para isso, utiliza métodos como estudos psicológicos e exames do cérebro. A ideia é criar programas que funcionem como a mente humana e resolvam problemas de forma semelhante. Essa linha de pesquisa combina inteligência artificial e psicologia para entender melhor como pensamos.
- Sistemas que pensam racionalmente (Leis do Pensamento): Baseada na lógica criada por Aristóteles, essa abordagem busca construir sistemas de IA que resolvem problemas por meio de regras lógicas. O desafio está em representar conhecimento informal de maneira rigorosa e no alto custo computacional para aplicar essas regras em problemas complexos.
- Sistemas que agem racionalmente (Agente Racional): Aqui, o foco é criar sistemas que tomam decisões inteligentes para atingir os melhores resultados. Um agente racional observa o ambiente, analisa informações e age de maneira lógica e eficiente. Essa abordagem é prática e amplamente usada, mas alcançar uma racionalidade perfeita ainda é um grande desafio, especialmente em ambientes complexos.

Gams *et al.* (2019) conceitua IA como a implementação de funções cognitivas

humanas, como percepção, aprendizado e tomada de decisão. Ahmed *et al.* (2022) ampliam essa definição ao considerar IA como um conjunto de tecnologias que permitem a sistemas e dispositivos perceberem, processarem informações e aprenderem com experiências passadas.

A IA abrange uma variedade de técnicas e métodos, sendo os principais:

- Aprendizado de Máquina: Campo que permite aos sistemas aprenderem padrões a partir de dados, utilizando algoritmos como redes neurais, árvores de decisão e modelos probabilísticos Wang (2019);
- Redes Neurais Artificiais: Inspiradas no funcionamento do cérebro humano, essas estruturas são capazes de processar grandes volumes de dados e resolver problemas complexos Yao (1999);
- Processamento de Linguagem Natural: Foca na interação entre computadores e a linguagem humana, permitindo aplicações como assistentes virtuais e tradutores automáticos (Jiang *et al.* 2022);
- Visão Computacional: Permite que máquinas analisem e interpretem imagens, sendo fundamental para aplicações como reconhecimento facial e veículos autônomos Lu (2019).

O desenvolvimento acelerado da IA tem impactado significativamente a sociedade. Empresas como Google, IBM e Microsoft investem em IA para aprimorar seus serviços e aumentar a eficiência operacional Zhang e Lu (2021). Além do setor tecnológico, a IA tem sido aplicada em áreas como saúde, finanças, entretenimento e educação, demonstrando sua versatilidade e potencial disruptivo.

Com o avanço das pesquisas, desafios éticos e regulatórios também surgem, como privacidade de dados, vieses algorítmos e impacto no mercado de trabalho Ludermir (2021). A necessidade de um desenvolvimento responsável da IA é cada vez mais evidente, com esforços acadêmicos e empresariais voltados para garantir que essa tecnologia beneficie a sociedade de forma equitativa.

A Inteligência Artificial evoluiu significativamente desde suas primeiras concepções, tornando-se um dos campos mais promissores da atualidade. Seu crescimento exponencial evidencia sua relevância em diversos setores, tornando-se um elemento essencial para o futuro da inovação tecnológica. No entanto, à medida que a IA avança, torna-se fundamental abordar questões éticas e regulatórias para garantir seu uso adequado e benéfico para a sociedade. Assim, compreender os fundamentos, as abordagens e os desafios da IA é essencial para avançar na pesquisa e aplicação dessa tecnologia de maneira responsável e eficaz.

# 2.3 Aprendizado de Máquina

O Aprendizado de Máquina (AM) é um ramo da Inteligência Artificial (IA) que tem como objetivo capacitar sistemas computacionais a aprenderem padrões a partir de dados e, com isso, melhorarem sua capacidade de tomada de decisão sem a necessidade de serem explicitamente programados para tal Russell e Norvig (2016), Coppin (2004). Essa característica o torna uma ferramenta essencial para a solução de problemas complexos em diversas áreas do conhecimento.

Segundo a definição da IBM (2023), o aprendizado de máquina utiliza dados e algoritmos para imitar a forma como os seres humanos aprendem, refinando continuamente sua precisão. Isso ocorre por meio de métodos estatísticos que permitem que os algoritmos sejam treinados para realizar classificações, previsões e extração de informações relevantes.

A evolução do aprendizado de máquina está ligada à crescente disponibilidade de dados e ao avanço no poder computacional. Embora suas origens possam ser traçadas até os primeiros modelos de neurônios artificiais Anantrasirichai e Bull (2022), foi na "Era da Informação" que essa abordagem ganhou destaque devido à coleta massiva de dados e ao desenvolvimento de algoritmos avançados.

O aprendizado de máquina pode ser categorizado em três principais abordagens: aprendizado supervisionado, aprendizado não supervisionado e aprendizado por reforço Russell e Norvig (2016). Cada uma dessas abordagens é adequada para diferentes tipos de problemas e apresenta desafios específicos.

#### *2.3.1 Aprendizado Supervisionado*

No aprendizado supervisionado, o algoritmo é treinado com um conjunto de dados rotulados, onde cada entrada está associada a uma saída desejada. O objetivo é permitir que o modelo aprenda padrões a partir desses exemplos e possa generalizar para novos dados não vistos Zhang e Lu (2021). Essa abordagem é amplamente utilizada em problemas de classificação e regressão.

Exemplos de aplicação incluem a filtragem de spam em e-mails Mohri (2018), onde um sistema aprende a categorizar automaticamente mensagens como spam ou não, e a análise de sentimentos, utilizada em redes sociais para identificar emoções expressas em textos.

# *2.3.2 Aprendizado Não Supervisionado*

Diferente do aprendizado supervisionado, o aprendizado não supervisionado não utiliza dados rotulados. Em vez disso, o algoritmo busca identificar padrões e estruturas nos dados, agrupando elementos semelhantes (clustering) ou reduzindo a dimensionalidade para extrair características essenciais Anantrasirichai e Bull (2022).

Uma das principais técnicas dessa abordagem é o clustering, que organiza os dados em grupos homogêneos. Um exemplo de aplicação é a segmentação de clientes em campanhas de marketing, onde os consumidores são agrupados com base em padrões de comportamento e preferências.

# *2.3.3 Aprendizado Por Reforço*

No aprendizado por reforço, um agente interage com um ambiente e aprende por meio de recompensas ou penalidades atribuídas a suas ações Russell e Norvig (2016). O objetivo é maximizar a recompensa acumulada ao longo do tempo, ajustando seu comportamento de acordo com a experiência adquirida. Essa abordagem é amplamente utilizada em jogos e robótica, onde sistemas aprendem a realizar tarefas complexas por meio da experimentação e feedback recebido.

#### 2.4 LSTM

As Redes Neurais Recorrentes (RNN)são amplamente utilizadas para processar dados sequenciais, pois permitem a modelagem de dependências temporais através de conexões recorrentes entre os neurônios. Entretanto, um dos principais desafios enfrentados por RNNs convencionais é a dificuldade em aprender relações de longo prazo devido ao problema do desaparecimento ou explodir do gradiente Hochreiter e Schmidhuber (1997). Para mitigar essa limitação, Hochreiter e Schmidhuber (1997)propuseram a arquitetura Long Short-Term Memory (LSTM), que se destaca pela capacidade de armazenar e processar informações ao longo de grandes intervalos temporais.

As redes LSTM possuem uma estrutura diferenciada em relação às RNNs tradicionais, sendo compostas por blocos de memória que incluem três elementos fundamentais: input gate, forget gate e output gate Duan *et al.* (2016). O input gate controla quais informações devem ser adicionadas ao estado da célula de memória, o forget gate decide quais informações

serão descartadas e o output gate regula a saída da célula para as próximas camadas Li *et al.* (2020). Essa estrutura possibilita que a rede aprenda padrões tanto de curto quanto de longo prazo, tornando-a eficaz para aplicações em séries temporais Siami-Namini *et al.* (2018). A Figura 2 ilustra a estrutura de uma rede neural LSTM, destacando os componentes principais do bloco de memória.

Figura 2 – Representação esquemática de uma rede LSTM, mostrando a propagação da informação ao longo do tempo. A célula central detalha os três gates (input, forget e output) responsáveis pelo controle do fluxo de informação dentro da rede.


Fonte: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

A arquitetura LSTM tem sido amplamente empregada em diferentes domínios, incluindo previsão de tráfego, análise financeira e modelagem de dados sequenciais em geral. No contexto da previsão de tráfego, a LSTM demonstrou desempenho superior em comparação com métodos tradicionais, como o ARIMA Fu *et al.* (2016). Laptev *et al.* (2017)propuseram uma abordagem baseada em LSTM para previsão da demanda de transporte urbano, utilizando uma estrutura encoder-decoder para capturar padrões complexos nos dados.

A capacidade das redes LSTM de lidar com a dinâmica não linear de fenômenos temporais é um dos principais fatores que justificam seu uso crescente em aplicações de previsão. A estrutura de memória permite que essas redes absorvam características complexas do conjunto de dados e, ao mesmo tempo, mantenham informações relevantes por períodos extensos. Dessa forma, a LSTM tem se consolidado como uma das principais abordagens para solução de problemas que envolvem dados sequenciais e dependências temporais prolongadas, destacandose como uma alternativa eficaz para desafios complexos em aprendizado de máquina.

# 2.5 Random Forest

O Random Forest (Árvore Aleatória) é um algoritmo de aprendizado de máquina baseado na abordagem de aprendizado em conjunto, introduzido por Breiman (2001). Esse método consiste na combinação de múltiplas árvores de decisão para formar um modelo mais robusto e preciso. A estratégia de aprendizado em conjunto visa reduzir a variabilidade dos modelos individuais e aumentar a precisão preditiva ao integrar várias previsões Sheykhmousa *et al.* (2020).

A ideia central do Random Forest é a construção de diversas árvores de decisão, cada uma treinada independentemente com subconjuntos aleatórios dos dados de treinamento (bootstrap dataset). Durante o treinamento, cada árvore recebe um subconjunto diferente de atributos, garantindo diversidade e evitando o sobreajuste. Dessa forma, a previsão final do modelo é obtida por meio de um processo de votação majoritária, no caso de classificação, ou pela média das previsões, no caso de regressão Zanotta *et al.* (2019).

Uma das principais vantagens do Random Forest é sua capacidade de lidar com grandes quantidades de dados e milhares de variáveis sem sobreajuste significativo Breiman (2001). O algoritmo se destaca também por ser robusto a outliers e ruídos nos dados, bem como por sua eficiência computacional quando comparado a outros modelos de aprendizado em conjunto Kulkarni e Lowe (2016).

Portanto, a utilização do Random Forest como ferramenta de aprendizado de máquina se justifica pela sua robustez, capacidade de lidar com dados complexos e facilidade de implementação, sendo uma escolha adequada para aplicações que exigem previsões confiáveis e interpretáveis.

#### 2.6 Processamento de Linguagem Natural

O Processamento de Linguagem Natural (PLN), ou Natural Language Processing (NLP), é uma área da inteligência artificial que busca permitir a interação entre humanos e máquinas por meio da linguagem natural. Seu objetivo principal é analisar e interpretar textos ou discursos, sejam eles escritos ou falados, utilizando diferentes abordagens computacionais Chowdhary e Chowdhary (2020).

O NLP tem suas raízes antes mesmo da invenção dos computadores modernos, com uma de suas primeiras aplicações sendo um dicionário desenvolvido no Birkbeck College, em Londres, no ano de 1948. Entretanto, os primeiros esforços na área enfrentaram dificuldades, pois os pesquisadores perceberam que o maior desafio não era apenas o conhecimento das línguas, mas sim a forma de representar esse conhecimento em um programa computacional Hancox (1996).

Para que os computadores sejam capazes de interpretar a linguagem humana, é fundamental compreender como os próprios humanos realizam essa interpretação. Por isso, grande parte do NLP está apoiada na linguística e na modelagem matemática. Existem diferentes abordagens para o processamento da linguagem, sendo as principais os métodos simbólicos e os métodos estatísticos. Enquanto os primeiros utilizam regras explícitas para interpretar o significado das palavras, os segundos baseiam-se em modelos probabilísticos desenvolvidos a partir de grandes volumes de dados Shannon (1948).

Com o avanço das técnicas de aprendizado profundo (deep learning), o NLP passou a empregar modelos estatísticos mais complexos, combinando linguística computacional com aprendizado de máquina e redes neurais profundas Torfi *et al.* (2020). Essas técnicas permitem que máquinas analisem textos de maneira semelhante aos humanos, utilizando métodos avançados como análise semântica, reconhecimento de entidades e geração de resumos Maulud *et al.* (2021). Aplicações práticas dessa tecnologia incluem tradução automática Jiang e Lu (2020), chatbots inteligentes Petrovic e Jovanovi ´ c (2021). ´

A relevância do NLP para a inteligência artificial é indiscutível, pois a linguagem humana é um dos recursos mais complexos de se modelar devido à sua infinidade de variações e regras Indurkhya e Damerau (2010). Além disso, a tecnologia tem se mostrado essencial em diversas aplicações, como a extração de informações de textos, classificação de documentos e geração de conteúdo. Os assistentes virtuais, como Siri, Alexa e Google Assistente, são exemplos de como o NLP tem se integrado à vida cotidiana das pessoas, permitindo interações mais naturais e eficientes Alencar *et al.* (2013), Jaybhaye *et al.* (2023).

Dessa forma, o NLP continua a evoluir, impulsionado pelo crescimento da inteligência artificial e pelo aumento da demanda por sistemas mais inteligentes e humanizados. Seu impacto abrange desde aplicações práticas em empresas até o desenvolvimento de inteligências artificiais cada vez mais avançadas, reforçando seu papel fundamental na interação entre humanos e máquinas.

## 2.7 Modelos de Linguagem de Grande Escala

Os Modelos de Linguagem de Grande Escala (LLMs) são um avanço significativo no campo da inteligência artificial e do processamento de linguagem natural (PLN). Esses modelos utilizam técnicas de aprendizado profundo para processar, compreender e gerar textos de forma autônoma Das *et al.* (2025). Por serem treinados com grandes volumes de dados textuais, os LLMs aprendem padrões e relações linguísticas, permitindo-lhes realizar diversas tarefas como responder perguntas, traduzir textos e gerar conteúdo coerente Fan *et al.* (2020).

A arquitetura predominante utilizada nos LLMs é a dos transformers, que se diferencia de modelos anteriores, como redes neurais recorrentes (RNNs), por empregar o mecanismo de self-attention. Esse mecanismo permite que o modelo avalie a importância de cada palavra em uma sequência, tornando a geração textual mais eficiente e coerente Yang *et al.* (2024). Graças a essa abordagem, modelos como *Generative Pre-Trained Transformers (GPT)*Radford *et al.* (2018), *LLaMA* Touvron *et al.* (2023)e *Gemini* 1 alcançaram resultados impressionantes na compreensão e produção de texto.

Os LLMs encontram aplicações em diversas áreas, incluindo assistentes virtuais, chatbots, avaliação automática de textos e até mesmo análise de criatividade na inovação de aplicativos. Sua capacidade de processar grandes volumes de informação os torna ferramentas valiosas na pesquisa científica e na automação de tarefas complexas Wei *et al.* (2024).

Em suma, os Large Language Models representam uma revolução no processamento de linguagem natural, permitindo avanços expressivos na interação entre humanos e máquinas. Contudo, é fundamental um uso responsável desses modelos, considerando tanto seu potencial quanto suas limitações e desafios éticos.

## 2.8 Gemini

O *Gemini*2 é um modelo de inteligência artificial (IA) desenvolvido pelo Google com capacidade multimodal, ou seja, pode processar e interpretar diferentes tipos de dados, como texto, código, imagens, áudio e vídeo. Essa característica permite maior flexibilidade na manipulação de informações e possibilita aplicações diversas em múltiplas áreas do conhecimento.

<sup>1</sup> <https://blog.google/technology/ai/google-gemini-ai/>

<sup>2</sup> <https://blog.google/technology/ai/google-gemini-ai/>

# *2.8.1 Características Principais*

- Multimodalidade: Treinado em múltiplos formatos de dados, o modelo pode correlacionar informações de diferentes fontes para uma compreensão mais abrangente.
- Flexibilidade: Disponível em diferentes versões (Ultra, Pro e Nano), o modelo pode ser adaptado para diversas tarefas e dispositivos.
- Capacidade de Processamento: Apresenta alto desempenho em tarefas como compreensão de linguagem natural, raciocínio lógico, geração de código e interpretação de imagens.
- Integração com Ferramentas: O modelo pode ser incorporado a diversas plataformas, auxiliando em processos computacionais e melhorando a interação com sistemas automatizados.

# *2.8.2 Aplicações*

O modelo pode ser empregado em diversas áreas, tais como:

- Busca de Informações: Possibilita aprimoramentos nos mecanismos de pesquisa, tornando a recuperação de dados mais eficiente.
- Produtividade: Pode ser utilizado na automação de tarefas, como geração de textos, desenvolvimento de código e análise de dados.
- Educação: Facilita processos educacionais personalizados, proporcionando feedback e auxiliando na criação de conteúdos interativos.
- Ciência: Contribui para a análise de grandes volumes de dados e modelagem de sistemas complexos em diferentes áreas do conhecimento.

# 2.9 Engenharia de Prompt

A engenharia de prompt é uma técnica essencial no uso de modelos de linguagem, pois permite a formulação de instruções específicas para guiar a geração de respostas mais precisas e alinhadas com as expectativas do usuário. Essa prática se mostra crucial, principalmente em aplicações que envolvem a interação com Large Language Models (LLMs), como o Gemini, onde a qualidade das respostas pode variar conforme a estrutura e o conteúdo dos prompts fornecidos Ekin (2023).

Os prompts são utilizados para interagir com os modelos de linguagem e podem assu-

mir diferentes formatos, desde perguntas diretas até comandos mais elaborados. A estruturação adequada dos prompts influencia diretamente a relevância e a coerência das respostas geradas, permitindo que os modelos de IA se adaptem a contextos específicos Giray (2023). Mesmo que os modelos de linguagem sejam treinados em grandes volumes de dados, a formulação cuidadosa dos prompts possibilita uma maior personalização das respostas sem a necessidade de reconfiguração ou retreinamento do modelo.

A engenharia de prompt também envolve o uso estratégico de palavras-chave, a clareza na formulação de perguntas e a adequação do estilo do prompt ao contexto necessário. Essas práticas permitem otimizar a interação com os modelos de linguagem, garantindo que o conteúdo gerado seja preciso, informativo e alinhado às necessidades específicas do usuário Ekin (2023). Assim, a engenharia de prompt se estabelece como um componente fundamental para extrair o máximo desempenho dos modelos de IA, tornando a interação com essas tecnologias mais eficiente e produtiva.

Nas seções subsequentes, exploraremos algumas das técnicas de engenharia de prompt que foram empregadas na elaboração desta pesquisa, incluindo:

#### *2.9.1 Zero-shot e Few-shot Prompting*

O Zero-shot Prompting3 consiste em fornecer apenas uma pergunta ou comando ao modelo, sem incluir exemplos adicionais, confiando em sua capacidade de interpretar e responder corretamente com base no treinamento prévio. No entanto, quando esse método não é suficiente, recorre-se ao Few-shot Prompting4 , que incorpora alguns exemplos dentro do próprio prompt para orientar melhor a geração de respostas.

O Few-shot Prompting é uma técnica de aprendizado de máquina que permite à IA realizar previsões precisas com um número mínimo de exemplos. Seus principais usos incluem:

- Classificação de texto: Identificação do tipo de conteúdo com base em poucos exemplos fornecidos.
- Geração de resumos: Criação de resumos seguindo o padrão dos exemplos dados.
- Análise de sentimentos: Determinação do tom emocional de um texto (positivo, negativo ou neutro) com base em exemplos rotulados.

<sup>3</sup> <https://www.promptingguide.ai/techniques/zeroshot>

<sup>4</sup> <https://www.promptingguide.ai/techniques/fewshot>

# *2.9.2 COSTAR*

Este é um método organizado para criar prompts de forma rápida e eficiente, garantindo que a resposta de uma LLM seja mais personalizada e relevante (Frugal Zentennial, 2024).(https://medium.com/@frugalzentennial/unlocking-the-power-of-costar-prompt-engineering-a-guide-and-example-on-converting-goals-into-dc5751ce9875) Ele considera seis elementos importantes:

- Contexto (C): Dê informações básicas para que a LLM entenda o cenário.
- Objetivo (O): Explique claramente o que você quer que a LLM faça.
- Estilo (S): Diga como você quer que o texto seja escrito (formal, descontraído, técnico, etc.).
- Tom (T): Defina o tom da resposta (amigável, sério, motivador, etc.).
- Público (A): Identifique quem vai ler a resposta para ajustá-la a esse grupo.
- Resposta (R): Especifique o formato da saída (como texto, lista ou arquivo JSON).

Figura 3 – Exemplo de um prompt, utilizando a técnica do COSTAR

### **Contexto**

Estou apresentando nosso novo aplicativo de fitness com tecnologia de IA, o FitAI, que oferece planos personalizados de condicionamento físico e nutrição.

## **Objetivo**

Seu objetivo é escrever uma postagem para o nosso blog, de modo que destaque os recursos e benefícios exclusivos do FitAI, diferenciando-o de outros aplicativos de fitness.

### **Estilo**

Adote o estilo envolvente e informativo dos blogs de fitness populares, tornando os aspectos técnicos complexos fáceis de entender.

### **Tom**

Motivacional e encorajador, inspirando os leitores a embarcar em sua jornada fitness com o FitAI.

## **Público**

Entusiastas do fitness e que também possuem um certo conhecimento de tecnologia, mas não necessariamente são especialistas em tecnologia.

#### **Resposta**

Uma postagem de blog bem estruturada com uma introdução, explicação detalhada dos recursos do FitAI, benefícios e um apelo à ação para baixar o aplicativo.

Fonte: elaborada pelo autor.

## 3 TRABALHOS RELACIONADOS

Nesta seção, serão apresentados os trabalhos correlatos, com o objetivo de destacar as contribuições relevantes de pesquisadores e profissionais no desenvolvimento de algoritmos baseados em LLMs para a previsão de séries temporais. A análise dos resultados enfatiza a identificação de estudos que utilizam modelos open-source, integrando estratégias avançadas de engenharia de prompt, como zero-shot, cadeia de pensamento e few-shot. Além disso, são abordados trabalhos que aplicam técnicas baseadas em transformers, bem como estudos que empregam algoritmos clássicos de aprendizado de máquina, como LSTM e Random Forest, proporcionando uma visão abrangente sobre as abordagens utilizadas na área de previsão de séries temporais.

### 3.1 Spatial-temporal large language model for traffic prediction

O artigo Liu *et al.* (2024)propõe um novo modelo para a previsão de tráfego, abordando as limitações dos modelos existentes em capturar dependências espaço-temporais complexas. Diferentemente das abordagens tradicionais que evoluíram de modelos de séries temporais para redes neurais complexas, este trabalho explora o uso de Large Language Models (LLMs), que ganharam destaque na análise de séries temporais.

Os autores argumentam que os métodos baseados em LLMs frequentemente negligenciam o aspecto espacial dos dados de tráfego, que é crucial para previsões precisas. Para resolver essa limitação, o ST-LLM define os timesteps em cada local como tokens e emprega uma camada de spatial-temporal embedding para enfatizar as localizações espaciais e os padrões temporais globais.

Uma contribuição chave do artigo é a introdução de uma estratégia de partially frozen attention (PFA), que adapta o LLM para capturar dependências espaço-temporais globais, preservando o conhecimento adquirido durante o pre-treinamento. Através de experimentos extensivos em conjuntos de dados de tráfego reais, os autores demonstram que o ST-LLM supera os modelos existentes, mostrando um desempenho robusto em cenários de few-shot e zero-shot prediction.

Em resumo, o artigo apresenta uma abordagem inovadora para a previsão de tráfego, combinando as capacidades dos LLMs com uma representação espaço-temporal dos dados e uma estratégia de treinamento adaptada para capturar as complexas dependências presentes nos

dados de tráfego. O ST-LLM oferece uma alternativa promissora aos modelos tradicionais, com potencial para melhorar a precisão e a adaptabilidade das previsões de tráfego.

#### 3.2 Large language models are zero-shot time series forecasters

A previsão de séries temporais é um desafio significativo devido à natureza variável e frequentemente incompleta dos dados. Diferentemente de outras modalidades, como vídeo ou áudio, séries temporais agregadas podem conter sequências de fontes distintas, frequentemente com valores ausentes. Nesse contexto, modelos de linguagem de grande porte (LLMs) emergem como uma abordagem promissora para preencher a lacuna entre os métodos tradicionais, que tendem a ser excessivamente enviesados, e os modelos modernos de aprendizado profundo, que oferecem capacidades representacionais avançadas. O Gruver *et al.* (2024)apresenta em seu artigo o método LLMTIME, que propõe a utilização de LLMs pré-treinados, como GPT-3 e LLaMA-2, para previsão de séries temporais contínuas.

O LLMTIME converte séries temporais em sequências numéricas representadas como strings de texto e utiliza a capacidade dos LLMs de extrapolar padrões para prever valores futuros. Essa abordagem apresenta vantagens significativas, como a eliminação da necessidade de ajuste fino, reduzindo a barreira de entrada para a aplicação de LLMs em séries temporais, além de ser altamente aplicável em cenários com disponibilidade limitada de dados. Além disso, o método aproveita a natureza probabilística dos LLMs, permitindo capturar a incerteza inerente a séries temporais estocásticas.

A avaliação do LLMTIME foi realizada com base em métricas como o *Erro Absoluto Médio (MAE)* e o *Continuous Ranked Probability Score (CRPS)*, que permitem comparar modelos baseados em amostragem sem necessidade de probabilidades explícitas. A previsão é feita por meio da extração de múltiplas amostras do modelo, cujas estatísticas são utilizadas para construir estimativas pontuais ou distribucionais. Os resultados obtidos pelo LLMTIME foram comparados com métodos tradicionais, como *ARIMA, redes convolucionais temporais (TCNs) e N-HiTS*, utilizando conjuntos de dados amplamente reconhecidos, como Darts, Monash e Informer.

Por fim, os autores discutem os desafios de aplicar modelos LLM a séries temporais, destacando que, embora modelos base apresentem boas propriedades de escalabilidade, esse comportamento pode não se manter para modelos pós-processados para aplicações de chatbot. Um exemplo é o GPT-4, que exibe melhorias substanciais em tarefas de linguagem natural em relação ao GPT-3 e LLaMA, mas cuja aplicação efetiva em séries temporais permanece um

desafio aberto.

#### 3.3 PromptCast: A New Prompt-based Learning Paradigm for Time Series Forecasting

A previsão de séries temporais tem sido amplamente estudada na literatura, com abordagens que variam desde modelos estatísticos clássicos, como ARIMA (AutoRegressive Integrated Moving Average), até técnicas baseadas em redes neurais profundas, como LSTMs (Long Short-Term Memory) e Transformers. No entanto, recentes avanços no uso de Modelos de Linguagem de Grande Escala (LLMs) têm aberto novas possibilidades para essa tarefa, explorando o uso de prompts como mecanismo de entrada para modelagem e previsão.

O Xue e Salim (2023)propõe um novo paradigma para a previsão de séries temporais, utilizando modelos de linguagem para capturar padrões temporais e gerar previsões a partir de descrições textuais. Trabalhos anteriores demonstraram que LLMs podem ser adaptados para tarefas diversas, incluindo raciocínio aritmético e geração de código, sugerindo que sua aplicação na previsão de séries temporais pode ser promissora. No entanto, a capacidade de generalização desses modelos para diferentes domínios ainda é um desafio em aberto.

Os modelos de previsão de séries temporais existentes geralmente recebem uma sequência de valores numéricos como entrada e produzem valores numéricos como saída. Os modelos mais avançados atualmente são amplamente baseados na arquitetura Transformer, com múltiplos mecanismos de codificação para incorporar contexto e semântica dos dados históricos. Inspirado pelos sucessos dos modelos de linguagem pré-treinados, PromptCast propõe reformular a previsão de séries temporais como uma tarefa de transformação de sentenças, permitindo a aplicação direta de modelos de linguagem para essa finalidade.

Para facilitar a pesquisa e o desenvolvimento nessa área, o artigo apresenta o PISA, um novo conjunto de dados em larga escala, juntamente com um benchmark que permite avaliar diferentes modelos e abordagens. O PISA inclui três cenários reais de previsão: temperatura das cidades (CT), carga de consumo de eletricidade (ECL) e mobilidade humana (SG). Esses conjuntos de dados foram selecionados para cobrir diferentes domínios e desafios, permitindo uma análise mais abrangente da aplicabilidade do PromptCast.

Os resultados demonstram que o PromptCast, ao utilizar modelos de geração de linguagem, representa uma direção promissora para pesquisa em previsão de séries temporais. Em comparação com abordagens convencionais baseadas em valores numéricos, o PromptCast exibe uma capacidade de generalização superior, especialmente em configurações de zero-shot. Além disso, ao discutir os resultados e limitações do PromptCast, este estudo visa incentivar futuras pesquisas em temas como a criação de prompts automáticos, explicabilidade dos modelos de linguagem e aplicações práticas, como sistemas de perguntas e respostas e chatbots orientados por séries temporais. A exploração desses aspectos pode ampliar ainda mais o uso de LLMs na previsão de séries temporais e consolidar esse novo paradigma como uma alternativa viável às abordagens tradicionais.

# 3.4 The impact of window size on univariate time series forecasting using machine learning

A escolha do tamanho da janela (w) em problemas de previsão de séries temporais é um aspecto fundamental na modelagem desses dados, influenciando diretamente o desempenho dos modelos de aprendizado de máquina. Diversos estudos analisam o impacto desse hiperparâmetro, buscando compreender como a quantidade de unidades temporais utilizadas como entrada pode afetar a capacidade de generalização dos algoritmos Azlan *et al.* (2019).

Pesquisas anteriores indicam que o tamanho da janela deve equilibrar informação suficiente para capturar padrões sazonais e tendências de longo prazo, sem introduzir ruídos desnecessários decorrentes de flutuações aleatórias Bergström e Hjelm (2019). Em estudos comparativos, observa-se que a variação de w impacta diretamente métricas de avaliação como erro quadrático médio (MSE) e erro absoluto médio (MAE), sendo que a escolha inadequada desse hiperparâmetro pode levar a um comprometimento da precisão preditiva Shynkevich *et al.* (2017).

No trabalho de Freitas *et al.* (2023a), foram analisadas 40 séries temporais de dois domínios distintos, utilizando diferentes abordagens de aprendizado de máquina, incluindo Bagging, Boosting, Stacking e Redes Neurais Recorrentes (RNNs). Os resultados indicaram que a expansão da janela melhora as previsões até um ponto de estabilização, normalmente quando w supera 100 passos temporais. Além disso, os autores destacam que modelos baseados em arquiteturas recorrentes nem sempre superam modelos de ensemble, o que reforça a importância de se explorar diferentes técnicas para previsão univariada.

Outros estudos na literatura também relatam tendências similares. Por exemplo, trabalhos que comparam diferentes tamanhos de janela em algoritmos tradicionais e redes neurais profundas indicam que o uso de janelas muito pequenas pode levar a previsões imprecisas devido à falta de informação histórica, enquanto janelas excessivamente grandes podem dificultar o

aprendizado do modelo ao introduzir ruídos desnecessários Liu *et al.* (2022). Assim, determinar um tamanho de janela adequado continua sendo um desafio relevante na modelagem de séries temporais, necessitando de abordagens empíricas para encontrar valores ótimos para cada conjunto de dados e domínio de aplicação.

Diante dessas considerações, a presente pesquisa contribui para o entendimento da influência do tamanho da janela na previsão de séries temporais, comparando diferentes abordagens de aprendizado de máquina e identificando padrões de estabilização na precisão preditiva. Os achados reforçam a necessidade de estudos adicionais que explorem essa relação em outros contextos e tipos de séries temporais, contribuindo para avanços no campo da previsão automatizada.

# 3.5 Análise Comparativa

Nesta seção, realizamos uma análise comparativa entre os trabalhos relacionados apresentados, com o objetivo de destacar suas principais contribuições, limitações e a forma como abordam a previsão de séries temporais por meio de Modelos de Linguagem de Grande Escala (LLMs) e outros métodos clássicos de aprendizado de máquina.

### *3.5.1 Abordagens Baseadas em LLMs*

Os trabalhos de Liu *et al.* (2024), Gruver *et al.* (2024) e Xue e Salim (2023)exploram o uso de LLMs para previsão de séries temporais, cada um com um enfoque distinto:

- 1. O ST-LLM Liu *et al.* (2024) introduz uma abordagem que incorpora dependências espaçotemporais, destacando-se por utilizar embeddings específicos para capturar relações espaciais e temporais. Seu diferencial é o uso da partially frozen attention (PFA), que permite um melhor aproveitamento do conhecimento pré-treinado do modelo.
- 2. O LLMTIME Gruver *et al.* (2024) propõe uma estratégia inovadora ao converter séries temporais em sequências textuais, utilizando a capacidade intrínseca dos LLMs para inferir padrões temporais sem necessidade de ajuste fino. O estudo destaca a aplicabilidade dessa abordagem em cenários com dados limitados e alto grau de incerteza.
- 3. O PromptCast Xue e Salim (2023) reformula a previsão de séries temporais como uma tarefa baseada em transformação de sentenças, explorando prompts como mecanismo central para modelagem. Esse trabalho também se diferencia ao apresentar um benchmark

próprio, o PISA, com conjuntos de dados diversos.

Embora os três trabalhos utilizem LLMs, suas abordagens variam na representação dos dados e nos métodos de inferência. O ST-LLM enfatiza relações espaço-temporais, enquanto o LLMTIME foca na conversão textual das séries temporais, e o PromptCast introduz um novo paradigma de modelagem baseado em prompts.

# *3.5.2 Abordagens Baseadas em Algoritmos Clássicos*

O estudo de Freitas *et al.* (2023a)investiga o impacto do tamanho da janela na previsão de séries temporais, utilizando técnicas tradicionais de aprendizado de máquina, como ensemble learning (Bagging, Boosting e Stacking) e Redes Neurais Recorrentes (RNNs). Ao contrário dos trabalhos baseados em LLMs, esse estudo se concentra na otimização de hiperparâmetros e na influência da quantidade de dados históricos na qualidade das previsões.

Os resultados indicam que a expansão da janela melhora a precisão das previsões até um certo limite, reforçando a necessidade de um balanceamento entre informação histórica e ruído. Essa abordagem contrasta com os modelos baseados em LLMs, que buscam inferir padrões sem necessidade de janelas fixas.

#### *3.5.3 Comparativo de Desempenho e Aplicabilidade*

Os modelos baseados em LLMs apresentam vantagens em cenários com poucos dados e alto grau de incerteza, devido à sua capacidade de generalização e de aprendizado implícito de padrões temporais. No entanto, eles também enfrentam desafios, como a necessidade de recursos computacionais elevados e dificuldades na interpretação dos resultados.

Por outro lado, os modelos clássicos, como os utilizados por Freitas *et al.* (2023a), são mais interpretáveis e permitem um controle mais refinado sobre os parâmetros da previsão, mas podem exigir mais ajustes e dados para alcançar um desempenho competitivo.

Em termos de aplicação, o ST-LLM se mostra particularmente adequado para problemas que envolvem dependências espaciais, como previsão de tráfego. O LLMTIME é mais versátil e pode ser aplicado a diferentes domínios sem necessidade de ajuste fino. O PromptCast, por sua vez, representa uma abordagem inovadora, mas ainda requer estudos adicionais para validar sua eficácia em cenários reais.

# *3.5.4 Preliminar*

A evolução dos modelos para previsão de séries temporais tem demonstrado que os LLMs oferecem novas possibilidades e desafios para a área. Enquanto abordagens tradicionais continuam sendo eficazes e amplamente utilizadas, os modelos de linguagem emergem como uma alternativa promissora, principalmente em cenários com dados limitados e onde a interpretação contextual dos padrões é necessária. No entanto, sua adoção ainda requer um maior entendimento sobre suas limitações e a elaboração de métodos para melhor integração com as técnicas já estabelecidas na literatura.

# 4 METODOLOGIA

Este capítulo apresenta a metodologia utilizada na previsão de séries temporais com modelos LLMs e métodos clássicos de aprendizado de máquina. A Seção 4.1 fornece uma visão geral do processo, ilustrado por um fluxograma que abrange desde a coleta e pré-processamento dos dados até a análise dos resultados. A Seção 4.2 detalha os conjuntos de dados utilizados (varejo e transporte público), destacando suas características e desafios. Na Seção 4.3, discutimos as técnicas de pré-processamento, como tratamento de valores ausentes, remoção de duplicatas e normalização. A Seção 4.4 aborda o treinamento dos modelos Random Forest e LSTM, explicando o uso de janelas deslizantes. A Seção 4.5 descreve o desenvolvimento do prompt para LLMs, destacando sua estrutura e impacto na previsão. A Seção 4.6 detalha as ferramentas utilizadas para o desenvolvimento dos algoritmos, incluindo a linguagem de programação, as bibliotecas e suas respectivas versões. Por fim, a Seção 4.7 apresenta as métricas utilizadas para avaliação dos modelos, com destaque para o Erro Percentual Médio Simétrico (*SMAPE*) e o Erro Padrão da Média (*SEM*). Esse detalhamento garante transparência e reprodutibilidade ao estudo.

#### 4.1 Visão Geral

O modelo proposto, ilustrado na Figura 4, é dividido em cinco etapas principais.

Figura 4 – A figura apresenta o fluxograma do modelo proposto, detalhando suas principais etapas e o fluxo de processamento dos dados.

!(_page_37_Picture_6.jpeg)

Fonte: Elaborada pelo autor.

Primeiramente, são definidos os conjuntos de dados utilizados no processo. Em seguida, realizase o pré-processamento, no qual os dados passam por ajustes para tratar possíveis duplicatas e valores faltantes. Na terceira etapa, são configurados os parâmetros dos modelos empregados

na previsão. Posteriormente, a sequência temporal é utilizada como entrada para os modelos Random Forest e LSTM, enquanto, no caso da LLM, os dados são estruturados em forma de prompt. Por fim, na etapa de visualização e avaliação, são gerados gráficos que representam os valores previstos, além de uma análise da quantidade de tokens consumidos especificamente pela LLM. As métricas de avaliação SMAPE e SEM são calculadas para medir o desempenho dos modelos.

# 4.2 Conjunto de Dados

O primeiro conjunto conjunto de dados trata de séries temporais de vendas de produtos de uma loja do varejo, no setor de supermercado, localizado na cidade de Fortaleza-CE. Obtiveram-se informações de vendas de vinte produtos da curva A (itens com maior contribuição no faturamento da loja) em um período de 02 de Janeiro/2017 a 30 de Abril/2019, totalizando cerca de 850 dias. As vendas dos produtos, por unidades ou por quilogramas, foram agrupadas por dias para cada um dos produtos analisados e montadas as séries temporais finais. Os identificadores dos produtos foram anonimizados. Neste trabalho utilizamos como dado de treino 02 de janeiro de 2017 até 02 janeiro de 2019, já o dado de teste foi de 03 de janeiro de 2019 até 03 de março de 2019. A Figura 5 ilustra uma série temporal de venda por dia de um produto da curva A em uma amostra de 200 dias.

0 10 20 30 40 50 15 20 25 30 35 40 45 55 Real Previsão de vendas Dias Vendas

Figura 5 – Quantidade de vendas de um produto de curva A, em uma amostra de 60 dias.

Fonte: Elaborada pelo Autor.

O segundo conjunto de dados trata de séries temporais do número de embarques de

passageiros nas vinte linhas de ônibus com maior uso dentro do sistema de transporte público na cidade de Fortaleza (Ceará). Os passageiros do sistema de ônibus possuem um *smart card* com o identificador do usuário e, toda vez que este cartão é usado, um registro de embarque é gravado. Os dados foram cedidos pela Prefeitura de Fortaleza e foram utilizados em outros artigos, respeitando a Lei Geral de Proteção de Dados Pessoais (LGPD) Caminha e Furtado (2017), Ponte *et al.* (2018), Bomfim *et al.* (2020), Ponte *et al.* (2021). Neste trabalho, foi utilizado como dado de treinamento o período de 01 de março de 2018 até 04 de junho de 2018, já o teste foi de uma semana, 168 horas, de 05 de junho de 2018 até 11 de junho de 2018. Desta forma, foram geradas vinte séries temporais com mais de 2280 horas de embarques para cada linha de ônibus no treino e 168 horas no teste. A Figura 6 ilustra uma série temporal de embarque por hora de uma linha de ônibus, detalhando os padrões de sazonalidade que ocorrem nos veículos em uma amostra de cerca de 7 dias (168 horas).

0 20 40 60 80 100 120 140 160 0 200 400 600 800 1000 1200 1400 Real Passageiros do ônibus Dias Vendas

Figura 6 – Quantidade de passageiros em uma linha de ônibus durante as primeiras 168 horas.

Fonte: Elaborada pelo Autor.

Os dados do domínio de Varejo apresentam padrões sazonais mais complexos e variados em comparação com os dados do domínio de Mobilidade. As vendas no setor de Varejo sofrem variações significativas devido a fatores como promoções, eventos sazonais e oscilações na oferta e demanda, que não estão totalmente capturados no conjunto de dados utilizado neste estudo. Isso resulta em padrões sazonais distintos em cada série temporal, onde certos produtos podem ter picos de vendas imprevisíveis, dependendo de campanhas promocionais ou mudanças nas condições de mercado. Por outro lado, os dados de Mobilidade, que registram o número de embarques de passageiros em linhas de ônibus, exibem padrões sazonais mais regulares, com variações previsíveis baseadas em fatores como dias da semana e horários do dia. Embora existam linhas mais movimentadas nos finais de semana ou com maior demanda em determinados dias da semana, a variação dentro de cada série é relativamente baixa, tornando os padrões temporais mais homogêneos e menos complexos de modelar.

# 4.3 Ajustes de Dados

Essa etapa é relativamente simples e tem como objetivo tratar situações que podem surgir em determinados conjuntos de dados. Entre os dois conjuntos utilizados — um referente a uma empresa de varejo da cidade de Fortaleza e outro contendo dados de mobilidade urbana das linhas de ônibus da mesma cidade —, foi necessário realizar ajustes apenas no *dataset* de mobilidade urbana. Isso ocorreu porque esse conjunto apresentava dados duplicados e valores ausentes em determinados horários, tornando-o não sequencial, o que poderia impactar negativamente a previsão dos modelos.

Para cada problema identificado, foi adotada uma estratégia específica: no caso dos dados duplicados, os valores foram somados e apenas um registro foi mantido para o respectivo horário. Já para os valores ausentes, adicionamos o horário correspondente ao *dataset* e atribuímos o valor zero, pois não houve coleta de dados nesse intervalo. Esses ajustes visam garantir a qualidade dos dados e melhorar a precisão da previsão da série temporal.

#### 4.4 Modelagem e Treinamento de Modelos

Utilizou-se o conceito de janelas deslizantes no processo de modelagem do problema de previsão de série temporal Chu (1995)para os modelos *Random Forest* e *LSTM*. A técnica de janelas deslizantes trata de uma abordagem em que o dado da série temporal é dividido em segmentos menores e de tamanho constante (*w*). O termo deslizante refere-se ao processo de deslocamento da janela ao longo da série e com um determinado passo (*p*) para a direita, permitindo a construção de um conjunto de dados de treinamento.

As janelas deslizantes tratam-se de um artifício para transformar a série temporal em um conjunto de dados rotulado, em que cada janela contém um conjunto de observações ocorridas no passado da série temporal e que consideramos a entrada para os modelos de previsão. A observação logo após o final da janela é definida como o valor alvo que se deseja prever dado a janela passada. Desta forma, está técnica é bastante aderente a métodos de Aprendizado de

Máquinas supervisionados de regressão para realizar previsão em séries temporais.

A Figura 7 ilustra o processo da geração dos exemplos de entradas e saídas que serão utilizadas para o treinamento de modelos de IA. Uma série temporal diária, em verde, como exemplo, será transformada em um conjunto de dados supervisionado. Uma janela de tamanho *w* é aplicada, gerando a primeira amostra de entrada do conjunto e que possui *w* valores, representando as características que devem ser aprendidas pelos modelos. Somado as informações da janela, é concatenado um *Embedding de tempo* com informações temporais a respeito da variável alvo, são elas: hora do dia (excepcionalmente para as séries de mobilidade); dia da semana; dia do mês; e dia do ano. Estas características permitem que os modelos aprendam, a partir de padrões e tendências presentes em observações passadas, as dependências temporais das séries. O dia logo após a janela representa a variável alvo que se deseja prever. Em seguida, desloca-se a janela *p* passos à direita, a fim de se obter novas amostras para o conjunto de dados e repetindo o processo até percorrer toda a série. Dependendo de *w* e *p* irá existir uma sobreposição nos dados, reforçando a descoberta do padrão dos dados e aumentando o número de amostras de treinamento. A parte final do fluxo da Figura 7 ilustra o processo de treinamento de modelos de Aprendizado de Máquina a partir dos dados rotulados das etapas anteriores.

Jul/2017 Aug/2017 Sep/2017 Oct/2017 Nov/2017 Dec/2017 Jan/2018 Feb/2018 Mar/2018 Apr/2018 May/2018 Jun/2018 Jul/2018 150

Figura 7 – Construção de exemplos utilizando o conceito de janelas deslizantes.

Fonte: Elaborada pelo autor.

(aproximadamente três meses), enquanto para as séries temporais de mobilidade urbana, o tamanho da janela foi definido como *w* = 168 (exatamente uma semana). Esses valores foram escolhidos porque abrangem um período de tempo suficiente para capturar os principais padrões de sazonalidade presentes nas séries, garantindo que as variações mais significativas sejam refletidas nos exemplos modelados.

Os modelos utilizados serão do tipo *ensemble* (*Random Forest* e uma rede neural (*LSTM*). No *Random Forest* Breiman (2001) foram utilizados os parâmetros padrões do *Scikitlearn* Pedregosa *et al.* (2011). Já na *LSTM* Hochreiter e Schmidhuber (1997) foi utilizada implementação do *Tensorflow* Abadi *et al.* (2016), com os parâmetros *neurons* = 200, *batch_size* = 32, e com função de ativação *ReLu*, *epochs* = 200, validação de 20% e otimizador "Adam" com learning rate de 0,0001. No caso da LLM *Gemini-1.5-PRO*, foi configurada apenas a temperatura de resposta para 1, mantendo os demais parâmetros, como max *tokens*, *top-p* e *top-k*, em seus valores padrão.

A escolha dos modelos *Random Forest* e *LSTM* para a previsão de séries temporais nesta pesquisa se justifica pela natureza das séries temporais analisadas, que são univariadas e não possuem um volume muito grande de dados no tempo. O *Random Forest* é conhecido por sua robustez em problemas univariados, especialmente quando se lida com séries temporais curtas e com padrões sazonais relativamente simples Freitas *et al.* (2023b). Já o *LSTM* é amplamente utilizado para capturar dependências temporais e padrões de curto e médio prazo, sendo eficaz em séries temporais com uma estrutura moderadamente complexa Sagheer e Kotb (2019). O uso de modelos *Transformers*, embora poderoso, não seria indicado neste contexto, pois esses modelos são mais apropriados para séries temporais que envolvem grandes volumes de dados no tempo ou múltiplas características que variam simultaneamente (séries multivariadas) com padrões complexos de sazonalidade Zeng *et al.* (2023). Dado que as séries temporais utilizadas nesta pesquisa não possuem essas características, a aplicação de *Transformers* seria desnecessária e potencialmente menos eficiente, justificando assim a escolha dos modelos mais simples e adequados ao tipo de dados disponível.

### 4.5 Prompt desenvolvido

Neste estudo, o processo de modelagem para a previsão de séries temporais utilizando LLMs é bastante diferente do que é feito em modelos como o *LSTM* e *Random Forest*, onde o conceito de janelas deslizantes é essencial. No caso dos LLMs, não faz sentido utilizar uma abordagem baseada em janelas, uma vez que o modelo opera sobre toda a sequência de dados fornecida de uma única vez, sem a necessidade de fragmentação dos dados em blocos temporais. Em vez disso, a modelagem é orientada por um *prompt* elaborado que instrui o modelo a realizar previsões de acordo com os padrões e tendências capturados nos dados.

A Figura 8 apresenta o *prompt* utilizado neste estudo para realizar as previsões de séries temporais. Esse *prompt* foi desenvolvido para aproveitar as capacidades de um LLM, guiando-o a focar nos aspectos mais relevantes da série temporal para realizar a previsão. Abaixo, detalhamos cada elemento do *prompt* e explicamos seu funcionamento:

- Variável *h*: Representa a quantidade de dias (ou outra unidade de tempo, conforme definido pela variável *passo_de_tempo*) a serem previstos, ou seja, define o horizonte de previsão que o modelo deve considerar ao gerar os valores futuros;
- Variável *passo_de_tempo*: Indica a unidade de tempo dos dados fornecidos, podendo ser horas, dias, semanas, meses, etc. Essa variável ajuda o modelo a entender a granularidade dos dados e a ajustar sua análise para captar adequadamente os padrões sazonais e tendências relevantes para aquela periodicidade;
- Variável *dados*_*treino*: Contém a série temporal que será utilizada para realizar a previsão. Essa série temporal é fornecida até o limite que, nos outros modelos (LSTM e *Random Forest*), seria considerado como o final do conjunto de dados de treinamento, excluindo-se os dados de teste. Desta forma, o LLM tem acesso apenas às informações que estariam disponíveis em um cenário de previsão real, semelhante ao processo realizado nos outros modelos de aprendizado de máquina;
- Variável *contexto*: Fornece informações adicionais sobre o período de tempo correspondente a determinadas posições no vetor de valores, como o dia da semana. Essa contextualização temporal desempenha um papel similar ao da janela de modelagem utilizada em LSTM e *Random Forest*, ajudando o modelo a capturar variações sazonais e padrões específicos ao gerar as previsões. Exemplos do conteúdo da variável *contexto* incluem:

Para dados que o passo de tempo em horas:

– Dia 0: posições 432 a 455 (Segunda-feira);

– Dia 1: posições 576 a 599 (Domingo);

– Dia 2: posições 696 a 719 (Sexta-feira).

Para dados que o passo de tempo em dias:

Figura 8 – Definição do *prompt* utilizado na previsão de séries temporais. A informações que aparecem entre chaves representam variáveis que são substituídas sempre que se deseja prever uma nova série.

#### **Contexto**

Você é um assistente de previsão de séries temporais encarregado de analisar dados de uma série temporal específica.

A série temporal tem dados de { h } períodos consecutivos. Cada anotação da série temporal representa a incidência de um evento que ocorre a cada { passo_de_tempo }.

#### **Objetivo**

Seu objetivo é prever a incidência de um evento para as próximos(as) { h } { passo_de_tempo }, levando em consideração não apenas os períodos anteriores, mas também o contexto geral. Para fazer isso com precisão, leve em consideração:

- **Padrões sazonias**: Picos e vales recorrentes que ocorrem com determinada periodicidade;
- **Tendências**: Tendências de subida ou descida na série temporal.

#### **Regras da Saída**

Após analisar os dados fornecidos e compreender os padrões, gere uma previsão para os(as) próximos(as) { h } { passo_de_tempo }, com as seguintes regras:

- A saída deve ser uma lista contendo apenas os valores previstos, sem explicação adicional ou texto introdutório;
- Em hipótese alguma gere um código;
- Forneça apenas e exclusivamente um vetor contendo a quantidade de números solicitados;
- A previsão deve começar imediatamente após o último dado fornecido.

```
Exemplo de Saída para N={ h }
{ dados_prompt[:h] }
```

#### **Instruções Adicionais**

- **Padrões Semanais**: Utilize os dados fornecidos para entender padrões sazonais, como picos de incidência em determinados períodos;
- **Dia da Semana**: O dia da semana também influencia a ocorrência de eventos;
- **Duração de um evento**: A série temporal fornecida representa a ocorrência de um evento a cada { passo_de_tempo }.

#### **Série temporal a ser analisada**

```
{ dados_treino }
```

#### **Contexto do período de tempo a ser considerado na previsão:**

```
{ contexto }
```

Gere um vetor com {h } posições ( N={ h } ) prevendo os números da sequência

Fonte: Elaborada pelo autor.

- posição 0 (Segunda-feira);
- posição 1 (Terça-feira);
- posição 2 (Quarta-feira).

O *prompt* elaborado foi estruturado para garantir que o LLM focasse em prever a sequência de valores futuros sem gerar código, explicações ou qualquer conteúdo adicional que pudesse interferir na precisão e eficiência do processo de previsão. O modelo é instruído a fornecer exclusivamente um vetor contendo os valores previstos, começando imediatamente após o último dado fornecido.

Esse design específico do *prompt* visa explorar a capacidade dos LLMs de capturar padrões complexos, como tendências e sazonalidades, de maneira holística, sem a necessidade de segmentar a série temporal em múltiplas janelas. Esse enfoque é especialmente útil para modelos de linguagem, que possuem um forte potencial de generalização e podem identificar padrões globais em um único passe pelos dados, sem depender das técnicas tradicionais de modelagem de séries temporais.

## 4.6 Ambiente de execução dos experimentos

Para realizar as inferências com o *Gemini-1.5-PRO*, será utilizada a API do *Google* 1 , sempre configurando a temperatura para 1. O treinamento e as previsões com os modelos *LSTM* e *Random Forest* foram realizados utilizando *Python 3.11*, com as bibliotecas *Pandas 2.0.3* e *Numpy 1.25.0* para manipulação de dados, além de *TensorFlow 2.11.1* e *Scikit-Learn 1.3.0* para a criação dos modelos.

Adicionalmente, será empregado o *Streamlit 1.42.0* para o desenvolvimento de uma interface web interativa, permitindo a visualização dos resultados por meio de gráficos gerados com *Plotly 6.0.0*. A aplicação também exibirá as métricas *SMAPE* e *SEM* e armazenará o histórico de testes em um banco de dados, utilizando *SQLite 3.49.1*.

#### 4.7 Avaliação

A avaliação dos resultados será realizada utilizando o Erro Percentual Médio Simétrico (*SMAPE*) Makridakis (1993), uma métrica escolhida por ser percentual, o que é particularmente relevante dado que o *dataset* de varejo contém unidades diferentes (e.g., produtos vendidos por unidade e por peso). Além disso, o *SMAPE* é uma medida geométrica média, tornando-o ideal para comparar o desempenho de múltiplos modelos em um grande número de previsões, conforme destacado em Kreinovich *et al.* (2014). O *SMAPE* será calculado conforme a Equação 4.1:


$$SMAPE = \frac{1}{h} \sum_{i=1}^{h} \frac{|y_i - \hat{y}_i|}{\frac{|y_i| + |\hat{y}_i|}{2}} \times 100$$
(4.1)

<sup>1</sup> <https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini?hl=pt-br>

onde *y*ˆ*<sup>i</sup>* representa o valor previsto, *y<sup>i</sup>* é o valor real observado, e *h* é o número total de unidades de tempo previstas no horizonte de previsão.

Para cada uma das 40 séries temporais estudadas, foram realizadas dez previsões por modelo avaliado, com *h* = 60 para as séries do varejo e *h* = 168 para a mobilidade. Para cada previsão, foi calculado o respectivo *SMAPE* e, posteriormente, foi obtida a média do *SMAPE* para cada série. Além disso, foi calculado o Erro Padrão da Média (SEM) Altman e Bland (2005), conforme mostrado na Equação 4.2:


$$SEM = \frac{\sigma}{\sqrt{n}} \tag{4.2}$$

, onde *n* é o total de previsões realizadas, no contexto deste estudo, sempre *n* = 10.

## 4.8 Cronograma

Para o desenvolvimento deste estudo, foram definidas várias etapas essenciais. O cronograma das atividades está apresentado na Tabela (.*?) As principais tarefas a serem realizadas incluem:

- A) Análise das bases de dados;
- B) Pré-processamento dos dados;
- C) Estudos sobre Engenharia de Prompt;
- D) Elaboração do Prompt;
- E) Implementação de código;
- F) Desenvolvimento de uma interface web;
- G) Escrita do TCC.

Tabela 1 – Cronograma de Atividades

| Atividade | 2024 |     |     |     |     |     | 2025 |     |
|-----------|------|-----|-----|-----|-----|-----|------|-----|
|           | Jul  | Ago | Set | Out | Nov | Dez | Jan  | Fev |
| A         | X    | X   | -   | -   | -   | -   | -    | -   |
| B         | -    | X   | X   | -   | -   | -   | -    | -   |
| C         | -    | X   | X   | X   | -   | -   | -    | -   |
| D         | -    | -   | X   | X   | -   | -   | -    | -   |
| E         | -    | -   | -   | X   | X   | X   | -    | -   |
| F         | -    | -   | -   | -   | X   | X   | X    | -   |
| G         | -    | -   | -   | -   | -   | X   | X    | X   |

Fonte: o autor.

# 5 RESULTADOS

Os resultados das previsões para as 40 séries temporais dos domínios de Varejo e Mobilidade, utilizando os modelos *Gemini 1.5 PRO*, *LSTM* e *Random Forest*, são apresentados na Tabela 1 Os valores de *SMAPE* (Erro Percentual Absoluto Médio Simétrico) com seus respectivos erros padrão (SEM) permitem avaliar a precisão das previsões para cada série temporal individualmente.

No domínio de Varejo, o modelo *Random Forest* demonstrou superioridade na maioria das séries temporais, com um desempenho médio de *SMAPE* de 36,22%, sendo o melhor ou empatado (considerando o *SEM*) com o melhor modelo em 15 das 20 séries temporais analisadas. O modelo *LSTM*, por sua vez, apresentou um *SMAPE* médio de 45,85%, enquanto o *Gemini 1.5 PRO* obteve um valor de 41,80%.

Analisando individualmente as séries temporais, o modelo *Gemini 1.5 PRO* superou ou empatou com os outros modelos em sete séries temporais (ids 3, 14, 15, 16, 18, 19, 20). O *LSTM*, embora tenha tido um desempenho inferior na maioria das séries temporais, destacou-se em três séries (ids 3, 13, 19), onde empatou com o *Gemini 1.5 PRO* e, em duas séries específicas (ids 3 e 19), superou ligeiramente o *Random Forest*.

No domínio de Mobilidade, o desempenho dos modelos foi mais equilibrado. O *Gemini 1.5 PRO* obteve um *SMAPE* médio de 20,60%, o *LSTM* alcançou 27,03%, enquanto o *Random Forest* teve um *SMAPE* médio de 19,67%. Notavelmente, o *Gemini 1.5 PRO* superou ou empatou com os outros modelos em 11 das 20 séries temporais (ids 4, 5, 9, 10, 12, 13, 15, 16, 17, 18, 19).

Os resultados obtidos neste estudo demonstram que o *Large Language Model* (LLM) *Gemini 1.5 PRO* apresentou um desempenho promissor quando comparado aos modelos tradicionais de aprendizado de máquina, como o *Random Forest* e o *LSTM*, na tarefa de previsão de séries temporais. Em diversas séries temporais, especialmente no domínio da Mobilidade, o LLM superou os algoritmos tradicionais, o que é particularmente interessante considerando que o modelo utilizou apenas suas capacidades intrínsecas de linguagem para capturar e inferir padrões de sazonalidade.

Este resultado sugere que, embora os LLMs como o *Gemini 1.5 PRO* não tenham sido originalmente projetados para a previsão de séries temporais, sua habilidade em modelar padrões complexos em dados variados pode ser explorada com sucesso em certas condições. A capacidade de um LLM de generalizar informações e identificar padrões ocultos nos dados, que

Tabela 2 – Valores de SMAPE obtidos nos experimentos.

| Varejo |              |              |              |    |              | Mobilidade   |              |
|--------|--------------|--------------|--------------|----|--------------|--------------|--------------|
| id     | Gemini       | LSTM         | RF           | id | Gemini       | LSTM         | RF           |
| 1      | 55,59 ± 1,28 | 50,70 ± 0,02 | 33,69 ± 0,12 | 1  | 15,96 ± 0,73 | 12,23 ± 0,25 | 30,56 ± 2,84 |
| 2      | 50,53 ± 0,97 | 46,92 ± 0,07 | 39,48 ± 0,14 | 2  | 17,75 ± 0,14 | 25,39 ± 0,87 | 11,49 ± 0,04 |
| 3      | 46,41 ± 1,70 | 43,51 ± 1,20 | 45,94 ± 0,29 | 3  | 16,27 ± 0,55 | 14,34 ± 0,28 | 21,42 ± 0,59 |
| 4      | 18,80 ± 0,68 | 52,01 ± 0,52 | 13,97 ± 0,07 | 4  | 17,15 ± 2,16 | 36,89 ± 0,72 | 16,10 ± 0,56 |
| 5      | 85,45 ± 1,93 | 85,78 ± 0,06 | 70,13 ± 0,34 | 5  | 12,55 ± 1,47 | 21,65 ± 0,46 | 10,61 ± 0,50 |
| 6      | 43,83 ± 0,70 | 39,04 ± 0,07 | 22,56 ± 0,17 | 6  | 29,28 ± 0,13 | 28,17 ± 1,01 | 17,29 ± 2,40 |
| 7      | 45,64 ± 0,56 | 47,98 ± 0,73 | 35,88 ± 0,15 | 7  | 19,36 ± 0,35 | 20,68 ± 0,86 | 9,39 ± 0,05  |
| 8      | 30,77 ± 1,75 | 33,54 ± 0,79 | 24,84 ± 1,02 | 8  | 50,63 ± 0,70 | 18,78 ± 0,77 | 14,62 ± 0,54 |
| 9      | 37,21 ± 0,54 | 32,91 ± 0,04 | 30,41 ± 0,17 | 9  | 24,82 ± 1,05 | 26,50 ± 0,30 | 25,34 ± 0,52 |
| 10     | 45,12 ± 2,56 | 41,69 ± 0,16 | 32,52 ± 0,19 | 10 | 14,66 ± 0,55 | 31,03 ± 1,04 | 14,94 ± 0,06 |
| 11     | 36,83 ± 0,50 | 31,59 ± 0,02 | 30,56 ± 0,19 | 11 | 23,52 ± 0,86 | 32,24 ± 0,73 | 15,81 ± 0,07 |
| 12     | 21,89 ± 0,61 | 20,89 ± 0,47 | 18,91 ± 0,24 | 12 | 15,48 ± 0,35 | 24,90 ± 0,42 | 21,06 ± 0,40 |
| 13     | 36,55 ± 0,55 | 34,15 ± 0,06 | 35,01 ± 0,19 | 13 | 13,41 ± 0,82 | 40,97 ± 1,35 | 19,85 ± 1,07 |
| 14     | 22,95 ± 0,51 | 35,14 ± 0,82 | 26,92 ± 0,40 | 14 | 26,03 ± 0,76 | 23,02 ± 0,53 | 26,31 ± 2,24 |
| 15     | 33,22 ± 0,91 | 57,61 ± 2,00 | 33,23 ± 0,25 | 15 | 16,36 ± 0,25 | 30,19 ± 0,72 | 22,04 ± 0,39 |
| 16     | 27,55 ± 0,40 | 49,14 ± 0,46 | 29,79 ± 0,15 | 16 | 15,01 ± 0,55 | 25,45 ± 0,60 | 26,63 ± 0,53 |
| 17     | 31,90 ± 0,63 | 37,18 ± 0,09 | 25,92 ± 0,17 | 17 | 19,76 ± 0,36 | 26,61 ± 0,35 | 28,95 ± 2,86 |
| 18     | 61,79 ± 1,02 | 70,64 ± 0,84 | 62,21 ± 0,41 | 18 | 13,90 ± 0,95 | 39,67 ± 1,43 | 15,64 ± 0,70 |
| 19     | 29,08 ± 0,29 | 29,12 ± 0,65 | 37,59 ± 0,62 | 19 | 23,47 ± 0,69 | 25,94 ± 0,38 | 30,32 ± 0,29 |
| 20     | 74,85 ± 0,86 | 77,49 ± 0,44 | 74,91 ± 0,20 | 20 | 26,64 ± 1,13 | 35,92 ± 1,18 | 15,03 ± 0,14 |
| µ      | 41,80        | 45,85        | 36,22        | µ  | 20,60        | 27,03        | 19,67        |

é crucial para a compreensão da linguagem natural, também pode ser útil em cenários específicos de previsão, como evidenciado pelos resultados obtidos com as séries temporais de Mobilidade.

No entanto, os resultados piores observados nas séries temporais do domínio de Varejo indicam que ainda há desafios significativos a serem superados para a aplicação eficaz de LLMs nessa área. As séries temporais do Varejo, com seus padrões mais complexos e diversificados, parecem exigir um nível de especialização que os LLMs ainda não conseguem atingir plenamente. A dificuldade do LLM em lidar com a variabilidade e a complexidade dessas séries temporais aponta para a necessidade de aprimoramentos nos modelos ou, possivelmente, a integração de técnicas complementares que possam lidar melhor com essas características dos dados.

Uma das contribuições deste estudo é o desenvolvimento de um *prompt* específico para previsão de séries temporais, que pode ser reutilizado em diferentes LLMs à medida que novos modelos sejam lançados. Isso permite que pesquisadores e profissionais avaliem a evolução dos LLMs na tarefa de prever séries temporais ao longo do tempo, proporcionando uma ferramenta prática para acompanhar e explorar o potencial crescente desses modelos em cenários variados.

# 6 CONCLUSÕES E TRABALHOS FUTUROS

Este estudo investigou a eficácia de um *Large Language Model* (LLM) na tarefa de previsão de séries temporais, comparando seu desempenho com modelos tradicionais de aprendizado de máquina, como o *Random Forest* e o *LSTM*. Os resultados demonstraram que embora o LLM utilizado, *Gemini 1.5 PRO*, tenha se mostrado com desempenho promissor, especialmente em séries temporais do domínio de Mobilidade, seu desempenho foi inferior ao dos métodos tradicionais no domínio de Varejo, onde as séries temporais apresentavam padrões mais complexos e diversificados.

Uma das principais contribuições deste trabalho é o desenvolvimento de um *prompt* específico para a previsão de séries temporais, que pode ser reutilizado em futuros estudos com diferentes LLMs. Esse *prompt* permite uma avaliação contínua da evolução dos LLMs à medida que novos modelos são lançados, oferecendo uma base sólida para comparações futuras.

Como trabalhos futuros, propomos a avaliação de LLMs de código aberto (*opensource*) na tarefa de previsão de séries temporais. O uso de modelos *opensource* permitirá uma maior flexibilidade na personalização e experimentação, além de possibilitar comparações diretas com modelos proprietários, como o *Gemini 1.5 PRO*. Essa investigação pode revelar o potencial dos LLMs *opensource* em capturar padrões temporais complexos e generalizar para diferentes contextos de previsão.

Além disso, é essencial expandir a avaliação para incluir séries temporais maiores e com padrões mais complexos, o que pode proporcionar uma visão mais abrangente do desempenho dos LLMs. Ao incluir essas séries, será possível comparar os resultados com modelos de estado da arte, especificamente desenhados para lidar com tais desafios, como os *Transformers*. Essa comparação será crucial para determinar se os LLMs podem competir de maneira eficaz com modelos altamente especializados em cenários onde a complexidade e a variabilidade das séries temporais são significativas.