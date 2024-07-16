import pika
import json

def send_message(source, destination):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='file_transfer_queue')

    message = json.dumps({'source': source, 'destination': destination})
    channel.basic_publish(exchange='',
                          routing_key='file_transfer_queue',
                          body=message)

    connection.close()

send_message('/path/to/source', 'user@remote:/path/to/destination')
