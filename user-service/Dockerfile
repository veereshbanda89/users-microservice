# https://hub.docker.com/layers/library/python/3.10-slim/images/sha256-b22d43a1278b3d417219cc2cdc375866d23ebcfb9d852b13b974d421158f6c08?context=explore
FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt


RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# RUN apt install 

RUN pip3 install -r /app/requirements.txt

COPY . /app/