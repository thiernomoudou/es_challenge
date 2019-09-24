FROM python:3.6

WORKDIR /app

COPY . /app

Expose 8000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
