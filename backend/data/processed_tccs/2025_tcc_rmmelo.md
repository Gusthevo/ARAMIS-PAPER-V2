#### SISTEMA DE MONITORAMENTO DE ABELHAS APIS MELLIFERA

## AGRADECIMENTOS

Gostaria de expressar minha profunda gratidão à Universidade Federal do Ceará, que foi o alicerce fundamental dessa jornada.

Agradeço de coração aos meus amigos em especial ao Gabriel Rudan e a Letícia Torres, que não apenas compartilharam momentos de risadas e desafios, mas também me ajudaram a crescer e a superar obstáculos.

Agradeço ao meu orientador Wellignton Franco e coorientador Renato William por todo apoio prestado durante a graduação.

Agradeço também à Fundação Cearense de Apoio ao Desenvolvimento (Funcap), na pessoa do Presidente Tarcísio Haroldo Cavalcante Pequeno pelo financiamento da pesquisa via bolsa de estudos.

Agradeço também Instituto Centro de Ensino Tecnológico (CENTEC), pelo apoio em durante a construção do projeto.

"Vivemos em uma era em que a tecnologia deixou de ser apenas uma ferramenta e se tornou uma extensão de nossas capacidades, moldando a forma como nos comunicamos, trabalhamos e interagimos com o mundo ao nosso redor."

(Satya Nadella)

## RESUMO

A incorporação da *Internet of Things* (IoT) no setor apícola tem sido considerada uma estratégia promissora para lidar com os desafios contemporâneos da produção de mel. Nesse contexto, este trabalho apresenta uma proposta de sistema de monitoramento para colmeias de abelhas Apis mellifera, com foco em apiários situados no sertão cearense, região que desempenha um papel relevante na apicultura brasileira. A apicultura no sertão cearense desempenha um papel crucial na economia local, sendo uma das atividades de destaque em uma região onde as condições climáticas adversas e a escassez de recursos tornam a produção agrícola mais desafiadora. A produção de mel, além de ser uma importante fonte de renda para muitos agricultores familiares, contribui para a preservação ambiental, devido ao papel das abelhas na polinização de diversas culturas. O sistema desenvolvido faz uso de tecnologias IoT para coletar e transmitir dados cruciais das colmeias, como temperatura, umidade, pressão atmosférica, peso e status de abertura. Esses dados são monitorados remotamente e em tempo real por meio da tecnologia de comunicação LoRa, permitindo ao apicultor ter acesso a informações precisas sem a necessidade de visitas frequentes ao apiário. Além disso, o sistema foi projetado para ser autossuficiente em termos de energia, garantindo sua operação contínua em locais remotos, sem depender de fontes externas de alimentação. Os resultados dos testes realizados mostraram-se promissores, com uma redução significativa nas visitas físicas ao apiário e uma gestão mais eficiente por parte do apicultor. Esse avanço facilita o acompanhamento constante da saúde das colmeias e melhora a tomada de decisões em tempo hábil. O projeto foi desenvolvido em colaboração com apicultores da região, o que garantiu uma maior compreensão das necessidades reais da aplicação. Essa abordagem colaborativa não só garante a relevância do sistema, mas também assegura que ele seja viável e aplicável para os produtores de mel, oferecendo soluções adaptadas às condições e demandas locais.

Palavras-chave: Apicultura de Precisão. Apicultura. Internet das Coisas. Transmissão de Dados.

ABSTRACT

The incorporation of IoT in the beekeeping sector has been considered a promising strategy for

addressing the contemporary challenges of honey production. In this context, this study presents

a proposed monitoring system for Apis mellifera beehives, focusing on apiaries located in the

semi-arid region of Ceará, an area that plays a significant role in Brazilian beekeeping.

Beekeeping in the semi-arid region of Ceará plays a crucial role in the local economy, being

one of the key activities in an area where adverse climatic conditions and resource scarcity

make agricultural production more challenging. Honey production, in addition to serving as

an important source of income for many small-scale farmers, contributes to environmental

conservation due to the role of bees in pollinating various crops.

The developed system utilizes IoT technologies to collect and transmit essential hive data, such

as temperature, humidity, atmospheric pressure, weight, and hive status. These data are remotely

and continuously monitored in real-time using LoRa communication technology, enabling

beekeepers to access precise information without the need for frequent visits to the apiary.

Furthermore, the system was designed to be energy self-sufficient, ensuring continuous operation

in remote locations without reliance on external power sources.

The results of the conducted tests proved to be promising, demonstrating a significant reduction in

the need for physical visits to the apiary and enabling more efficient management by beekeepers.

This advancement facilitates constant monitoring of hive health and improves decision-making

in a timely manner.

The project was developed in collaboration with local beekeepers, ensuring a deeper unders-

tanding of the real needs of the application. This collaborative approach not only enhances

the system's relevance but also ensures its feasibility and applicability for honey producers by

offering solutions tailored to local conditions and demands.

Keywords: Precision Beekeeping. Beekeeping. Internet of Things. Data Transmission.

## LISTA DE TABELAS

| Tabela 1 | – | Diferença entre trabalhos relacionados                                    | 32 |
|----------|---|---------------------------------------------------------------------------|----|
| Tabela 2 | – | Especificações técnicas do BME280                                         | 38 |
| Tabela 3 | – | Especificações Técnicas do HX711 .                                        | 39 |
| Tabela 4 | – | Especificações Técnicas da Célula de Carga de 50kg .                      | 40 |
| Tabela 5 | – | Especificações Técnicas do Sensor Magnético MC-38                         | 41 |
| Tabela 6 | – | Especificações Técnicas do Rádio E32-433T20D                              | 42 |
| Tabela 7 | – | Especificações Técnicas da Placa fotovoltaica Resun RSM020P .             | 43 |
| Tabela 8 | – | Especificações Técnicas do Regulador LM2596                               | 44 |
| Tabela 9 | – | Especificações Técnicas do<br>Battery Management-Monitoring Unit<br>(BMS) |    |
|          |   | HX-2S-A10                                                                 | 45 |

## LISTA DE ABREVIATURAS E SIGLAS

ADC conversor analógico-digital

AP *Agricultura de Precisão*

API *Application Programming Interface*

BLE *Bluetooth Low Energy*

BMS *Battery Management-Monitoring Unit*

DAC Digital-to-Analog Converter

DC *Direct Current*

DT *Data*

EXI *Efficient XML Interchange*

FPGA *field programmable gate array*

GPIO General-Purpose Input/Output

HTTP *Hypertext Transfer Protocol*

I2C Inter-Integrated Circuit

I2S Inter-IC Sound

IoT *Internet of Things*

kg *Quilograma*

LoRa *Long Range*

LoRaWAN *Long Range Wide Area Network*

mA *Miliampere*

MAC *Media Access Control*

NFC *Near Field Communication*

OWL *Web Ontology Language*

PWM Pulse Width Modulation

RDF *Resource Description Framework*

RFID *Radio Frequency Identification*

ROM *Read-Only Memory*

RXD *Received Data*

SAP Sistema de Apicultura de Precisão

SCK *Serial Clock*

SCL *Serial Clock*

SDA *Serial Data*

SPI Serial Peripheral Interface

TXD *Transmit Data*

UART Universal Asynchronous Receiver/Transmitter

USB Universal Serial Bus

V *Volt*

W *Watt*

# SUMÁRIO

| 1       | INTRODUÇÃO .                                                            | 15 |
|---------|-------------------------------------------------------------------------|----|
| 1.1     | Contextualização                                                        | 15 |
| 1.2     | Justificativa                                                           | 16 |
| 1.3     | Escopo do Trabalho                                                      | 16 |
| 1.4     | Objetivos                                                               | 17 |
| 1.4.1   | Objetivo Geral                                                          | 17 |
| 1.4.2   | Objetivos Específicos                                                   | 17 |
| 1.5     | Organização do Trabalho                                                 | 18 |
| 2       | FUNDAMENTAÇÃO TEÓRICA                                                   | 19 |
| 2.1     | Apicultura na Região Nordeste                                           | 19 |
| 2.2     | Apicultura de Precisão                                                  | 21 |
| 2.3     | Sistemas embarcados                                                     | 22 |
| 2.4     | Internet das Coisas                                                     | 23 |
| 2.5     | Sensores                                                                | 25 |
| 3       | TRABALHOS RELACIONADOS                                                  | 26 |
| 3.1     | Design and development of low-power, long-range data acquisition system |    |
|         | for beehives - BeeDAS                                                   | 26 |
| 3.2     | An Integrated Multi-Sensor System for Remote Bee Health Monitoring      | 27 |
| 3.3     | Application of A Precision Apiculture System to Monitor Honey Daily     |    |
|         | Production                                                              | 28 |
| 3.4     | A Smart Sensor-Based Measurement System for Advanced Bee Hive           |    |
|         | Monitoring                                                              | 29 |
| 3.5     | Discussão sobre os trabalhos relacionados                               | 30 |
| 4       | BEEHY                                                                   | 33 |
| 4.1     | Metodologia                                                             | 33 |
| 4.2     | Definição de Parâmetros                                                 | 34 |
| 4.3     | Planejamento                                                            | 35 |
| 4.3.1   | Microcontrolador                                                        | 35 |
| 4.3.2   | Sensores                                                                | 37 |
| 4.3.2.1 | BME280                                                                  | 37 |

| 4.3.2.2 | Sensor de peso                  | 38 |
|---------|---------------------------------|----|
| 4.3.2.3 | Reed Switch                     | 40 |
| 4.3.3   | Transmissor de Rádio Frequência | 41 |
| 4.3.4   | Alimentação                     | 42 |
| 4.3.4.1 | Placa Fotovoltaica              | 43 |
| 4.3.4.2 | Regulador de tensão             | 44 |
| 4.3.4.3 | Carregador                      | 45 |
| 4.4     | Desenvolvimento                 | 46 |
| 4.4.1   | Nó colmeia                      | 46 |
| 4.4.1.1 | BME280                          | 49 |
| 4.4.1.2 | Balança                         | 49 |
| 4.4.1.3 | Reed Switch                     | 52 |
| 4.4.1.4 | Alimentação                     | 53 |
| 4.4.1.5 | E32 433T20D                     | 54 |
| 4.4.1.6 | Fluxograma                      | 56 |
| 4.4.2   | Gateway                         | 58 |
| 4.4.3   | Aplicação Web                   | 61 |
| 4.5     | Experimentação                  | 62 |
| 4.6     | Exibição dos dados              | 63 |
| 5       | RESULTADOS E DISCUSSÃO          | 65 |
| 6       | CONCLUSÕES E TRABALHOS FUTUROS  | 72 |
|         | REFERÊNCIAS                     | 73 |

## 1 INTRODUÇÃO

## 1.1 Contextualização

A atual transição do paradigma tecnológico mundial é um fenômeno revolucionário que está remodelando a sociedade e os negócios de mercado (COTA *et al.*, 2023). Essa transição é marcada pela ampla adoção de tecnologias baseadas em Conectividade e Inteligência Artificial, configurando a chamada 4ª Revolução Industrial, e permeia os vários segmentos socioeconômicos originando termos como Agro 4.0 (GIACOBBO; FROTA, 2021).

Contrastando com esse cenário, a apicultura, embora seja uma atividade agrícola de grande relevância aos sistemas produtivos locais, sofre com entraves que atrasam o seu desenvolvimento por carência de tecnologias para auxílio ao manejo (MONTEIRO *et al.*, 2015). Com vista para esse desafio, várias pesquisas vêm sendo conduzidas com objetivo de promover avanços tecnológicos na apicultura e fortalecer a ideia da Apicultura de Precisão, conceito presente no contexto da Apicultura 4.0. Segundo (COTA *et al.*, 2023), a abordagem relacionada à Apicultura de Precisão é baseada em metodologias para mitigar o estresse ocasionado pela intervenção humana no biosistema das colônias, melhorando a produtividade. Outra característica importante é de reduzir a quantidade de trabalho necessária para o gerenciamento do apiário e simplificaria a recuperação de dados de cada colmeia (MEIKLE; HOLST, 2015).

Para tanto, essas metodologias costumam ser organizadas em três fases: coleta de dados, processamento de dados e fase de apresentação dos dados em que, nesta última, o objetivo é apresentar ao usuário final informações diretas para tomadas de decisão (BUMANIS, 2020). Essas informações são construídas na fase de processamento, em que os dados passam por métodos de análise estatística aplicados sobre os dados coletados (HENRY *et al.*, 2019).

Na etapa de coleta, os dados podem ser capturados por diferentes tipos de sensores para monitoramento, por exemplo, peso, temperatura, umidade, sons, etc (MONTEIRO *et al.*, 2015). Os sensores da coleta de dados podem ser colocados dentro ou fora da colmeia e, como eles, a colmeia pode se tornar "inteligente", ao tempo que evolui para um nó de IoT, proporcionando supervisão remota e em tempo real por meio de aplicativos específicos em diferentes dispositivos (DANIELI *et al.*, 2024).

