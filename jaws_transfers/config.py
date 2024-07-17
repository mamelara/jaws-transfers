import configparser
import os


class Config:
    def __init__(self, config_file=None):
        self.config = configparser.ConfigParser()

        # Read from specified config file path if provided
        if config_file:
            self.config.read(config_file)
        else:
            self.config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

    @property
    def rabbitmq_host(self):
        return os.getenv('RABBITMQ_HOST', self.config.get('default', 'RABBITMQ_HOST', fallback='localhost'))

    @property
    def rabbitmq_queue(self):
        return os.getenv('RABBITMQ_QUEUE', self.config.get('default', 'RABBITMQ_QUEUE', fallback='api_request_queue'))

    @property
    def rabbitmq_user(self):
        return os.getenv('RABBITMQ_USER', self.config.get('default', 'RABBITMQ_USER', fallback='guest'))

    @property
    def rabbitmq_password(self):
        return os.getenv('RABBITMQ_PASSWORD', self.config.get('default', 'RABBITMQ_PASSWORD', fallback='guest'))

    @property
    def rabbitmq_vhost(self):
        return os.getenv('RABBITMQ_VHOST', self.config.get('default', 'RABBITMQ_VHOST', fallback='/'))


