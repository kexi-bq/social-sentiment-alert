import praw
import pandas as pd
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT


def fetch_reddit_posts(keywords, limit: int = 100) -> pd.DataFrame:
    """
    тянет посты из reddit по ключевым словам
    возвращает dataframe с базовыми полями
    """
    if not keywords:
        return pd.DataFrame(columns=["keyword", "title", "content", "date", "username", "url"])

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    results = []
    for kw in keywords:
        subreddit = reddit.subreddit("all")
        for submission in subreddit.search(kw, limit=limit):
            results.append({
                "keyword": kw,
                "title": submission.title,
                "content": submission.selftext,
                "date": submission.created_utc,
                "username": submission.author.name if submission.author else "unknown",
                "url": submission.url
            })

    if not results:
        return pd.DataFrame(columns=["keyword", "title", "content", "date", "username", "url"])

    return pd.DataFrame(results)