Dessa forma, é apresentado neste trabalho uma solução tecnológica para apicultura de precisão que tem por objetivo contribuir com a gestão de apiários, buscando tanto a maximização da produtividade, quanto a verificação da saúde e o bem-estar das colônias. Como principal contribuição, propomos uma arquitetura baseada em IoT de baixo custo, adequada às condições de escassez do semiárido do nordeste brasileiro.

## 1.2 Justificativa

A apicultura enfrenta diversos desafios que impactam diretamente a produção e a sustentabilidade da atividade. Dentre os principais problemas apresentados pelos apicultores, destacam-se:

A gestão da produção e do manejo, que ainda carece da utilização de meios digitais para registro e análise dos dados. As vantagens das tecnologias digitais estão em sua capacidade de armazenar e processar grande volume de informações, além de automatizar processos (PEREIRA; CASTRO, 2022). Atualmente, não há uma sistematização eficiente para inserir informações sobre a produção e o manejo das colmeias, sendo este último aspecto ainda mais crítico. A ausência de informações estruturadas sobre os tipos de manutenção a serem realizados em cada colmeia e os períodos ideais para tais intervenções dificulta a otimização das práticas apícolas (BENDINI *et al.*, 2014).

Outro problema significativo também está relacionado ao manejo. Durante as inspeções físicas das colmeias, há um aumento do nível de estresse das abelhas, o que pode levar à interrupção temporária da produção. Além disso, essas inspeções demandam deslocamento, tempo, custos operacionais e uma preparação adequada. A necessidade de inspeções frequentes limita a capacidade de resposta rápida a mudanças nas condições internas da colmeia, comprometendo a eficiência e a sustentabilidade da produção apícola (SANTOS *et al.*, 2022).

Adicionalmente, a atividade apícola enfrenta problemas relacionados à segurança das colmeias, tais como o roubo e a destruição das caixas, o que gera prejuízos econômicos e impacta diretamente a produção de mel (CERQUEIRA; FIGUEIREDO, ; FONTENELE, 2022). Diante desses desafios, a implementação de tecnologias para monitoramento remoto e gestão eficiente das colmeias pode contribuir significativamente para a redução dos impactos negativos, promovendo uma apicultura mais sustentável e produtiva.

#### 1.3 Escopo do Trabalho

Este trabalho abrange o desenvolvimento de um sistema de monitoramento para colmeias, baseado na implementação de sensores capazes de coletar dados em tempo real sobre variáveis ambientais e comportamentais das abelhas. O sistema incluirá um módulo de transmissão de dados para permitir a visualização remota das informações coletadas, visando reduzir a necessidade de inspeções físicas frequentes e melhorar a eficiência da gestão apícola.

O escopo do trabalho envolve as seguintes etapas:

- Levantamento de requisitos para a construção do sistema de monitoramento;
- Seleção e calibração dos sensores apropriados para medição de temperatura, umidade e atividade das colmeias;
- Desenvolvimento de um módulo de comunicação para transmissão de dados via rede sem fio;
- Utilização de uma plataforma para visualização e análise remota dos dados coletados;
- Testes e validação do sistema em um ambiente controlado para avaliar sua eficácia;
- Análise dos impactos do sistema na redução dos custos operacionais e na produtividade apícola.

Este projeto se limita ao desenvolvimento de um protótipo funcional para validação da viabilidade da tecnologia proposta, não abrangendo a produção em larga escala ou aspectos econômicos detalhados da sua comercialização.

#### 1.4 Objetivos

#### *1.4.1 Objetivo Geral*

Desenvolver um sistema de monitoramento baseado em sensores para acompanhar o estado das colônias em tempo real, proporcionando maior eficiência na gestão das colmeias e reduzindo custos operacionais.

#### *1.4.2 Objetivos Específicos*

- Analisar na literatura quais são os dados mais relevantes a serem monitorados/capturados nas colmeias, relacionados ao bem-estar, saúde e produção das colmeias;
- Desenvolver um hardware baseado em tecnologias IoT para monitoramento das colmeias;
- Pesquisar uma tecnologia de meio de transmissão sem fio adequada à aplicação, considerando longas distâncias;
- Implementar sensores para coletar dados sobre temperatura, umidade e atividade das colmeias em tempo real;

• Testar em campo o protótipo e apresentar os resultados obtidos.

## 1.5 Organização do Trabalho

Este trabalho está estruturado em diferentes seções, cada uma abordando aspectos fundamentais para o desenvolvimento da pesquisa.

A introdução apresenta a contextualização do problema, os objetivos e a relevância do estudo.

A revisão da literatura discute os principais conceitos e tecnologias relacionadas ao monitoramento de colmeias.

A metodologia detalha as etapas de desenvolvimento do sistema, desde a escolha dos sensores até a implementação do hardware e software.

Os resultados e discussões apresentam a análise dos dados coletados e a avaliação do sistema proposto.

Por fim, as considerações finais trazem uma síntese dos achados, bem como sugestões para trabalhos futuros.

## 2 FUNDAMENTAÇÃO TEÓRICA

Neste capítulo será apresentado a fundamentação teórica para um melhor entendimento do BeeHy. A mesma está dividia da seguinte forma: Na seção 2.1 apresenta a atual situação da apicultura na região nordeste do Brasil; Na seção 2.2 aborda a utilização da tecnologia para a melhoria na produção apícola; Na seção 2.3 é abordado o conceito de sistemas embarcado; Na seção 2.4 é tratado a concepção de internet das coisas; Por fim, na seção 2.5 é discorrido sobre sensores.

## 2.1 Apicultura na Região Nordeste

A apicultura é uma atividade milenar que desempenha um papel significativo na economia e no meio ambiente, especialmente na região nordeste do Brasil. A prática da apicultura no Brasil remonta aos tempos em que apenas os povos indígenas habitavam o território nacional, os quais já criavam abelhas nativas, como as melíponas e trígonas (Guimarães, 1989). No entanto, a apicultura racional é uma prática relativamente nova no Brasil. Estudiosos sugerem que ela teve início por volta de 1839 com a chegada da Apis mellifera mellifera, embora a criação de outras subespécies europeias tenha ocorrido posteriormente (KHAN *et al.*, 2014). Mas em 1956, houve um cruzamento acidental entre abelhas africanas e europeias, originando um híbrido mais adequado ao clima tropical, mais produtivo e resistente a pragas e doenças, embora mais agressivo, Esse fato provocou a gradual africanização das abelhas Apis mellifera de toda América do Sul e Central (PAULA, 2008).

Com novas espécies de abelhas, também teve que ser alterado o tipo de manejo, pois este era feito praticamente de forma extrativa e manejo rudimentar, eram criadas em caixões de madeira no fundo dos quintais, próximas a animais domésticos (PEREIRA *et al.*, 2003). A partir de 1970, foram adotadas novas técnicas de manejo para criação racional das abelhas africanizadas, e desde então a produção de mel no Brasil, especialmente no Nordeste, tem registrado um notável crescimento devido à crescente profissionalização da atividade apícola (VIDAL, 2020). Diante do aperfeiçoamento do manejo, o aumento da produtividade com uma nova espécie de abelha e o surgimento de uma demanda internacional, o mel em especial o do nordeste teve um crescimento acelerado, cujo a taxa de crescimento tem sido superior à do Brasil (XIMENES; VIDAL, 2023). O mel nordestino se destaca pela baixa contaminação por pesticidas e resíduos de antibióticos, uma vez que uma parcela significativa é produzida a partir

da vegetação nativa da região. Além disso, a baixa umidade do ar contribui para a prevenção de doenças nas abelhas, reduzindo a necessidade de medicamentos (VIDAL, 2022).

Nessa região semiárida, a apicultura se destaca como uma importante fonte de subsistência para muitas famílias, oferecendo uma alternativa de renda em meio às condições climáticas adversas. Os apicultores brasileiros são predominantemente de pequeno porte, sendo a apicultura uma atividade de elevada importância social. Dados do censo agropecuário apontam que a maioria dos empreendimentos que trabalham com produtos apícolas estão concentrados no nordeste brasileiro, mais especificamente nos estados do Piauí, Bahia e Ceará, onde são poucas as opções de atividades produtivas rentáveis no meio rural devido às limitações socioeconômica e edafoclimática da Região, em especial escassez de água (AGROPECUÁRIO, 2006). De acordo com Santos e Ribeiro (2009), "a apicultura contribui para o desenvolvimento regional e a preservação do meio ambiente, sendo uma atividade essencialmente ecológica, comprovadamente lucrativa e sustentável". Além disso, a apicultura também pode aumentar a produtividade do setor primário, estimulando o crescimento e a diversificação da produção agrícola e reduzindo subempregos (LOURENÇO; CABRAL, 2016).

Os produtos apícolas obtidos a partir da atividade das abelhas, especialmente o mel, desempenham um papel crucial na dieta humana e são valorizados por suas propriedades nutricionais e medicinais. Além do mel, a apicultura na região nordeste também é responsável pela produção de outros produtos apícolas, como o própolis, geleia real, veneno (apitoxina), criação de rainhas, produção de enxames e polinização dirigida, o pólen e a cera de abelha, que têm diversas aplicações na indústria alimentícia, farmacêutica e cosmética (BOTH *et al.*, 2008). A comercialização desses produtos, tanto no mercado nacional quanto internacional, representa uma importante fonte de renda para os apicultores da região, contribuindo para o desenvolvimento econômico e social das comunidades locais. Entre 2019 e 2020, o Nordeste destacou-se como a região brasileira que mais impulsionou as exportações de mel, registrando um crescimento de 117,7% em valor e 132% em volume, resultando em um aumento de 8,7 mil toneladas. Em 2021, o faturamento com as exportações do produto continuou a crescer, alcançando quase 72,0% a mais que no ano anterior (VIDAL, 2020).

Em resumo, a apicultura na região nordeste desempenha um papel vital na promoção da sustentabilidade ambiental, na geração de renda e na segurança alimentar das comunidades locais, destacando-se pela produção de mel de alta qualidade e pela adoção de práticas agrícolas sustentáveis.

## 2.2 Apicultura de Precisão

A agricultura de precisão *Agricultura de Precisão* (AP) ou agricultura 4.0 é uma abordagem tecnológica bem desenvolvida para produção mais eficiente e sustentável de produtos agrícolas (SRINIVASAN, 2006). Isso ocorre pela otimização do manejo agrícola por meio da coleta e análise de dados detalhados sobre as variabilidades espaciais e temporais presentes nos sistemas de produção agrícola (SISHODIA *et al.*, 2020). Essa prática engloba o uso de Tecnologias de Informação e Comunicação (TICs) e técnicas científicas para otimizar o uso de recursos e maximizar a produtividade das culturas. Dentre os vários sub-ramos da agricultura de precisão, podemos citar, a pecuária de precisão (GOMES, 2022), viticultura de precisão (SILVA, 2021), fruticultura de precisão (ZHOU *et al.*, 2022), e por último a Apicultura de precisão (ALLERI *et al.*, 2023).

A Apicultura de Precisão é um método de gestão da produção apícola que combina tecnologias de informação e ciência apícola para monitorar colônias de abelhas individuais para reduzir o consumo de recursos e maximizar a produtividade das abelhas (ZACEPINS *et al.*, 2015). Também pode ser definida como uma estratégia de manejo do apiário com o objetivo de criar as abelhas nas condições ideais para o melhor rendimento (RUMMAN *et al.*, 2021). O principal objetivo da Apicultura de Precisão é permitir que os apicultores possam contar com ferramentas automatizadas para diminuir a sua carga de trabalho e, ao mesmo tempo, fortalecer a produção proveniente das colmeias (HADJUR *et al.*, 2022). Por meio do uso de sensores, dispositivos de monitoramento e análise de dados em tempo real, os apicultores podem acompanhar de perto o comportamento e a saúde de cada colônia de abelhas (KRIDI *et al.*, 2014). Isso permite a identificação precoce de problemas, como doenças ou escassez de alimentos, e a implementação de medidas corretivas de maneira rápida e eficiente (SIMÃO; FERREIRA, 2023). A ideia da apicultura de precisão é introduzir ferramentas que possam ser facilmente implementadas, utilizadas e mantidas pelos apicultores.

Diferentes parâmetros, como temperatura, umidade, gás, peso, som, vibração e diferentes sistemas de medição ou monitoramento podem ser desenvolvidos e apresentados aos apicultores para monitoramento on-line e em tempo real da colônia de abelhas (ZACEPINS *et al.*, 2015). O peso da colmeia é um bom indicador da evolução da floração e do fluxo de mel. Facilita a seleção ideal de flora e o momento da colheita. Por outro lado, a saúde e o crescimento de uma colônia podem ser monitorados por valores de temperatura e umidade interna e externa (COUSIN *et al.*, 2019). De acordo com Kviesis *et al.* (2015), o sistema de monitoramento das colmeias proposto por ele é composto por nós de medição, que incluem microcontroladores de baixa potência, transmissores sem fio, sensores integrados e fontes de energia. Além disso, o sistema conta com unidades principais responsáveis pela transferência de dados, as quais possuem microcontroladores de baixo consumo, transceptores sem fio, conectores para periféricos e fontes de alimentação. Os dados coletados são armazenados em servidores de banco de dados remotos para análises posteriores. Nesse modelo, os nós de medição são instalados externamente à colmeia, enquanto os sensores são posicionados em seu interior.

