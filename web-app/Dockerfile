FROM python:3.7

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["gunicorn","--forwarded-allow-ips=*", "--bind", "0.0.0.0:5000", "wsgi:app"]
