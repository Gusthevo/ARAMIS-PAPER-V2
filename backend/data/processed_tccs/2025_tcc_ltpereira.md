# UM ESTUDO COMPARATIVO DE MODELOS DE APRENDIZADO DE MÁQUINA PARA CLASSIFICAÇÃO DE FLORES APÍCOLAS: INTEGRANDO EXTRATORES DE TEXTURAS E CLASSIFICADORES

#### RESUMO

A Flora Apícola é o grupo de plantas das quais as abelhas retiram algum recurso floral, podendo este ser polén, néctar ou ambos. Sendo o potencial de produção apícola de uma região determinado pelo revestimento floral da mesma, entender o pasto apícola contribui para um manejo planejado e a otimização de apiários. Isto posto, este trabalho propõe a construção de um modelo computacional baseado em aprendizado de máquina, que classifica imagens de flores em três classes: poliníferas, nectaríferas e nectaríferas-poliníferas, buscando, assim, fornecer subsídios para determinar o potencial de produção apícola de uma região. Os experimentos utilizaram um conjunto de dados com 1.145 imagens de flores presentes na flora apícola do Sertão Central do estado do Ceará. Para extração das características dez Redes Neurais Convolucionais foram usadas, enquanto os algoritmos SVM, KNN, MLP e uma CNN proposta, foram responsáveis pelo processo de classificação. Assim, buscou-se encontrar a melhor combinação entre extrator e classificador. Por fim, os resultados indicaram a eficiência do sistema proposto, com a melhor combinação sendo o ResNet50 + SVM, que atingiu um MCC de 92.94%.

Palavras-chave: Abelhas; Flora Apícola; Aprendizado de Máquina; Redes Neurais Artificiais.

### ABSTRACT

The Beekeeping Flora comprises the group of plants from which bees extract floral resources, which may include pollen, nectar, or both. Since the beekeeping production potential of a region is determined by its floral coverage, understanding the foraging resources available to bees contributes to planned management and the optimization of apiaries. In this context, this study proposes the development of a computational model based on machine learning to classify flower images into three categories: pollen-producing, nectar-producing, and both nectar and pollen producing. The objective is to provide insights into the beekeeping production potential of a given region. The experiments were conducted using a dataset containing 1.145 flower images from the beekeeping flora of the Sertão Central region in the state of Ceará, Brazil. Feature extraction was performed using ten Convolutional Neural Networks (CNNs), while classification was carried out using SVM, KNN, MLP, and a proposed CNN. The study aimed to identify the best combination of feature extractor and classifier. The results demonstrated the efficiency of the proposed system, with the best combination being ResNet50 + SVM, achieving an MCC of 92.94%.

Keywords: Bee; Bee Flora; Machine Learning; Artificial Neural Networks.

# 1 INTRODUÇÃO

Sistemas computacionais encontram-se cada vez mais integrados ao cotidiano das pessoas, fazendo-se presentes em interações sociais, atividades domésticas, trabalhos e até mesmo atividades de lazer. A computação, como é conhecida hoje, é fruto de um processo histórico de pessoas que acreditavam na possibilidade da criação de ferramentas que aumentariam a capacidade intelectual, e na criação de dispositivos que substituiriam pensamentos mecanizados do ser humano (GOSHT, 2007, p. 85).

Uma das ferramentas da computação que vem ganhando destaque nos últimos anos é a Inteligência Artificial (IA).Para Ghosh *et al.* (2018), IA é a tecnologia que objetiva tornar computadores capazes de fazerem raciocínios semelhantes ao seres humano. Já Jiang *et al.* (2022) caracteriza IA como as teorias, os métodos, as tecnologias e as aplicações que simulam, estendem e expandem a inteligência humana. Assim, a IA se apresenta como mais uma tecnologia que visa facilitar as tarefas cotidianas das pessoas.

Para que sistemas que utilizam a tecnologia previamente apresentada cumpram com os objetivos propostos, uma subárea da IA, que também vem ganhando notoriedade, precisa ser desenvolvida: o Aprendizado de Máquina (AM). Segundo Minh *et al.* (2022), AM é um conjunto de técnicas que dependem de modelos matemáticos para melhorar a inteligência das máquinas. Treina-se o modelo utilizando um conjunto de dados e se produz predições sem a necessidade de regras programadas explicitamente para aquilo. Outra área que se relaciona com a IA é a Visão Computacional (CV), que consiste em um conjunto de técnicas, que permitem que o computador receba e processe informações visuais, como imagens ou vídeos KAUL *et al.*, (2020). Dessa forma, estas técnicas, possibilitam que sistemas computacionais consigam tomar decisões mais precisas e automáticas com base em conjunto de dados previamente repassados a eles.

Dentre as técnicas computacionais, o AM tem se destacado nas tarefas de classificação de padrões em diversas áreas. Aplicações na área da saúde (SOUZA *et al.*, 2021; MEDEIROS *et al.*, 2024), construção civil (MUNAWAR *et al.*, 2022; MACAULAY; SHAFIEE, 2022), na análise de componentes de segurança (XU *et al.*, 2023), agropecuária (SANTOS; FALCÃO, 2023; XI *et al.*, 2023) e na apicultura (SILVA *et al.*, 2023; BHUIYAN *et al.*, 2022) estão entre alguns do exemplos de uso do AM.

