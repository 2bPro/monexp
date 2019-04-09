#!/usr/bin/env python
'''This is a very basic version of a producer created for the purpose
   of testing monitoring tools such as Zabbix and Prometheus
'''
import os
import json
import pika
import threading

# --------------------------------------------------------------------------- #
def main():
    amqp_url = os.environ.get("AMQP_URL")
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = create_channel(connection)
    count = 0

    while count < 1000:
        create_thread(channel)
        count = count + 1
    
    connection.close()

# --------------------------------------------------------------------------- #
def create_channel(connection):
    '''Channel exchange types:
       - fanout sends messages to all available queues
       - direct sends messages to the queues that have the same binding key as
         the routing key
       - topic sends messages to different queues depending on the topics
         described in the routing key (e.g. "quick.organge.fox" has 3 topics)
          - when a queue is bound with '#' it acts like fanout
          - when bindings are done with '*' and '#' it acts like a direct ex.
    '''
    print("Creating channel...")
    channel = connection.channel()
    channel.confirm_delivery()
    channel.queue_declare(durable=True, queue='jobs_queue')

    return channel

# --------------------------------------------------------------------------- #
def create_thread(channel):
    '''This is initialising messages for topic exchanges'''
    with open('/usr/src/app/messages.json', 'r') as jsf:
        messages = json.load(jsf)

        for name, message in messages.items():
            send_message(channel, message)

# --------------------------------------------------------------------------- #
def send_message(channel, message):
    print(" [P] Sending message...")
    channel.basic_publish(exchange='',
                          routing_key='jobs_queue',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              delivery_mode = 2,  # message persistency 0.2
                          )
                         )

    print(" [P] Sent message: " + message.get("message"))

# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    main()