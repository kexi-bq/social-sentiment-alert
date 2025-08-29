# Social Sentiment Alert

Система мониторинга соцсетей с анализом тональности и уведомлениями в Telegram.  
Работает автоматически: каждые N минут собирает посты, определяет настроение и сообщает о потенциальных рыночных сигналах.  

A monitoring system for social networks with sentiment analysis and Telegram alerts.  
It runs automatically: every N minutes it fetches posts, evaluates sentiment, and reports potential market signals.  

---

## Возможности / Features

- сбор сообщений из Twitter, Reddit и Telegram  
- анализ тональности (VADER)  
- определение всплесков интереса и изменения настроений  
- уведомления в Telegram при срабатывании сигнала  
- сохранение данных в PostgreSQL и CSV  
- опционально запуск через Airflow или APScheduler  

- fetch posts from Twitter, Reddit and Telegram  
- sentiment analysis using VADER  
- detect spikes in mentions and sentiment trends  
- send Telegram alerts when a signal is triggered  
- save all data in PostgreSQL and CSV  
- optional scheduling with Airflow or APScheduler  

---

## Установка / Installation

1. скачайте проект и перейдите в каталог  
   download the project and enter the folder  

2. поднимите сервисы через docker-compose  
   start the services with docker-compose  
   ```bash
   docker-compose up --build
