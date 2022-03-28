FROM python:3.9.10

RUN useradd yamol_user

USER yamol_user

WORKDIR /home/yamol_user

ENV PATH="/home/yamol_user/.local/bin:${PATH}"

COPY --chown=yamol_user:yamol_user ./ ./

RUN pip install --user -r requirements.txt