FROM python:3.7-alpine

WORKDIR /code

COPY requirements.txt .

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget \
    && apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base git\
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del build-dependencies

COPY main.py .


ENTRYPOINT  ["python3.7", "main.py"]
