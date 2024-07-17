import pika
import json
from config import Config

from jaws_transfers.tasks import rsync_transfer

def create_connection(config_file=None):
    config = Config(config_file)
    connection_params = pika.ConnectionParameters(
        host=config.rabbitmq_host,
        virtual_host=config.rabbitmq_vhost,
        credentials=pika.PlainCredentials(config.rabbitmq_user, config.rabbitmq_password)
    )
    connection = pika.BlockingConnection(connection_params)
    return connection


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

def main(config_file=None):
    connection = create_connection(config_file)
    channel = connection.channel()
    channel.queue_declare('file_transfer_queue')
    channel.basic_consume(queue='file_transfer_queue', on_message_callback=callback)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    import sys
    config_file = sys.argv[1] if len(sys.argv) > 1 else None
    main(config_file)