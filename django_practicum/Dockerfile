# Используем официальный образ Python
FROM python:3.13-slim

# Не сохраняем pyc, вывод без буфера
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Рабочая директория внутри контейнера
WORKDIR /usr/src/app

# Копируем зависимости
COPY requirements.txt .

# Обновляем pip и ставим зависимости
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Делаем статическую папку (для collectstatic)
RUN mkdir -p /usr/src/app/static/

# Копируем entrypoint
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Делаем его исполняемым
RUN chmod +x /usr/src/app/entrypoint.sh

# Запуск контейнера через entrypoint
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
