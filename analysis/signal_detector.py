from config import SENTIMENT_THRESHOLD, MENTIONS_THRESHOLD

def is_signal_detected(df):
    """
    Проверяет, стоит ли отправлять сигнал по текущим данным.
    Учитывает:
      - количество сообщений
      - среднюю тональность
    Возвращает True или False
    """

    num_mentions = len(df)
    avg_sentiment = df['sentiment'].mean() if num_mentions > 0 else 0

    print(f"🧾 Найдено упоминаний: {num_mentions}")
    print(f"📈 Средняя тональность: {avg_sentiment:.3f}")

    if num_mentions >= MENTIONS_THRESHOLD and avg_sentiment >= SENTIMENT_THRESHOLD:
        return True
    else:
        return False
