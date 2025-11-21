![](_page_0_Picture_0.jpeg)

# UNIVERSIDADE FEDERAL DO CEARÁ CAMPUS DE CRATEÚS CURSO DE GRADUAÇÃO EM SISTEMAS DE INFORMAÇÃO

### JOEL DE SOUSA SILVA

UMA AVALIAÇÃO COMPARATIVA ENTRE MECANISMOS DE AUTENTICAÇÃO PARA DISPOSITIVOS INTERNET OF THINGS (IOT) COM BAIXO PODER COMPUTACIONAL NA INDÚSTRIA 4.0.

CRATEÚS

### JOEL DE SOUSA SILVA

UMA AVALIAÇÃO COMPARATIVA ENTRE MECANISMOS DE AUTENTICAÇÃO PARA DISPOSITIVOS INTERNET OF THINGS (IOT) COM BAIXO PODER COMPUTACIONAL NA INDÚSTRIA 4.0.

> Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em Sistemas de Informação do Campus de Crateús da Universidade Federal do Ceará, como requisito parcial à obtenção do grau de bacharel em Sistemas de Informação.

> Orientador: Prof. Dr. Antonio Emerson B. Tomaz

> Coorientador: Prof. Dr. Allysson Allex Araújo

### JOEL DE SOUSA SILVA

UMA AVALIAÇÃO COMPARATIVA ENTRE MECANISMOS DE AUTENTICAÇÃO PARA DISPOSITIVOS INTERNET OF THINGS (IOT) COM BAIXO PODER COMPUTACIONAL NA INDÚSTRIA 4.0.

> Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em Sistemas de Informação do Campus de Crateús da Universidade Federal do Ceará, como requisito parcial à obtenção do grau de bacharel em Sistemas de Informação.

Aprovada em:

### BANCA EXAMINADORA

Prof. Dr. Antonio Emerson B. Tomaz (Orientador) Universidade Federal do Ceará (UFC)

Prof. Dr. Allysson Allex Araújo (Coorientador) Universidade Federal do Cariri (UFCA)

Prof. Me. Filipe Fernandes dos Santos B. de Matos Universidade Federal do Ceará (UFC)

> Prof. Dr. Reuber Régis de Melo Universidade Federal do Ceará (UFC)

### RESUMO

A autenticidade é um aspecto essencial da segurança da informação, abordada em vários Sistemas de Informação (SI), incluindo dispositivos da Internet das Coisas (IoT) na Indústria 4.0. A implementação eficiente de métodos de segurança, como a autenticação, é um desafio considerável no contexto da IoT, devido à alta demanda computacional das operações. Isso é particularmente verdadeiro para dispositivos IoT com limitações de energia, memória e capacidade de processamento, frequentemente utilizados no ambiente da Indústria 4.0. Neste contexto, o estudo tem como objetivo investigar qual mecanismo de autenticação criptográfica — RSA, AES, HMAC ou NIZKP — oferece o melhor desempenho em termos de tempo de processamento, utilização de memória e consumo de energia quando implementados em dispositivos IoT com limitações de recursos computacionais. Para alcançar o objetivo proposto, inicialmente apresenta-se um desenho metodológico que visa realizar uma análise comparativa abrangente dos mecanismos de autenticação selecionados. A hipótese é que o mecanismo de autenticação NIZKP requer menos recursos computacionais em comparação com métodos convencionais como RSA, AES e HMAC. Portanto, são expostos resultados empíricos preliminares de um experimento computacional utilizando o algoritmo NIZKP em um Arduino Nano, demonstrando a viabilidade de sua implementação em dispositivos com severas limitações de recursos. Este estudo busca contribuir para uma compreensão mais aprofundada do desempenho de esquemas de autenticação populares em dispositivos IoT com recursos limitados na era da Indústria 4.0. Os achados desta pesquisa podem direcionar decisões estratégicas de indústrias que estão adotando ou planejam adotar dispositivos IoT, auxiliando na seleção de esquemas de autenticação que se ajustem às suas necessidades específicas.

Palavras-Chave: Autenticidade. Segurança da Informação. Dispositivos IoT. Indústria 4.0. Mecanismos de Autenticação

### ABSTRACT

Authenticity is an essential aspect of information security, addressed in various Information Systems (IS), including Internet of Things (IoT) devices in Industry 4.0. The efficient implementation of security methods, such as authentication, is a considerable challenge in the context of IoT, due to the high computational demand of operations. This is particularly true for IoT devices with energy, memory, and processing limitations, often used in the Industry 4.0 environment. In this context, the study aims to investigate which cryptographic authentication mechanism — RSA, AES, HMAC, or NIZKP — offers the best performance in terms of processing time, memory usage, and energy consumption when implemented on IoT devices with limited computational resources. To achieve the proposed objective, a methodological design is initially presented, aiming to perform a comprehensive comparative analysis of the selected authentication mechanisms. The hypothesis is that the NIZKP authentication mechanism requires fewer computational resources compared to conventional methods such as RSA, AES, and HMAC. Therefore, preliminary empirical results of a computational experiment using the NIZKP algorithm on an Arduino Nano are presented, demonstrating the feasibility of its implementation on devices with severe resource limitations. This study seeks to contribute to a deeper understanding of the performance of popular authentication schemes on IoT devices with limited resources in the era of Industry 4.0. The findings of this research can guide strategic decisions of industries that are adopting or planning to adopt IoT devices, assisting in the selection of authentication schemes that fit their specific needs.

Keywords: Authenticity. Information Security. IoT Devices. Industry 4.0. Authentication Mechanisms

### LISTA DE ILUSTRAÇÕES

| Figura 1<br>– | Processo de cifração do AES.                                              | 12 |
|---------------|---------------------------------------------------------------------------|----|
| Figura 2<br>– | Criptografia de chave pública para garantir a confidencialidade.          | 14 |
| Figura 3<br>– | Criptografia de chave pública para garantir a autenticidade.              | 15 |
| Figura 4<br>– | Uso do HMAC para aplicação de autenticidade.                              | 17 |
| Figura 5<br>– | Protocolo genérico interativo ZKP.                                        | 19 |
| Figura 6<br>– | Transformação de ZKP em NIZKP usando a heurística Fiat-Shamir .           | 20 |
| Figura 7<br>– | Procedimentos metodológicos .                                             | 26 |
| Figura 8<br>– | Estimativa de consumo de tempo e energia para geração de par de chaves no |    |
|               | NIZKP                                                                     | 29 |

# SUMÁRIO

| 1                                                                              | INTRODUÇÃO .                                              | 7  |  |  |
|--------------------------------------------------------------------------------|-----------------------------------------------------------|----|--|--|
| 1.1                                                                            | Declaração do problema e questão de pesquisa              | 8  |  |  |
| 1.2                                                                            | Objetivo geral                                            | 9  |  |  |
| 1.3                                                                            | Objetivos específicos                                     | 9  |  |  |
| 1.4                                                                            | Contribuições                                             | 9  |  |  |
| 1.5                                                                            | Estrutura do trabalho                                     | 9  |  |  |
| 2                                                                              | FUNDAMENTAÇÃO TEÓRICA                                     | 10 |  |  |
| 2.1                                                                            | Indústria 4.0 e<br>Internet of Things                     | 10 |  |  |
| 2.2                                                                            | Mecanismos de autenticação criptográficos                 | 11 |  |  |
| 2.2.1                                                                          | Autenticação baseada em cifra simétrica                   | 11 |  |  |
| 2.2.2                                                                          | Autenticação baseada em cifra assimétrica                 | 13 |  |  |
| 2.2.3                                                                          | Código de autenticação de mensagem baseado em função hash | 15 |  |  |
| 2.2.4                                                                          | Autenticação baseada em desafio-resposta                  | 18 |  |  |
| 2.3<br>Autenticação em cenários críticos da indústria que dispensam confidenci |                                                           |    |  |  |
|                                                                                | alidade                                                   | 21 |  |  |
| 3                                                                              | TRABALHOS RELACIONADOS                                    | 22 |  |  |
| 4                                                                              | ESTUDO EMPÍRICO                                           | 25 |  |  |
| 4.1                                                                            | Procedimentos metodológicos                               | 25 |  |  |
| 4.2                                                                            | Resultados preliminares                                   | 28 |  |  |
| 5                                                                              | CRONOGRAMA E PRÓXIMOS PASSOS .                            | 30 |  |  |
|                                                                                | REFERÊNCIAS                                               | 31 |  |  |

## <span id="page-7-0"></span>1 INTRODUÇÃO

