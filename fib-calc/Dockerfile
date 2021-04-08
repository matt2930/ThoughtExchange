FROM python:3.6

WORKDIR /usr/src/fib

COPY ./ ./

# RUN apt-get update
# RUN apt-get install rabbitmq-server -y

RUN pip install --no-cache -r requirements.txt

CMD ["python3", "-u", "fib.py"]
