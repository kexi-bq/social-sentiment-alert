from telethon.sync import TelegramClient, events
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_CHANNELS
from analysis.sentiment import analyze_sentiment
from analysis.signal_detector import is_signal_detected
from notifier.telegram_bot import send_alert

import pandas as pd


def run_realtime_listener() -> None:
    """
    слушает новые сообщения в указанных телеграм каналах
    анализирует их на тональность и при сигнале отправляет уведомление
    """
    print("ожидание новых сообщений в реальном времени...")

    client = TelegramClient(
        "telegram_session",
        TELEGRAM_API_ID,
        TELEGRAM_API_HASH,
        device_model="SentimentListener",
        system_version="Linux",
        app_version="1.0"
    )

    @client.on(events.NewMessage(chats=TELEGRAM_CHANNELS))
    async def handler(event):
        text = event.message.message
        ts = event.message.date
        uid = event.message.sender_id

        if not text:
            return

        df = pd.DataFrame([{
            "content": text,
            "date": ts,
            "username": uid
        }])

        analyzed = analyze_sentiment(df)
        if is_signal_detected(analyzed):
            send_alert(analyzed)

    with client:
        client.run_until_disconnected()