De acordo com ZACEPINS *et al.* (2012), a apicultura de precisão pode ser dividida em três classes. Onde inicialmente os dados são coletados por meio de equipamentos e redes de sensores. Em seguida, ocorre a análise desses dados, comparando-os com parâmetros e algoritmos automatizados para avaliar as condições da colmeia, o comportamento da colônia, o desenvolvimento de doenças e as atividades das abelhas. Na terceira etapa, são implementadas medidas de gerenciamento com base nos dados adquiridos para alcançar os resultados desejados. Assim, pode-se afirmar que o Sistema de Apicultura de Precisão (SAP) envolve principalmente três elementos essenciais: informação, tecnologia e gestão (ZACEPINS; STALIDZANS, 2013).

Além disso, a apicultura de precisão também oferece benefícios ambientais, ajudando a reduzir o uso desnecessário de insumos e minimizando os impactos negativos da atividade apícola no ecossistema (PEJIC´ *et al.*, 2022). Ao promover uma gestão mais eficiente dos apiários, essa abordagem contribui para a sustentabilidade da apicultura e para a preservação das populações de abelhas, tão importantes para a polinização e a produção de alimentos (TRINDADE, 2024).

### 2.3 Sistemas embarcados

Um sistema embarcado é um sistema computacional integrado a um sistema maior, sendo responsável por executar funções específicas dentro desse contexto, seja esse sistema um circuito integrado, equipamento ou um sistema computacional mais amplo (ISO/IEC/IEEE. . . , 2010; CUNHA, 2007). Além de serem projetados para tarefas específicas, os sistemas embarcados podem interagir continuamente com o ambiente circundante por meio de sensores e atuadores (BALL, 2002).

Por serem projetados para tarefas específicas, sistemas embarcados, podem ter um design eficiente. Como priorizam a otimização de custos e operações em processamento contínuo, esses sistemas frequentemente utilizam sistemas operacionais em tempo real. A eficiência energética é crucial, pois muitos são alimentados por baterias e operam em condições ambientais extremas. Com recursos limitados e software armazenado em memória *Read-Only Memory* (ROM), o desenvolvimento desses sistemas exige ferramentas e métodos especializados, além de circuitos para depuração e otimização do código (BERGER, 2001).

Segundo Chase e Almeida (2007), a denominação "embarcado"decorre do fato de que esses sistemas são projetados, em geral, para serem independentes de uma fonte de energia fixa, como uma tomada ou gerador. As principais características que classificam esses sistemas são a sua capacidade computacional e a independência de operação. Outros aspectos relevantes variam de acordo com os tipos de sistemas, modos de funcionamento e requisitos específicos das aplicações embarcadas.

Cada sistema embarcado é composto por uma unidade de processamento, que é um circuito integrado fixado a uma placa de circuito impresso. Essa unidade tem a capacidade de processar informações com base em um software que está sendo executado internamente. Portanto, o software está "embarcado"na unidade de processamento. Todo software embarcado é classificado como *firmware* (BALL, 2002).

No contexto de aquisição de dados, esses sistemas utilizam sensores para capturar variáveis ambientais que podem ser analisadas e armazenadas em memoria ou externamente para consultas futuras. Além de monitorar o ambiente, por meio de sensores, o sistema tem a capacidade de controlar as variáveis ambientais através de atuadores, com base em critérios estabelecidos no projeto (PONT; ANTUNES, 2020).

## 2.4 Internet das Coisas

O termo IoT foi cunhado pela primeira vez por Kevin Ashton em 1999, durante uma apresentação para a Procter & Gamble. Ashton, um dos fundadores do Laboratório de Identificação Automática do MIT, utilizou o conceito para descrever a ideia de conectar objetos físicos à internet por meio de sensores e redes de comunicação, permitindo a troca de dados em tempo real (MOUHA *et al.*, 2021).

Embora o termo não possua uma definição única, o conceito central do IoT é que objetos do dia a dia podem ser equipados com capacidades de identificação, detecção, rede e processamento. Isso permite que eles se comuniquem entre si e com outros dispositivos e serviços pela Internet para alcançar algum objetivo útil (WHITMORE *et al.*, 2015).

De acordo com Santos *et al.* (2016), os blocas básicos para a construção da IoT são:

- Identificação: Essencial para conectar objetos à Internet, usando tecnologias como *Radio Frequency Identification* (RFID), *Near Field Communication* (NFC) e endereçamento IP.
- Sensores/Atuadores: Sensores coletam dados do ambiente e os enviam para armazenamento, enquanto atuadores ajustam o ambiente com base nesses dados.
- Comunicação: Técnicas usadas para conectar objetos inteligentes, impactando o consumo de energia, com tecnologias como WiFi, Bluetooth, IEEE 802.15.4 e RFID.
- Computação: Inclui microcontroladores, processadores e *field programmable gate array* (FPGA) que executam algoritmos nos objetos inteligentes.
- Serviços: A IoT pode oferecer diversas classes de serviços, dentre os quais se destacam:
  - Serviços de Identificação: Responsáveis por mapear Entidades Físicas (EF) de interesse do usuário em Entidades Virtuais (EV), como a temperatura de um local físico, coordenadas geográficas do sensor e instante da coleta.
  - Serviços de Agregação de Dados: Coletam e sumarizam dados homogêneos ou heterogêneos obtidos dos objetos inteligentes.
  - Serviços de Colaboração e Inteligência: Agem sobre os serviços de agregação de dados para tomar decisões e reagir adequadamente a determinados cenários.
  - Serviços de Ubiquidade: Visam prover serviços de colaboração e inteligência em qualquer momento e lugar onde forem necessários.
- Semântica: Envolve a extração de conhecimento dos dados da IoT, utilizando técnicas como *Resource Description Framework* (RDF), *Web Ontology Language* (OWL) e *Efficient XML Interchange* (EXI) para fornecer serviços específicos.

Com a evolução da IoT, a consciência de contexto por meio de sensores estabelece uma ponte entre a interconexão do mundo físico e entidades de computação virtual. Esse processo envolve a detecção do ambiente, comunicação com a rede e metodologias de análise de dados, permitindo que objetos físicos "vejam", "ouçam", "pensem"e realizem tarefas ao se comunicarem entre si, compartilharem informações e coordenarem decisões. A IoT transforma esses objetos de tradicionais em inteligentes ao explorar tecnologias subjacentes como computação ubíqua e pervasiva, dispositivos embarcados, tecnologias de comunicação, redes de sensores, protocolos de Internet e aplicativos (AL-FUQAHA *et al.*, 2015).

Em essência, o IoT busca criar um mundo onde objetos inteligentes entendam seus ambientes, interajam com as pessoas e tomem decisões, impulsionando melhorias em processos de negócios e na vida das pessoas (MOUHA *et al.*, 2021).

## 2.5 Sensores

Em termos amplos, sensores são definidos como dispositivos sensíveis a alguma forma de energia do ambiente, que podem ser luz, calor, movimento ou outras grandezas físicas mensuráveis, como temperatura, pressão, radiação, velocidade, corrente, aceleração, posição e etc, (WENDLING, 2010). De maneira geral, podem ser descritos como dispositivos que convertem uma grandeza física, ou seja, uma entrada, em um sinal de saída (JOHN, 1998). Por operarem em função de grandezas físicas, Chaves (2012) pontua a necessidade de ter conhecimentos prévios em diversas disciplinas, como física, eletrônica, química e biologia, para entender melhor o funcionamento de alguns sensores.

Devido à vasta gama de sensores, sua segmentação pode ser feita com base em diversas características. No entanto, aqui discutiremos as definições de sensores analógicos e digitais segundo Chaves (2012).

- Sensores analógicos: Cujos sinais de saída podem variar continuamente ao longo do tempo, sendo esses valores medidos por elementos sensíveis como circuitos eletrônicos analógicos.
- Sensores digitais: Podem assumir somente dois valores distintos em seu sinal de saída ao longo do tempo, interpretados como zero ou um. Embora não existam naturalmente grandezas físicas que apresentem esses valores, os sinais são convertidos para esse formato pelo circuito eletrônico antes de serem apresentados ao sistema de controle.

Em um horizonte próximo, a IoT se beneficiará da consciência de contexto para integrar o mundo físico com as entidades virtuais de computação. Esse processo inclui, entre outras coisas, a detecção do ambiente (LIU *et al.*, 2020). Essa detecção envolve o uso de sensores para monitorar e medir diferentes condições e variáveis do mundo físico.

#### 3 TRABALHOS RELACIONADOS

Este capítulo tem como objetivo apresentar os trabalhos relacionados ao monitoramento de colmeias no cenário atual da pesquisa, além de realizar uma comparação entre essas abordagens e o estudo desenvolvido neste trabalho.

# 3.1 Design and development of low-power, long-range data acquisition system for beehives - BeeDAS

Neste trabalho, Anwar *et al.* (2022) apresenta o BeeDAS, um sistema de aquisição de dados de baixo consumo de energia e longo alcance para monitoramento remoto de colmeias. O sistema integra múltiplos sensores para coletar dados sobre temperatura, umidade, pressão atmosférica, CO2, acústica, vibrações e peso da colmeia, com foco em estimar o peso diário das colmeias por meio de regressão linear, abordando os desafios de design associados a tais sistemas.

Para a coleta de dados, o BeeDAS utiliza diversos sensores: o sensor BME280, responsável por medir temperatura, umidade e pressão atmosférica; o microfone analógico ADMP401 para a coleta de dados acústicos; o CCS811 para medir os níveis de CO2; o acelerômetro MMA8452Q para capturar as vibrações da colmeia; e, por fim, uma balança composta por 4 células de carga conectadas a um ADC HX711, construída externamente para fornecer parâmetros para o treinamento da regressão linear.

A transmissão de dados é realizada por meio de duas tecnologias: NB-IoT e Lo-RaWAN. O método principal utilizado no equipamento é o NB-IoT, pois este padrão oferece um alcance estendido de até 35 km e utiliza a cobertura da rede Telstra para comunicação, em comparação com o LoRaWAN, que geralmente tem um alcance de no máximo 10 km. O NB-IoT tenta primeiro se conectar à rede Telstra e, em seguida, se comunica com o host por meio do MQTT. Após estabelecer a conexão, o BeeDAS publica os dados e aguarda a confirmação do host. A conexão é considerada completa apenas quando o dispositivo recebe a confirmação do host.

Embora a utilização do LoRaWAN não seja detalhada no projeto, é sugerida uma abordagem de comunicação híbrida, em que vários dispositivos utilizam LoRaWAN e apenas um deles possui o NB-IoT, devido ao maior alcance deste protocolo. Essa metodologia híbrida é proposta como uma solução para economia de energia nos dispositivos que utilizam LoRa como método de comunicação.

O dispositivo possui um cartão SD de 32 GB, utilizado para armazenar os dados brutos lidos pelos sensores. Caso necessário, os dados podem ser transmitidos posteriormente. Além disso, os dados armazenados também são usados para recalibrar alguns sensores. Um problema identificado foi que a umidade interna da colmeia danificava o cartão SD. O trabalho mostra que a vida útil do cartão utilizado era de 8 a 10 meses, tornando-o inutilizável após a remoção do dispositivo.

A alimentação do sistema é fornecida por uma placa solar de 10 W, 5 V, responsável pelo carregamento de uma bateria de 3,7 V e 6000 mAh. Com essa configuração de bateria, o sistema pode operar por vários dias sem necessidade de recarga, tornando-se ideal para o projeto. O dispositivo também possui um sistema de segurança para o nível de carga da bateria: quando a carga atinge 10

O consumo de energia do dispositivo varia conforme os equipamentos utilizados. Em modo de sono (mínimo consumo de energia), o dispositivo consome 7 mA constantemente. Esse consumo elevado é devido ao sensor de gás, que não pode ser desligado sem comprometer a precisão das leituras. Quando o LoRaWAN é utilizado, o dispositivo consome até 150 mA no pico de envio dos dados, com um consumo médio de 120 mA. No caso do NB-IoT, o consumo médio durante o envio é de 140 mA. O consumo do dispositivo durante a coleta de dados é de 25 mA, e durante o processo de armazenamento no cartão SD e coleta de dados, o consumo é de 60 mA por ciclo.

Com o uso de todos os recursos de dados disponíveis no equipamento, a previsão do peso diário da colmeia obteve um erro médio absoluto (MAE) de 0,2 kg, com registros dos sensores e dados meteorológicos coletados ao longo de 1250 dias. A eficácia da estimativa de peso demonstrou a precisão dos sensores utilizados no equipamento. O dispositivo foi capaz de se comunicar utilizando o NB-IoT a uma distância de 21 km da torre de comunicação, com apenas algumas falhas e a necessidade de pequenas adaptações, mostrando a eficiência do meio de comunicação utilizado. Os dados coletados por este dispositivo estão disponíveis no GitHub (UM *et al.*, 2022).