O primeiro registro da atividade apícola no Brasil data do ano de 1839, com a introdução das primeiras colônias de abelhas da espécie *Apis mellifera* no país (BRASIL, 1839). Borges *et al.* (2022) caracteriza a apicultura como uma importante atividade agropecuária com benefícios econômicos, sociais e ambientais. No desenvolvimento desta prática, destacase a figura dos pequenos agricultores, que procuram nela uma fonte de renda alternativa e complementar (KLOSOWSKI *et al.*, 2020). Segundo a FAO e Apimondia (2021), a geração de renda, a movimentação da economia local, o fornecimento de diversos produtos apícolas e o desenvolvimento e a conservação da vegetação estão entre alguns dos benefícios propiciados pela apicultura. Klosowski *et al.* (2020) ressalta a importância das abelhas para a economia e agricultura mundialmente, destacando que cerca de 70% da plantas consumidas dependem do processo de polinização, realizado predominantemente por essa espécie. Ademais, ainda segundo o autor, os produtos derivados da atividade apícola - mel, própolis, geleia real, pólen, cera e apitoxina, tem o potência para alcançar valores superiores aos demais produtos agrícolas.

No que se refere à produção de mel orgânico, o Brasil é o país com maior capacidade de produção do mundo (VIDAL, 2018). Em seu relatório, IBGE (2024) apresenta que, somente no ano de 2022, foram produzidas 60.966 toneladas de mel, com a produção sendo liderada pela região nordeste, com cerca de 23.578 toneladas, e seguida pela região sul, com aproximadamente 22.406 toneladas. A baixa contaminação por pesticidas e resíduos antibióticos, já que o mel, em sua maioria é proveniente da vegetação nativa, fazem os produtos apícolas produzidos na região nordeste do Brasil possuírem elevada competitividade no mercado internacional (VIDAL, 2020).

De acordo com Batista *et al.* (2018), a flora apícola compreende o conjunto de plantas de uma determinada região das quais abelhas coletam pólen e néctar. As características das espécies de plantas que compõe o pasto apícola variam em função do tipo vegetação, das condições edafoclimáticas, das estações do ano e da região que estas plantas estão (BRUGNEROTTO *et al.*, 2021). A Caatinga é um dos biomas da região nordeste que possui uma enorme variedade de tipos vegetais e uma elevada quantidade de espécies endêmicas (GIULIETTI *et al.*, 2004). Freitas (1996 apud SANTOS *et al.*, 2006) observa que a frequência e a densidade de espécies vegetais, que variam entre as localidades do bioma, é um fator que influencia diretamente no fluxo de pólen e néctar que entram nas colmeias da região. Isto posto, o estudo da flora apícola permite ao produtor estar ciente da quantidade de pastagem de flores presente ao redor de seus apiários (ALVES; CARNEIRO, 2021), identificar as fontes dos recursos florais e, assim, a realizar o planejamento e a otimização do manejo (VASCONCELOS *et al.*, 2021).

Contudo, o processo de identificação destas flores ainda é executado de forma manual, que, além de ser um trabalho dispendioso, pode ocasionar classificações distorcidas e erros de precisão por aqueles que realizam este processo. Um estudo conduzido na cidade de Marcelino Vieira, no Rio Grande do Norte, por Câmara *et al.* (2021), objetivou identificar as espécies mais representativas da flora apícola com base no etnoconhecimento dos apicultores do município. Os autores fizeram levantamentos em quatro fazendas da região e aplicaram questionários ao produtores para realizar a pesquisa. Como resultado, foram identificados 93 espécies vegetais com potencial apícola e um total de 91 destas foram consideradas importantes fontes de recursos florais na região.

A identificação de flores de forma geral é um processo complexo, que demanda experiência e um conhecimento botânico profundo e, dada a similaridade de algumas flores, desafia até mesmo profissionais experientes LI *et al.*, (2024). Entretanto, no estado atual da tecnologia, técnicas mais modernas para classificação de flores já estão disponíveis para facilitar o trabalho de pesquisadores ou qualquer indivíduo que possua interesse sobre a temática.

Nesse contexto, este estudo teve como objetivo desenvolver um modelo computacional que utiliza arquitetura híbrida para classificar imagens de flores presentes na flora apícola do Sertão Central Cearense, as quais as abelhas *Apis mellifera* usam em sua alimentação, quanto ao recurso floral por elas fornecido. Para isto, foi utilizada uma base de dados própria com imagens classificadas em três classes: flores poliníferas, nectaríferas e nectaríferas-poliníferas.

As imagens foram processadas e submetidas aos extratores, que deram como resultado matrizes de características, então divididas em conjuntos de treino e teste. Devido ao desbalanceamento das classes do conjunto de dados, foi utilizado a técnica de *Synthetic Minority Oversampling Technique* (SMOTE) (CHAWLA *et al.*, 2002) no conjunto de treino, para possibilitar que o modelo aprendesse todas as classes da melhor maneira possível. Em seguida, os dados foram entregues aos classificadores para que ocorresse o processo de treinamento e, posteriormente, a avaliação do modelo. Por fim, buscou-se determinar qual a melhor combinação entre extrator e classificador.

O presente trabalho encontra-se estruturado da seguinte maneira: na Seção 2 discutese trabalhos relevantes para a temática; na Seção 3 a arquitetura proposta do sistema é apresentada; na Seção 4 os resultados obtidos são analisados e na Seção 5 são apresentados as conclusões e são introduzidos os direcionamentos para o futuros do estudo.

## 2 ESTADO DA ARTE

No trabalho de Patel e Patel (2019) os autores apresentam um modelo híbrido para classificação *multi-label* de flores. O mesmo, utiliza técnicas de CV para realizar o préprocessamento, segmentação das imagens e extração de características, enquanto os algoritmos *Multiple Kernel Labeling* (MKL) (BUCAK *et al.*, 2013) e *Support Vector Machine* (SVM) (VAPNIK *et al.*, 1996) são combinados e designados para o processo de classificação. Ao todo 14 características, como cor, tamanho, textura, tipo de pétala e número de pétalas, foram extraídas utilizando diferentes técnicas de CV. Essas características foram então repassadas ao algoritmo MKL que combinou os diferentes dados extraídos e os repassou ao SVM que realiza a classificação final. Para seu treinamento, o *Oxford flower dataset* foi utilizado em conjunto com imagens adquiridas na internet, o que totalizou um conjunto de dados com 25.000 imagens e 102 diferentes espécies de flores. Por fim, ao comparar o desempenho da arquitetura proposta com os algoritmos de classificação *K-Nearest Neighbors* (KNN) (FIX; HODGES, 1951), *Random Forest* (BREIMAN, 2001), SVM e Redes Neurais Artificiais, percebeu-se um desempenho superior da mesma, que atingiu uma acurácia de 78%.

