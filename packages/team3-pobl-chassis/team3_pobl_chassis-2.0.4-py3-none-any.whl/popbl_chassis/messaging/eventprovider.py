import asyncio
import logging.config
import random
import ssl

import aio_pika
from aio_pika import IncomingMessage, ExchangeType


class EventProvider:

    connection: aio_pika.RobustConnection = None
    channel: aio_pika.Channel = None
    exchange_name = None
    exchange: aio_pika.RobustExchange = None
    rabbitmq_hosts = None
    rabbitmq_user = None
    rabbitmq_password = None
    logger: logging.Logger = None
    ssl_context = None
    

    @classmethod
    async def create(cls, rabbitmq_hosts, rabbitmq_user, rabbitmq_password, logger: logging.Logger, exchange_name: str = 'events'):
        self = EventProvider()
        self.rabbitmq_hosts = rabbitmq_hosts.split(',')
        self.rabbitmq_user = rabbitmq_user
        self.rabbitmq_password = rabbitmq_password
        self.logger = logger
        self.exchange_name = exchange_name
        self.ssl_context = ssl.create_default_context(cafile="./code/certificates/certs/cacert.pem")
        self.ssl_context.load_cert_chain(certfile="./code/certificates/certs/rabbitmq.pem", keyfile="./code/certificates/private/rabbitmq.pem")
     
        await self.subscribe_channel(exchange_name)
        return self

    async def subscribe_channel(self, exchange_name):
        retries = 5
        for attempt in range(retries):
            try:
                self.connection = await aio_pika.connect_robust(
                    host=random.choice(self.rabbitmq_hosts),
                    virtualhost='/',
                    login=self.rabbitmq_user,
                    password=self.rabbitmq_password,
                    ssl=self.ssl_context,  
                    port=5671 
                )
                self.logger.info("Connection established")
                break
            except Exception as e:
                self.logger.error(f"Connection failed: {e}")
                if attempt < retries - 1:
                    self.logger.info(f"Retrying in 5 seconds...")
                    await asyncio.sleep(5)
                else:
                    self.logger.error("All retry attempts failed")
                    raise

        # Create a channel
        self.channel = await self.connection.channel()
        self.logger.info("Channel created")
        self.exchange = await self.channel.declare_exchange(name=exchange_name, type=ExchangeType.TOPIC, durable=True)
        self.logger.info(f"Exchange '{exchange_name}' created")

    async def subscribe_to_service(self, queue_name: str, routing_key: str, callback: callable([IncomingMessage])):
        # Create a queue
        queue = await self.channel.declare_queue(name=queue_name, exclusive=True)
        # Bind the queue to the exchange
        await queue.bind(exchange=self.exchange_name, routing_key=routing_key)
        # Set up a message consumer
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                self.logger.info(f"Received message on queue '{queue_name}' with routing key '{routing_key}'")
                await callback(message)

    async def publish(self, message_body, routing_key):
        # Publish the message to the exchange
        self.logger.info(f"Publishing message to exchange '{self.exchange_name}' with routing key '{routing_key}'")
        await self.exchange.publish(
            aio_pika.Message(
                body=message_body.encode(),
                content_type="text/plain",
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            ),
            routing_key=routing_key
        )

    async def publish_to_exchange(self, message, routing_key, exchange_name):
        await self.subscribe_channel(exchange_name)
        self.logger.info(f"Sending log to exchange '{exchange_name}' with routing key '{routing_key}'")
        await self.publish(message, routing_key)
