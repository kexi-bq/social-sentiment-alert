from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta, timezone
import pandas as pd

from config import TELEGRAM_API_ID, TELEGRAM_API_HASH


def fetch_telegram_messages(channel_username: str, limit_per_page: int = 100, hours_back: int = 1) -> pd.DataFrame:
    """
    получает текстовые сообщения за последние n часов из указанного канала
    """
    client = TelegramClient(
        session="telegram_session",
        api_id=TELEGRAM_API_ID,
        api_hash=TELEGRAM_API_HASH,
        device_model="SentimentScraper",
        system_version="Linux",
        app_version="1.0"
    )

    since_time = datetime.now(timezone.utc) - timedelta(hours=hours_back)
    messages = []

    with client:
        channel = client.get_entity(channel_username)
        offset_id = 0

        while True:
            history = client(GetHistoryRequest(
                peer=channel,
                limit=limit_per_page,
                offset_date=None,
                offset_id=offset_id,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            if not history.messages:
                break

            for msg in history.messages:
                if not msg.message or msg.media:
                    continue
                if msg.date < since_time:
                    return pd.DataFrame(messages)

                messages.append({
                    "content": msg.message,
                    "date": msg.date,
                    "username": msg.sender_id or "unknown"
                })

            offset_id = history.messages[-1].id

    if not messages:
        return pd.DataFrame(columns=["content", "date", "username"])

    return pd.DataFrame(messages)
