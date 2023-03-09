FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

