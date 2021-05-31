FROM python:3.9-slim-buster

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY gcloud-emulators-docker-python/main.py /app/

ENV BIGTABLE_EMULATOR_HOST=127.0.0.1:8086
ENTRYPOINT python /app/main.py