#### 3.2 An Integrated Multi-Sensor System for Remote Bee Health Monitoring

Neste trabalho, Bellino *et al.* (2022) apresenta um sistema multissensor para coleta de dados dentro das colmeias, utilizando um sistema personalizado de longo alcance. O sistema integra diversos sensores para coletar dados de temperatura, umidade, peso e CO2.

Para a coleta de dados, foram utilizados dois sensores principais: o sensor SCD30, responsável por medir temperatura, umidade e CO2, e uma balança construída em duas partes para medir o peso. A primeira parte é composta por uma célula de carga de viga flexível, equipada com quatro extensômetros com capacidade de 100 kg. A segunda parte da balança é formada pelo conversor ADC HX711, utilizado para amplificar o sinal emitido pela célula de carga.

A comunicação do equipamento é realizada por meio de um rádio LoRa, criando uma rede LoRaWAN. O sistema utiliza o TTN como gateway, responsável por receber todos os dados dos nós cadastrados. À medida que os dados chegam ao TTN, ele se comunica com o InfluxDB por meio do protocolo MQTT. O TTN publica os dados em um tópico específico, e o InfluxDB escuta esse tópico, criando e organizando um banco de dados.

Embora o dispositivo possua um cartão SD, o trabalho não esclarece como ele é utilizado, mencionando apenas que serve para fins de registro, sem especificar quais registros são feitos.

A alimentação do dispositivo é fornecida por uma bateria LiPo de 3,7V. O trabalho não menciona como o carregamento das baterias é realizado, nem detalha o consumo do dispositivo. Os sensores são alimentados por um MOSFET de baixa vazão, ligado diretamente à bateria e controlado pelo microcontrolador.

O dispositivo foi capaz de coletar dados no norte da Itália, mas o trabalho não especifica o período de teste completo, mencionando apenas os dados coletados ao longo de quatro dias no mês de maio, o que deixa a desejar em termos de aplicabilidade do dispositivo. Os dados coletados indicam variações que correspondem ao funcionamento normal da colmeia.

#### 3.3 Application of A Precision Apiculture System to Monitor Honey Daily Production

O trabalho Catania e Vallone (2020) apresenta um sistema para monitoramento e controle de colmeias, no qual o dispositivo coleta dados de temperatura e umidade interna e externa da colmeia, além do peso e da velocidade do vento. O objetivo da coleta de dados é avaliar a influência desses parâmetros na produção de mel.

Para a coleta de dados, foram utilizados dois sensores AM2302 para medir a temperatura e umidade internas e externas da colmeia. A velocidade do vento foi medida por um anemômetro de rotor de copo com três braços e um sensor magnético de estado sólido. O peso

foi monitorado por um dispositivo composto por duas partes: a primeira é uma célula de carga PSD-S1, com capacidade de 100 kg, e a segunda parte é composta pelo conversor ADC HX711, que converte os sinais analógicos da célula de carga para o microcontrolador.

O dispositivo utiliza um módulo Bluetooth para a transferência de dados, o que impede o acompanhamento em tempo real. Assim, os dados precisam ser coletados manualmente a cada sete dias por meio de um celular. Como o dispositivo não transmite os dados em tempo real, é necessário armazená-los temporariamente, sendo utilizado um cartão SD de tamanho não especificado para esse fim.

A alimentação do equipamento é fornecida por duas baterias de 100 Ah cada, utilizadas de forma alternada para alimentar os três dispositivos instalados. O trabalho não especifica se o equipamento utiliza uma bateria enquanto a outra carrega ou se elas alternam o consumo sem carga simultânea.

O sistema foi instalado em três colmeias localizadas em Monreale, Itália. A área é cultivada com uma variedade de madressilva francesa, uma espécie importante para o forrageamento no Mediterrâneo, sendo este apiário composto por 50 colmeias.

O monitoramento ocorreu entre 24 de abril e 1 de junho de 2019, com os sensores coletando dados a cada 10 minutos, totalizando 4.492 leituras durante esse período.

O estudo permitiu correlacionar diversos fatores com a produção de mel. Entre as observações, destacam-se a diminuição na produção de mel durante picos de vento e o impacto negativo da queda de temperatura na produção. Além disso, a manutenção da umidade relativa interna da colmeia em 60% resultou em uma melhoria na produção de mel. Dessa forma, é possível perceber que o dispositivo contribui para a tomada de decisões importantes, tanto para a saúde das colmeias quanto para o aumento da produção de mel.

#### 3.4 A Smart Sensor-Based Measurement System for Advanced Bee Hive Monitoring

No trabalho Cecchi *et al.* (2020), é desenvolvido o Bee Board, uma plataforma de aquisição multiparamétrica que coleta dados sobre peso, temperatura, umidade, som gerado pelas abelhas e CO<sup>2</sup> interno da colmeia. O sistema também conta com outro equipamento, o Bee Queen, que centraliza os dados coletados pela Bee Board e realiza a coleta de parâmetros climáticos por meio de sensores empregados na mesma.

Para a coleta de dados, o dispositivo utiliza dois microfones analógicos ADMP401, responsáveis por captar os sons emitidos pelas abelhas, e dois sensores DTH22, que realizam

as leituras de temperatura e umidade internas da colmeia em dois pontos diferentes. A balança utilizada é composta por duas partes: a primeira é formada por quatro células de carga de 50 kg cada, interconectadas para formar uma ponte Wheatstone, pesando até 200 kg. A segunda parte consiste em um conversor ADC HX711, onde as células de carga são conectadas. Por fim, foi utilizado o sensor analógico Telaire TL6615 para medir o CO2. Como esse sensor é analógico, foi empregado um ADC ADS115 para realizar a conversão analógico-digital dos valores do sensor.

Para a transmissão dos dados, foi utilizada uma conexão Ethernet sem fio de 5 GHz para a placa Queen. O trabalho não esclarece como se dá a transmissão entre a placa Bee e a placa Queen, podendo-se interpretar que a comunicação é feita por meio de Ethernet, dado o local de instalação do equipamento. Assim, o dispositivo está conectado à internet e envia os dados para um servidor remoto, embora o protocolo de comunicação não seja mencionado.

O consumo de energia da placa Bee Board é de aproximadamente 4,2 W, enquanto o da placa Queen Board é de 4 W, com o sistema sendo alimentado pela rede elétrica da universidade. O equipamento realiza leituras constantes, com a alimentação dos sensores sendo fornecida diretamente pelo microcontrolador.

Com o uso do equipamento, é possível monitorar a atividade das colmeias, a quantidade de mel e os eventos de enxameação. O dispositivo foi instalado em junho de 2017 e continuou coletando dados até a redação do trabalho. Durante esse período de análise, o equipamento registrou várias alterações nos dados, incluindo duas ocorrências de enxameação. Pontos como ganho de peso e variação de temperatura também foram observados na análise dos dados, demonstrando que esse sistema permite um monitoramento avançado das colmeias, possibilitando a avaliação da saúde das colmeias e o acompanhamento da produção de mel.

## 3.5 Discussão sobre os trabalhos relacionados

Diversos pesquisadores têm medido a força para o estudo de monitoramento remoto de colmeias, conforme apresentado nas seções anteriores. Nesta seção, serão abordadas as lacunas e os aprimoramentos identificados nos trabalhos analisados.

Anwar *et al.* (2022) desenvolveu um sistema de coleta de dados para colmeias, caracterizado pelo baixo consumo de energia e longo alcance. O sistema foi projetado para coletar a maioria dos parâmetros descritos na literatura. No entanto, a solução proposta por Anwar *et al.* (2022) é invasiva, pois requer a modificação de parte do ninho para a instalação

do equipamento. Além disso, o sistema foi implantado em uma área com acesso à rede móvel, eliminando a necessidade de uma arquitetura de transmissão mais complexa.

Bellino *et al.* (2022) implementou um sistema multissensor capaz de coletar diversos parâmetros das colmeias. Entretanto, o estudo não esclarece o intervalo de tempo entre as coletas de dados, tampouco detalha se o dispositivo opera de forma intermitente. Além disso, embora o equipamento utilize baterias, não há informações sobre o método de recarga adotado.

Catania e Vallone (2020) desenvolveu um sistema de monitoramento e controle de colmeias, analisando diversos parâmetros relevantes encontrados na literatura. Contudo, o sistema não emprega um método de transmissão de longo alcance, exigindo que os dados sejam coletados manualmente no apiário a cada sete dias, o que demanda atenção semanal ao equipamento. Além disso, o estudo menciona o uso de duas baterias de forma alternada, mas não esclarece como ocorre essa alternância nem o processo de recarga.

Cecchi *et al.* (2020) apresentou uma plataforma de aquisição de dados multiparamétrica. No entanto, o sistema utiliza monitoramento remoto por meio de conexão Ethernet, o que limita seu alcance a poucos metros, inviabilizando a comunicação em longas distâncias. Por não depender de transmissão de longo alcance e estar conectado à rede elétrica, o dispositivo coleta dados de forma contínua, permitindo medições precisas das variações nos parâmetros da colmeia.

Após revisar estudos sobre monitoramento de colmeias, é possível identificar suas contribuições distintas. A análise comparativa evidencia que este trabalho se destaca por abordagens inovadoras e soluções únicas. A Tabela 1 apresenta a comparação entre os estudos.

## Pontos analisados:

- 1. Coleta de dados com acompanhamento em tempo real. Aumenta o custo do equipamento e complexidade de implantação.
- 2. Autossuficiência energética. Aumenta o custo do equipamento devido o acrescimo de dispositivos como placa solar.
- 3. Coleta de parâmetros de colmeias.
- 4. Utilização em locais remotos. A possibilidade de utilizar em um local remoto e de difícil acesso.
- 5. Utilização de comunicação LoRa.

Tabela 1 – Diferença entre trabalhos relacionados

| Autores                  | Contribuições |   |   |   |   |
|--------------------------|---------------|---|---|---|---|
| -                        | 1             | 2 | 3 | 4 | 5 |
| Anwar et al. (2022)      | X             | X | X | X |   |
| Bellino et al. (2022)    | X             |   | X |   | X |
| Catania e Vallone (2020) |               |   | X |   |   |
| Cecchi et al. (2020)     | X             |   | X |   |   |
| Este trabalho            | X             | X | X | X | X |

Fonte: Elaboração própria, 2025.

## 4 BEEHY

Neste capítulo será apresentado o BeeHy, um sistema de monitoramento de colmeias construído para monitorar variáveis ambientais das colmeias em tempo real.

## 4.1 Metodologia

As etapas de desenvolvimento do sistema de monitoramento de colmeias são apresentadas na Figura 1, onde é exposto o fluxo metodológico seguido pelo projeto, dividido em cinco etapas: Definição dos Parâmetros, Planejamento, Desenvolvimento, Experimentação e Exibição dos Dados. Cada uma dessas fases desempenha um papel fundamental na construção do sistema e está descrita detalhadamente a seguir:

A seguir será apresentado cada uma das etapas do desenvolvimento do projeto BeeHy mostrados na Figura 1:

- 1. Definição dos Parâmetros Inicialmente estabelecido os requisitos e métricas para a coleta de dados;
- 2. Planejamento Seleção de componentes e definição da estratégia de implementação;
- 3. Desenvolvimento Construção e integração do sistema, incluindo hardware, software e protocolos de comunicação;
- 4. Experimentação Validação do sistema em ambiente real, garantindo a eficácia e a confiabilidade da solução proposta;
- 5. Exibição dos dados Por fim a apresentação dos dados, permitindo a visualização das

informações coletadas em tempo real.

#### 4.2 Definição de Parâmetros

Na literatura, diversos dispositivos de monitoramento de colmeias têm sido apresentados, destacando-se diferentes abordagens para a coleta e análise de dados. Em Anwar *et al.* (2022) a temperatura da colmeia é um indicador essencial da saúde da ninhada e da força da colônia de abelhas . Uma vez que a faixa térmica ideal para a reprodução é significativamente mais restrita do que a faixa de sobrevivência das abelhas, já que a temperatura na câmara de ninhada composta por ovos, larvas e pupas, requer um ambiente térmico estável para garantir seu desenvolvimento adequado, mantendo uma temperatura entre 34 °C e 36 °C, pois variações além desse intervalo podem comprometer o crescimento das larvas e a saúde da colônia (ME-DRZYCKI *et al.*, 2010). Dessa modo, monitorar a temperatura interna da colmeia é essencial para garantir a estabilidade térmica. Manter a temperatura dentro da faixa ideal impacta diretamente a eficiência térmica, a estabilidade e a produtividade da colmeia, assegurando condições adequadas para a sobrevivência e o crescimento da colônia.

