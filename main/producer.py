import json

import pika
from pika import channel, connection

params = pika.URLParameters('amqps://jobkmzrp:Xdhn0fWxXVadN_kXbEyZK31M1ykqrHz9@roedeer.rmq.cloudamqp.com/jobkmzrp')


connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
 