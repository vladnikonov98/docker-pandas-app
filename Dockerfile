# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY data.csv data.csv

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Указываем команду запуска
CMD ["python", "app.py"]