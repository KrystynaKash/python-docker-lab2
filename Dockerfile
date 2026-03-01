# Пункт 3: ОС Linux (Debian) та Python 3.11
FROM python:3.11-slim

# Пункт 4: Створення папки
WORKDIR /Kashtanova_Krystyna

# Пункт 5: Копіювання файлів
COPY main.py .
COPY requirements.txt .

# Встановлення бібліотеки
RUN pip install --no-cache-dir -r requirements.txt

# Пункт 6: Команда для запуску
CMD ["python", "main.py"]