A Indústria 4.0 engloba processos de produção eficientes, gerenciamento de dados, relacionamento com consumidores e competitividade, sendo frequentemente referida como a Quarta Revolução Industrial [\(PICCAROZZI](#page-34-0) *et al.*, [2018\)](#page-34-0). De acordo com Liu *[et al.](#page-33-0)* [\(2020\)](#page-33-0), a Indústria 4.0 se destaca por incorporar um conjunto diversificado de tecnologias emergentes, entre elas a Internet das Coisas (em inglês, *Internet of Things* - IoT). Em termos gerais, a IoT é caracterizada por ser uma ampla rede interconectada de dispositivos inteligentes com a capacidade de se comunicar automaticamente, compartilhando dados e recursos entre si, reagindo e se adaptando às situações e alterações no ambiente [\(MADAKAM](#page-33-1) *et al.*, [2015\)](#page-33-1).

Os dispositivos de IoT têm ganhado ampla aceitação, sendo integrados a diversos domínios de aplicação, tais como agricultura inteligente [\(PERWEJ](#page-34-1) *et al.*, [2019\)](#page-34-1), automação industrial [\(GARDAŠEVIC´](#page-32-0) *et al.*, [2017\)](#page-32-0), cidades inteligentes [\(LOHIYA; THAKKAR, 2020\)](#page-33-2) e, consequentemente, a Indústria 4.0. No entanto, o aumento da adoção de dispositivos IoT traz consigo ameaças significativas para a segurança da informação, conforme destacado por [Abomhara e Køien](#page-31-1) [\(2015\)](#page-31-1). No contexto da cibersegurança, uma ameaça é uma atividade que explora vulnerabilidades de segurança de um sistema e tem um efeito negativo sobre ele [\(KRISHNA](#page-33-3) *et al.*, [2021\)](#page-33-3). Uma das propriedades fundamentais para a segurança da informação é a autenticação. O processo de autenticação consiste, de modo geral, na verificação de que algo ou alguém é realmente o que ou quem se declara ser [\(ALNAHARI; QUASIM, 2021\)](#page-31-2).

Nesse cenário, garantir a autenticidade dos dispositivos IoT torna-se essencial para assegurar a integridade dos dados e o funcionamento seguro do sistema. Um dispositivo IoT não autenticado adequadamente representa uma ameaça grave aos sistemas da Indústria 4.0. Na ausência de autenticação apropriada, entidades mal-intencionadas podem infiltrar-se no sistema, fingindo uma identidade confiável enquanto, na realidade, buscam causar danos, incluindo a manipulação de dados críticos ou a execução de ações disruptivas que levam a paradas na produção [\(MARÍN](#page-33-4) *et al.*, [2024\)](#page-33-4).

Conforme destacado por Roy *[et al.](#page-34-2)* [\(2018\)](#page-34-2), um dos principais desafios para implementar esquemas de segurança em dispositivos IoT é o fato de muitos deles serem projetados com restrições severas de recursos, visando garantir a eficiência energética. Dispositivos de baixo poder computacional são especialmente relevantes na Indústria 4.0 porque são projetados para consumir menos energia, o que é essencial em aplicações onde muitos dispositivos precisam funcionar continuamente sem intervenção humana. A eficiência energética não apenas reduz

os custos operacionais, mas também é fundamental para aplicações onde o acesso à energia é limitado ou onde a substituição de baterias é impraticável.

Muitas pesquisas têm abordado o desafio de implementar mecanismos de autenticação em dispositivos IoT. Alguns deles utilizam criptografia de chave pública baseada em RSA (Rivest, Shamir e Adleman) ou ECC (*Elliptic Curve Cryptography*), como os estudos de [Mumtaz](#page-33-5) *[et al.](#page-33-5)* [\(2019\)](#page-33-5), Xu *[et al.](#page-36-0)* [\(2018\)](#page-36-0) e [Porambage](#page-34-3) *et al.* [\(2014\)](#page-34-3). Outros são baseados na tradicional cifra simétrica AES (*Advanced Encryption Standard*), como por exemplo os trabalhos de [Jan](#page-32-1) *[et al.](#page-32-1)* [\(2014\)](#page-32-1), Jan *[et al.](#page-32-2)* [\(2019\)](#page-32-2) e [Zhou](#page-36-1) *et al.* [\(2019\)](#page-36-1). Além disso, o esquema de autenticação HMAC (*Hash-Based Message Authentication Codes*) também tem sido amplamente utilizado, como demonstrado por [Khemissa e Tandjaoui](#page-32-3) [\(2015\)](#page-32-3) e [Taha](#page-35-0) *et al.* [\(2020\)](#page-35-0). Há ainda um crescente emprego do esquema de autenticação ZKP (*Zero-Knowledge Proof*) ou da varição NIZKP (Noninteractive Zero-Knowledge Proofs) no campo da IoT, conforme demonstrado pelos estudos de [Nissar](#page-34-4) *et al.* [\(2022\)](#page-34-4), [Puthiyidam](#page-34-5) *et al.* [\(2023\)](#page-34-5) e [Tomaz](#page-35-1) *et al.* [\(2020\)](#page-35-1). No entanto, a literatura acadêmica ainda carece de estudos comparativos entre esses diferentes esquemas dentro de um mesmo ambiente de configuração e implementação.

#### <span id="page-8-0"></span>1.1 Declaração do problema e questão de pesquisa

Dispositivos IoT comumente enfrentam limitações de poder computacional, restrições energéticas e memória reduzida (WEI *[et al.](#page-35-2)*, [2016\)](#page-35-2). A implementação eficaz de métodos de segurança, incluindo autenticação, representa um desafio significativo no contexto da IoT, especialmente devido à alta demanda computacional das operações [\(NGUYEN](#page-33-6) *et al.*, [2015\)](#page-33-6).

Embora os diversos trabalhos que abordam mecanismos de autenticação tenham aplicado e avaliado os esquemas baseados em RSA, AES, HMAC e ZKP (ou sua versão nãointerativa NIZKP) em cenários isolados, ainda não há na literatura um estudo que compare exatamente esses quatro esquemas de autenticação no mesmo ambiente de implementação. Assim, é essencial realizar uma análise comparativa abrangente, avaliando o desempenho desses diferentes esquemas de autenticação em um ambiente IoT padronizado.

Neste contexto, este trabalho visa investigar a seguinte questão de pesquisa: *qual dos esquemas de autenticação – RSA, AES, HMAC e NIZKP – apresenta o melhor desempenho em termos de tempo de processamento, uso de memória e consumo de energia quando implementados em dispositivos IoT com restrições de recursos computacionais?*

### <span id="page-9-0"></span>1.2 Objetivo geral

Realizar uma análise comparativa abrangente dos algoritmos RSA, AES, HMAC e NIZKP, avaliando seu desempenho como esquemas de autenticação em um ambiente IoT padronizado.

### <span id="page-9-1"></span>1.3 Objetivos específicos

- Implementar os esquemas de autenticação RSA, AES, HMAC e NIZKP.
- Executar os algoritmos em dispositivos IoT com severas restrições de recursos.
- Coletar informações sobre o tempo de processamento, o consumo de energia e a utilização de memória.
- Avaliar o desempenho dos algoritmos nos experimentos realizados.

### <span id="page-9-2"></span>1.4 Contribuições

Este trabalho contribui para uma compreensão mais aprofundada do desempenho de esquemas de autenticação populares em dispositivos IoT com recursos limitados na era da Indústria 4.0. As descobertas desta pesquisa têm o potencial de orientar as decisões estratégicas das indústrias que estão implementando ou planejando implementar dispositivos IoT, facilitando a escolha de esquemas de autenticação adequados para suas aplicações específicas. Além disso, fora do ambiente da Indústria 4.0, este trabalho também oferece *insights* para pesquisadores e desenvolvedores, ajudando-os a fazer escolhas e implementações adequadas, levando em consideração as peculiaridades operacionais dos dispositivos IoT.

### <span id="page-9-3"></span>1.5 Estrutura do trabalho

O presente trabalho é composto por cinco capítulos, incluindo esta Introdução. O [Capítulo 2](#page-10-0) aborda o referencial teórico que embasa este estudo. No [Capítulo 3,](#page-22-0) são apresentados os trabalhos relacionados. O [Capítulo 4](#page-25-0) detalha o procedimento metodológico adotado e apresenta os resultados preliminares. Por fim, o [Capítulo 5](#page-30-0) apresenta os próximos passos da pesquisa.

### <span id="page-10-0"></span>2 FUNDAMENTAÇÃO TEÓRICA

Neste capítulo, são abordados os aspectos teóricos fundamentais do trabalho, iniciando com uma análise da Indústria 4.0 e da *Internet of Things* na Seção [2.1.](#page-10-1) Em seguida, na Seção [2.2,](#page-11-0) são apresentados os mecanismos de autenticação criptográficos investigados neste trabalho. Na Seção [2.3,](#page-21-0) há uma discussão sobre autenticação em cenários industriais críticos.

### <span id="page-10-1"></span>2.1 Indústria 4.0 e *Internet of Things*

A Indústria 4.0 é frequentemente referida como a Quarta Revolução Industrial, caracterizando-se não só pelo uso de tecnologias avançadas, mas também pela integração do mundo digital com o ambiente físico, conectando recursos tecnológicos, produtos, pessoas e empresas [\(SILVA](#page-35-3) *et al.*, [2020\)](#page-35-3). Nesse contexto, destacam-se benefícios consideráveis, tais como o monitoramento e controle remotos de processos de produção, a redução de desperdício, a economia de recursos naturais e a diminuição do consumo de energia [\(WAIBEL](#page-35-4) *et al.*, [2018\)](#page-35-4).

Nesse cenário de transformações impulsionadas por tecnologias avançadas, a Internet das Coisas (em inglês, *Internet of Things* ou IoT) se revela como um componente estratégico na Indústria 4.0 [\(HUANG, 2017\)](#page-32-4). Conforme discutido por [Rose](#page-34-6) *et al.* [\(2015\)](#page-34-6), o uso de IoT abrange cenários nos quais a conectividade de rede e a capacidade de computação se expandem para objetos, sensores e itens do dia a dia que tradicionalmente não são classificados como computadores. Assim, esses dispositivos têm a capacidade de gerar, trocar e consumir dados com intervenção humana mínima.

Uma vez compreendida a natureza dos dispositivos IoT, é essencial ressaltar os desafios associados a sua implementação, como, por exemplo, o consumo de energia. A maioria dos dispositivos IoT é alimentada por bateria devido a uma combinação de fatores, incluindo custo, conveniência e a necessidade de operação sem fio, conforme afirmado por [\(JAYAKUMAR](#page-32-5) *[et al.](#page-32-5)*, [2014\)](#page-32-5). Dispositivos IoT geralmente têm restrições de tamanho, pois muitas vezes são integrados a objetos pequenos ou possuem design compacto para facilitar sua instalação em diferentes ambientes. Assim, para manter o dispositivo IoT pequeno e discreto, são preferíveis baterias menores e mais leves, mesmo que isso signifique uma capacidade de armazenamento de energia mais limitada. Apesar disso, muitos dispositivos IoT exigem longevidade operacional, evitando a troca frequente da bateria, pois tal procedimento seria contraproducente.

Outro desafio na implementação de IoT é a limitação de recursos, como memória e

poder de processamento. Devido a essas limitações, é essencial desenvolver algoritmos leves e eficientes. Esses algoritmos são projetados para minimizar o uso de recursos, garantindo que os dispositivos IoT possam executar suas funções de forma eficaz, mesmo com recursos limitados.

Considerando os aspectos críticos da limitação de recursos nos dispositivos IoT, a seleção cuidadosa de métodos criptográficos é essencial para garantir a segurança e o desempenho desses dispositivos em contextos de operação desafiadores.

### <span id="page-11-0"></span>2.2 Mecanismos de autenticação criptográficos

Tradicionalmente, a criptografia é definida como a ciência da escrita secreta, visando ocultar o significado de uma mensagem. Atualmente, porém, a garantia da confidencialidade não é o único objetivo da criptografia moderna. Ela também é utilizada para fornecer soluções a outros problemas, como a autenticação [\(DELFS](#page-31-3) *et al.*, [2002\)](#page-31-3). Para garantir a autenticidade, um método criptográfico deve permitir que o receptor confirme a identidade do remetente da mensagem [\(TOMASIN, 2017\)](#page-35-5). De acordo com [Delgado-Vargas](#page-31-4) *et al.* [\(2023\)](#page-31-4), mecanismos de autenticação criptográficos referem-se às técnicas e protocolos usados para verificar a identidade de um usuário, dispositivo ou sistema de forma segura, utilizando princípios criptográficos. Em contraste, abordagens de autenticação não criptográfica podem basear-se em biometria, conhecimento (como senhas) ou proximidade física.

Os mecanismos de autenticação criptográficos podem ser classificados em três abordagens principais: baseados em cifra simétrica, baseados em cifra assimétrica e baseados em função hash. Outras abordagens também podem ser utilizadas, como a autenticação baseada em desafio-resposta, em que uma parte apresenta um desafio e a outra parte deve fornecer uma resposta válida para provar sua identidade.

A seguir, são descritos os métodos investigados neste trabalho, os quais se enquadram em uma das quatros categorias mencionadas anteriormente.

#### <span id="page-11-1"></span>*2.2.1 Autenticação baseada em cifra simétrica*

Uma cifra simétrica é um método criptográfico que usa a mesma chave criptográfica tanto para cifrar o texto simples quanto para decifrar o texto cifrado. De acordo com [Alizai](#page-31-5) *[et al.](#page-31-5)* [\(2018\)](#page-31-5), neste tipo de método, há uma chave secreta compartilhada, disponível tanto no dispositivo a ser autenticado quanto no verificador. Neste contexto, o AES (*Advanced Encryption* *Standard*) é comumente utilizado, como no trabalho de Jan *[et al.](#page-32-1)* [\(2014\)](#page-32-1).

O AES é um importante e popular algoritmo simétrico de bloco de 128 bits. Ele é baseado em um princípio de design conhecido como rede de substituição-permutação, que combina substituição e permutação em cada rodada, sendo eficiente tanto em ambientes de software quanto de hardware, e considerado muito seguro [\(RAWAL, 2016\)](#page-34-7). Com seus três comprimentos de chave de 128, 192 e 256 bits, o AES tem se demonstrado seguro contra ataques de força bruta por várias décadas, e não há ataques analíticos com qualquer chance razoável de sucesso conhecidos [\(PAAR; PELZL, 2009\)](#page-34-8).

O algoritmo é referido como AES-128, AES-192 ou AES-256, dependendo do comprimento da chave. O número de rodadas internas do cifrador é determinado pelo comprimento da chave: o AES-128 possui 10 rodadas, AES-192 possui 12 rodadas e AES-256 possui 14 rodadas [\(GHORADKAR; SHINDE, 2015\)](#page-32-6). A estrutura geral do processo de cifração do AES é apresentada na [Figura 1.](#page-12-0)

**Transformação Inicial Bloco de texto claro de 128 bits Rodada 1 Rodada** *2* **Rodada** *n* **Bloco de texto cifrado de 64 bits Chave (128,192 ou 256 bits)** *K<sup>0</sup>* (128 bits) **Expasãodechav e***K<sup>1</sup>* (128 bits) *K<sup>2</sup>* (128 bits) *K<sup>n</sup>* (128 bits) Número de Rodadas Tamanho da Chave 10 128 12 192 14 256

<span id="page-12-0"></span>Figura 1 – Processo de cifração do AES.

Fonte: adaptada de [Stallings](#page-35-6) [\(2018\)](#page-35-6).

A função de *expansão da chave*, mostrada na [Figura 1,](#page-12-0) cria *n*+1 chaves de rodada (*K*0,*K*1,...,*Kn*) de 128 bits cada a partir da chave principal, em que *n* é o número de rodadas. Em cada rodada do AES, o bloco de dados, combinado com a chave de rodada, passa por uma série de transformações para produzir o bloco de texto cifrado. Cada operação contribui para a segurança do AES de uma maneira específica [\(AUMASSON, 2017\)](#page-31-6).

### <span id="page-13-0"></span>*2.2.2 Autenticação baseada em cifra assimétrica*

O conceito de criptografia assimétrica, também chamada de criptografia de chave pública foi introduzido por [Diffie e Hellman](#page-31-7) [\(2022\)](#page-31-7). Este método utiliza um par de chaves, que consiste em uma chave privada e uma chave pública. Assim, uma chave é usada para cifrar e a outra chave é usada para decifrar. Em 1978, Rivest, Shamir e Adleman publicaram o sistema RSA, o primeiro criptossistema prático de chave pública completo, que se baseia na dificuldade de fatorar inteiros grandes e suporta assinaturas digitais [\(BOLFING, 2020\)](#page-31-8). O RSA é o criptossistema de chave pública mais amplamente utilizado e conhecido.

Para que duas entidades comunicantes utilizem o RSA, é necessário gerar um par de chaves para cada uma delas. O criptossistema consiste em três protocolos: geração de chaves, cifração e decifração, conforme descrito por [Paar e Pelzl](#page-34-8) [\(2009\)](#page-34-8) a seguir.

Geração das chaves: o protocolo de geração de chaves procede em cinco etapas:

- 1. Escolha grandes números primos distintos *p* e *q*.
- 2. Calcule *n* = *p* · *q*.
- 3. Calcule φ(*n*) = (*p*−1)(*q*−1).
- 4. Escolha *e* que seja primo relativo a φ(*n*). O par (*n*, *e*) é a chave pública.
- 5. Calcule *d* ≡ *e* <sup>−</sup><sup>1</sup> mod φ(*n*). O par (*n*,*d*) é usado como a chave secreta.

[Delfs](#page-31-3) *et al.* [\(2002\)](#page-31-3) destaca que é necessário multiplicar dois números primos muito grandes, e seu produto *n*, chamado de módulo, pode ser tornado público. O módulo *n*, juntamente com *e*, compõem a chave pública. Os fatores de *n*, os primos *p* e *q*, são mantidos em segredo. Assim, *d* e *n* representam a chave secreta. A ideia fundamental é que os fatores de um número *n* não podem ser recuperados apenas a partir de *n*, devido à dificuldade de fatorar números inteiros extremamente grandes.

Cifração: dada uma chave pública do receptor (*n*, *e*) e o texto simples *M* < *n*, o emissor calcula o texto cifrado como:

$$C = M^e \bmod n \tag{2.1}$$

Decifração: de posse da sua chave privada (*n*,*d*) e o texto cifrado *C*, o receptor calcula o texto simples como:

$$M = C^d \bmod n \tag{2.2}$$

<span id="page-14-0"></span>[Galla](#page-32-7) *et al.* [\(2016\)](#page-32-7) destacam que o RSA oferece dois serviços distintos: confidencialidade e autenticidade.

**Alice Bob**

Figura 2 – Criptografia de chave pública para garantir a confidencialidade.

**chave pública de Bob chave privada de Bob Cifração com RSA Decifração com RSA Texto claro Texto cifrado Texto claro**

Fonte: elaborada pelo autor.

A [Figura 2](#page-14-0) ilustra o uso da criptografia de chave pública para garantir a confidencialidade dos dados. Neste esquema, como a chave pública está acessível a todos, qualquer pessoa pode utilizá-la. O emissor emprega o RSA para cifrar o texto simples utilizando a chave pública de destinatário. Após o processo de cifração, um texto cifrado é gerado. No destino, o receptor obtém o texto claro decifrando a mensagem com sua chave privada. Este processo garante a confidencialidade dos dados.

Para garantir a autenticidade, o processo inverte a ordem do uso das chaves. A [Figura 3](#page-15-0) ilustra o uso da criptografia de chave pública para garantir autenticidade. Neste contexto, o processo de cifração recebe o nome de assinatura e o processo de decifração recebe o nome de verificação da assinatura.

O emissor utiliza a sua chave privada para assinar uma mensagem em texto claro. Ao receber a mensagem assinada, o receptor tenta verificar a assinatura utilizando a chave pública do emissor. Se o processo for bem-sucedido, então a mensagem foi realmente assinada com a chave privada do legítimo emissor. Isso confirma a autenticidade da mensagem, pois apenas o legítimo emissor tem acesso à sua chave privada. Observe que a chave pública do emissor deve ser utilizada obrigatoriamente para decifrar a mensagem, permitindo que o receptor obtenha a mensagem original. Nesse esquema, qualquer pessoa com acesso à chave pública pode decifrar a mensagem, mas o objetivo principal não é ocultar o conteúdo, e sim garantir sua autenticidade.

chave privada
de Alice

Chave pública
de Alice

Mensagem a
ser assinada

Assinatura

Mensagem
assinada

Assinatura

Mensagem
assinada

Assinatura

Mensagem
assinada

Assinatura

Mensagem
assinada

<span id="page-15-0"></span>Figura 3 – Criptografia de chave pública para garantir a autenticidade.

Fonte: elaborada pelo autor.

#### <span id="page-15-1"></span>2.2.3 Código de autenticação de mensagem baseado em função hash

Código de Autenticação de Mensagem (em inglês, *Message Authentication Code* ou MAC), são primitivas criptográficas simétricas que permitem que remetentes e destinatários compartilhando uma chave secreta comum e garantam que o conteúdo de uma mensagem transmitida não foi adulterado (WAGNER, 2008).

Os algoritmos MAC frequentemente se baseiam em funções hash, conforme detalhado por Gauravaram (2007), que descreve as funções hash como primitivas criptográficas capazes de mapear uma mensagem de tamanho arbitrário para uma string de tamanho fixo, conhecida como código hash ou resumo. O código hash é uma representação única da mensagem (PAAR; PELZL, 2009). As funções hash auxiliam na obtenção de alguns objetivos na segurança da informação, como por exemplo, integridade de dados e possibilitar assinaturas digitais. Para exemplificar, Kotzanikolaou e Douligeris (2007) demonstram uma forma básica de um MAC, denotada como:

$$MAC = \mathcal{H}(m,k)$$
 (2.3)

em que:

- *MAC* = código de autenticação de mensagem.
- $\mathcal{H}$  = função hash criptográfica.
- m = mensagem de entrada.
- k = chave secreta compartilhada.

O MAC é o resultado de uma função hash em que, geralmente, a entrada consiste na concatenação da mensagem de entrada *m* com uma chave secreta *k*. Essa função permite gerar, de maneira unidirecional, uma identificação unívoca para a mensagem. Na prática, o MAC é enviado junto com a mensagem por meio de um canal seguro. Como o destinatário possui a mesma chave secreta, ele pode recalcular o MAC usando a mensagem *m* e a chave *k*. Se o MAC calculado pelo destinatário for o mesmo recebido do remetente, então constata-se que a autenticidade e a integridade da mensagem foram preservadas (ISA *[et al.](#page-32-9)*, [2014\)](#page-32-9).

Dentre os diversos tipos de MAC, [Rechberger e Rijmen](#page-34-9) [\(2007\)](#page-34-9) destacam o *Hashbased Message Authentication Code* (HMAC). A escolha do HMAC como um dos algoritmos investigados neste trabalho deve-se à sua ampla adoção em diversas aplicações comerciais, na área da saúde [\(KHEMISSA; TANDJAOUI, 2015\)](#page-32-3) e no contexto industrial [\(DUKA](#page-31-9) *et al.*, [2018\)](#page-31-9).

Conforme descrito por [Stallings](#page-35-8) [\(2014\)](#page-35-8), o HMAC apresenta diversas características que o tornam uma opção atraente em comparação a outros métodos de autenticação de mensagens. Dentre elas, destaca-se a facilidade de implementação, sem a necessidade de modificações significativas, uma vez que utiliza as funções hash já disponíveis. Além disso, o HMAC permite uma substituição simples da função hash incorporada, caso surjam necessidades de maior segurança ou desempenho. No entanto, a solidez criptográfica da autenticação depende da força criptográfica da função hash utilizada.

O esquema de funcionamento geral do HMAC é ilustrado na [Figura 4.](#page-17-0) Antes de um aprofundamento em sua operação, considere os seguintes termos relevantes:

- H = função hash embutida (por exemplo, SHA-1 ou SHA-256);
- *IV* = entrada de valor inicial para função hash;
- *M* = mensagem de entrada (incluindo o preenchimento especificado na função hash embutida);
- *Y<sup>i</sup>* = i-ésimo bloco de M, 0 ≤ *i* ≤ (*L*−1);
- *L* = número de blocos em *M*;
- *b* = número de bits em um bloco;
- *n* = tamanho do código hash produzido pela função hash embutida;
- *K* = chave secreta; recomenda-se ≥ *n*; se o tamanho da chave for maior que *b*, a chave é entrada para a função de hash para produzir uma chave de *n* bits;
- *K* <sup>+</sup> = *K* preenchido com zeros à esquerda de modo que o resultado tenha *b* bits de extensão;

- *ipad* = 00110110 (36 em hexadecimal) repetido *b*/8 vezes;
- *opad* = 01011100 (5C em hexadecimal) repetido *b*/8 vezes.

Portanto, o algoritmo HMAC é definido da seguinte forma:

$$HMAC(K,M) = \mathcal{H}\left[ (K \oplus opad) || \mathcal{H}\left[ (K \oplus ipad) || M \right] \right]$$
 (2.4)

<span id="page-17-0"></span>Figura 4 – Uso do HMAC para aplicação de autenticidade.

![](_page_17_Figure_6.jpeg)

Fonte: adaptada de [Stallings](#page-35-8) [\(2014\)](#page-35-8)

O algoritmo ilustrado na [Figura 4](#page-17-0) pode ser descrito de forma clara e concisa da seguinte maneira:

- 1. Adicione zeros à extremidade esquerda de *K* para criar uma sequência de *b* bits *K* <sup>+</sup>. Por exemplo, se *K* tiver 160 bits e *b* = 512, então *K* será complementado com 352 bits zeros.
- 2. Faça o XOR (OU exclusivo bit a bit) de *K* <sup>+</sup> com *ipad* para produzir o bloco *S<sup>i</sup>* de *b* bits.

- 3. Anexe *M* a *S<sup>i</sup>* .
- 4. Aplique H ao bloco de dados gerado na etapa 3.
- 5. Faça o XOR de *K* <sup>+</sup> com *opad* para produzir o bloco *S<sup>o</sup>* de *b* bits.
- 6. Anexe o resultado de H da etapa 4 a *So*.
- 7. Aplique H ao fluxo gerado na etapa 6 e retorne o resultado.

### <span id="page-18-0"></span>*2.2.4 Autenticação baseada em desafio-resposta*

O conceito de Prova de Conhecimento Zero (em inglês, *Zero-knowledge Proof* - ZKP) foi introduzido por [GOLDWASSER](#page-32-10) *et al.* [\(1989\)](#page-32-10). Um sistema ZKP é um protocolo que permite a uma parte, chamada de *provador*, provar que uma determinada afirmação é verdadeira para outra parte, chamada de *verificador*, mas sem revelar qualquer informação que não seja a validade da afirmação. Nestes sistemas, de acordo com [Pieprzyk](#page-34-10) *et al.* [\(2013\)](#page-34-10), as partes interagem e, no final da interação, o verificador é convencido de que a declaração é verdadeira ou descobre que a declaração não é verdadeira.

A interação consiste em várias rodadas de troca de informações entre o provador e o verificador. Cada rodada é composta por três movimentos, que são três mensagens chamadas *compromisso*, *desafio* e *resposta*. Inicialmente, o comprovante gera uma primeira mensagem (compromisso), que é a declaração a ser provada e a envia para o verificador. Em seguida, o verificador escolhe aleatoriamente um desafio e o envia para o provador. Por fim, o comprovante calcula a resposta com base no desafio e a envia para o verificador [\(TOMAZ](#page-35-1) *et al.*, [2020\)](#page-35-1). A [Figura 5](#page-19-0) representa a interação em um protocolo ZKP genérico.

A ideia é que, em uma prova de conhecimento zero, o provador deve convencer o verificador de que uma determinada afirmação α pertence a uma linguagem *L* da classe NP, sem revelar nenhuma informação adicional além do fato de que tal afirmação pertence a *L*. De maneira geral, as afirmações que o provador deseja provar na prática podem ser representadas como um problema de pertinência em linguagens NP [\(GOLDREICH, 2007\)](#page-32-11).

Problemas NP (*Nondeterministic Polynomial Time*) são um conjunto de problemas de decisão para os quais uma solução candidata (chamada de testemunha ou prova) pode ser verificada em tempo polinomial por um verificador determinístico. Portanto, a classe de complexidade NP está associada a um tipo de problema computacional cuja solução, uma vez fornecida, permite verificar sua validade de forma eficiente [\(SMART, 2016\)](#page-35-9). Em outras palavras, embora não se conheçam algoritmos eficientes (algoritmos de tempo polinomial) para resolver

Figura 5 – Protocolo genérico interativo ZKP.

<span id="page-19-0"></span>![](_page_19_Figure_2.jpeg)

Fonte: adaptada de Tomaz (2021).

problemas **NP**, dado uma instância do problema  $\alpha$  e uma testemunha  $\omega$ , é possível verificar em tempo polinomial se  $\omega$  é de fato uma solução válida para  $\alpha$ .

Um protocolo de prova de conhecimento zero deve satisfazer três propriedades (SMART, 2016).

- 1. **Completude:** é a capacidade do provador convencer o verificador que certas declarações são verdadeiras, desde que o provador tenha uma prova disso.
- 2. **Solidez:** é a capacidade do verificador de se proteger de ser convencido de declarações falsas, exceto com uma probabilidade muito pequena.
- 3. **Conhecimento zero:** nenhum verificador malicioso pode obter conhecimento extra a partir da interação, isto é, a interação nada produz além do fato de a afirmação ser verdadeira.

Uma variação não interativa do ZKP, chamada de *Non-Interactive Zero-Knowledge Proof* (NIZKP), foi proposta por Santis *et al.* (1988). Essa abordagem consiste em um único fluxo de prova do provador para o verificador, após uma fase inicial de configuração confiável. De acordo com Tong *et al.* (2024), a principal vantagem desse método é que o provador pode pré-gerar uma prova e reutilizá-la em vários cenários, eliminando a necessidade de interação contínua com o verificador. Essa abordagem é adequada para cenários em que a interação não é viável ou não é desejada.

Para transformar um protocolo interativo (ZKP) em um formato não interativo

(NIZKP), uma técnica comum é a heurística de Fiat-Shamir (FIAT; SHAMIR, 1986), em que os desafios do verificador ao provador são substituídos por uma saída uniformemente aleatória, que na prática é uma função de hash criptográfica. Neste trabalho, a transformação de um ZKP interativo em um ZKP não interativo é realizada aplicando a heurística Fiat-Shamir. Para isso, é fundamental empregar uma função hash criptográfica  $\mathcal{H}$ . O provador calcula suas mensagens como faria no protocolo interativo, mas o desafio  $\sigma$ , em vez de escolhido pelo verificador, é substituído por um valor hash, conforme ilustrado na Figura 6.

<span id="page-20-0"></span>Figura 6 – Transformação de ZKP em NIZKP usando a heurística Fiat-Shamir

![](_page_20_Figure_3.jpeg)

Fonte: adaptada de Tomaz (2021)

Nesta abordagem, a aplicação do NIZKP envolve uma transmissão unidirecional da prova, acrescida da mensagem de compromisso do provador  $\mathcal P$  para o verificador  $\mathcal V$ , sem interação adicional. Ou seja, nenhuma verificação adicional precisa ser feita pelo verificador além da prova. A transformação de ZKP em NIZKP usando a heurística Fiat-Shamir ocorre pelo seguinte protocolo:

- 1.  $\mathcal{P}$  calcula o compromisso  $\delta$  a partir da declaração  $\alpha$  e da testemunha  $\omega$ .
- 2.  $\mathcal{P}$  calcula o desafio  $\sigma$  usando a função hash  $\mathcal{H}$ , que recebe como entrada  $\sigma$  e  $\delta$ .
- 3.  $\mathcal{P}$  calcula a prova  $\pi$  usando  $\alpha$ ,  $\omega$ , e  $\sigma$ , e então envia  $\pi$  e  $\delta$  para  $\mathcal{V}$ .
- 4.  $\mathcal{V}$  calcula  $\sigma$ , da mesma forma que  $\mathcal{P}$ , usando  $\mathcal{H}$ , que recebe como entrada  $\alpha$  e  $\delta$ .
- 5. V verifica a prova e decide se aceita ou rejeita.

Como mencionado anteriormente, para construir qualquer ZKP é necessário selecionar um problema matemático da classe **NP** que forme sua base. Entre os problemas **NP** mais

comuns que podem ser usados para construir uma prova de conhecimento zero, está o tradicional problema do logaritmo discreto. O protocolo ZKP baseado no problema do logaritmo discreto foi proposto por [Schnorr](#page-34-12) [\(1991\)](#page-34-12).

Para implementar o sistema NIZKP utilizado neste trabalho, foi empregada uma variação do protocolo de Schnorr baseada em curvas elípticas, mais especificamente no problema do logaritmo discreto sobre curvas elípticas (*Elliptic Curve Discrete Logarithm Problem* - ECDLP), que foi padronizado na RFC 8235 [\(HAO, 2017\)](#page-32-12).

### <span id="page-21-0"></span>2.3 Autenticação em cenários críticos da indústria que dispensam confidencialidade

Em alguns cenários específicos, é prescindível a aplicação da propriedade da confidencialidade em mecanismos criptográficos. Para exemplificar, Liu *[et al.](#page-33-8)* [\(2007\)](#page-33-8) defende no seu trabalho sobre Redes Ad Hoc Veiculares (*Vehicular Ad Hoc Networks* - VANETs), que devido à natureza das mensagens de segurança não serem sensíveis, prioriza-se a autenticação segura em detrimento da confidencialidade. A legitimidade das mensagens no contexto apontado é obrigatória para proteger as VANETs de invasores, bem como de *insiders* mal-intencionados.

Em outra abordagem conduzida por Shi *[et al.](#page-34-13)* [\(2012\)](#page-34-13), foi introduzido o esquema de Autenticação de Rede Corporal (*Body Area Network Authentication* - BANA). Os BANAs são caracterizados como nós sensores vestíveis leves, compactos e de baixo consumo de energia. Dentro desse cenário, os autores optaram por adotar um método de autenticação mais confiável, ao invés de mecanismos de autenticação que utilizam a distribuição de chaves. Essa escolha, que dispensou a aplicação de confidencialidade, resultou em economia de recursos e atendeu aos requisitos de legitimidade no contexto discutido.

De forma análoga, em situações específicas da Indústria 4.0, observa-se que os sistemas ciberfísicos, que interagem diretamente com infraestrutura crítica, em aplicações como energia, água e transporte, geralmente não utilizam criptografia para suas mensagens de controle. Isso ocorre porque os sistemas de computador que se conectam a dispositivos físicos estão sujeitos a restrições rigorosas de tempo real, e é amplamente assumido que os custos computacionais da criptografia são muito altos em tais situações [\(HUNTER](#page-32-13) *et al.*, [2017\)](#page-32-13). Portanto, em situações críticas na Indústria 4.0 que dispensam a necessidade de confidencialidade, como em mensagens de alerta [\(JIN; SONG, 2014\)](#page-32-14), de controle ou afins, apenas a autenticação é exigida.

### <span id="page-22-0"></span>3 TRABALHOS RELACIONADOS

Este capítulo apresenta uma revisão da literatura relevante para o presente estudo. Inicialmente, serão examinadas as pesquisas empíricas que investigaram mecanismos de autenticação em dispositivos com recursos computacionais limitados, no contexto da Indústria 4.0. Em seguida, será apresentada uma análise comparativa das referências consultadas, com o objetivo de destacar a lacuna de pesquisa que este estudo se propõe a preencher.

[Suárez-Albela](#page-35-12) *et al.* [\(2018\)](#page-35-12) em um estudo comparativo focado em segurança na camada de transporte no contexto de redes de IoT, realizaram uma avaliação do protocolo TLS (*Transport Layer Security*) utilizando a implementação de dois algoritmos. Inicialmente, os autores utilizaram o TLS baseado em RSA, posteriormente aplicaram o TLS baseado em Criptografia de Curva Elíptica (*Elliptic Curve Cryptography* - ECC). O algoritmo RSA foi empregado devido à sua preferência em termos de segurança. Os resultados foram então comparados com uma abordagem amplamente empregada em dispositivos com recursos limitados, o algoritmo ECC. Os resultados obtidos do experimento foram os seguintes:

- Para chaves RSA de 1024 bits, o consumo de energia foi de 17.86 mWh, enquanto para chaves ECC de 192 bits, o consumo foi de 9.05 mWh.
- Para chaves RSA de 2048 bits, o consumo de energia foi de 21.55 mWh, enquanto para chaves ECC de 224 bits, o consumo foi de 17.38 mWh.
- Continuando os testes, chaves RSA de 3072 bits consumiram 56.78 mWh, enquanto chaves ECC de 256 bits consumiram 15.43 mWh.

Os experimentos demonstraram que o TLS baseado em ECC supera o TLS baseado em RSA em termos de eficiência energética.

Em outro trabalho, [El-Hajj](#page-31-11) *et al.* [\(2023\)](#page-31-11) realizaram uma pesquisa visando identificar os algoritmos mais eficientes e seguros para uso em dispositivos com recursos limitados, como dispositivos IoT. Realizou-se uma avaliação abrangente de algoritmos criptográficos leves conhecidos, com o objetivo de comparar cifras simétricas. Os resultados dessa avaliação foram obtidos por meio da implementação em software dos algoritmos selecionados, executados no microcontrolador ATMEGA328P-Arduino (Uno) e no Raspberry Pi. As implementações das cifras de bloco foram analisadas em termos de velocidade, custo computacional e eficiência energética durante a cifração e decifração para diferentes tamanhos de bloco e chave.

Em termos de uso de recursos computacionais, dentre cinco algoritmos simétricos avaliados, estes apresentaram os seguintes consumos de memória ROM no Arduino:

- Para o algoritmo Prince-128, com chave de 128 bits, o consumo foi de 13,7 KB.
- Para o algoritmo AES-192, com chave de 192 bits, o consumo foi de 13,9 KB.
- Para o algoritmo AES-256, com chave de 256 bits, o consumo foi de 14,2 KB.
- Para o algoritmo Rectangle-128, chave de 128 bits, o consumo foi de 16,3 KB.
- Para o algoritmo Piccolo-80, com chave de 80 bits, o consumo foi de 21 KB.

Este experimento demonstrou, dentro do cenário apresentado, que mesmo quando comparado com outros algoritmos da mesma família simétrica, os algoritmos AES-192 e o AES-256 destacaram-se de forma performática, consumindo menos memória que outros.

[Eldefrawy](#page-31-12) *et al.* [\(2018\)](#page-31-12) conduziram um experimento para estabelecer canais seguros e trocar credenciais de segurança entre os componentes de uma infraestrutura IoT em aplicações industriais (IIoT), considerando dois mecanismos de autenticação diferentes. Para construir o ambiente operacional do experimento, os pesquisadores empregaram o sistema operacional Contiki OS e o microcontrolador MSP430, utilizando o simulador de hardware MSPSim. Essa abordagem possibilitou uma análise detalhada do esquema de gerenciamento de chaves proposto, especialmente adaptado para o ambiente de IIoT. Após os testes verificaram-se os seguintes resultados em relação ao consumo energético:

- Para o SHA-224, com chave de 224 bits, o consumo energético foi de 56 µJ.
- Para o SHA-256, com chave de 256 bits, o consumo energético foi de 56 µJ.
- Para o HMAC-SHA-256, com chave de 256 bits, o consumo energético foi de 97,83 µJ.
- Para o ECC-159, com chave de 159 bits, o consumo energético foi de 2300 µJ.

Após a análise desses resultados, conclui-se que o algoritmo HMAC-SHA256 apresenta uma vantagem significativa em eficiência energética em comparação com o ECC-159, embora ainda seja superado pelo SHA-224 e SHA-256.

[Tomaz](#page-35-1) *et al.* [\(2020\)](#page-35-1) realizaram uma pesquisa que explorou a autenticação baseada em Prova de Conhecimento Zero Não Interativas (NIZKP) em dispositivos *mobile health* com severas restrições de recursos, demonstrando a viabilidade deste esquema de autenticação em dispositivos com apenas 2 KB de memória RAM.

Os artigos anteriormente mencionados focaram na aplicação isolada do HMAC ou NIZKP, bem como na comparação do AES e RSA como mecanismos de autenticação para dispositivos com restrição de recursos. No entanto, ainda não há na literatura uma análise comparativa abrangente envolvendo esses quatro esquemas de autenticação no mesmo ambiente de implementação. Em um cenário de IoT da Indústria 4.0, por exemplo, frequentemente existem vários dispositivos com consideráveis restrições de recursos. Esta revisão da literatura indica que não há um estudo que avalie e compare todos esses importantes algoritmos que podem ser aplicados na Indústria 4.0. Portanto, existe uma lacuna que requer uma investigação empírica mais abrangente, comparando o desempenho dos algoritmos RSA, AES, HMAC e NIZKP considerando as limitações computacionais e energéticas dos dispositivos.

### <span id="page-25-0"></span>4 ESTUDO EMPÍRICO

Nesta seção, são descritos os procedimentos metodológicos adotados para esta pesquisa, incluindo o desenho metodológico. Em seguida, é apresentada uma seção com os resultados preliminares obtidos por meio de um experimento computacional.

### <span id="page-25-1"></span>4.1 Procedimentos metodológicos

Este trabalho se caracteriza como uma pesquisa de natureza aplicada e do tipo descritiva. Seu objetivo é realizar uma análise comparativa entre os mecanismos de autenticação criptográficos RSA, AES, HMAC e NIZKP. Assim, busca-se determinar qual desses mecanismos de autenticação consome menos recursos computacionais, considerando o tempo de processamento, o consumo de memória e o gasto energético.

A partir das pesquisas de [Martín-Fernández](#page-33-9) *et al.* [\(2016\)](#page-33-9), [Walshe](#page-35-13) *et al.* [\(2019\)](#page-35-13), [Tomaz](#page-35-1) *et al.* [\(2020\)](#page-35-1) e outros estudos neste contexto, propõe-se a seguinte hipótese: *o mecanismo de autenticação NIZKP demanda uma quantidade menor de recursos computacionais em comparação com métodos de autenticação convencionais, como aqueles baseados em cifras simétricas, cifras assimétricas e MACs*.

Esta hipótese pode ser justificada pelos resultados satisfatórios descritos pelos autores dos trabalhos acima mencionados. Esses estudos aplicam o NIZKP em cenários com dispositivos IoT que possuem restrições de recursos, e, mesmo assim, consideraram o mecanismo de autenticação NIZKP viável e satisfatório.

Na presente pesquisa, que adota uma abordagem estritamente quantitativa, delineouse um escopo metodológico por meio de um experimento computacional. O experimento baseia-se na avaliação do desempenho dos mecanismos de autenticação acima mencionados em dispositivos IoT com restrições de recursos computacionais. A implementação dos algoritmos utiliza a plataforma de prototipagem Arduino Nano [1](#page-25-2) para representar os dispositivos de baixo poder computacional empregados na Indústria 4.0.

Conforme ilustrado na [Figura 7,](#page-26-0) esta pesquisa adota um processo metodológico composto por seis passos fundamentais. No Passo 1 (indicado em azul), procedeu-se à definição das variáveis independentes, representadas pelos algoritmos integrantes do experimento: RSA, HMAC, AES e NIZKP+ECDLP. Esses algoritmos foram selecionados devido à sua ampla adoção

<span id="page-25-2"></span><sup>1</sup> https://store.arduino.cc/products/arduino-nano

PASSO 1 PASSO 2 PASSO 3 Definição de Variáveis Independentes Definição de Variáveis Dependentes Definição de Grupos de Controle e Experimental GRUPO DE CONTROLE: RSA, HMAC, AES TEMPO DE PROCESSAMENTO, MEMÓRIA RSA, HMAC, AES E (NIZKP + ECDLP) GRUPO EXPERIMENTAL : NIZKP + ECDLP Experimento 1 PASSO 4 Experimento 2 Experimento 3 PASSO 5 PASSO 6 Análise Comparativa de Dados OS RESULTADOS OBTIDOS DE CADA ALGORITMO SERÃO COMPARADOS, INCLUINDO NIZKP (GRUPO EXPERIMENTAL), COM OS GRUPOS DE CONTROLE (RSA, AES E HMAC) SERÃO CONDUZIDOS COM OS ALGORITMOS PARA COLETAR OS VALORES DAS VARIÁVEIS DEPENDENTES

<span id="page-26-0"></span>Figura 7 – Procedimentos metodológicos

Fonte: elaborada pelo autor.

em diversas aplicações comerciais, na área da saúde e no contexto industrial, como evidenciado nos Capítulos 2 e 3.

Conforme comentado na Seção 2.2.4, um sistema de prova de conhecimento zero depende de um problema computacional da classe **NP**. Assim, nesta pesquisa, o problema de base escolhido foi o problema do logaritmo discreto sobre curvas elípticas (*Elliptic Curve Discrete Logarithm Problem* - ECDLP), que foi padronizado em Hao (2017), o que será denotado aqui por NIZKP+ECDLP.

No **Passo 2** (indicado em cinza), foram definidas as variáveis dependentes, que incluem o tempo de processamento, a utilização de memória e o consumo de energia. A escolha cuidadosa dessas variáveis baseia-se nos desafios relacionados à capacidade computacional limitada, restrições de energia e limitações no tamanho da memória de dispositivos IoT, conforme detalhado na Seção 1.1.

No **Passo 3** (indicado em amarelo), os grupos de **controle** e **experimental** foram definidos para testar a eficácia comparativa dos algoritmos. O grupo de controle é composto

pelos algoritmos tradicionais RSA, HMAC e AES, enquanto o grupo experimental incluiu o mecanismo NIZKP+ECDLP. A hipótese subjacente é que o NIZKP+ECDLP pode oferecer vantagens significativas em relação aos algoritmos tradicionais, o que será investigado neste estudo. Esta configuração permite uma avaliação objetiva do desempenho do NIZKP+ECDLP em comparação com os métodos estabelecidos.

No Passo 4 (indicado em verde), será realizada a implementação dos testes, os quais serão estruturados em três experimentos distintos. O objetivo desses experimentos é realizar uma análise comparativa entre diversos algoritmos de autenticação, sendo que cada um atuará como controle em relação ao NIZKP+ECDLP. Em resumo, serão conduzidas avaliações de desempenho específicas: no Experimento 1, será feita uma comparação entre NIZKP+ECDLP e RSA; no Experimento 2, o NIZKP+ECDLP será comparado com o AES; e, por fim, no Experimento 3, o NIZKP+ECDLP será confrontado com o algoritmo HMAC. Esse planejamento experimental possibilitará uma avaliação abrangente dos algoritmos selecionados, evidenciando suas eficiências e limitações individuais.

No Passo 5 (indicada em lilás), será realizada uma série específica de iterações entre o dispositivo emissor e o dispositivo receptor, visando aprimorar a consistência dos resultados e reduzir a influência de possíveis erros aleatórios. Para essas interações, serão registrados detalhadamente as condições experimentais, a definição das tarefas, os parâmetros de segurança dos algoritmos em teste e as configurações do Arduino Nano, como dispositivo emissor, e do ESP32, como dispositivo receptor. Esse procedimento visa garantir a reprodutibilidade dos resultados e uma análise mais sólida dos efeitos de possíveis variações nos resultados esperados. Durante essas interações, serão feitas as coletas dos valores das variáveis dependentes, em que o tempo de processamento será registrado com precisão em milissegundos (ms), a utilização de memória será medida em kilobytes (KB), e o consumo de energia em milijoule (mJ). Esses registros detalhados fornecerão informações importantes para uma análise completa do desempenho de cada algoritmo.

No Passo 6 (indicada em roxo), será realizada a análise dos dados obtidos anteriormente. Essa análise comparativa dos resultados terá como base as variáveis dependentes. Serão comparados os resultados de cada algoritmo do grupo controle com o NIZKP+ECDLP, considerando as métricas definidas. Com base nesses resultados, será possível determinar qual algoritmo apresentou melhor desempenho.

### <span id="page-28-0"></span>4.2 Resultados preliminares

Para obter alguns resultados preliminares, realizou-se um breve experimento para verificar a viabilidade de usar o NIZKP em um Arduino Nano. Neste experimento, mediu-se os valores das seguintes variáveis dependentes em 30 execuções do NIZKP, focando no processo de geração de chaves (pares de chaves pública e privada): alocação de memória, consumo de energia e tempo de processamento computacional. Para o ambiente experimental, utilizamos o Arduino Nano equipado com 32 KB de memória Flash ROM, 2 KB de memória SRAM e um processador ATmega328 operando a 16 MHz. Além disso, utilizamos o módulo Bluetooth HM-10 para comunicação entre o Arduino e um smartphone Android 10 equipado com processador octa-core Snapdragon 632 e 2GB de RAM. Além disso, utilizamos o BetterTools [\(BETTERTOOLS, 2023\)](#page-31-13), que foi explorado para enviar comandos e interagir com a placa Arduino. Todo o código-fonte está disponível em nosso repositório de suporte[2](#page-28-1) .

Para estimar o consumo de energia, utilizou-se a seguinte equação, que também foi adotada por outros estudos [\(CHATZIGIANNAKIS](#page-31-14) *et al.*, [2011;](#page-31-14) MA *[et al.](#page-33-10)*, [2014;](#page-33-10) [MOOSAVI](#page-33-11) *et [al.](#page-33-11)*, [2016;](#page-33-11) LI *[et al.](#page-33-12)*, [2017\)](#page-33-12):

$$E = V \cdot I \cdot t,$$

em que:

- *E* é o consumo de energia em milijoules (*mJ*),
- *V* é a tensão de operação em volts (*V*),
- *I* é a corrente em miliampères (*mA*),
- *t* é o tempo em segundos de cada operação.

De acordo com o documento técnico da Arduino[3](#page-28-2) , o Arduino Nano consome 19 mA em uma voltagem de 5V. Além disso, como mencionado anteriormente, um módulo Bluetooth[4](#page-28-3) BLE V4.0 HM-10 foi usado para comunicação entre o Arduino e o Smartphone. Portanto, quando aplicada à equação anterior, temos:

$$E = 5 \cdot (19 + 4.8) \cdot t$$

onde 19 mA é a corrente elétrica do Arduino Nano, e 4,8 mA refere-se à corrente elétrica do módulo Bluetooth HM-10 no modo ativo. Sobre o consumo de memória, o terminal de saída

<span id="page-28-1"></span><sup>2</sup> Repositório de código-fonte: [<https://github.com/joe-sousa/nizkp\\_algorithm>](https://github.com/joe-sousa/nizkp_algorithm)

<span id="page-28-2"></span><sup>3</sup> Documentação da Arduino: [<https://store.arduino.cc/usa/arduino-nano>](https://store.arduino.cc/usa/arduino-nano)

<span id="page-28-3"></span><sup>4</sup> Documentação do módulo Bluetooth: [<https://seeeddoc.github.io/BLE\\_Bee/res/Bluetooth40\\_en.pdf>](https://seeeddoc.github.io/BLE_Bee/res/Bluetooth40_en.pdf)

integrado ao IDE do Arduino fornece informações sobre a alocação de memória necessária para o armazenamento do código NIZKP+ECDLP na memória ROM e o uso da memória RAM durante sua execução, conforme informado a seguir.

A Figura [8](#page-29-0) ilustra o comportamento do NIZKP durante o processo de geração de chaves, destacando o consumo de energia (em mJ) e o tempo de processamento computacional (em ms). Essa análise preliminar do tempo de processamento computacional revelou que o NIZKP requeriu uma média de 3739,07 ms, com um desvio padrão de 3,86 ms. Em relação ao consumo de energia, observamos uma média de 514,12 mJ, com um desvio padrão de 0,53 mJ. Por fim, observamos que o NIZKP alocou 25832 bytes de memória Flash ROM, representando 84% do espaço de memória Flash disponível (30720 bytes). O NIZKP utilizou 766 bytes de memória SRAM dinâmica, correspondendo a 37% do espaço total disponível (2048 bytes). Portanto, podemos concluir que o NIZKP foi implementado com sucesso e obteve resultados promissores, mesmo considerando o cenário de recursos limitados do Arduino Nano.

<span id="page-29-0"></span>

Figura 8 – Estimativa de consumo de tempo e energia para geração de par de chaves no NIZKP.

Fonte: elaborado pelo autor

### <span id="page-30-0"></span>5 CRONOGRAMA E PRÓXIMOS PASSOS

Este Capítulo descreve o cronograma planejado com os passos que serão seguidos para materializar na conclusão desta pesquisa. Logo em seguida, são definidas cada uma das atividades, tal como pode ser visualizado através da tabela 1.

Tabela 1 – Cronograma das próximas atividades

| Atividades                                | Maio | Jun | Jul | Ago | Set | Out |
|-------------------------------------------|------|-----|-----|-----|-----|-----|
| Ajustes no TCC I                          | X    |     |     |     |     |     |
| Finalizar a implementação dos algoritmos  | X    | X   |     |     |     |     |
| Coleta de dados das variáveis dependentes |      |     | X   |     |     |     |
| Análise e comparação de resultados        |      |     |     | X   |     |     |
| Escrita dos resultados                    |      |     |     |     | X   |     |
| Conclusão                                 |      |     |     |     |     | X   |
| Defesa do TCC II                          |      |     |     |     |     | X   |

Fonte: elaborado pelo autor

# REFERÊNCIAS

- <span id="page-31-1"></span><span id="page-31-0"></span>ABOMHARA, M.; KØIEN, G. M. Cyber security and the internet of things: vulnerabilities, threats, intruders and attacks. Journal of Cyber Security and Mobility, p. 65–88, 2015.
- <span id="page-31-5"></span>ALIZAI, Z. A.; TAREEN, N. F.; JADOON, I. Improved iot device authentication scheme using device capability and digital signatures. In: IEEE. 2018 International conference on applied and engineering mathematics (ICAEM). [S.l.], 2018. p. 1–5.
- <span id="page-31-2"></span>ALNAHARI, W.; QUASIM, M. T. Authentication of iot device and iot server using security key. In: IEEE. 2021 International Congress of Advanced Technology and Engineering (ICOTEN). [S.l.], 2021. p. 1–9.
- <span id="page-31-6"></span>AUMASSON, J.-P. Serious cryptography: a practical introduction to modern encryption. [S.l.]: No Starch Press, 2017.
- <span id="page-31-13"></span>BETTERTOOLS. Bluetooth Terminal eDebugger. 2023. Disponível em Google Play Store. [<https://play.google.com/store/apps/details?id=com.e.debugger>.](https://play.google.com/store/apps/details?id=com.e.debugger)
- <span id="page-31-8"></span>BOLFING, A. Cryptographic Primitives in Blockchain Technology: A Mathematical Introduction. [S.l.]: Oxford University Press, USA, 2020.
- <span id="page-31-14"></span>CHATZIGIANNAKIS, I.; PYRGELIS, A.; SPIRAKIS, P. G.; STAMATIOU, Y. C. Elliptic curve based zero knowledge proofs and their applicability on resource constrained devices. In: IEEE. 2011 IEEE eighth international conference on mobile ad-hoc and sensor systems. [S.l.], 2011. p. 715–720.
- <span id="page-31-3"></span>DELFS, H.; KNEBL, H.; KNEBL, H. Introduction to cryptography: Principles and Applications. [S.l.]: Springer, 2002. v. 2.
- <span id="page-31-4"></span>DELGADO-VARGAS, K. A.; GALLEGOS-GARCIA, G.; ESCAMILLA-AMBROSIO, P. J. Cryptographic protocol with keyless sensors authentication for wban in healthcare applications. Applied Sciences, v. 13, n. 3, 2023. ISSN 2076-3417. Disponível em: [<https://www.mdpi.com/2076-3417/13/3/1675>.](https://www.mdpi.com/2076-3417/13/3/1675)
- <span id="page-31-7"></span>DIFFIE, W.; HELLMAN, M. E. New directions in cryptography. In: Democratizing Cryptography: The Work of Whitfield Diffie and Martin Hellman. [S.l.: s.n.], 2022. p. 365–390.
- <span id="page-31-9"></span>DUKA, A.-V.; GENGE, B.; HALLER, P. Enabling authenticated data exchanges in industrial control systems. In: IEEE. 2018 6th International Symposium on Digital Forensic and Security (ISDFS). [S.l.], 2018. p. 1–5.
- <span id="page-31-11"></span>EL-HAJJ, M.; MOUSAWI, H.; FADLALLAH, A. Analysis of lightweight cryptographic algorithms on iot hardware platform. Future Internet, MDPI, v. 15, n. 2, p. 54, 2023.
- <span id="page-31-12"></span>ELDEFRAWY, M. H.; PEREIRA, N.; GIDLUND, M. Key distribution protocol for industrial internet of things without implicit certificates. IEEE Internet of Things Journal, IEEE, v. 6, n. 1, p. 906–917, 2018.
- <span id="page-31-10"></span>FIAT, A.; SHAMIR, A. How to prove yourself: Practical solutions to identification and signature problems. In: SPRINGER. Conference on the theory and application of cryptographic techniques. [S.l.], 1986. p. 186–194.

- <span id="page-32-7"></span>GALLA, L. K.; KOGANTI, V. S.; NUTHALAPATI, N. Implementation of rsa. In: IEEE. 2016 International Conference on Control, Instrumentation, Communication and Computational Technologies (ICCICCT). [S.l.], 2016. p. 81–87.
- <span id="page-32-0"></span>GARDAŠEVIC, G.; VELETI ´ C, M.; MALETI ´ C, N.; VASILJEVI ´ C, D.; RADUSINOVI ´ C, I.; ´ TOMOVIC, S.; RADONJI ´ C, M. The iot architectural framework, design issues and application ´ domains. Wireless personal communications, Springer, v. 92, p. 127–148, 2017.
- <span id="page-32-8"></span>GAURAVARAM, P. Cryptographic hash functions: cryptanalysis, design and applications. Tese (Doutorado) — Queensland University of Technology, 2007.
- <span id="page-32-6"></span>GHORADKAR, S.; SHINDE, A. Review on image encryption and decryption using aes algorithm. International Journal of Computer Applications, Citeseer, v. 975, p. 8887, 2015.
- <span id="page-32-11"></span>GOLDREICH, O. Foundations of Cryptography: Volume 1, Basic Tools. Cambridge University Press, 2007. ISBN 9781139430234. Disponível em: [<https://books.google.com.br/](https://books.google.com.br/books?id=Z_OweRm7sD8C) [books?id=Z\\_OweRm7sD8C>.](https://books.google.com.br/books?id=Z_OweRm7sD8C)
- <span id="page-32-10"></span>GOLDWASSER, S.; MICALI, S.; RACKOFF, C. The knowledge complexityof interactive proof systems. SIAM J. COMPUT, v. 18, n. 1, p. 186–208, 1989.
- <span id="page-32-12"></span>HAO, F. Schnorr non-interactive zero-knowledge proof. [S.l.], 2017.
- <span id="page-32-4"></span>HUANG, T. Development of small-scale intelligent manufacturing system (SIMS). A case study at Stella Polaris AS. Dissertação (Mestrado) — UiT Norges arktiske universitet, 2017.
- <span id="page-32-13"></span>HUNTER, D.; PARRY, J.; RADKE, K.; FIDGE, C. Authenticated encryption for time-sensitive critical infrastructure. In: Proceedings of the Australasian Computer Science Week Multiconference. [S.l.: s.n.], 2017. p. 1–10.
- <span id="page-32-9"></span>ISA, M. A. M.; AHMAD, M. M.; SANI, N. F. M.; HASHIM, H.; MAHMOD, R. Cryptographic key exchange protocol with message authentication codes (mac) using finite state machine. Procedia Computer Science, Elsevier, v. 42, p. 263–270, 2014.
- <span id="page-32-2"></span>JAN, M. A.; KHAN, F.; ALAM, M.; USMAN, M. A payload-based mutual authentication scheme for internet of things. Future Generation Computer Systems, Elsevier, v. 92, p. 1028–1039, 2019.
- <span id="page-32-1"></span>JAN, M. A.; NANDA, P.; HE, X.; TAN, Z.; LIU, R. P. A robust authentication scheme for observing resources in the internet of things environment. In: IEEE. 2014 IEEE 13th International Conference on Trust, Security and Privacy in Computing and Communications. [S.l.], 2014. p. 205–211.
- <span id="page-32-5"></span>JAYAKUMAR, H.; LEE, K.; LEE, W. S.; RAHA, A.; KIM, Y.; RAGHUNATHAN, V. Powering the internet of things. In: Proceedings of the 2014 international symposium on Low power electronics and design. [S.l.: s.n.], 2014. p. 375–380.
- <span id="page-32-14"></span>JIN, D.; SONG, J. A traffic flow theory aided physical measurement-based sybil nodes detection mechanism in vehicular ad-hoc networks. In: IEEE. 2014 IEEE/ACIS 13th International Conference on Computer and Information Science (ICIS). [S.l.], 2014. p. 281–286.
- <span id="page-32-3"></span>KHEMISSA, H.; TANDJAOUI, D. A lightweight authentication scheme for e-health applications in the context of internet of things. In: IEEE. 2015 9th International Conference on Next Generation Mobile Applications, Services and Technologies. [S.l.], 2015. p. 90–95.

- <span id="page-33-7"></span>KOTZANIKOLAOU, P.; DOULIGERIS, C. Cryptography primer: Introduction to cryptographic principles and algorithms. Network Security: Current Status and Future Directions, Edited by C. Douligeris and DN Serpanos, IEEE Press, p. 459–479, 2007.
- <span id="page-33-3"></span>KRISHNA, R. R.; PRIYADARSHINI, A.; JHA, A. V.; APPASANI, B.; SRINIVASULU, A.; BIZON, N. State-of-the-art review on iot threats and attacks: Taxonomy, challenges and solutions. Sustainability, MDPI, v. 13, n. 16, p. 9463, 2021.
- <span id="page-33-12"></span>LI, F.; HONG, J.; OMALA, A. A. Efficient certificateless access control for industrial internet of things. Future Generation Computer Systems, Elsevier, v. 76, p. 285–292, 2017.
- <span id="page-33-8"></span>LIU, X.; FANG, Z.; SHI, L. Securing vehicular ad hoc networks. In: IEEE. 2007 2nd International Conference on Pervasive Computing and Applications. [S.l.], 2007. p. 424–429.
- <span id="page-33-0"></span>LIU, Y.; MA, X.; SHU, L.; HANCKE, G. P.; ABU-MAHFOUZ, A. M. From industry 4.0 to agriculture 4.0: Current status, enabling technologies, and research challenges. IEEE Transactions on Industrial Informatics, IEEE, v. 17, n. 6, p. 4322–4334, 2020.
- <span id="page-33-2"></span>LOHIYA, R.; THAKKAR, A. Application domains, evaluation data sets, and research challenges of iot: A systematic review. IEEE Internet of Things Journal, IEEE, v. 8, n. 11, p. 8774–8798, 2020.
- <span id="page-33-10"></span>MA, C.; XUE, K.; HONG, P. Distributed access control with adaptive privacy preserving property for wireless sensor networks. Security and Communication Networks, Wiley Online Library, v. 7, n. 4, p. 759–773, 2014.
- <span id="page-33-1"></span>MADAKAM, S.; LAKE, V.; LAKE, V.; LAKE, V. *et al.* Internet of things (iot): A literature review. Journal of Computer and Communications, Scientific Research Publishing, v. 3, n. 05, p. 164, 2015.
- <span id="page-33-4"></span>MARÍN, E. G. *et al.* Secure interaction with iiot nodes using new technologies. Universidad de Granada, 2024.
- <span id="page-33-9"></span>MARTÍN-FERNÁNDEZ, F.; CABALLERO-GIL, P.; CABALLERO-GIL, C. Authentication based on non-interactive zero-knowledge proofs for the internet of things. Sensors, MDPI, v. 16, n. 1, p. 75, 2016.
- <span id="page-33-11"></span>MOOSAVI, S. R.; GIA, T. N.; NIGUSSIE, E.; RAHMANI, A. M.; VIRTANEN, S.; TENHUNEN, H.; ISOAHO, J. End-to-end security scheme for mobility enabled healthcare internet of things. Future Generation Computer Systems, Elsevier, v. 64, p. 108–124, 2016.
- <span id="page-33-5"></span>MUMTAZ, M.; AKRAM, J.; PING, L. An rsa based authentication system for smart iot environment. In: IEEE. 2019 IEEE 21st International Conference on High Performance Computing and Communications; IEEE 17th International Conference on Smart City; IEEE 5th International Conference on Data Science and Systems (HPCC/SmartCity/DSS). [S.l.], 2019. p. 758–765.
- <span id="page-33-6"></span>NGUYEN, K. T.; LAURENT, M.; OUALHA, N. Survey on secure communication protocols for the internet of things. Ad Hoc Networks, Elsevier, v. 32, p. 17–31, 2015.

- <span id="page-34-4"></span>NISSAR, G.; KHAN, R. A.; MUSHTAQ, S.; LONE, S. A.; MOON, A. A lightweight authentication scheme and security key establishment for internet of medical things. In: SPRINGER. International Conference on Computing, Communications, and Cyber-Security. [S.l.], 2022. p. 797–809.
- <span id="page-34-8"></span>PAAR, C.; PELZL, J. Understanding cryptography: a textbook for students and practitioners. [S.l.]: Springer Science & Business Media, 2009.
- <span id="page-34-1"></span>PERWEJ, Y.; HAQ, K.; PARWEJ, F.; MUMDOUH, M.; HASSAN, M. The internet of things (iot) and its application domains. International Journal of Computer Applications, v. 975, n. 8887, p. 182, 2019.
- <span id="page-34-0"></span>PICCAROZZI, M.; AQUILANI, B.; GATTI, C. Industry 4.0 in management studies: A systematic literature review. Sustainability, 2018.
- <span id="page-34-10"></span>PIEPRZYK, J.; HARDJONO, T.; SEBERRY, J. Fundamentals of computer security. [S.l.]: Springer Science & Business Media, 2013.
- <span id="page-34-3"></span>PORAMBAGE, P.; SCHMITT, C.; KUMAR, P.; GURTOV, A.; YLIANTTILA, M. Two-phase authentication protocol for wireless sensor networks in distributed iot applications. In: IEEE. 2014 IEEE Wireless Communications and Networking Conference (WCNC). [S.l.], 2014. p. 2728–2733.
- <span id="page-34-5"></span>PUTHIYIDAM, J. J.; JOSEPH, S.; BHUSHAN, B. Enhanced authentication security for iot client nodes through t-ecdsa integrated into mqtt broker. The Journal of Supercomputing, Springer, p. 1–35, 2023.
- <span id="page-34-7"></span>RAWAL, S. Advanced encryption standard (aes) and it's working. International Research Journal of Engineering and Technology, v. 3, n. 8, p. 1165–1169, 2016.
- <span id="page-34-9"></span>RECHBERGER, C.; RIJMEN, V. On authentication with hmac and non-random properties. In: SPRINGER. Financial Cryptography and Data Security: 11th International Conference, FC 2007, and 1st International Workshop on Usable Security, USEC 2007, Scarborough, Trinidad and Tobago, February 12-16, 2007. Revised Selected Papers 11. [S.l.], 2007. p. 119–133.
- <span id="page-34-6"></span>ROSE, K.; ELDRIDGE, S.; CHAPIN, L. The internet of things: An overview. The internet society (ISOC), Reston, VA, v. 80, p. 1–50, 2015.
- <span id="page-34-2"></span>ROY, S. S.; PUTHAL, D.; SHARMA, S.; MOHANTY, S. P.; ZOMAYA, A. Y. Building a sustainable internet of things: Energy-efficient routing using low-power sensors will meet the need. IEEE Consumer Electronics Magazine, IEEE, v. 7, n. 2, p. 42–49, 2018.
- <span id="page-34-11"></span>SANTIS, A. D.; MICALI, S.; PERSIANO, G. Non-interactive zero-knowledge proof systems. In: SPRINGER. Advances in Cryptology—CRYPTO'87: Proceedings 7. [S.l.], 1988. p. 52–72.
- <span id="page-34-12"></span>SCHNORR, C.-P. Efficient signature generation by smart cards. Journal of cryptology, Springer, v. 4, p. 161–174, 1991.
- <span id="page-34-13"></span>SHI, L.; LI, M.; YU, S.; YUAN, J. Bana: Body area network authentication exploiting channel characteristics. In: Proceedings of the fifth ACM conference on Security and Privacy in Wireless and Mobile Networks. [S.l.: s.n.], 2012. p. 27–38.

- <span id="page-35-3"></span>SILVA, V. L. D.; KOVALESKI, J. L.; PAGANI, R. N.; SILVA, J. D. M.; CORSI, A. Implementation of industry 4.0 concept in companies: Empirical evidences. International Journal of Computer Integrated Manufacturing, Taylor & Francis, v. 33, n. 4, p. 325–342, 2020.
- <span id="page-35-9"></span>SMART, P. N. Cryptography made simple. [S.l.]: Springer, 2016.
- <span id="page-35-8"></span>STALLINGS, W. Cryptography and Network Security: Principles and Practice. 6th. ed. United States: Pearson Education Limited, 2014.
- <span id="page-35-6"></span>STALLINGS, W. Cryptography and Network Security: Principles and Practice, Global Edition. [S.l.]: Pearson Education, 2018. ISBN 9781292158594.
- <span id="page-35-12"></span>SUÁREZ-ALBELA, M.; FERNÁNDEZ-CARAMÉS, T. M.; FRAGA-LAMAS, P.; CASTEDO, L. A practical performance comparison of ecc and rsa for resource-constrained iot devices. In: IEEE. 2018 Global Internet of Things Summit (GIoTS). [S.l.], 2018. p. 1–6.
- <span id="page-35-0"></span>TAHA, A.-E. M.; RASHWAN, A. M.; HASSANEIN, H. S. Secure communications for resource-constrained iot devices. Sensors, MDPI, v. 20, n. 13, p. 3637, 2020.
- <span id="page-35-5"></span>TOMASIN, S. Comparison between asymmetric and symmetric channel-based authentication for mimo systems. In: VDE. WSA 2017; 21th International ITG Workshop on Smart Antennas. [S.l.], 2017. p. 1–5.
- <span id="page-35-10"></span>TOMAZ, A. E. B. Security and privacy-preserving of data in mobile health systems: an approach based on non-interactive zero-knowledge proof and blockchain. Tese (Tese (Doutorado em Ciência da Computação)) — Universidade Federal do Ceará, Fortaleza, 2021.
- <span id="page-35-1"></span>TOMAZ, A. E. B.; NASCIMENTO, J. C. D.; HAFID, A. S.; SOUZA, J. N. D. Preserving privacy in mobile health systems using non-interactive zero-knowledge proof and blockchain. IEEE access, IEEE, v. 8, p. 204441–204458, 2020.
- <span id="page-35-11"></span>TONG, W.; YANG, L.; LI, Z.; JIN, X.; TAN, L. Enhancing security and flexibility in the industrial internet of things: Blockchain-based data sharing and privacy protection. Sensors, MDPI, v. 24, n. 3, p. 1035, 2024.
- <span id="page-35-7"></span>WAGNER, D. Advances in Cryptology-CRYPTO 2008: 28th Annual International Cryptology Conference, Santa Barbara, CA, USA, August 17-21, 2008, Proceedings. [S.l.]: Springer, 2008. v. 5157.
- <span id="page-35-4"></span>WAIBEL, M.; OOSTHUIZEN, G.; TOIT, D. D. Investigating current smart production innovations in the machine building industry on sustainability aspects. Procedia Manufacturing, Elsevier, v. 21, p. 774–781, 2018.
- <span id="page-35-13"></span>WALSHE, M.; EPIPHANIOU, G.; AL-KHATEEB, H.; HAMMOUDEH, M.; KATOS, V.; DEHGHANTANHA, A. Non-interactive zero knowledge proofs for the authentication of iot devices in reduced connectivity environments. Ad Hoc Networks, Elsevier, v. 95, p. 101988, 2019.
- <span id="page-35-2"></span>WEI, W.; YANG, A. T.; SHI, W.; SHA, K. Security in internet of things: Opportunities and challenges. In: IEEE. 2016 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI). [S.l.], 2016. p. 512–518.

<span id="page-36-0"></span>XU, G.; QIU, S.; AHMAD, H.; XU, G.; GUO, Y.; ZHANG, M.; XU, H. A multi-server two-factor authentication scheme with un-traceability using elliptic curve cryptography. Sensors, MDPI, v. 18, n. 7, p. 2394, 2018.

<span id="page-36-1"></span>ZHOU, L.; LI, X.; YEH, K.-H.; SU, C.; CHIU, W. Lightweight iot-based authentication scheme in cloud computing circumstance. Future generation computer systems, Elsevier, v. 91, p. 244–251, 2019.