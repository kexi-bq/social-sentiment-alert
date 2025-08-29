from config import (
    KEYWORDS, TWEET_LIMIT,
    TELEGRAM_CHANNELS, TELEGRAM_ENABLED,
    SQL_DATABASE_URL
)
from fetch.telegram_scraper import fetch_telegram_messages
from fetch.realtime_listener import run_realtime_listener
from analysis.sentiment import analyze_sentiment
from analysis.signal_detector import is_signal_detected
from notifier.telegram_bot import send_alert
from storage.sql_storage import save_to_sql

import pandas as pd
from datetime import datetime
import os


LOG_PATH = "logs/sentiment_log.csv"


def save_to_log(df: pd.DataFrame) -> None:
    """
    пишет результаты в csv лог
    если файла нет создается новый
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["timestamp"] = now

    if not os.path.exists(LOG_PATH):
        df.to_csv(LOG_PATH, index=False)
    else:
        df.to_csv(LOG_PATH, mode="a", header=False, index=False)


def collect_historical_data() -> None:
    """
    собирает сообщения за выбранное количество часов назад
    сохраняет в лог и базу, если есть сигнал вызывает отправку алерта
    """
    try:
        hours = int(input("введите сколько часов назад собирать: "))
    except ValueError:
        print("неверный ввод, ожидалось число")
        return

    all_data = []
    for channel in TELEGRAM_CHANNELS:
        df = fetch_telegram_messages(channel, TWEET_LIMIT, hours_back=hours)
        if not df.empty:
            all_data.append(df)

    if not all_data:
        print("нет данных для анализа")
        return

    combined_df = pd.concat(all_data, ignore_index=True)
    analyzed_df = analyze_sentiment(combined_df)

    save_to_log(analyzed_df)
    save_to_sql(analyzed_df, SQL_DATABASE_URL)

    if is_signal_detected(analyzed_df):
        send_alert(analyzed_df)
    else:
        print("сигналов не обнаружено")


def menu() -> None:
    print("запуск мониторинга")
    print("1) анализ прошедших сообщений")
    print("2) режим реального времени")
    choice = input(">>> ")

    if choice == "1":
        collect_historical_data()
    elif choice == "2":
        run_realtime_listener()
    else:
        print("неверный выбор")


if __name__ == "__main__":
    menu()
