import pika
import json

from jaws_transfers.tasks import rsync_transfer

def callback(ch, method, properties, body):
    data = json.loads(body)
    source = data.get('source')
    destination = data.get('destination')

    if source and destination:
        print(f"Received message: {source} -> {destination}")
        rsync_transfer.delay(source, destination)
    else:
        print("Invalid message: source and destination are required")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare('file_transfer_queue')

    channel.basic_consume(queue='file_transfer_queue', on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()