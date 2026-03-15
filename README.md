# Labs

## Análise da influência de argumentos persuasivos sobre um LLM

No trabalho ["Measuring the Persuasiveness of Language Models"](https://www.anthropic.com/news/measuring-model-persuasiveness) é estudado como argumentos persuasivos, gerados por LLM, podem afetar as avaliações feitas por pessoas.

Em um primeiro momento, os participantes do estudo precisam avaliar uma alegação em uma escala Likert de 1 a 7 (`rating_initial`). Após essa avaliação, é pedido que novamente as pessoas façam uma avaliação (`rating_final`), agora levando em conta argumentos gerados por modelos LLMs (compactos e de fronteira). Os autores consideram uma forma simples de medir o efeito persuasivo deste argumento na resposta, utilizando a seguinte métrica: `persuasiveness_metric = rating_final - rating_initial`.

Motivado por este estudo, cujo dataset é disponibilizado na Hugging Face ([`Anthropic/persuasion`](https://huggingface.co/datasets/Anthropic/persuasion)), realizamos testes para checar o efeito dos argumentos persuasivos (`argument`) nas avaliações que um modelo de LLM escolhido faz das alegações disponibilizadas na base de dados (`claim`).

Será que um modelo de LLM muda sua avaliação inicial de uma alegação, após levar em conta argumentos persuasivos em seu contexto?

<img src="./llm_persuasive_arguments/imgs/rating_changes_graph_human.png">

### Conteúdo

- Checa algumas informações sobre o dataset [`Anthropic/persuasion`](https://huggingface.co/datasets/Anthropic/persuasion), seguindo o artigo: ["Measuring the Persuasiveness of Language Models"](https://www.anthropic.com/news/measuring-model-persuasiveness).
  
- Realiza testes com modelos LLM em subconjunto de amostras para um estudo inicial.

- Prepara dataset para testes considerando os argumentos persuasivos gerados pelo modelo `Claude 3 Opus` de acordo com os seguintes tipos de prompt, descritos no artigo:

    - `Compelling Case` (**convincente**): o modelo gera um argumento convincente, buscando convencer alguém em cima do muro.

    - `Logical Reasoning` (**lógico**): o modelo elabora argumentos usando raciocínio lógico, tentando trazer clareza e transparência nos seus argumentos.

    - `Expert Writer Rhetorics` (**retórico**): o modelo cria argumentos persuasivos como um especialista em retórica, utilizando-se de _pathos_ (apelo às emoções do leitor; por ex., contar uma história emocionante para gerar empatia), _logos_ (apelo à lógica e razão; por ex., apresentar estatísticas na argumentação) e _ethos_ (apelo à credibilidade ou autoridade; por ex., citar especialistas numa certa área).

    - `Deceptive` (**falacioso**):  o modelo formula argumentos que parecem verossímeis, mas são amparados por fatos e fontes inventadas, de forma que o argumento criado seja o mais convincente possível.

- Roda localmente um modelo LLM disponibilizado na Hugging Face para classificar as alegações humanas _com_ e _sem_ a presença dos argumentos persuasivos.

- Usa a estrutura do artigo para classificação das alegações feitas pelo `modelo LLM de testes`:

  - `1 - Strongly oppose`

  - `2 - Oppose`

  - `3 - Somewhat oppose`

  - `4 - Neither oppose nor support`

  - `5 - Somewhat support`

  - `6 - Support`

  - `7 - Strongly support`
  
- Gera gráficos para análise dos resultados

### Notebooks
- [prepare_dataset](./llm_persuasive_arguments/01.prepare_dataset.ipynb)
- [initial_tests_eval](./llm_persuasive_arguments/02.initial_tests_eval.ipynb)
- [eval_sample_dataset](./llm_persuasive_arguments/03.eval_sample_dataset.ipynb)
- [eval_input_dataset](./llm_persuasive_arguments/04.eval_input_dataset.ipynb)

<br/>

<img src="./llm_persuasive_arguments/imgs/std_persuasiveness_metric.gif">

<br/>

---

<br/>

## Modelagem com auto ML e LLM para predição de sucesso em campanha de telemarketing

### Objetivo

Classificar se um cliente irá (ou não) realizar um depósito, levando em conta informações de campanhas de marketing via telefone.

<img src="./pred_telemarketing_success/imgs/metrics_llm.png" size="70%">

### Conteúdo

  - Uso de auto ML para análise exploratória (EDA) e treinamento de modelos de machine learning.
  
  - Análise de correlação de features; geração de gráficos e visualizações para EDA.
  
  - Geração de relatórios automatizados em html, contendo informações sobre a qualidade do dataset de treino.

  - Cálculo de métricas de performance para o modelo ótimo.

  - Uso de LLM para explicar os resultados obtidos.
  
### Dataset
[Bank Marketing (UCI)](https://archive.ics.uci.edu/dataset/222/bank+marketing)

### Notebook
[pred_telemarketing_product_acquisition_success](pred_telemarketing_success/pred_telemarketing_product_acquisition_success.ipynb)
  

---

<br/>



## Multi-agentes de IA para análises de revisões de papers

A partir de uma [base de reviews de artigos (UCI)](https://archive.ics.uci.edu/dataset/410/paper+reviews) e Langchain, criamos uma chain com três agentes para analisar questões sobre um tema escolhido por um usuário. A partir deste input, o mini sistema de multi-agentes busca esclarecer a questão/tópico questionado: um deles responde as questões de forma generalista; outro busca responder usando o contexto do dataset disponibilizado (RAG); e outro realiza uma busca de vídeos no Youtube para complementar a resposta.

<img src="./analyse_reviews_multi_agents/imgs/multi_agents_paper_reviews.png" size="60%">


### Conteúdo

- Criação de vector store (FAISS) a partir de embbedings calculados com um modelo disponibilizado na Hugging Face.

- Buscas por similaridade e prompts com retrievers.

- Testes com elementos do Langchain: prompt template, tools, retrievers, chains e runnable parallel.

- Implementação de multi-agentes com tools e RAG.


### Notebooks

-  [prepare_data](./analyse_reviews_multi_agents/01.prepare-data.ipynb)

-  [create-paper-review-agent](./analyse_reviews_multi_agents/02.create-paper-review-agent.ipynb)



---

<br/>

## RAG local para sessão de perguntas e resposta sobre o cardápio de hoje

Neste lab testamos a extração de conteúdo de texto via OCR de uma imagem de cardápio. Realizamos o parsing do texto OCR com LLM e implementamos uma agente com RAG simples para responder questões sobre o cardápio fornecido.

<img src="./local_rag_qa_menu/imgs/rag_menu.png" size="70%">


### Conteúdo
  
- Usa OCR (Tesseract) para extrair informações de um cardápio na forma de imagem (PNG).

- Realiza o parsing das informações extraídas usando uma LLM.

- Exporta as informações estruturadas com CSV e JSON.

- Gera embedding a partir de informações da imagem do cardápio estruturadas, usando modelo disponibilizado pela Hugging Face.

- Cria banco vetorial (FAISS) e realiza buscas semânticas.

- Realiza sessão de perguntas e respostas sobre o cardápio fornecido.

### Notebooks
-  [read_menu](./local_rag_qa_menu/01.read_menu.ipynb)

-  [rag_qa_menu](./local_rag_qa_menu/02.rag_qa_menu.ipynb)


<br/>