O estudo de Togaçar  *et al.* (2020) propõe uma abordagem para a classificação de flores utilizando Redes Neurais Convolucionais (CNN) para extração de características e o algoritmo SVM para a classificação. Seu principal diferencial está no refinamento da seleção de atributos, combinando vetores de características extraídos por AlexNet (KRIZHEVSKY *et al.*, 2012), GoogLeNet (SZEGEDY *et al.*, 2015a), ResNet50 (HE *et al.*, 2015) e VGG16 (SIMONYAN; ZISSERMAN, 2015). O conjunto de dados utilizado contém 4.252 imagens de margaridas, rosas, dentes de leão, girassóis e tulipas, obtidas da internet com resoluções variadas. Para lidar com o desequilíbrio entre classes, foi aplicado o método de *Random Under Sampling*, que aleatoriamente reduz as imagens a uma quantidade comum a todas as classes. Foram usadas as técnicas *F-regression* e *Multiple Inclusion Criterion (MIC)* para selecionar as características mais relevantes. Ao usarem essas técnicas os autores visam encontrar características especificas e relevantes para o problema analisado de forma a melhorar a classificação das imagens. Ao total três experimentos foram conduzidos, no primeiro, nenhuma das técnicas foi usada, no segundo, elas foram empregadas individualmente e no terceiro foram combinadas. Em todos os experimentos atingiu-se acurácia acima de 89%, com o melhor resultado, de 98.91% de acurácia, sendo obtido utilizando 2.500 características resultadas da combinação das duas técnicas.

Já o trabalho de Huang e Xu (2023), apresenta um modelo para classificação de flores medicinais chinesas usando CNNs. O estudo se difere dos demais ao fazer uso de módulos de atenção em sua arquitetura para melhorar processo de classificação. Com um conjunto de dados próprio, com 12.538 imagens reunidas da internet, totalizadas após a aplicação da técnica de *Data Augmentation*, os autores testaram dois módulos de atenção com a CNN ResNet101: o *Squeeze-and-excitation network* (SENet) e o *Convolutional block attention module* (CBAM). Para treinamento, usou-se o *K-fold Cross Validation* com cinco *folds*. O desempenho das combinações da ResNet101 com os módulos de atenção foram comparadas entre si e com a mesma rede usando Otimização Bayesiana (OB). Além disso, as redes VGG16, VGG19 e DenseNet121 foram testadas e comparadas, as duas primeiras com e sem os módulos SENet e CBAM, e a última com o SENet e somente uma parte do CBAM. Como resultado, Huang e Xu (2023) concluem que, mesmo suas arquiteturas propostas atinjam bons resultados, com acurácias acima de 70%, o modelo que usa a ResNet101 com OB performa melhor no problema proposto, atingindo uma acurácia de 97.64%.

Por fim, Endo *et al.* (2024) aborda o problema da coleta de pólen em árvores de Pereiras no Japão, que, por conta do período de floração destes, encontra a necessidade de ser realizada de forma artificial por produtores. Neste contexto, visando auxiliar nesse processo, os autores propõem um sistema para estimar a quantidade de pólen presente em ramo contendo flores em diferentes fases de floração. O sistema proposto usa *Deep Learning* (DL) para detectar e classificar as flores e suas fases de floração presentes nas imagens para, a partir da quantidade de flores presentes, estimar a quantidade de pólen a ser colhido nela. Para a execução deste trabalho, foi utilizada uma base de dados contendo 1.271 imagens de flores de diferentes espécies de Pereiras com cinco fases de floração: imatura, forma de balão, floração, fim de floração e outros, que compreende flores que estão em posições que não permitem uma classificação dos estados anteriores. O modelo YOLOv8n foi empregado para detectar e classificar as flores presentes nas imagens. Posteriormente, estimou-se a quantidade total de pólen coletado, utilizando a quantidade de flores detectadas e multiplicando pela quantidade de pólen por flor, previamente coletado. Em seus resultados os autores obtiveram que, no processo de detecção e classificação o sistema obteve bons resultados, com acurácias acima de 80% em algumas classes. Todavia, no processo de estimação da quantidade de pólen nas flores o sistema sofreu ao ter que lidar erros cometidos durante a etapa de aquisição da quantidade de pólen em cada flor, por não conseguir capturar de forma eficiente flores que estivessem sobrepostas por galhos na imagens e erros de classificação entre classes com flores similares, como as das classes: floração e fim de floração, que possuem como única diferença a cor das anteras dos estames.

Uma vez apresentados os trabalhos científicos que exploram problemáticas similares a deste estudo, é possível identificar as contribuições ofertadas por cada um deles. A Tabela 1 mostras as principais contribuições de cada trabalho, incluindo este. Foram estas a utilização de: técnicas de pré-processamento (A), arquitetura híbrida (B), CNNs como extratores de características (C), um banco de dados com imagens de uma flora endêmica de um região (D), a classificação da flor quanto ao recurso flor fornecido a uma espécie (E).

Dessa forma, é possível perceber que este trabalho engloba a maior parte das técnicas já exploradas por outros estudos, inovando ao realizar a classificação de flores quanto ao recurso floral fornecido por elas a espécie de abelha *Apis mellifera* e usando, para isto, uma base de dados com imagens de flores de um região inexplorada por esse tipo de estudo.

Tabela 1 – Comparação entre os trabalhos correlatos

