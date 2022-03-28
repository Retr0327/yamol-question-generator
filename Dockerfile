FROM python:3.9.10

RUN useradd myuser

USER myuser

WORKDIR /home/myuser

# COPY --chown=myuser:myuser requirements.txt requirements.txt

# RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser ./ ./


RUN pip install --user -r requirements.txt