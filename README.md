# Projeto: Análise de Sentimento de Avaliações de Filmes

### Introdução

Este projeto consiste em uma análise completa de um conjunto de dados de 50.000 avaliações de filmes do IMDB. O objetivo é utilizar técnicas de Processamento de Linguagem Natural (PLN) para determinar o sentimento das avaliações (positivo ou negativo) e identificar as palavras-chave mais relevantes para cada categoria de sentimento.

### Tecnologias Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas e ferramentas:

* **Pandas:** Para manipulação e limpeza dos dados.
* **NLTK e Re:** Para pré-processamento e limpeza de texto.
* **TextBlob:** Para realizar a análise de sentimento.
* **Matplotlib, Seaborn e WordCloud:** Para visualização de dados e criação de nuvens de palavras.
* **Jupyter Notebook:** Para a documentação e execução interativa da análise.
* **Git & GitHub:** Para controle de versão e hospedagem do projeto.

### Estrutura do Projeto

A estrutura de pastas foi organizada para manter o projeto limpo e organizado:

Perfeito! Agora que todos os problemas de configuração foram resolvidos e seu projeto foi enviado para o GitHub, o último passo é criar o README.md.

Este arquivo transformará seus scripts em uma apresentação profissional, explicando o que você fez e os resultados que alcançou.

Aqui está um modelo de README.md completo e bem estruturado para o seu projeto de Análise de Sentimento. Basta copiar o texto abaixo e criar um arquivo com o nome README.md na pasta raiz do seu projeto no GitHub.

Conteúdo para o README.md:
Markdown

# Projeto: Análise de Sentimento de Avaliações de Filmes

### Introdução

Este projeto consiste em uma análise completa de um conjunto de dados de 50.000 avaliações de filmes do IMDB. O objetivo é utilizar técnicas de Processamento de Linguagem Natural (PLN) para determinar o sentimento das avaliações (positivo ou negativo) e identificar as palavras-chave mais relevantes para cada categoria de sentimento.

### Tecnologias Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas e ferramentas:

* **Pandas:** Para manipulação e limpeza dos dados.
* **NLTK e Re:** Para pré-processamento e limpeza de texto.
* **TextBlob:** Para realizar a análise de sentimento.
* **Matplotlib, Seaborn e WordCloud:** Para visualização de dados e criação de nuvens de palavras.
* **Jupyter Notebook:** Para a documentação e execução interativa da análise.
* **Git & GitHub:** Para controle de versão e hospedagem do projeto.

### Estrutura do Projeto

A estrutura de pastas foi organizada para manter o projeto limpo e organizado:

.

├── data/
│   ├── IMDB Dataset.csv
│   └── imdb_limpo.csv

├── notebooks/
│   └── analise_sentimento.ipynb
├── reports/
│   ├── distribuicao_sentimento.png
│   ├── wordcloud_negativo.png
│   └── wordcloud_positivo.png

└── scripts/
├── analise_sentimento.py
└── limpeza_texto.py


### Análise e Resultados

#### 1. Pré-processamento de Texto

A etapa de limpeza de texto foi crucial para preparar os dados não estruturados para a análise. O processo incluiu:
-   Remoção de tags HTML e caracteres especiais.
-   Conversão do texto para minúsculas.
-   Remoção de "stop words" (palavras irrelevantes como 'o', 'a', 'de').
-   Aplicação de *Stemming* para reduzir as palavras às suas raízes (ex: "running" -> "run").

#### 2. Análise de Sentimento

Utilizando a biblioteca TextBlob, cada avaliação foi classificada como `positive`, `negative` ou `neutral` com base em sua polaridade. A maioria das avaliações no conjunto de dados foi classificada como positiva.

#### 3. Visualização de Dados

Os gráficos e nuvens de palavras gerados revelaram insights importantes:
-   **Distribuição de Sentimento:** Um gráfico de barras mostrou a proporção de avaliações positivas e negativas.
-   **Nuvens de Palavras:** Nuvens de palavras distintas foram criadas para avaliações positivas e negativas, destacando as palavras mais comuns em cada grupo. Isso ajudou a identificar os termos que mais influenciam o sentimento dos clientes (ex: "great", "love" vs. "bad", "worst").

### Como Executar o Projeto

1.  **Clone o repositório:**
    `git clone https://github.com/dencode7/analise-sentimento-imdb.git`
2.  **Navegue para a pasta do projeto:**
    `cd analise-sentimento-imdb`
3.  **Inicie o Jupyter Notebook:**
    `jupyter notebook`
4.  Abra o arquivo `notebooks/analise_sentimento.ipynb` para ver a análise completa e interativa.
