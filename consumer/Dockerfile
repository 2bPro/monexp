FROM python:3.7-alpine
WORKDIR /usr/src/app
RUN pip3 install pika
ENV PYTHONUNBUFFERED=1

COPY receive.py .

CMD ["python3", "/usr/src/app/receive.py"]