# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster


WORKDIR /home/harshit/Documents/techathon/

COPY requirements.txt requirements.txt

RUN  apt update

RUN  apt install -y gcc

RUN  apt install -y g++

RUN  apt install -y nodejs

RUN apt install --no-install-recommends -y r-base

RUN apt install -y default-jdk

RUN apt install -y default-jre



RUN pip3 install -r requirements.txt

COPY . .


CMD gunicorn --bind 0.0.0.0:${PORT} --log-file=logs/all.log --log-level=info --access-logfile=logs/access.log app:app