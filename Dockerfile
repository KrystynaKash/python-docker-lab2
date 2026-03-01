# Пункт 3: ОС Linux (Debian) та Python 3.11
FROM python:3.11-slim

# Пункт 4: Створити папку (заміни Prizvysche на своє)
WORKDIR /Prizvysche_Imya

# Пункт 5: Копіюємо файли
COPY main.py .
COPY requirements.txt .

# Встановлюємо бібліотеку
RUN pip install --no-cache-dir -r requirements.txt

# Пункт 6: Команда для запуску
CMD ["python", "main.py"]