FROM python:3.9.10

ADD ./requirements.txt /app/

WORKDIR /app

COPY ./ ./

# RUN apt-get update && /usr/local/bin/python -m pip install --upgrade pip && pip install -r requirements.txt

# RUN ./deploy.sh