| Trabalhos                | A | B | C | D | E |
|--------------------------|---|---|---|---|---|
| (PATEL; PATEL, 2019)     | X | X | - | - | - |
| (TOGAÇAR ˘ et al., 2020) | - | X | X | - | - |
| (HUANG; XU, 2023)        | X | - | X | X | - |
| (ENDO et al., 2024)      | - | - | - | X | - |
| Este estudo              | - | X | X | X | X |

Fonte: Elaborada pela autora.

### 3 METODOLOGIA

Este artigo investiga a eficiência de arquiteturas híbridas no processo de classificação de flores utilizadas por abelhas *Apis mellifera* para retirada de alimentos a partir de imagens. Para isso, foram usadas CNN como extratores de características, combinados a quatro classificadores de aprendizado de máquina, incluindo a própria CNN.

## 3.1 Visão Geral

A Figura 1 ilustra o processo desenvolvido neste trabalho. Ao total sete passos foram conduzidos para alcançar o objetivo final: Carregamento das imagens, preparação dos dados, extração das características, divisão dos dados em treino e teste, treinamento, predição das classes e avaliação do modelo. Tais etapas são descritas com maiores detalhes na sequência:

- Etapa 1: As imagens são, inicialmente, carregadas da base dados;
- Etapa 2: Passam por uma etapa de preparação, que inclui a conversão destas para matrizes, seu redimensionamento e sua normalização;
- Etapa 3: Estas são, posteriormente, enviadas para as CNNs, onde terão suas características extraídas e armazenadas em uma matriz;
- Etapa 4: A matriz de características, resultado da última etapa é, então, divida em dados para treinamento e dados para teste;
- Etapa 5: Os dados de treinamento são submetidos a um processo de balanceamento de classes, chamado SMOTE e fornecidos aos classificadores para realizarem seus processos de treinamento;
- Etapa 6: Em seguida, ocorre a predição das classes das características dos dados de teste com os modelos desenvolvidos;
- Etapa 7: Por fim, os modelos são avaliados utilizando as predições realizadas e as classes dos dados de teste.

#### 3.2 Conjunto de Dados

Os dados usados neste estudo foram obtidos de uma base de dados própria, que encontra-se em processo de publicação, constituída por imagens de flores da flora apícola do Sertão Central do estado do Ceará, mais especificamente da cidade de Boa Viagem. As imagens foram capturadas em campo, ou seja, em um ambiente não controlado, por um *smartphone* Samsung A32 equipado com uma câmera de 64 Megapixel, possibilitando obter imagens de alta resolução com dimensões de (2675x3547). Além disso, também foram capturadas imagens com um fundo branco opaco, sob diferentes ângulos e iluminações, visando aumentar a variedade e qualidade das imagens do mesmo.

Para a classificação das imagens foram usados trabalhos especializados, de referência a fim de se determinar quais flores as abelhas *Apis mellifera* coletam pólen, néctar ou ambos recursos. No total, o conjunto de dados contém 1.145 imagens, todas de mesmas dimensões divididos em três grandes classes: flores poliníferas (pólen), flores nectaríferas (néctar) e flores nectaríferas-poliníferas (pólen e néctar).

Além disso, o conjunto de dados é formado por 20 espécies de plantas distribuídas entre as três classes discutidas neste trabalho. A Tabela 2 apresenta uma descrição detalhada do banco de dados utilizado, mostrando a distribuição de imagens e quantidade de espécie por classe. Assim, a classe polinífera dispõe de sete espécies de plantas e 395 imagens, a classe nectarífera compreende nove espécies e 457 imagens e por fim a classe nectaríferas-poliníferas é composta por quatro espécies de plantas e 293 imagens.

Tabela 2 – Descrição do Dataset.

| Classes        | Qtd.<br>de espécies | Nº de<br>Imagens |  |  |
|----------------|---------------------|------------------|--|--|
| Pólen          | 7                   | 395              |  |  |
| Néctar         | 9                   | 457              |  |  |
| Pólen e Néctar | 4                   | 293              |  |  |

Fonte: Elaborada pela autora.

### 3.3 Preparação das Imagens

Informações visuais, como imagens e vídeos, precisam ser processadas para que computadores possam compreendê-las. Dessa forma, as imagens do conjunto de dados foram, primeiramente, carregadas e convertidas em matrizes. Em seguida, foram redimensionadas para 244 x 244 pixels, atendendo as dimensões requeridas pelas CNNs. Além disso, seus três canais cor foram preservados, dado a relevância desta característica para o problema (FIORATTI, 2023, p. 19). Por fim, as mesmas foram submetidas a um processo de normalização, realizado pela função *preprocess_input* da biblioteca Keras (versão 3.8.0), a fim de garantir que os dados estejam nos padrões corretos esperados pelos modelos.

### 3.4 Configurações Experimentais

O experimento foi desenvolvido no ambiente virtual do Google Colab, em uma máquina com 53 GB de memória RAM, 22.5 GB de VRAM e um disco de 235.7 GB. Para sua implementação foi usada a linguagem Python na versão 3.11.11.

Para a etapa de extração de características foram usados 10 modelos de CNNs prétreinadas, importadas da biblioteca Keras: VGG16 e VGG19 (SIMONYAN; ZISSERMAN, 2015), ResNet50 e ResNet50V2 (HE *et al.*, 2015), InceptionResNetV2 (SZEGEDY *et al.*, 2016), InceptionV3 (SZEGEDY *et al.*, 2015b), MobileNetV3Small (HOWARD *et al.*, 2017), ConvNeXtSmall (LIU *et al.*, 2022), EfficientNetV2B0 e EfficientNetV2B3 (TAN; LE, 2021b). Todos os modelos selecionados tiveram sua camada totalmente conectada desativadas não realizando, assim, o processo de classificação. Somado a isso, foram pré-treinadas com os pesos do banco de dados Imagenet (DENG *et al.*, 2009) e tiveram suas camadas convolucionais congeladas, garantindo que as características extraídas permanecessem inalteradas. Esse processo caracteriza o uso de *Transfer Learning* na abordagem de extração de características.

