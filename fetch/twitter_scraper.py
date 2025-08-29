import snscrape.modules.twitter as sntwitter
import pandas as pd


def fetch_tweets(keywords, limit: int = 100) -> pd.DataFrame:
    """
    тянет твиты по списку ключевых слов
    возвращает dataframe с колонками content, date, username
    """
    if not keywords:
        return pd.DataFrame(columns=["content", "date", "username"])

    query = " OR ".join(keywords) + " lang:en"
    tweets = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append({
            "content": tweet.content,
            "date": tweet.date,
            "username": tweet.user.username
        })

    return pd.DataFrame(tweets)
