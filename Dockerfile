FROM python:3.11

RUN pip install -U pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