A cada rodada do experimento cada extrator foi executado com todos os classificadores. Cada extrator gerou como resultado uma matriz de características das imagens. Posteriormente, ocorreu o particionamento dos dados em dois conjuntos: treino e teste. Para isso, foi usado a técnica de K-Fold *Cross-Validation*, com 5 *folds*. Assim, ao longo das iterações, 4 *folds* foram usados para treinamento e 1 para teste, alternando-se o *fold* de teste entre as *features* do conjunto de dados ao longo das execuções.

Dado o desequilíbrio das classes no conjunto de dados a técnica chamada *Synthetic Minority Oversampling Technique* (SMOTE) foi empregada no conjunto de treino para balancear as classes. Este método cria amostras sintéticas da classe minoritária usando um algoritmo semelhante ao KNN, assim, as novas amostras são criadas com base em amostras vizinhas (CHAWLA *et al.*, 2002). Com o uso deste, torna-se possível, portanto, que o modelo aprenda melhor as características das classes minoritárias.

Sua implementação foi realizada com a biblioteca Imbalanced-learn (LEMAîTRE *et al.*, 2017), equiparando as classes minoritárias a classe com o maior número de amostras. Dessa forma, devido a quantidade total de amostra ser um número ímpar, após a aplicação da técnica, em duas iterações, a quantidade de número de imagens para treinamento passou de 916 para 1095, enquanto nas outras três passou 916 para 1098 imagens.

Em seguida, os dados de treinamento foram repassados para os classificadores. Foram selecionados quatro algoritmos para esta tarefa: o *Multilayer Perceptron* (MLP), KNN, SVM e uma CNN.

Como neste trabalho modelos de CNNs já são empregados no processo de extração de características, a CNN usada para classificação utiliza-se do modelo extrator, adicionando-se a este somente as camadas previamente retiradas. A arquitetura desta, apresentada na Figura 2, é composta por uma camada de Flatten, dois módulos com uma camada Densa, uma de Batch Normalizarion e outra de Dropout, e, por fim, finalizando com uma camada Densa. Este algoritmo utiliza o otimizador Adam com um *learning rate* de 1e-4 e como função de loss a *sparse_categorical_crossentrop*. Além disso, foi treinado em 10 épocas, um *batch_size* de 32 e 0.2 de *validation_split*.

Por outro lado, o classificador MLP foi executado com um número máximo de 200 iterações, usando o otimizador Adam e a função de ativação Relu, bem como um *random state* igual a um. Já o algoritmo KNN, utilizou o número de vizinhos mais próximos igual cinco e todos os outros hiperparâmetros configurados como padrão. Por fim, o algoritmo SVM usou o *kernel* linear em seu funcionamento e também teve todos os outros parâmetros configurados como padrão.

## 3.5 Métricas de Avaliação

Este estudo explora um problema de classificação, assim, para a avaliação será utilizada a Matriz de Confusão do modelo e métricas derivadas da mesma. Dessa maneira, foram analisados os Verdadeiros Positivos (VP), Falso Positivos (FP), Verdadeiros Negativos (VN) e os Falsos Negativos (FN). Ademais, também foram consideradas as métricas *Matthews Correlation Coefficient* (MCC), Acurácia global (AccGlobal), precisão da classe pólen (PrecPolen), precisão da classe néctar (PrecNectar), precisão da classe pólen e néctar (PrecPolenNectar).

- Verdadeiro Positivo (VP): Ocorre quando a flor, no conjunto real dos dados, possui um recurso floral e é predita com aquele recurso.
- Falso Positivo (FP): Ocorre quando o recurso da classe, no conjunto real de dados, que se procura prever é prevista de forma errônea. Ou seja, a flor não possuia o recurso em foco, mas o modelo previu que ela tinha.
- Verdadeiro Negativo (VN): Ocorre quando o recurso floral da classe, que não é a que está em foco, no conjunto real, é previsto de forma correta.
- Falso Negativo (FN): Ocorre quando, no conjunto real, a classe que não se buscar realizar a predição, é predita de forma incorreta. Ou seja, quando a classe possui o recurso floral, mas foi previsto que ela não continha.
- *Matthews Correlation Coefficient* (MCC) (MATTHEWS, 1975; BALDI *et al.*, 2000): É um coeficiente de correlação, utilizado para avaliar modelos que utilizam conjuntos de dados desbalanceados, já que leva em consideração todos os elementos da matriz de confusão .

$$MCC = \frac{VN \times VP - FP \times FN}{\sqrt{(VN + FN)(FP + VP)(VP + FP)(FN + VP)}}$$
(1)

– Acurácia Global (Acc): Refere-se ao percentual total de acertos global. A acurácia, então, contempla os acertos das classes, sob todos os erros e acertos.

$$Acc = \frac{VP + VN}{VP + FP + VN + FN} \tag{2}$$

– Precisão classe pólen (PrecPolen): É a probabilidade de uma flor possuir pólen e ela realmente conter.

$$PrecPolen = \frac{VP}{VP + FN} \tag{3}$$

– Precisão classe néctar (PrecNectar): É a probabilidade de uma flor possuir néctar e ela realmente conter.

$$PrecNectar = \frac{VP}{VP + FN} \tag{4}$$

– Precisão classe pólen e néctar (PrecPolenNectar): É a probabilidade de uma flor possuir pólen e néctar e ela realmente conter.

$$PrecPolenNectar = \frac{VP}{VP + FN} \tag{5}$$

## 4 RESULTADOS

Neste estudo, foram extraídas as características de 1.145 imagens utilizando dez modelos de CNN pré-treinados, que foram combinados a quatro algoritmos classificadores. Ao total 40 resultados forma obtidos. Dessa forma, buscou-se identificar a melhor combinação entre extrator e classificador.

