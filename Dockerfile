FROM python:3.9-slim

ARG DATABASE_URL
ARG SECRET_KEY=local-secret-key
ARG DEBUG=True

LABEL maintainer=vinay.kudari30@gmail.com \
    name=treat-covid-at-home-api

ENV APP_USER=admin \
    APP_ROOT=/code \
    APP_NAME=treat-covid-at-home-api \
    LOG_LEVEL=info \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=${DEBUG} \
    SECRET_KEY=${SECRET_KEY} \
    PORT=8080

WORKDIR $APP_ROOT

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    postgresql-client \
    wget \
    python-psycopg2 \
    && \
    apt-get clean

COPY requirements.txt $APP_ROOT
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . $APP_ROOT

WORKDIR $APP_ROOT

RUN python3 manage.py migrate --no-input

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 --worker-class=gevent app.wsgi:application