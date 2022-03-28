FROM python:3.9.10

RUN useradd myuser

USER myuser

WORKDIR /home/myuser

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser ./ ./

RUN pip install --user -r requirements.txt