A Tabela 3 apresenta os resultados obtidos por extrator e classificador. Ao examinála é possível notar que os extratores VGG16, VGG19, ResNet50V2, InceptionV3, Mobile-NetV3Small, ConvNeXtSmall, EfficientNetV2B3 e EfficientNetV2B0 alcançaram seus melhores desempenhos quando combinados a CNN proposta. Já o extrator InceptionResNetV2 obteve seu melhor resultado com o classificador KNN, atingindo apenas um MCC de 43.43%, com um desvio padrão de 2.64%. Além disso, o ResNet50 foi o único extrator que demonstrou o melhor desempenho com o classificador SVM, alcançando um MCC de 92.95%, com 1.37% de desvio padrão.

A análise da tabela também revela que o extrator InceptionResNetV2 apresentou o pior desempenho global. Embora o ResNet50V2 combinado ao MLP tenha registrado o menor resultado, com apenas 11.16% de MCC e desvio padrão de 18.68%, o InceptionResNetV2 não conseguiu atingir sequer 50% de MCC em nenhuma das combinação. Os resultados indicam, portanto, que a eficiência deste extrator é limitada, algo evidenciado ainda mais pelo fato de apresentar o maior tempo de extração entre todos os modelos avaliados, como ilustrado na Figura 3, que mostra o tempo de extração dos extratores.

No que diz respeito aos classificadores, o MLP apresentou resultados razoáveis, mas não atingiu desempenho superior em nenhumas das configurações, limitando seu melhor desempenho a 85.87% MCC, com um desvio padrão de 2.83%, como mostradado pela Figura 4, que dispõe os melhores resultados de cada classificador. Por sua vez, o KNN obteve seu melhor desempenho com o extrator ResNet50, atingindo um MCC de 72.12%, o que indica que uma ineficiência do mesmo para a tarefa. Em contrapartida, a CNN e o SVM demonstraram elevado desempenho, alcançando MCC superiores a 92% nas melhores combinações.

A Figura 5 mostra as dez melhores combinações. Ao examinar os dados dispostos,

Tabela 3 – Resultados obtidos por Extrator e Classficador


