FROM python:3.8-alpine

WORKDIR /app/api

ADD ./requirements.txt /app/api

RUN pip install --no-cache-dir -r requirements.txt

ADD . /app/api

EXPOSE 5000
CMD ["python", "app.py"]