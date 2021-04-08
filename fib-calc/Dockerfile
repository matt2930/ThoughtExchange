FROM python:3.6

WORKDIR /usr/src/fib

COPY ./ ./

RUN apt-get update
RUN apt-get install rabbitmq-server -y

RUN pip install --no-cache -r requirements.txt

RUN service rabbitmq-server start
CMD ["python3","fib.py"]
