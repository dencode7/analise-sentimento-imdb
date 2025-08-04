import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Carregar o conjunto de dados
df = pd.read_csv('../data/IMDB Dataset.csv')

# Exibir os dados originais
print("Dados originais:")
print(df.head())
print("-" * 50)

# Inicializar o stemmer e a lista de stop words
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    """
    Função para pré-processar o texto.
    """
    # 1. Remover tags HTML
    text = re.sub(r'<.*?>', '', text)

    # 2. Remover caracteres especiais e pontuação
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 3. Converter para minúsculas
    text = text.lower()

    # 4. Remover stop words (palavras irrelevantes como 'a', 'o', 'e')
    text = ' '.join([word for word in text.split() if word not in stop_words])

    # 5. Stemming (reduzir a palavra à sua raiz)
    text = ' '.join([stemmer.stem(word) for word in text.split()])

    return text


# Aplicar a função de pré-processamento à coluna 'review'
df['clean_review'] = df['review'].apply(preprocess_text)

# Exibir os dados após a limpeza
print("Dados após o pré-processamento:")
print(df.head())
print("-" * 50)

# Salvar o conjunto de dados limpo
df.to_csv('../data/imdb_limpo.csv', index=False)
print("Dados limpos e processados salvos com sucesso em 'data/imdb_limpo.csv'.")