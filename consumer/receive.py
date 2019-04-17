#!/usr/bin/env python
'''This is a very basic version of a consumer created for the purpose
   of testing monitoring tools such as Zabbix and Prometheus
'''
import os
import json
import pika
import time

# --------------------------------------------------------------------------- #
def main():
    amqp_url = os.environ.get("AMQP_URL")
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    
    create_channel(connection)

    connection.close()
    
# --------------------------------------------------------------------------- #
def create_channel(connection):
    print("Creating channel...")
    channel = connection.channel()
    channel.exchange_declare(exchange='jobs_queue', exchange_type='fanout')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='jobs_queue', queue=queue_name)

    channel.basic_consume(queue=queue_name,
                          on_message_callback=receive_message,
                         )

    print("Waiting for messages...")
    channel.start_consuming()
        
# --------------------------------------------------------------------------- #
def receive_message(ch, method, properties, body):
    data = json.loads(body)
    time.sleep(1)
    print(" [C] Received " + data.get("message"))
    ch.basic_ack(delivery_tag = method.delivery_tag)

# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    main()