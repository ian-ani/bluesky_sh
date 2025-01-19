# image
FROM python:3.12.7-alpine

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/src/ .