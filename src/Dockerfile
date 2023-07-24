# pull official base image
FROM python:3.11.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt .

# install system dependencies
RUN  apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN  pip install --upgrade pip \
  && pip install -r requirements.txt

# add app
COPY . .