FROM python:3.9.0-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install 'tortoise[asyncpg]'
RUN pip uninstall -y tortoise-orm
RUN pip3 install tortoise-orm

COPY app .