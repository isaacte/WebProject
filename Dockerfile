FROM python:3

RUN mkdir /home/Practica1/

WORKDIR /home/Practica1/

COPY . /home/Practica1/

RUN pip install -r requirements.txt
