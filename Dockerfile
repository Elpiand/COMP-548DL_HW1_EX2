FROM python:3.11

WORKDIR /app

COPY benchmark.py .

CMD ["python", "benchmark.py"]