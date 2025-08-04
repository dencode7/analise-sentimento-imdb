import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Configurações do estilo dos gráficos
sns.set_style('whitegrid')

# 1. Carregar os dados limpos
df = pd.read_csv('../data/imdb_limpo.csv')

# Exibir as primeiras linhas do dataframe limpo para confirmar
print("Visualizando os dados limpos:")
print(df.head())
print("-" * 50)


# 2. Análise de Sentimento
# A coluna 'clean_review' contém o texto processado.
# Vamos calcular a polaridade de cada review.
def get_sentiment(text):
    """
    Função para calcular o sentimento (polaridade) do texto.
    A polaridade varia de -1 (negativo) a 1 (positivo).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Criar uma nova coluna com a polaridade
df['sentiment_score'] = df['clean_review'].apply(get_sentiment)

# Criar uma coluna de sentimento categórico (positivo, negativo, neutro)
def get_sentiment_category(score):
    if score > 0.1:
        return 'positive'
    elif score < -0.1:
        return 'negative'
    else:
        return 'neutral'

df['sentiment_category'] = df['sentiment_score'].apply(get_sentiment_category)


# 3. Visualização da Distribuição do Sentimento
plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment_category', data=df)
plt.title('Distribuição de Sentimento das Avaliações')
plt.xlabel('Categoria de Sentimento')
plt.ylabel('Número de Avaliações')
plt.savefig('../reports/distribuicao_sentimento.png')
plt.show()


# 4. Visualização com Nuvem de Palavras
# Criar uma nuvem de palavras para reviews positivos
positive_reviews = ' '.join(df[df['sentiment_category'] == 'positive']['clean_review'])
wordcloud_pos = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_pos, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras - Avaliações Positivas')
plt.savefig('../reports/wordcloud_positivo.png')
plt.show()

# Criar uma nuvem de palavras para reviews negativos
negative_reviews = ' '.join(df[df['sentiment_category'] == 'negative']['clean_review'])
wordcloud_neg = WordCloud(width=800, height=400, background_color='white').generate(negative_reviews)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_neg, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras - Avaliações Negativas')
plt.savefig('../reports/wordcloud_negativo.png')
plt.show()


print("Análise de sentimento e gráficos gerados e salvos na pasta 'reports/'.")