A bibliografia indica que as abelhas regulam a umidade relativa na área de criação, mantendo-a acima de 50%, um fator essencial para o desenvolvimento saudável da colônia (ABOU-SHAARA *et al.*, 2017). Níveis reduzidos de umidade podem levar à desidratação dos ovos. Para mitigar esse efeito, as abelhas nutrizes cobrem a área de criação, reduzindo a perda de umidade e garantindo condições adequadas para o desenvolvimento da colônia (AL-GHAMDI *et al.*, 2014). A evaporação dentro da colmeia desempenha um papel fundamental na maturação do mel, contribuindo para a redução do teor de água no néctar, que geralmente varia entre 17% e 21% (SOPADE *et al.*, 2003; YANNIOTIS *et al.*, 2006). As abelhas utilizam a ventilação na entrada da colmeia como um mecanismo para regular a umidade e a temperatura, garantindo condições adequadas para a sobrevivência e o desenvolvimento da colônia (SUDARSAN *et al.*, 2012). Conforme Anwar *et al.* (2022), "Colônias saudáveis são boas em regular o microclima dentro da colmeia, então os níveis de umidade também devem ser um indicador da saúde da colmeia". Dessa forma, o monitoramento da umidade relativa dentro da colmeia é um fator importante para garantir condições ambientais adequadas ao desenvolvimento da colônia e à qualidade dos produtos apícolas.

A utilização da pressão atmosférica, em conjunto com as condições climáticas locais, pode contribuir para uma leve melhora no desempenho dos modelos preditivos da atividade de

forrageamento das abelhas (CLARKE; ROBERT, 2018). A variação nos níveis de CO<sup>2</sup> dentro da colmeia é prevista como resultado das flutuações locais na pressão do ar, que influenciam o fluxo de ar no interior da colmeia (SHARIF *et al.*, 2022). No entanto, grandes variações na pressão atmosférica ocorrem principalmente devido a mudanças na altitude, as quais também influenciam significativamente a temperatura Anwar *et al.* (2022). Assim, mesmo que os impactos da pressão atmosférica sobre as abelhas ainda não sejam amplamente estudados, a coleta desses dados será útil para aprimorar previsões relacionadas ao comportamento da colônia.

De acordo com (DANIELI *et al.*, 2023), o peso de uma colmeia varia ao longo das estações, sendo menor em alguns períodos do ano e atingindo seu pico durante o período produtivo, podendo servir como um indicador valioso tanto da produção de mel quanto da atividade geral da colmeia. O peso da colmeia está diretamente relacionado a eventos cruciais que ocorrem em seu interior, como o início da coleta de néctar, o consumo de recursos, a necessidade de suplementação alimentar e o estado de saúde da colônia, entre outros fatores (KVIESIS *et al.*, 2020; DEGENFELLNER; TEMPL, 2024). Dessa maneira, o monitoramento do peso da colmeia é um aspecto relevante para a avaliação de diversos fatores, incluindo a disponibilidade de recursos, a produtividade e o bem-estar da colônia.

#### 4.3 Planejamento

Nesta seção, serão apresentados os equipamentos selecionados para o projeto, juntamente com os motivos que embasaram a escolha de cada um. Serão abordados o microcontrolador, os sensores utilizados e o sistema de alimentação do equipamento, destacando suas características e funcionalidades que atendem às necessidades do monitoramento da colmeia.

#### *4.3.1 Microcontrolador*

O dispositivo foi equipado com o microcontrolador ESP32 (Figura 2) (SYSTEMS, 2024), sendo ele um microcontrolador altamente versátil desenvolvido pela Espressif Systems, que se destaca por suas capacidades de conectividade sem fio, processamento eficiente e baixo consumo de energia. A decisão de utilização deste foi baseada em sua excelente relação custobenefício, aliada à sua capacidade de atender integralmente às necessidades do projeto.

Baseado em um processador Xtensa LX6 de 32 bits, disponível em configurações de núcleo single-core ou dual-core, operando a uma frequência de até 240 MHz. O microcontrolador possui 520 KB de RAM interna, além da integração nativa de Wi-Fi 802.11 b/g/n e Bluetooth 4.2 (*Bluetooth Low Energy* (BLE) e clássico).

O ESP32 oferece um conjunto abrangente de interfaces de comunicação, permitindo a integração com diversos sensores e atuadores. Ele conta com 4 Serial Peripheral Interface (SPI), 2 interfaces Inter-Integrated Circuit (I2C), 2 interfaces Inter-IC Sound (I2S) para comunicação de áudio, 3 Universal Asynchronous Receiver/Transmitter (UART) para transmissão serial. O dispositivo também possui 16 canais Pulse Width Modulation (PWM), 18 entradas conversor analógico-digital (ADC) de 12 bits para leituras analógicas precisas e 2 saídas Digital-to-Analog Converter (DAC) para geração de sinais analógicos. Além disso, disponibiliza até 34 General-Purpose Input/Output (GPIO) configuráveis.

O desenvolvimento do sistema utilizou a plataforma *Arduino IDE 2*1 , que oferece um ambiente integrado para programação de microcontroladores. Junto a isso, utiliza-se um cabo Universal Serial Bus (USB) e uma conexão serial (UART) para estabelecer a comunicação entre o ESP32 e o computador. A Arduino IDE 2 (ARDUINO, 2025) foi a ferramenta escolhida para o desenvolvimento, pois oferece suporte ao C++ e facilita a implementação, depuração e carregamento do código no microcontrolador.

O ESP32 desempenha um papel central no sistema, sendo responsável tanto pela coleta de dados dos sensores quanto pelo controle das operações, garantindo a integridade das informações antes de sua transmissão.

<sup>1</sup> Disponível em: <https://docs.arduino.cc/software/ide/#ide-v1>.(https://docs.arduino.cc/software/ide/##ide-v1) Acesso em: 21 de fevereiro de 2025.

37

## *4.3.2 Sensores*

O equipamento é composto por três sensores que capturam os dados de temperatura, umidade, pressão, peso e status de abertura da colmeia. A seguir serão detalhados individualmente cada sensor utilizado.

#### *4.3.2.1 BME280*

O BME280 (Figura 3) é um sensor de umidade projetado para dispositivos móveis e wearables, com ênfase em baixo consumo de energia e tamanho compacto. Ele combina sensores com alta linearidade e precisão, garantindo baixo consumo de corrente, estabilidade a longo prazo e alta robustez em relação à EMC2 . O sensor oferece resposta rápida e atende aos requisitos de desempenho de aplicações como consciência de contexto, operando com alta precisão em uma ampla faixa de temperatura (SENSORTEC, 2025).

Além da umidade o sensor BME280 (SENSORTEC, 2025) é empregado na coleta de dados de temperatura, umidade e pressão atmosférica, sendo uma ferramenta essencial para o monitoramento ambiental da colmeia.

A Tabela 2 apresenta as especificações do sensor BME280.

<sup>2</sup> EMC (Compatibilidade Eletromagnética), o termo se refere à capacidade de um dispositivo ou sistema de funcionar corretamente em seu ambiente eletromagnético sem causar interferência eletromagnética inaceitável para outros dispositivos e sem ser suscetível a essa interferência.

Tabela 2 – Especificações técnicas do BME280

| Especificações                    |                                     |  |
|-----------------------------------|-------------------------------------|--|
| Especificação                     | Valor                               |  |
| Faixa de temperatura              | -40°C a +85°C                       |  |
| Precisão da temperatura           | ±1.0°C                              |  |
| Faixa de pressão                  | 300 hPa a 1100 hPa                  |  |
| Precisão da pressão               | ±1.0 hPa                            |  |
| Faixa de umidade relativa         | 0 a 100%                            |  |
| Precisão da umidade               | ±3%                                 |  |
| Tensão de operação                | 1.71V a 3.6V                        |  |
| Consumo de corrente (modo normal) | 3.6 µA                              |  |
| Consumo de corrente (modo sleep)  | 0.1 µA                              |  |
| Interface de comunicação          | I2C (até 3.4 MHz), SPI (até 10 MHz) |  |
| Dimensões                         | 2.5 mm x 2.5 mm x 0.93 mm           |  |

Fonte: Adaptado de (SENSORTEC, 2024).

#### *4.3.2.2 Sensor de peso*

O sensor de peso é composto por duas partes:

1. A primeira parte é o HX711 (Figura 4) (SEMICONDUCTOR, 2016), um ADC de 24 bits, responsável por converter os sinais analógicos provenientes das células de carga em valores digitais. Esse componente é essencial para garantir medições precisas de peso, pois amplifica e filtra os sinais fracos gerados pelas células de carga antes de transmiti-los ao microcontrolador.

A Tabela 3 apresenta as especificações do ADC HX711.

Tabela 3 – Especificações Técnicas do HX711

| Especificações             |                        |  |
|----------------------------|------------------------|--|
| Especificação              | Valor                  |  |
| Tensão de operação         | 2.6V a 5.5V            |  |
| Corrente típica            | 1.5 mA (modo normal)   |  |
| Corrente em modo de espera | <1 µA                  |  |
| Resolução do ADC           | 24 bits                |  |
| Taxa de amostragem         | 10 Hz ou 80 Hz         |  |
| Ganho do amplificador      | 32, 64 ou 128 vezes    |  |
| Interface de comunicação   | Serial (Clock + Dados) |  |
| Temperatura de operação    | -40°C a +85°C          |  |

Fonte: Adaptado de (SEMICONDUCTOR, 2016).

2. A segunda parte do sensor de peso é composta por quatro células de carga de 50 *Quilograma* (kg) (Figura 5) (EUROPE, 2025). Para garantir medições precisas, as células de carga devem ser interconectadas na configuração de uma ponte de Wheatstone, que permite a compensação de variações e aprimora a sensibilidade do sistema. Após essa configuração, a saída resultante da ponte é conectada ao HX711.

A Tabela 4 apresenta as especificações da célula de carga de 50kg.

Tabela 4 – Especificações Técnicas da Célula de Carga de 50kg

| Especificações                     |                                        |  |
|------------------------------------|----------------------------------------|--|
| Especificação                      | Valor                                  |  |
| Capacidade máxima                  | 50 kg                                  |  |
| Sensibilidade                      | 1.0 ± 0.15 mV/V                        |  |
| Tensão de excitação recomendada    | 5V a 10V                               |  |
| Tensão de excitação máxima         | 15V                                    |  |
| Resistência do ponte de Wheatstone | 1kΩ (típico)                           |  |
| Erro total                         | ≤ ±0.05% FS                            |  |
| Histerese                          | ≤ ±0.03% FS                            |  |
| Repetibilidade                     | ≤ ±0.03% FS                            |  |
| Faixa de temperatura de operação   | -10°C a +50°C                          |  |
| Material                           | Alumínio                               |  |
| Dimensões                          | Aproximadamente 80mm x 12.7mm x 12.7mm |  |

Fonte: Adaptado de (EUROPE, 2025).

#### *4.3.2.3 Reed Switch*

O reed switch utilizado foi o MC-38 (Figura 6) (SYNACORP, 2024), responsável por monitorar o status da tampa da colmeia, indicando se ela está aberta ou fechada. O sensor é composto por duas partes: a chave magnética, que é fixada na tampa, e o ímã, que é instalado na colmeia ou na melgueira. Quando ambos estão alinhados e próximos, o circuito permanece fechado; ao separar-se, o circuito é interrompido, permitindo a detecção da abertura da tampa.

A Tabela 5 apresenta as especificações do sensor magnético MC-38.

Tabela 5 – Especificações Técnicas do Sensor Magnético MC-38

| Especificações           |                                           |  |
|--------------------------|-------------------------------------------|--|
| Especificação            | Valor                                     |  |
| Tipo                     | Sensor magnético de contato (reed switch) |  |
| Tensão de operação       | 3V a 36V DC                               |  |
| Corrente máxima          | 0.5A                                      |  |
| Distância de acionamento | 15mm a 25mm                               |  |
| Material do invólucro    | Plástico ABS                              |  |
| Modo de operação         | Normalmente aberto (NO)                   |  |
| Temperatura de operação  | -10°C a +50°C                             |  |
| Dimensões                | 27mm x 14mm x 9mm                         |  |
| Comprimento dos fios     | Aproximadamente 35cm                      |  |

Fonte: Adaptado de (SYNACORP, 2024).

## *4.3.3 Transmissor de Rádio Frequência*

O dispositivo foi equipado com o Rádio Ibyte E32 433T20D (Figura 7) (TECHNO-LOGY, 2024), um rádio altamente prático e eficiente, que se destaca pelo seu excelente alcance e facilidade de uso. Esse módulo de rádio permite a comunicação sem fio entre os dispositivos do sistema, proporcionando transmissão de dados de longa distância e garantindo a integridade da comunicação, mesmo em ambientes com possíveis obstáculos ou interferências. Este transmissor trabalha com a tecnologia *Long Range* (LoRa) com o protocolo de transmissão *Long Range Wide Area Network* (LoRaWAN).

