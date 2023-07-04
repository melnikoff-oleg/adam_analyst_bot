FROM python:3.10


WORKDIR /usr/src/code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --no-cache-dir --upgrade pip setuptools
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .
