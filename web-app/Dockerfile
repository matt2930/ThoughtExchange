FROM python:3.6

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

# CMD ["python3","app.py"]
CMD ["gunicorn","--forwarded-allow-ips=*", "--bind", "0.0.0.0:5000", "wsgi:app"]