| Extratores        | Métricas                      | CNN                           | MLP                          | KNN                          | SVM                          |
|-------------------|-------------------------------|-------------------------------|------------------------------|------------------------------|------------------------------|
| VGG16             | MCC                           | 92.02 ± 7.54                  | 79.42 ± 3.25                 | 61.59 ± 1.37                 | 87.43 ± 2.16                 |
|                   | ACC                           | 94.67 ± 5.02                  | 86.11 ± 2.07                 | 74.41 ± 1.25                 | 91.70 ± 1.43                 |
|                   | PrecPolen                     | 98.98 ± 2.02                  | 82.78 ± 3.63                 | 74.41 ± 1.25                 | 91.89 ± 3.45                 |
|                   | PrecNectar                    | 98.69 ± 2.60                  | 94.73 ± 3.36                 | 68.04 ± 1.94                 | 92.54 ± 2.65                 |
|                   | PrecPolenNectar               | 82.53 ± 13.05                 | 77.11 ± 3.32                 | 80.21 ± 4.72                 | 90.06 ± 5.31                 |
| VGG19             | MCC                           | 92.25 ± 8.03                  | 79.95 ± 2.54                 | 58.83 ± 2.68                 | 86.50 ± 1.32                 |
|                   | ACC                           | 94.75 ± 5.49                  | 86.55 ± 1.71                 | 71.44 ± 2.04                 | 91.09 ± 0.89                 |
|                   | PrecPolen                     | 97.97 ± 4.05                  | 81.26 ± 4.48                 | 77.72 ± 4.20                 | 89.87 ± 3.48                 |
|                   | PrecNectar                    | 99.34 ± 1.30                  | 94.08 ± 2.25                 | 56.90 ± 6.36                 | 92.99 ± 1.79                 |
|                   | PrecPolenNectar               | 83.19 ± 14.23                 | 81.88 ± 4.65                 | 85.68 ± 5.71                 | 89.74 ± 1.94                 |
| ResNet50          | MCC                           | 92.28 ± 6.46                  | 83.95 ± 4.88                 | 72.12 ± 3.77                 | 92.94 ± 1.37                 |
|                   | ACC                           | 94.75 ± 4.45                  | 89.34 ± 3.33                 | 79.56 ± 2.80                 | 95.37 ± 0.89                 |
|                   | PrecPolen                     | 98.73 ± 2.53                  | 87.84 ± 7.27                 | 89.11 ± 3.63                 | 95.94 ± 0.94                 |
|                   | PrecNectar                    | 99.12 ± 1.26                  | 92.78 ± 2.00                 | 59.09 ± 4.45                 | 95.40 ± 0.82                 |
|                   | PrecPolenNectar               | 82.51 ± 12.59                 | 85.96 ± 6.60                 | 98.62 ± 2.00                 | 94.52 ± 2.28                 |
| ResNet50V2        | MCC                           | 84.12 ± 16.48                 | 11.16 ± 18.68                | 46.09 ± 5.17                 | 58.13 ± 2.76                 |
|                   | ACC                           | 89.51 ± 10.82                 | 44.19 ± 11.01                | 62.88 ± 3.77                 | 72.48 ± 1.81                 |
|                   | PrecPolen                     | 96.20 ± 5.12                  | 33.67 ± 42.43                | 70.63 ± 5.45                 | 78.73 ± 3.33                 |
|                   | PrecNectar                    | 91.51 ± 11.36                 | 75.22 ± 37.88                | 49.01 ± 6.41                 | 72.63 ± 5.97                 |
|                   | PrecPolenNectar               | 77.35 ± 18.51                 | 10.0 ± 20.00                 | 74.05 ± 3.85                 | 63.80 ± 6.65                 |
| InceptionResNetV2 | MCC                           | 24.18 ± 5.64                  | 24.87 ± 6.44                 | 43.43 ± 2.64                 | 37.91 ± 3.78                 |
|                   | ACC                           | 46.46 ± 5.97                  | 45.85 ± 6.37                 | 61.74 ± 1.75                 | 59.12 ± 2.47                 |
|                   | PrecPolen                     | 24.55 ± 29.80                 | 47.84 ± 35.50                | 67.59 ± 2.84                 | 67.59 ± 1.29                 |
|                   | PrecNectar                    | 53.60 ± 22.82                 | 41.65 ± 35.37                | 51.42 ± 2.31                 | 57.79 ± 5.41                 |
|                   | PrecPolenNectar               | 64.72 ± 19.10                 | 50.04 ± 26.34                | 69.97 ± 3.09                 | 49.83 ± 2.73                 |
| InceptionV3       | MCC                           | 87.54 ± 11.17                 | 44.77 ± 14.76                | 51.27 ± 2.13                 | 61.28 ± 2.42                 |
|                   | ACC                           | 91.70 ± 7.45                  | 62.79 ± 10.66                | 65.85 ± 1.36                 | 74.67 ± 1.58                 |
|                   | PrecPolen                     | 92.91 ± 7.45                  | 58.22 ± 29.77                | 75.94 ± 3.58                 | 76.96 ± 1.47                 |
|                   | PrecNectar                    | 97.39 ± 3.26                  | 71.39 ± 18.33                | 49.22 ± 4.05                 | 78.10 ± 3.23                 |
|                   | PrecPolenNectar               | 81.14 ± 15.63                 | 55.69 ± 24.02                | 78.12 ± 4.89                 | 66.21 ± 1.49                 |
| MobileNetV3Small  | MCC                           | 91.75 ± 8.14                  | 80.83 ± 2.04                 | 52.67 ± 1.80                 | 83.57 ± 2.24                 |
|                   |                               |                               |                              |                              |                              |
|                   | ACC                           | 94.41 ± 5.57                  | 87.24 ± 1.41                 | 63.66 ± 1.75                 | 89.17 ± 1.47                 |
|                   | PrecPolen                     | 97.72 ± 4.55                  | 87.34 ± 5.24                 | 71.39 ± 5.80                 | 90.37 ± 2.84                 |
|                   | PrecNectar                    | 99.13 ± 1.73                  | 93.65 ± 3.18                 | 36.55 ± 2.08                 | 91.89 ± 3.59                 |
|                   | PrecPolenNectar               | 82.51 ± 13.28                 | 77.14 ± 3.11                 | 95.56 ± 2.75                 | 83.30 ± 4.13                 |
| ConvNeXtSmall     | MCC                           | 92.54 ± 6.83                  | 84.72 ± 2.94                 | 62.25 ± 2.26                 | 87.29 ± 2.84                 |
|                   | ACC                           | 95.02 ± 4.55                  | 89.78 ± 1.94                 | 71.00 ± 2.07                 | 91.61 ± 1.90                 |
|                   | PrecPolen                     | 99.24 ± 1.51                  | 89.36 ± 5.22                 | 83.79 ± 4.62                 | 92.65 ± 2.70                 |
|                   | PrecNectar                    | 98.69 ± 2.60                  | 93.65 ± 5.24                 | 42.67 ± 2.51                 | 92.54 ± 4.14                 |
|                   | PrecPolenNectar               | 83.55 ± 11.96                 | 84.27 ± 5.74                 | 97.94 ± 1.27                 | 88.72 ± 2.36                 |
| EfficientNetV2B3  | MCC                           | 92.60 ± 6.07                  | 85.87 ± 2.83                 | 62.29 ± 5.15                 | 91.38 ± 2.01                 |
|                   |                               |                               |                              |                              | 94.32 ± 1.29                 |
|                   |                               |                               |                              |                              |                              |
|                   | ACC                           | 95.02 ± 4.11                  | 90.56 ± 1.96                 | 71.87 ± 4.03                 |                              |
|                   | PrecPolen                     | 98.98 ± 2.02                  | 92.65 ± 2.17                 | 85.56 ± 5.10                 | 94.43 ± 0.62                 |
|                   | PrecNectar<br>PrecPolenNectar | 99.34 ± 1.30<br>82.87 ± 11.53 | 88.61 ± 6.46<br>90.77 ± 5.28 | 45.52 ± 5.97<br>94.53 ± 2.96 | 95.18 ± 1.62<br>92.79 ± 4.29 |
|                   |                               |                               |                              |                              |                              |
| EfficientNetV2B0  | MCC                           | 90.75 ± 10.09                 | 81.69 ± 2.58                 | 55.55 ± 5.23                 | 84.43 ± 3.34                 |
|                   | ACC                           | 93.88 ± 6.61                  | 87.94 ± 1.69                 | 67.24 ± 3.79                 | 89.78 ± 2.18                 |
|                   | PrecPolen                     | 97.46 ± 5.06                  | 88.86 ± 2.81                 | 80.75 ± 6.47                 | 90.63 ± 1.01                 |
|                   | PrecNectar<br>PrecPolenNectar | 97.82 ± 4.34<br>82.85 ± 12.62 | 91.69 ± 2.78<br>80.90 ± 3.71 | 41.36 ± 5.45<br>89.42 ± 3.47 | 91.68 ± 3.14<br>85.66 ± 3.19 |

Fonte: Elaborada pela autora.

pode-se observar que, de forma geral, foram obtidas boas combinações, com MCCs acima dos 90% e erros relativamente baixos, com o erro das cinco melhores combinações ficando a baixo de 10%. Ademais, é possível notar que os extratores ResNet50 e EfficientNetV2B3 obtiveram um bom desempenho, o que pode ser atribuído a suas arquiteturas, que permitem uma melhor generalização (HE *et al.*, 2020; TAN; LE, 2021a).

