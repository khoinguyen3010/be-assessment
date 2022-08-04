FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /app/

EXPOSE 8000

CMD ["gunicorn", "main_app.wsgi", "-b", "0.0.0.0:8000", "-w", "4"]
