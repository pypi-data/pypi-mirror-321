import pika
from time import sleep
import logging


logger = logging.getLogger(__name__)
logging.getLogger("pika").setLevel(logging.WARNING)


class WabbitMQ:
    def __init__(self, queue_name: str, server: str = 'rabbitmq'):
        self.server = server
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.server, heartbeat=300))
        logger.info(f'Connected to {self.server}, opening channel')
        self.channel = self.connection.channel()
        logger.info(f'Channel opened: {self.channel}, creating queue')
        self.queue_name = queue_name
        self.queue = self.create_queue()
        logger.info(f'Queue created: {self.queue}')

    def create_queue(self):
        return self.channel.queue_declare(queue=self.queue_name)

    def publish(self, message: str):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
        logger.info(f" [x] Sent:    {message}")

    def consume(self, callback: object = None):
        def _callback(ch, method, properties, body):
            message = body.decode('utf-8')
            logger.info(f" [x] Received: {message}")
            sleep(1)

        callback = callback if callback is not None else _callback
        self.channel.basic_consume(queue=self.queue_name, auto_ack=True, on_message_callback=callback)
        while True:
            try:
                logger.info(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()
            except ConnectionResetError:
                pass

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S')
    wabbit = WabbitMQ()
    wabbit.publish('test message')
