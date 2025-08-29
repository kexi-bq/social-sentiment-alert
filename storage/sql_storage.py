import psycopg2
from psycopg2.extras import execute_values
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def connect():
    """
    подключение к postgres
    """
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def init_db() -> None:
    """
    создаем таблицу если её ещё нет
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists messages (
            id serial primary key,
            content text,
            date timestamp,
            username text,
            sentiment real,
            timestamp timestamp
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def save_to_postgresql(df) -> None:
    """
    сохраняет dataframe в postgres
    """
    if df.empty:
        return

    init_db()
    conn = connect()
    cur = conn.cursor()

    rows = [
        (
            row["content"],
            row["date"],
            row["username"],
            row.get("sentiment", 0.0),
            row.get("timestamp")
        )
        for _, row in df.iterrows()
    ]

    execute_values(
        cur,
        "insert into messages (content, date, username, sentiment, timestamp) values %s",
        rows
    )
    conn.commit()
    cur.close()
    conn.close()
