FROM python:3.11

RUN mkdir -p /otp/service/manga-backend

WORKDIR /otp/service/manga-backend

COPY requirements /otp/service/manga-backend/requirements
COPY requirements.txt /otp/service/manga-backend

RUN pip install -r requirements.txt