LoRa é uma tecnologia de modulação sem fio patenteada, adquirida pela Semtech Corporation em 2012, voltada para comunicações de longa distância com baixo consumo de energia (HORNBUCKLE, 2010). LoRa foi desenvolvido para operar com baixa taxa de transmissão e baixo consumo de energia, oferecendo um alcance estendido em condições de linha de visão ou em áreas rurais, podendo atingir de 10 a 20 km ao ar livre, graças à alta sensibilidade da modulação LoRa CSS, que permite uma conectividade eficiente em longas distâncias (ATTIA *et al.*, 2019).

Segundo Almuhaya *et al.* (2022), LoRaWAN é um protocolo de rede de camada *Media Access Control* (MAC) baseado em nuvem que é projetado e mantido pela LoRa Alliance para definir as camadas superiores de redes de longa distância com uma camada física LoRa. O LoRaWAN possibilita que os nós sensores enviem pequenos pacotes de dados com baixo consumo de energia para um gateway distante, cobrindo vários quilômetros em uma única transmissão, destacando-se por sua resistência à interferência, garantindo uma comunicação confiável (OSORIO *et al.*, 2020).

A escolha do rádio deve-se à sua praticidade de implantação, funcionalidades e compatibilidade com os protocolos LoRa, tornando-o a opção ideal para a transmissão de dados do equipamento.

A Tabela 5 apresenta as especificações do rádio LoRa E32-433T20D.

Tabela 6 – Especificações Técnicas do Rádio E32-433T20D

| Especificações                  |                                                         |  |
|---------------------------------|---------------------------------------------------------|--|
| Especificação                   | Valor                                                   |  |
| Frequência de operação          | 433 MHz                                                 |  |
| Potência de transmissão         | 20 dBm (100 mW)                                         |  |
| Sensibilidade                   | -116 dBm                                                |  |
| Tipo de modulação               | FSK (Frequency Shift Keying)                            |  |
| Tensão de operação              | 3.3V a 5V DC                                            |  |
| Corrente de operação            | 25 mA (modo de recepção) / 120 mA (modo de transmissão) |  |
| Distância máxima de transmissão | Até 1.8 km (em condições ideais)                        |  |
| Interface de comunicação        | UART (TTL)                                              |  |
| Temperatura de operação         | -40°C a +85°C                                           |  |
| Dimensões                       | 27.8 mm x 14.3 mm x 3.8 mm                              |  |

Fonte: Adaptado de (TECHNOLOGY, 2024).

#### *4.3.4 Alimentação*

O dispositivo é alimentado por uma placa fotovoltaica, que fornece energia em conjunto com duas baterias responsáveis pelo armazenamento e fornecimento de energia ao sistema. Além disso, são utilizados componentes para a equalização do carregamento e um regulador de tensão, garantindo a estabilidade da alimentação e o funcionamento adequado do equipamento.

#### *4.3.4.1 Placa Fotovoltaica*

O equipamento foi equipado com uma placa fotovoltaica de 20*Watt* (W) (Figura 8) (ENERGY, 2025), capaz de suprir as necessidades energéticas do sistema de forma autônoma e sustentável. A utilização da energia fotovoltaica permite a operação contínua do dispositivo em ambientes remotos, reduzindo a dependência de fontes externas de energia e aumentando a eficiência do monitoramento da colmeia.

A Tabela 7 apresenta as especificações da placa fotovoltaica.

Tabela 7 – Especificações Técnicas da Placa fotovoltaica Resun RSM020P

| Especificações                   |                                       |  |
|----------------------------------|---------------------------------------|--|
| Especificação                    | Valor                                 |  |
| Potência máxima (Pmax)           | 20W                                   |  |
| Tensão em Pmax (Vmp)             | 18V                                   |  |
| Corrente em Pmax (Imp)           | 1.11A                                 |  |
| Tensão de circuito aberto (Voc)  | 21.6V                                 |  |
| Corrente de curto-circuito (Isc) | 1.2A                                  |  |
| Eficiência do módulo             | Aproximadamente 17%                   |  |
| Tensão máxima do sistema         | 1000V DC                              |  |
| Temperatura de operação          | -40°C a +85°C                         |  |
| Dimensões                        | 485mm x 350mm x 25mm                  |  |
| Peso                             | 1.8kg                                 |  |
| Material do vidro frontal        | Vidro temperado de alta transparência |  |
| Tipo de célula                   | Policristalino                        |  |
| Número de células                | 36                                    |  |

Fonte: Adaptado de (ENERGY, 2025).

#### *4.3.4.2 Regulador de tensão*

Para a adequação de tensão, foi utilizado o regulador de tensão LM2596 (Figura 9) (INSTRUMENTS, 2025), um conversor *Direct Current* (DC)-DC step-down que ajusta a tensão vinda da placa fotovoltaica para o nível necessário para o funcionamento do sistema e para o carregamento das baterias. Esse componente assegura que a energia gerada pela placa fotovoltaica seja convertida de forma eficiente e segura, garantindo a estabilidade e a operação contínua do sistema sem sobrecarregar os circuitos

A Tabela 8 apresenta as especificações do regulador de tensão LM2596.

Tabela 8 – Especificações Técnicas do Regulador LM2596

| Especificações              |                                 |  |
|-----------------------------|---------------------------------|--|
| Especificação               | Valor                           |  |
| Tensão de entrada           | 4.5V a 40V                      |  |
| Tensão de saída ajustável   | 1.23V a 37V                     |  |
| Corrente de saída máxima    | 3A                              |  |
| Eficiência típica           | 73% a 90%                       |  |
| Frequência de operação      | 150 kHz                         |  |
| Precisão da tensão de saída | ±4%                             |  |
| Ripple típico da saída      | 50mV                            |  |
| Proteções                   | Sobrecorrente, superaquecimento |  |
| Temperatura de operação     | -40°C a +125°C                  |  |
| Tipo de encapsulamento      | TO-220, TO-263                  |  |

Fonte: Adaptado de (INSTRUMENTS, 2025).

## *4.3.4.3 Carregador*

Para o carregamento das baterias em série, foi utilizado o BMS HX-2S-A10 (Figura 10) (ALEXNLD.COM, 2025), um controlador de carga e descarga responsável por garantir o funcionamento ideal das baterias conectadas em série. Este componente assegura que a tensão e corrente fornecidas às baterias estejam dentro dos parâmetros ideais, otimizando a eficiência e a segurança do sistema. Com isso, o BMS contribui para a proteção contra sobrecarga, sobredescarga e equilíbrio de carga entre as células, prolongando a vida útil das baterias e mantendo o equipamento operando de forma estável.

A Tabela 9 apresenta as especificações do controlador de carga BMS HX-2S-A10.

Tabela 9 – Especificações Técnicas do BMS HX-2S-A10

| Especificações                 |                          |  |
|--------------------------------|--------------------------|--|
| Especificação                  | Valor                    |  |
| Tipo de bateria suportada      | Íons de lítio (2S)       |  |
| Tensão de operação             | 7.4V a 8.4V              |  |
| Corrente máxima de carga       | 10A                      |  |
| Corrente máxima de descarga    | 10A                      |  |
| Tensão de corte de carga       | 8.4V ±0.05V              |  |
| Tensão de corte de descarga    | 5.4V ±0.1V               |  |
| Proteção contra sobrecarga     | Sim                      |  |
| Proteção contra sobredescarga  | Sim                      |  |
| Proteção contra curto-circuito | Sim                      |  |
| Temperatura de operação        | -40°C a +50°C            |  |
| Dimensões                      | Aprox. 45mm x 15mm x 3mm |  |

Fonte: Adaptado de (ALEXNLD.COM, 2025).

## 4.4 Desenvolvimento

Nesta seção, serão detalhados os métodos empregados no desenvolvimento do projeto, incluindo os componentes de hardware e software utilizados, bem como as estratégias adotadas para a implementação.

Na Figura 11, é apresentado o fluxo de funcionamento do sistema como um todo. O sistema é dividido em três partes: o nó colmeia, responsável pela coleta de dados; o gateway, que realiza a transmissão das informações; e a aplicação web, onde os dados são processados e visualizados. Os dados de temperatura, umidade, pressão, peso, status de abertura da tampa e porcentagem de bateria são inicialmente coletados no nó colmeia. Em seguida, esses dados são transmitidos para o gateway via rádio LoRa. Após o recebimento, o gateway envia uma confirmação de recebimento dos dados para o nó colmeia e, então, os transmite para a aplicação web utilizando o protocolo de comunicação *Hypertext Transfer Protocol* (HTTP). A seguir, cada uma dessas partes serão detalhadas individualmente.

#### *4.4.1 Nó colmeia*

Esta etapa é composta por um sistema responsável pela coleta e transmissão de dados essenciais para o monitoramento da colmeia, incluindo umidade, pressão, peso, status de abertura da tampa e porcentagem de bateria. A obtenção desses dados é realizada por meio de um sensor BME280, um Reed Switch e uma balança equipada com quatro células de carga conectadas a um ADC HX711.

Os sensores são estrategicamente posicionados na colmeia para garantir medições precisas e representativas. A balança encontra-se na base da colmeia, permitindo a aferição exata do peso total. O Reed Switch é fixado na colmeia ou na melgueira, próximo à tampa, enquanto o ímã correspondente é fixado na tampa para garantir proximidade ideal e o correto funcionamento do sensor. Já o BME280 foi posicionado no centro da colmeia para fornecer medições mais representativas das condições internas. Segundo Simpson (1961), as abelhas regulam a temperatura dos quadros centrais da câmara de criação com maior eficiência em comparação com os quadros posicionados nas bordas externas, que sofrem maior influência das variações térmicas do ambiente. Essa organização pode ser visualizada na Figura 12.

Todos os componentes são interligados ao microcontrolador ESP32, que gerencia a aquisição dos dados e os transmite para o sistema por meio do rádio LoRa E32 433T20D, garantindo comunicação eficiente e de longo alcance. As especificações completas dos dispositivos utilizados está detalhadamente descrita na seção 4.3, enquanto o esquema de conexões pode ser visualizado na Figura 13.

A Figura 13 é um esquema de conexões do dispositivo, onde o mesmo é composto por 7 partes distintas:

- 1. A primeira parte do sistema onde é demonstrado a construção do sistema de alimentação e a ligação do mesmo com o microcontrolador;
- 2. Na segunda parte é exposto a ligação das células de carga para o HX711 e a comunicação do ADC ao ESP32;
- 3. Já na terceira parte é apresentado representação da ligação do BME280 com o microcontrolador;
- 4. Neste setor é representado a ligação do botão de tara;
- 5. Nessa parte é demonstra a conexão do Reed Switch;
- 6. A sexta parte é expresso a ligação do rádio E32 com todas as suas necessidades de adequação para a ligação com o ESP32;
- 7. Aqui é evidenciado todas as conexões realizadas ao microcontrolador.

## *4.4.1.1 BME280*

O BME280 se comunica com o microcontrolador ESP32 por meio do protocolo de comunicação I2C. A alimentação do sensor é fornecida com uma tensão de 3,3*Volt* (V) proveniente do próprio ESP32. Os pinos *Serial Clock* (SCL) e *Serial Data* (SDA) da conexão I2C estão conectados, respectivamente, às portas GPIO22 e GPIO21 do microcontrolador. Essa conexão está ilustrada na Figura 14.

#### *4.4.1.2 Balança*

A balança é composta por quatro células de carga interligadas em uma configuração de ponte de *Wheatstone*, o que possibilita uma capacidade de leitura de até 200 kg, com cada célula tendo capacidade para 50 kg. Conforme mostrado na Figura 16 e na Figura 17, as quatro células de carga são fixadas a uma base, com uma bandeja posicionada sobre elas para transferir o peso da colmeia. As conexões restantes da ponte de *Wheatstone* das células de carga são conectadas ao conversor analógico-digital HX711, que por sua vez se comunica com o microcontrolador via protocolo de comunicação serial. A alimentação do conversor é fornecida pela GPIO14 do ESP32, que, com capacidade de 10 *Miliampere* (mA), é suficiente para alimentar o HX711, que consome cerca de 1,5 mA. Os pinos *Data* (DT) e *Serial Clock* (SCK) da conexão serial são interligados respectivamente às portas GPIO33 e GPIO32 do microcontrolador. Essa conexão está ilustrada na Figura 15.

Para realização de tara foi incorporado um botão ao equipamento, onde uma extremidade do botão é ligada ao 3,3V e a outra ao GPIO2 do microcontrolador, assim quando o botão é pressionado o GPIO2 assume o valor de HIGH ativando o led builtin e sinalizando ao ESP32 a interrupção de tara da balança. Essa conexão é ilustrada na seguinte Figura 18.

## *4.4.1.3 Reed Switch*

O Reed Switch se comunica com o ESP32 por meio da porta GPIO4, onde sua leitura é realizada de forma analógica para detectar alterações no estado do sensor. Essa conexão está ilustrada na Figura 19.

#### *4.4.1.4 Alimentação*

