FROM python:3.6

WORKDIR /usr/src/queue

COPY ./queue.py ./
COPY ./requirements.txt ./

RUN pip install --no-cache -r requirements.txt

RUN apt-get update
RUN apt-get install rabbitmq-server -y

RUN service rabbitmq-server start

CMD ["python3","queue.py"]
