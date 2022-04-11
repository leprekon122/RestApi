FROM python:latest

COPY ./ requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . / rest_api ./