A alimentação do equipamento é composta por uma placa fotovoltaica, um regulador de tensão, um controlador de carga 2S e duas baterias de lítio 18650. A placa fotovoltaica de 20 W é responsável por carregar as baterias, porém fornece uma tensão máxima de 21,6V, enquanto as baterias e o sistema operam em uma faixa de 6,2V a 8,4V. Dessa forma, é necessário o uso do regulador de tensão LM2596 para reduzir a tensão de 21,6V para 8,4V, garantindo a alimentação do sistema e o carregamento das baterias.

Para carregar corretamente as baterias conectadas em série, é fundamental o uso de um controlador de carga, que assegura um carregamento uniforme e uma descarga equilibrada. A alimentação do sistema é feita diretamente no pino VIN do ESP32, pois o módulo suporta tensões de entrada entre 5V e 12V. A partir do microcontrolador, o restante dos componentes do sistema é alimentado com a tensão de 3,3V.

A fim de monitorar os níveis de bateria do sistema, foi desenvolvido um divisor de tensão que permite a medição da voltagem utilizando o PWM do GPIO13 do ESP32. Esse divisor de tensão reduz a tensão da bateria para um nível adequado à entrada analógica do microcontrolador, garantindo leituras seguras e precisas. Com essa abordagem, é possível acompanhar o estado de carga da bateria em tempo real, permitindo a implementação de estratégias para otimizar o consumo energético e garantir o funcionamento contínuo do sistema. Essa conexão está ilustrada na Figura 20.

### *4.4.1.5 E32 433T20D*

Na transmissão de dados, foi utilizado o rádio LoRa E32 433T20D, que se comunica com o microcontrolador ESP32 por meio dos pinos GPIO19, GPIO18, GPIO16 (RX), GPIO17 (TX) e GPIO5, conectados, respectivamente, aos pinos M0, M1, *Received Data* (RXD), *Transmit Data* (TXD) e AUX do módulo LoRa. Os pinos RXD e TXD são responsáveis pela comunicação serial, permitindo a troca de informações entre o ESP32 e o rádio. Já os pinos M0 e M1 controlam o modo de operação do rádio, possibilitando alternar entre estados como transmissão normal, recepção ou modo de baixo consumo. O pino AUX, por sua vez, indica o status do funcionamento do módulo e pode ser utilizado para sinalizar quando uma transmissão foi concluída ou até mesmo para despertar o microcontrolador, caso necessário.

Como o módulo LoRa opera com uma tensão recomendada de 5V e o ESP32 trabalha com 3,3V, torna-se necessário o uso de divisores de tensão com resistores de 4,7kΩ para ajustar os sinais de comunicação serial, garantindo que os níveis de tensão estejam dentro dos limites adequados para o funcionamento correto do rádio. A alimentação do módulo é fornecida pelo pino de 3,3V do ESP32, que disponibiliza uma corrente máxima de 200 mA. Esse valor é suficiente para suprir o consumo do rádio, que pode atingir um pico de 150 mA durante a transmissão de dados, garantindo a operação estável do sistema sem comprometer a alimentação dos demais componentes. Essa conexão está ilustrada na Figura 21.

#### *4.4.1.6 Fluxograma*

- Início: Começa o funcionamento assim que o equipamento é ligado.
- Verificação do despertar: Verifica qual a razão do ESP32 acordar.

- Sim: Prossegue para a razão na qual acordou, podendo ser devido ao tempo que a cada 1 hora ele desperta, a uma abertura da colmeia ou pertinente a tara da balança.
- Não: O dispositivo continua dormindo.
- Despertou devido a tempo: Começa o funcionamento principal do sistema.
  - Inicializa sensores: Configura as comunicações dos sensores e testa conexão.
  - Captura dados sensores: Ler os dados de cada sensor individualmente.
  - Montagem da Estrutura de dados: Monta a estrutura de dados atribuindo os dados lidos pelos sensores além do Mac do ESP32.
  - Trasmissão dos dados: O dados são transmitidos pelo rádio LoRa para o gateway.
  - Verifica recebimento: Verifica se o gateway recebeu os dados.
    - * Sim: Configura o deep sleep.
      - · Configura interrupção do deep sleep: É configurado os métodos de interrupção, que é por timer a cada uma hora, pelo reed switch quando ele emite um sinal de HIGH, ou pelo botão de tara quando emite um sinal de HIGH.
      - · Deep sleep: O dispositivo volta a dormir.
    - * Não: Reenvia os dados até o gateway retornar a confirmação.
- Despertou devido a abertura da colmeia: Começa o ciclo de funcionamento de quando a tampa da colmeia é aberta.
  - Inicializa sensores: Configura as comunicações dos sensores e testa conexão.
  - Verifica se o status da tampa: Verifica de a tampa da colmeia está aberta.
    - * Sim: Será lido os dados dos sensores indicando que a colmeia está aberta.
    - * Não: Será lido os dados dos sensores indicando que a colmeia está fechada
  - Captura dados sensores: Ler os dados de cada sensor individualmente de quando a porta está aberta.
  - Montagem da Estrutura de dados: Monta a estrutura de dados atribuindo os dados lidos pelos sensores além do Mac do ESP32 de quando a porta está aberta.
  - Trasmissão dos dados: O dados são transmitidos pelo rádio LoRa para o gateway de quando a porta está aberta.
  - Verifica recebimento: Verifica se o gateway recebeu os dados.
    - * Sim: Realiza a verificação de a colmeia ainda está aberta.
      - · Sim: Continua verificando se a colmeia permanece aberta.
      - · Não: É realizada fluxo de leitura normal dos dados de quando a colmeia

está fechada.

- * Não: Reenvia os dados até o gateway retornar a confirmação.
- Captura dados sensores: Ler os dados de cada sensor individualmente de quando a porta está fechada.
- Montagem da Estrutura de dados: Monta a estrutura de dados atribuindo os dados lidos pelos sensores além do Mac do ESP32 de quando a porta está aberta.
- Trasmissão dos dados: O dados são transmitidos pelo rádio LoRa para o gateway de quando a porta está aberta.
- Verifica recebimento: Verifica se o gateway recebeu os dados de quando a porta está aberta.
  - * Sim: Configura o deep sleep.
    - · Configura interrupção do deep sleep: É configurado os métodos de interrupção, que é por timer a cada uma hora, pelo reed switch quando ele emite um sinal de HIGH, ou pelo botão de tara quando emite um sinal de HIGH.
    - · Deep sleep: O dispositivo volta a dormir.
  - * Não: Reenvia os dados até o gateway retornar a confirmação.
- Despertou para tara: Acordou para realizar a tara da balança.
  - Ativa o HX711: Ativa o HX711 botando o GPIO14 para HIGH.
  - Realiza a tara: Realiza a leitura da tara.
  - Armazena tara: Armazena o valor lido na tara na memória flash do ESP32 para esse valor não ser perdido quando o dispositov dormir.
  - Desativa o HX711: Desativa o HX711 botando o GPIO14 para LOW.
  - Configura interrupção do deep sleep: É configurado os métodos de interrupção, que é por timer a cada uma hora, pelo reed switch quando ele emite um sinal de HIGH, ou pelo botão de tara quando emite um sinal de HIGH.
  - Deep sleep: O dispositivo volta a dormir.

#### *4.4.2 Gateway*

Este dispositivo tem a função de receber os dados transmitidos via rádio LoRa, identificar o remetente e encaminhá-los para a aplicação web por meio do protocolo HTTP. Esse processo garante a integração dos dados coletados na colmeia com o sistema de monitoramento remoto, permitindo o armazenamento, a análise e a visualização das informações em tempo real.

O equipamento é composto por um rádio LoRa E32 433T20D e um microcontrolador ESP32, dispositivos que possuem os recursos necessários para desempenhar essa função de forma eficiente. O ESP32, além de processar os dados recebidos, conta com conectividade Wi-Fi, permitindo o envio das informações para a aplicação web de maneira rápida e segura.

Já o rádio LoRa se destaca por suas funções avançadas, como o recebimento e a identificação de pacotes específicos, além da capacidade de comunicação com múltiplos remetentes dentro de uma topologia estrela. Essa configuração proporciona maior flexibilidade ao sistema, permitindo a integração de diversos nós sensores e garantindo confiabilidade na transmissão dos dados, mesmo em ambientes com obstáculos ou distâncias consideráveis entre os dispositivos.

A interação entre o ESP32 e o módulo LoRa possibilita uma comunicação eficiente e de baixo consumo energético, aspectos fundamentais para aplicações em monitoramento remoto, como no caso das colmeias inteligentes. Esse dispositivo está ilustrado na Figura 21.

A alimentação do equipamento é realizada por meio de uma fonte de 5V, garantindo seu funcionamento contínuo. Como o dispositivo precisa permanecer em um local com conexão Wi-Fi para o envio dos dados, presume-se que haverá disponibilidade de energia elétrica para mantê-lo operante de forma ininterrupta.

O fluxo de funcionamento deste equipamento é apresentado na seguinte Figura 23.

- Início: O processo começa assim que o equipamento é ligado.
- Configuração do Wi-Fi: Configura os parâmetros de conexão e tenta se conectar até

alcançar a conexão.

- Configuração do rádio: Configura o rádio para que ele funcione com estruturas específicas de dados.
- Início do loop: Verifica se algum dado foi recebido.
  - Sim: Passa para a verificação se é um dado de colmeia.
  - Não: Fica disponível para a leitura de novos dados.
- Verificação dos dados: Verifica se os dados que chegaram é de uma colmeia.
  - Sim: Organiza os dados em uma estrutura compatível.
  - Não: Fica disponível para a leitura de novos dados.
- Identifica colmeia: Relaciona o MAC da colmeia aos dados para identificar a colmeia.
- Confirmação de recebimento: Retorna ao nó colmeia que os dados foram recebidos.
- Estruturação da rota: Monta a rota especificando o MAC da respectiva colmeia que dejesa enviar os dados.
- Estruturação do Json: Monta o Json com os dados vindos da colmeia.
- Envia dados: Envia via HTTP o Json com os dados para a rota que identifica qual colmeia enviou.
- Confirmação de recebimento: Verifica se o retorno do servidor foi 201.
  - Sim: Fica disponível para a leitura de novos dados.
  - Não: Tenta enviar novamente.
- Tentativas de envio: Verifica a quantidade de vezes que foi reenviado a requisição é no máximo 5.
  - Sim: Reenvia a requisição com os dados.
  - Não: Fica disponível para a leitura de novos dados.

### *4.4.3 Aplicação Web*

Este serviço tem a função de receber os dados transmitidos pelo gateway por meio da *Application Programming Interface* (API), armazená-los em um banco de dados e, posteriormente, disponibilizá-los ao usuário. Dessa forma, torna-se possível o acompanhamento em tempo real das informações coletadas pelo dispositivo da colmeia, permitindo a análise contínua e a tomada de decisões com base nos dados registrados.

Nesta etapa, é utilizada a aplicação web que está sendo desenvolvida nos laboratórios Lisa, do Intituto Federal do Ceará - Campus Boa Viagem, e Engine Lab, da Universidade Federal do Ceará - Campus Crateús. Essa plataforma tem como objetivo possibilitar o acompanhamento e o gerenciamento remoto de apiários, permitindo a visualização e a análise dos dados coletados em tempo real.

Atualmente, a plataforma ainda está em fase de desenvolvimento, porém já permite a realização de funções básicas, como o cadastro de propriedades, apiários e colmeias. Além disso, já é possível acompanhar os dados coletados das colmeias, proporcionando uma visão inicial do monitoramento remoto dos apiários.

A API disponibiliza rotas específicas para o recebimento de dados, garantindo a correta atribuição das informações coletadas. No momento do cadastro de uma colmeia, é registrado o endereço MAC do dispositivo correspondente, que passa a atuar como seu identificador único. Dessa forma, ao enviar os dados para a API por meio de uma requisição HTTP, o gateway deve incluir o MAC do dispositivo remetente, assegurando a identificação precisa e a vinculação correta das informações a cada colmeia monitorada.

## 4.5 Experimentação

O dispositivo foi testado pela primeira vez em laboratório no dia 11 de novembro de 2024, com o objetivo de verificar o funcionamento de todos os sensores. Após essa etapa inicial, o equipamento foi posicionado a aproximadamente 30 metros do gateway, onde passou por testes contínuos de operação, garantindo sua estabilidade em um ambiente controlado.

Com os testes laboratoriais bem-sucedidos, o dispositivo foi levado para um ambiente real de funcionamento em um apiário localizado no Palmares 2, na zona rural de Crateús - CE na coordenada -5.054242, -40.699645. Nessa fase, diversos problemas foram identificados. Um dos principais desafios foi a insuficiência da placa solar utilizada na época, que possuía apenas 5W de potência. Devido ao sombreamento causado pela vegetação alta no apiário, a placa não conseguia fornecer energia suficiente para manter o equipamento operante, tornando necessária sua substituição por uma placa de 20W.

Outro problema observado foi a construção do dispositivo utilizando jumpers. Como esses fios são soldados diretamente na placa, o equipamento tornou-se suscetível a quebras durante o manuseio, comprometendo sua durabilidade e confiabilidade. Além disso, o suporte de baterias apresentou dificuldades para acoplar corretamente as células de lítio, resultando em desconexões ocasionais ao movimentar o dispositivo, o que exigiu ajustes no sistema de fixação das baterias.

