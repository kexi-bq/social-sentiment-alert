from typing import Any
import logging

import pandas as pd
from telegram import Bot, error as tg_error
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

logger = logging.getLogger(__name__)


def send_alert(df: pd.DataFrame) -> None:
    """
    Отправляет в телеграм короткую сводку по анализу сообщений
    """
    if df.empty:
        logger.warning("Попытка отправки с пустым DataFrame")
        return

    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # статистика
    num_mentions = len(df)
    avg_sentiment = float(df["sentiment"].mean())

    # топ посты по sentiment
    top_posts = (
        df.sort_values(by="sentiment", ascending=False)
        .head(3)
        .reset_index(drop=True)
    )

    lines = []
    lines.append("Сигнал обнаружен\n")
    lines.append(f"Упоминаний: {num_mentions}")
    lines.append(f"Средняя тональность: {avg_sentiment:.2f}\n")
    lines.append("Лучшие посты:\n")

    for _, row in top_posts.iterrows():
        text = str(row["content"])[:200].replace("\n", " ")
        score = float(row["sentiment"])
        lines.append(f"- {text}\n(sentiment {score:.2f})\n")

    message = "\n".join(lines)

    try:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
            parse_mode="Markdown"
        )
        logger.info("alert отправлен")
    except tg_error.TelegramError as e:
        logger.error("ошибка при отправке в телеграм: %s", e)
