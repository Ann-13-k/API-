#!/bin/sh

# Ждём базу данных (если используем Postgres)
# sleep 5  # можно раскомментировать при необходимости

# Применяем миграции
python manage.py migrate --no-input

# Собираем статику
python manage.py collectstatic --no-input

# Запускаем Gunicorn
gunicorn django_practicum.wsgi:application -b 0.0.0.0:8000 --workers 3 --threads 3