Dentre todas as combinações, destacam-se a ResNet50 + SVM, com o melhor resultado geral, e a EfficientNetV2B3 + CNN, que atingiu o segundo melhor resultado, com um MCC de 92.60% e um desvio padrão de 6.07%. Avaliando a precisão de cada classe nessas combinações, tem-se que a primeira configuração apresenta um maior equilíbrio, com 95.94% de PrecPolen, 95.40% de PrecNectar, 94.52% de PrecPolenNectar e respectivos 0.94%, 0.82%, 2.28% de desvio padrão. Por outro lado, a segunda combinação exibe um desequilíbrio mais significante, com 98.98% de PrecPolen, 99.34% de PrecNectar, 82.87% de PrecPolenNectar, com respectivos 2.02%, 1.30% e 11.53% de desvio padrão, porém já esperado devido ao desbalanceamento do próprio conjunto de dados. Além disso, como mostrado na Figura 3, o tempo de extração da ResNet50, 14.33 segundo, é inferior ao da EfficientNetV2B3, 23.90 segundo, o que o torna melhor do que o segundo.

Assim, a combinação ResNet50 + SVM mostra-se como a mais eficiente para o processo de classificação de flores quanto ao recurso floral fornecido a abelhas *Apis mellifera*, mesmo apresentando um maior tempo de treinamento e teste, com 35.3679 e 8.6335 segudnos, quando comparado a combinação EfficientNetV2B3 + CNN, com 7.1206 e 0.2766 segundos, como destacado na Tabela 4.

Tabela 4 – Tempos de treinamento e teste por extrator e classificador

| Extrator             | Tempo  | CNN      | MLP       | KNN      | SVM      |
|----------------------|--------|----------|-----------|----------|----------|
| **VGG16**            | Treino | 4.5171   | 7.0594    | 0.0103   | 7.2657   |
|                      | Teste  | 0.1922   | 0.0138    | 0.0479   | 2.0053   |
| **VGG19**            | Treino | 4.2874   | 9.2125    | 0.0104   | 8.7973   |
|                      | Teste  | 0.1866   | 0.0090    | 0.4808   | 1.9393   |
| **ResNet50**         | Treino | 8.6470   | 71.9531   | 0.0484   | **35.3679** |
|                      | Teste  | 0.3112   | 0.0454    | 2.4701   | **8.6335** |
| **ResNet50V2**       | Treino | 8.5089   | 73.9998   | 0.0483   | 45.9590   |
|                      | Teste  | 0.3116   | 0.0425    | 2.4534   | 6.2121    |
| **InceptionResNetV2**| Treino | 5.3741   | 20.4372   | 0.0211   | 22.0193   |
|                      | Teste  | 0.2260   | 0.0214    | 1.0492   | 2.4776    |
| **InceptionV3**      | Treino | 6.4347   | 93.6101   | 0.0283   | 26.5923   |
|                      | Teste  | 0.2560   | 0.0312    | 1.3781   | 2.4450    |
| **MobileNetV3Small** | Treino | 4.7139   | 13.4345   | 0.0143   | 14.2405   |
|                      | Teste  | 0.1959   | 0.0162    | 0.7140   | 1.3597    |
| **ConvNeXtSmall**    | Treino | 4.5836   | 9.4942    | 0.0147   | 14.7436   |
|                      | Teste  | 0.1975   | 0.0162    | 0.7133   | 1.4428    |
| **EfficientNetV2B3** | Treino | **7.1206** | 32.8763  | 0.0368   | 31.4387   |
|                      | Teste  | **0.2766** | 0.0383   | 1.8390   | 3.1855    |
| **EfficientNetV2B0** | Treino | 6.4119   | 27.2324   | 0.0307   | 25.3736   |
|                      | Teste  | 0.2539   | 0.0349    | 1.5414   | 3.1831    |
Fonte: Elaborada pela autora.

## 5 CONCLUSÕES E TRABALHOS FUTUROS

Este estudo explora o problema de classificação de imagens de flores quanto ao recurso floral fornecido a abelhas *Apis mellifera*. Além do problema explorado, sua unicidade, encontra-se, também, no uso de uma base de dados própria, com imagens que refletem condições reais nas quais essas plantas são encontradas. O que permite que o modelo desenvolvido aprenda com um cenário mais próximo da realidade daqueles que o utilizarão. Assim, o sistema elaborado possui o potencial de auxiliar pesquisadores, apicultores e outros interessados no assunto oferecendo uma ferramenta rápida e confiável para classificar as flores da flora apícola em poliníferas, nectaríferas e nectaríferas-poliníferas, facilitando a identificação das fontes de alimento disponíveis para as colmeias de abelhas.

Além disso, dez CNNs foram usadas como extratores de características e quatro algoritmos, incluindo uma CNN, foram utilizados para o processo de classificação, explorando, assim, o emprego de arquiteturas híbridas na solução do problema discutido. Em sua maioria, as combinações geradas obtiveram performances satisfatórias com MCC acima de 80%.

As duas melhores combinações que tiveram os melhores resultados foram a ResNet50 + SVM, com um MCC de 92.94% e um erro de 1.37%, seguido pelo EfficientNetV2B3 + CNN com um MCC de 92.60% e erro de 6.07%. Mesmo com valores similares, o primeiro aprensentou um melhor equilíbrio entre as classes, bem como usa uma CNN que realiza o processo de extração mais rapidamente. Dessa maneira, mesmo a configuração ResNet50 + SVM possuindo um maior tempo de treinamento e teste, o acerto entre as classes é mais harmônico, o que o torna melhor para a função.

Para trabalho futuros propõe-se o aumento do conjunto de dados, a fim de os modelos possam ter mais informações para seus processos de treinamento. Ademais, tem-se como intenção, investigar se adicionando uma camada de pré-processamento ao *pipeline* desenvolvido auxilia na melhor performance dos modelos, bem como pretende-se integrar o modelo a um sistema embarcado.