Atualmente, o equipamento instalado no Palmares 2 encontra-se inativo devido à necessidade de substituição da placa solar e outros componentes. No entanto, um segundo dispositivo foi instalado em outro apiário, localizado na região de Lagoas, distrito de Tucuns, também na zona rural de Crateús - CE na coordenada -5.209066, -40.868391. Esse equipamento permanece em funcionamento, mas enfrenta desafios relacionados à comunicação com o gateway, ocasionando falhas intermitentes na transmissão dos dados. A simples reinicialização do dispositivo restabelece sua operação, indicando que o problema pode estar relacionado a falhas temporárias no software ou na conectividade do sistema, exigindo uma investigação mais detalhada para encontrar uma solução definitiva.

A realização dos testes iniciais em laboratório e sua posterior aplicação em um ambiente real de funcionamento permitiram identificar pontos cruciais para o desenvolvimento do dispositivo. Os desafios enfrentados, como a insuficiência da placa solar e as dificuldades estruturais com o uso de jumpers, destacaram a importância de uma análise detalhada dos componentes utilizados, bem como da necessidade de ajustes no design do equipamento para garantir maior durabilidade e confiabilidade em campo. A substituição da placa solar por uma de maior potência e a modificação no sistema de fixação das baterias são passos fundamentais para melhorar a eficiência do dispositivo.

Ademais, a persistência de falhas intermitentes na comunicação do segundo dispositivo evidenciou a necessidade de aprimorar a conectividade e a robustez do software, a fim de garantir a estabilidade na transmissão de dados. Embora o dispositivo esteja operando, os ajustes necessários no sistema exigem atenção para que os objetivos do projeto sejam plenamente alcançados. O monitoramento contínuo e a busca por soluções mais eficazes são essenciais para superar os desafios encontrados, visando a viabilização de uma tecnologia que contribua de maneira significativa para a coleta de dados em ambientes de apicultura.

#### 4.6 Exibição dos dados

No desenvolvimento do sistema Web, são utilizadas tecnologias web, para o desenvolvimento do Front-end e BackEnd. Onde para o front, são utilizadas tecnologias como HTML5, CCS3, React.js e TypeScript, Já para o back-end, foi usado Node.js para comunicação com os dispositivos e processamento dos dados, para o armazenamento de dados é utilizado o PostgreSQL, que tem como principal característica o desempenho na gestão de grandes volumes de dados. A interface é intuitiva, permitindo visualização em tempo real, geração de relatórios e alertas sobre mudanças críticas nos parâmetros.

Na Figura 24, o diagrama ilustra o fluxo de informações e operações dentro de uma aplicação web, destacando a interação entre os diferentes componentes e o banco de dados PostgreSQL.

O processo começa com a coleta e processamento de dados, que são enviados para uma API. Esses dados são então utilizados para configurar a interface web e gerar relatórios. A interface permite a entrada do usuário, que é validada e utilizada para atualizar o banco de dados. O servidor web coordena todas as operações e envia as respostas de volta para o navegador, completando o ciclo de comunicação.

## 5 RESULTADOS E DISCUSSÃO

O estudo envolveu a instalação de dois dispositivos em um apiário localizado na região de Lagoas, distrito de Tucuns, zona rural de Crateús – CE, nas coordenadas -5.209066, -40.868391. Os equipamentos permaneceram em funcionamento durante o período de testes até a redação deste trabalho.

Os dados utilizados para análise correspondem ao período entre 10/01/2025 e 20/02/2025, durante o qual foram identificadas diversas falhas operacionais. Nesse intervalo, foram analisados os dados de duas colmeias, denominadas colmeia 1 e colmeia 2. Durante essa fase, múltiplas manutenções foram realizadas para corrigir erros, o que impactou a continuidade da coleta de dados.

Dentre os principais problemas encontrados, destaca-se a interrupção na transmissão dos dados, causada por diversos fatores. A falta de energia na residência onde está localizado o gateway resultou na interrupção da transmissão, assim como a ausência de conexão com a internet. No entanto, algumas falhas na transmissão ainda não foram plenamente identificadas. Além disso, foram observadas falhas no funcionamento da balança, que apresentou interrupções frequentes devido à oxidação nos conectores e a incompatibilidades geradas por atualizações de bibliotecas no código, comprometendo a comunicação entre o sensor e o microcontrolador.

Devido a essas falhas, a coleta de dados da balança foi prejudicada, resultando em funcionamento intermitente e medições imprecisas. Como consequência, verificaram-se variações anômalas nos dados, como observado no período entre 5h e 7h da manhã do dia 14/02/2025 na colmeia 1, conforme ilustrado na Figura 25. Durante esse intervalo, esperava-se uma redução do peso da colmeia devido à saída das abelhas para a coleta de pólen e néctar, em vez de um aumento. Além disso, padrões de inconsistência semelhantes podem ser observados na Figura 26, especialmente no período entre 18h e 23h, quando o peso deveria se manter mais estável, visto que há menor atividade de saída de abelhas.

A inconsistência nos registros pode estar relacionada a ruídos nas conexões da balança, tornando necessária a adoção de estratégias para mitigar esse problema, tais como o uso de cabos blindados, a implementação de técnicas de software para redução de interferências e a aplicação de filtros para minimizar o ruído. Além disso, já é utilizada uma média flutuante na coleta do peso, considerando a possibilidade de variações naturais nas medições da balança.

Ao considerar a média diária dos pesos coletados, foi possível identificar a variação do peso das colmeias ao longo dos dias, como demonstrado nas Figura 27 e Figura 28, que apresentam a média de peso registrada entre os dias 13/02/2025 e 17/02/2025. Nessas figuras, observa-se que tanto a colmeia 1 quanto a colmeia 2 apresentaram uma perda de peso entre os dias 14 e 16, seguida de um aumento no dia subsequente. Esses resultados indicam que, com alguns ajustes adicionais na balança, o sistema poderá operar de forma ideal, proporcionando um suporte mais eficiente ao apicultor na tomada de decisões.

Já os dados de temperatura, umidade e pressão foram coletados de forma adequada pelo sensor BME280, que demonstrou alta eficiência e conformidade com os requisitos do projeto. O sensor operou de maneira contínua durante todo o período em que os dados foram transmitidos ao servidor, possibilitando uma análise mais precisa das informações.

Observou-se que os sensores instalados nas duas colmeias operaram de forma consistente, uma vez que as médias diárias de temperatura, umidade e pressão apresentadas na Figura 29 e na Figura 30, coletadas no período de 10/01/2025 a 31/01/2025, exibem variações semelhantes, evidenciando o adequado funcionamento dos dispositivos. No entanto, no dia 15/01/2025, foi registrada uma queda abrupta na temperatura acompanhada de um aumento na umidade relativa e na pressão. Essa mudança repentina foi causada por uma intensa chuva na região, que acumulou 131 milímetros ao longo do dia (FUNCEME, 2025), influenciando diretamente a temperatura interna da colmeia.

Observa-se que as abelhas buscam manter a temperatura interna dentro da faixa ideal, que, conforme descrito na definição de parâmetros, varia entre 34°C e 36°C. Temperaturas fora dessa faixa podem comprometer a estabilidade da colmeia. Os dados apresentados nas Figura 29 e Figura 30 indicam que a colmeia não permaneceu por longos períodos dentro dessa faixa ideal, possivelmente devido à ocorrência de chuvas intensas na região durante o período de coleta.

Essa condição climática resultou em temperaturas ambientais mais baixas, porém dentro do padrão esperado para a localidade pela época do ano, variando entre 26ºC e 28ºC (IPECE, 2012), influenciando diretamente a regulação térmica dentro da colmeia, fazendo com que as mesmas não conseguissem se manter na sua temperatura ideal.

Adicionalmente, a média de umidade se manteve dentro da faixa considerada ideal para a colmeia, conforme descrito na definição de parâmetros deste estudo, que é superior a 50%. No entanto, mesmo dentro dessa faixa, foram registrados períodos de baixa umidade que podem impactar a saúde da colmeia, exigindo atenção para possíveis intervenções.

A temperatura, a umidade e a pressão estão diretamente relacionadas e possuem uma relação inversamente proporcional. Da mesma forma, a pressão atmosférica está intimamente relacionada à umidade, sendo inversamente proporcional à temperatura.

Com uma análise mais detalhada por hora do dia 10/01/2025, é possível perceber as variações de temperatura e umidade ao longo do dia, como observado na Figura 31 e na Figura 32. Nessas figuras, é possível notar que a temperatura da colmeia diminui e a umidade aumenta conforme a noite avança. De forma contrária, durante o dia, a temperatura sobe e a umidade tende a diminuir.

Com a coleta desses parâmetros, é possível realizar uma avaliação detalhada do estado da colmeia, fornecendo informações cruciais para o monitoramento e a gestão do apiário de forma mais eficiente. Isso não apenas facilita a tomada de decisões informadas pelos apicultores, mas também contribui significativamente para a redução de custos com o manejo apícola, otimizando o uso de recursos e o tempo dedicado à supervisão física das colmeias.

O apicultor, com o auxílio desse sistema de monitoramento remoto, poderá identificar o momento exato para implementar medidas como o sombreamento da colmeia, baseando-se na análise da temperatura interna, o que ajuda a evitar o superaquecimento durante períodos de altas temperaturas. Além disso, os dados de peso permitirão determinar o momento ideal para a colheita do mel, otimizando a produção e evitando perdas.

Outro benefício importante do sistema é a possibilidade de monitorar o forrageamento das abelhas, observando como a temperatura, a umidade e outros parâmetros influenciam os períodos em que as abelhas estão mais ativas, o que pode fornecer *insights* valiosos sobre o comportamento das colônias. Dessa forma, o apicultor não apenas gerencia melhor o ambiente das colmeias, mas também tem a capacidade de antecipar e corrigir potenciais problemas antes que eles afetem a saúde das abelhas e a produtividade do apiário.

Dessa forma, o dispositivo se mostra uma solução promissora para o monitoramento de colmeias, sendo capaz de coletar e registrar dados ambientais internos relevantes, como temperatura, umidade, pressão e peso. Esses parâmetros são essenciais para o acompanhamento da saúde das colônias e a eficiência do apiário. Embora tenha apresentado algumas falhas na transmissão dos dados, o equipamento demonstrou sua funcionalidade ao fornecer informações vitais para a gestão das colmeias.

A utilização do dispositivo pode, portanto, auxiliar de maneira significativa o apicultor no processo de manejo, permitindo uma tomada de decisão mais informada e eficiente. Isso resulta em uma gestão mais eficiente do apiário, ajudando a otimizar os recursos, melhorar a saúde das abelhas e maximizar a produção de mel. Além disso, com o aprimoramento contínuo do sistema e a correção das falhas de transmissão, espera-se que a ferramenta se torne ainda mais robusta e eficaz no futuro, consolidando-se como um aliado importante para os apicultores na modernização da apicultura.

## 6 CONCLUSÕES E TRABALHOS FUTUROS

O desenvolvimento e a implementação do sistema de monitoramento remoto de colmeias demonstraram ser uma solução promissora para enfrentar os desafios tradicionais da apicultura. A integração de sensores para coleta de dados em tempo real permitirá reduzir significativamente a necessidade de visitas físicas aos apiários, pois, com a análise dos dados, o apicultor terá uma noção mais precisa do estado das colmeias, diminuindo custos operacionais e minimizando o estresse causado às colônias. A análise contínua dos dados coletados possibilita uma resposta rápida a possíveis problemas, contribuindo para a eficiência e produtividade das colmeias.

Embora algumas soluções tenham sido encontradas para os desafios técnicos enfrentados, nem todos os problemas foram completamente resolvidos. O sistema ainda apresenta falhas no envio dos dados, cuja causa não foi identificada, além de instabilidades na comunicação e no funcionamento de alguns sensores, indicando a necessidade de aprimoramentos futuros.

O sistema demonstrou seu potencial para transformar a apicultura no região Nordeste do Brasil, proporcionando aos apicultores uma ferramenta valiosa para o monitoramento em tempo real de suas produções. O interesse manifestado por cooperativas, associações de produtores e órgãos governamentais reforça a relevância e o impacto positivo dessa tecnologia para a sustentabilidade da apicultura.

Para propostas futuras, sugere-se a implantação de um maior número de sensores, ampliando a coleta de dados e proporcionando uma análise mais detalhada das condições das colmeias. Além disso, o estudo aprofundado dos dados coletados poderá viabilizar intervenções mais precisas e eficazes na gestão apícola. Outro ponto importante para a melhoria do sistema é a utilização de uma miniestação meteorológica, que permitirá capturar parâmetros climáticos do apiário, auxiliando na análise dos dados. O aprimoramento contínuo do sistema garantirá maior robustez em diferentes condições ambientais, permitindo sua adaptação às necessidades específicas dos apicultores e consolidando sua importância para o setor.