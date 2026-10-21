FROM python:3.10-slim
RUN apt-get update && apt-get install -y ffmpeg imagemagick git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN git clone https://github.com/harry0703/MoneyPrinterTurbo.git /app/MoneyPrinterTurbo
RUN pip install --no-cache-dir -r /app/MoneyPrinterTurbo/requirements.txt
RUN pip install --no-cache-dir python-telegram-bot==20.7 Flask
CMD ["python", "bot.py"]