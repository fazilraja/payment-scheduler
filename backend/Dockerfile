FROM python:3.11

WORKDIR /app

ENV FLASK_APP = server.py

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "server.py"]