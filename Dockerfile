FROM python:3.9.10

ADD ./requirements.txt /app/

WORKDIR /app

COPY ./yamol ./

RUN apt-get update && pip install -r requirements.txt
