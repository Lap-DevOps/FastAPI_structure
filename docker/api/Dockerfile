FROM python:3.10-alpine
RUN mkdir -p usr/src/app
WORKDIR usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

