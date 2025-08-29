from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# добавляем путь до корня проекта чтобы видеть main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import process  # точка входа

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["your_email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "social_sentiment_alert",
    default_args=default_args,
    description="мониторинг соцсетей и анализ тональности",
    schedule_interval="*/15 * * * *",  # каждые 15 минут
    start_date=datetime(2024, 4, 1),
    catchup=False,
    tags=["sentiment", "social", "alerts"]
)

run_sentiment_alert = PythonOperator(
    task_id="run_sentiment_monitoring",
    python_callable=process,
    dag=dag,
)
