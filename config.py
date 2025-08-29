# ключевые слова для поиска
KEYWORDS = [
    "Tesla", "TSLA", "Elon Musk",
    "Apple", "AAPL",
    "Bitcoin", "BTC",
    "Nvidia", "NVDA",
]

# сколько сообщений тянуть за один запуск
TWEET_LIMIT = 500  # было 10**10, оставил адекватное число

# пороги для срабатывания сигнала
SENTIMENT_THRESHOLD = 0.3
MENTIONS_THRESHOLD = 15

# интервал запуска (минуты)
JOB_INTERVAL_MINUTES = 15

# источники
TWITTER_ENABLED = False
REDDIT_ENABLED = False
TELEGRAM_ENABLED = True

# параметры телеграм-бота
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# telethon api ключи
TELEGRAM_API_ID = 
TELEGRAM_API_HASH = ""

# список каналов
TELEGRAM_CHANNELS = [
    "AK47pfl",
]

# postgres
DB_NAME = "sentiment_db"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "db"   # имя сервиса из docker-compose
DB_PORT = 5432

# строка подключения
SQL_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
