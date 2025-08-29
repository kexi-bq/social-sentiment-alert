from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(df):
    """
    Принимает DataFrame с колонкой 'content' и возвращает тот же DF с колонкой 'sentiment'.
    """
    sentiments = []

    for text in df['content']:
        if not isinstance(text, str):
            sentiments.append(0)
            continue

        score = analyzer.polarity_scores(text)
        sentiments.append(score['compound'])  # Значение от -1 до 1

    df = df.copy()
    df['sentiment'] = sentiments
    return df
