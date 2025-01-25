"""
Rabbitmq related module
"""

import functools
import json
import multiprocessing
import time
from dataclasses import dataclass, field
from logging import getLogger
from multiprocessing.synchronize import Event as EventClass
from typing import Optional

import pika
from typing_extensions import TypeAlias

from s3ben.constants import AMQP_HOST, NOTIFICATION_EVENTS, TOPIC_ARN
from s3ben.helpers import check_object, remmaping_message
from s3ben.s3 import S3Events

_logger = getLogger(__name__)
Queue: TypeAlias = multiprocessing.Queue
Event: TypeAlias = EventClass
ConnectionParameters: TypeAlias = pika.ConnectionParameters


@dataclass
class MqConnection:
    """
    RabbitMQ dataclass to hold all required parameters in one object
    """

    host: str
    user: str
    password: str = field(repr=False)
    port: int
    virtualhost: str
    exchange: str
    queue: str

    @property
    def __uri(self) -> str:
        """
        Create and return amqp uri
        """
        return AMQP_HOST.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            virtualhost=self.virtualhost,
        )

    @property
    def attributes(self) -> dict:
        """
        Returns attribute dictionary
        """
        return {
            "push-endpoint": self.__uri,
            "amqp-exchange": self.exchange,
            "amqp-ack-level": "broker",
            "persistent": "true",
        }

    @property
    def notification_config(self) -> dict:
        """
        Property to return topic arn
        :rtype: str
        """
        return {
            "TopicConfigurations": [
                {
                    "Id": f"s3ben-{self.exchange}",
                    "TopicArn": TOPIC_ARN.format(self.exchange),
                    "Events": NOTIFICATION_EVENTS,
                }
            ]
        }


@dataclass
class MqExQue:
    """
    Dataclas for Exchange and queue definition
    """

    exchange: str
    queue: str


class RabbitMQ:
    """
    Class to setup and consume rabbitmq cluster
    :param str hostname: rabbitmq server address
    :param str user: username for connection
    :param str password: password for user
    :param int port: port of mq server, default: 5672
    :param str virtualhost: virtual host to connect, default: /
    """

    def __init__(self, conn_params: MqConnection) -> None:
        self.mq_params = conn_params
        self.should_reconnect: bool = False
        self.was_consuming = False

        self._connection: pika.SelectConnection = None
        self._channel: pika.channel.Channel = None
        self._consuming: bool = False
        self._closing: bool = False
        self._consumer_tag = None
        self._prefetch_count = 1
        self._s3_client: Optional[S3Events] = None
        self._exchange: Optional[str] = None
        self._queue: Optional[str] = None
        self._routing_key: Optional[str] = None
        self._mp_data_queue: Optional[Queue] = None
        self._mp_end_event: Optional[Event] = None

    def prepare(self, exchange: str, queue: str, routing_key: str) -> None:
        """
        Method to prepare rabbitmq cluster for consumer
        :param str exchange: Exchange to create
        :param str queue: queue to create
        :param str routing_key: bind queu to exchange ussing routing key
        """
        _logger.info("Preparing rabbitmq cluster for work")
        conn_params = self.__conn_params()
        connection = pika.BlockingConnection(parameters=conn_params)
        self._channel = connection.channel()
        self.setup_exchange(exchange=exchange)
        self.setup_queue(queue=queue)
        self.quene_bind(routing_key=routing_key)
        self.close_channel()
        connection.close()

    def __conn_params(self) -> ConnectionParameters:
        """
        Method to construct and return pika connection parameters
        """
        logins = pika.credentials.PlainCredentials(
            self.mq_params.user, self.mq_params.password
        )
        return pika.ConnectionParameters(
            host=self.mq_params.host,
            port=self.mq_params.port,
            virtual_host=self.mq_params.virtualhost,
            credentials=logins,
        )

    def __connect(self):
        conn_params = self.__conn_params()
        return pika.SelectConnection(
            parameters=conn_params,
            on_open_callback=self.on_connection_open,
            on_open_error_callback=self.on_connection_open_error,
            on_close_callback=self.on_connection_closed,
        )

    def consume(
        self,
        queue: str,
        s3_client: S3Events,
        mp_data_queue: Queue,
        # mp_end_event: Event
    ) -> None:
        """
        This method connects to RabbitMQ, returning the connection handle.
        When the connection is established, the on_connection_open method
        will be invoked by pika.

        :rtype: pika.SelectConnection
        """
        # self._mp_end_event = mp_end_event
        self._mp_data_queue = mp_data_queue
        self._s3_client = s3_client
        self._queue = queue
        self._connection = self.__connect()
        self._connection = self._connection.ioloop.start()

    def on_connection_open(self, _unused_connection) -> None:
        """This method is called by pika once the connection to RabbitMQ has
        been established. It passes the handle to the connection object in
        case we need it, but in this case, we'll just mark it unused.

        :param pika.SelectConnection _unused_connection: The connection
        """
        _logger.debug("Connection opened")
        self.open_channel()

    def open_channel(self) -> None:
        """
        Open a new channel with RabbitMQ by issuing the Channel.Open RPC
        command. When RabbitMQ responds that the channel is open, the
        on_channel_open callback will be invoked by pika.
        """
        _logger.debug("Creating new channel")
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel: pika.channel.Channel) -> None:
        """
        This method is invoked by pika when the channel has been opened.
        The channel object is passed in so we can make use of it.
        Since the channel is now open, we'll declare the exchange to use.

        :param pika.channel.Channel channel: The channel object
        """
        _logger.debug("Channel opened")
        self._channel = channel
        self.add_on_channel_close_callback()
        self.set_qos()

    def add_on_channel_close_callback(self) -> None:
        """
        This method tells pika to call the on_channel_closed method if
        RabbitMQ unexpectedly closes the channel.
        """
        _logger.debug("Adding channel close callback")
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channle_closed(self, channel, reason) -> None:
        """
        Invoked by pika when RabbitMQ unexpectedly closes the channel.
        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.

        :param pika.channel.Channel: The closed channel
        :param Exception reason: why the channel was closed
        """
        _logger.warning("Channel %s was closed: %s", channel, reason)
        self.close_connection()

    def close_connection(self) -> None:
        """
        Close connection

        :return: None
        """
        self._consuming = False
        if self._connection.is_closing or self._connection.is_closed:
            _logger.info("Connection closing or already closed")
            return
        _logger.info("Closing connection")
        self._connection.close()

    def on_connection_open_error(self, _unused_connection, err) -> None:
        """
        This method is called by pika if the connection to RabbitMQ
        can't be established.

        :param pika.SelectConnection _unused_connection: The connection
        :param Exception err: The error
        """
        _logger.error("Connection open failed: %s", err)
        self.reconnect()

    def reconnect(self) -> None:
        """
        Will be invoked if the connection can't be opened or is
        closed. Indicates that a reconnect is necessary then stops the
        ioloop.
        """
        self.should_reconnect = True
        self.stop()

    def stop(self) -> None:
        """
        Cleanly shutdown the connection to RabbitMQ by stopping the consumer
        with RabbitMQ. When RabbitMQ confirms the cancellation, on_cancelok
        will be invoked by pika, which will then closing the channel and
        connection. The IOLoop is started again because this method is invoked
        when CTRL-C is pressed raising a KeyboardInterrupt exception. This
        exception stops the IOLoop which needs to be running for pika to
        communicate with RabbitMQ. All of the commands issued prior to starting
        the IOLoop will be buffered but not processed.
        """
        if not self._closing:
            self._closing = True
            _logger.info("Stopping")
            if self._consuming:
                _logger.debug("still consuming")
                self.stop_consuming()
                self._connection.ioloop.start()
            else:
                self._connection.ioloop.stop()
            _logger.info("Stopped")

    def stop_consuming(self) -> None:
        """
        Tell RabbitMQ that you would like to stop consuming by sending the
        Basic.Cancel RPC command.
        """
        if self._channel:
            _logger.debug("Sending a Basic.Cancel RPC command to RabbitMQ")
            callback = functools.partial(self.on_cancelok, userdata=self._consumer_tag)
            self._channel.basic_cancel(self._consumer_tag, callback)

    def on_cancelok(self, _unused_frame, userdata) -> None:
        """
        This method is invoked by pika when RabbitMQ acknowledges the
        cancellation of a consumer. At this point we will close the channel.
        This will invoke the on_channel_closed method once the channel has been
        closed, which will in-turn close the connection.

        :param pika.frame.Method _unused_frame: The Basic.CancelOk frame
        :param str|unicode userdata: Extra user data (consumer tag)
        """
        self._consuming = False
        _logger.debug(
            "RabbitMQ acknowledged the cancellation of the consumer: %s", userdata
        )
        self.close_channel()

    def close_channel(self) -> None:
        """
        Call to close the channel with RabbitMQ cleanly by issuing the
        Channel.Close RPC command.
        """
        _logger.info("Closing the channel")
        self._channel.close()

    def on_connection_closed(self, _unused_connection, reason) -> None:
        """
        This method is invoked by pika when the connection to RabbitMQ is
        closed unexpectedly. Since it is unexpected, we will reconnect to
        RabbitMQ if it disconnects.

        :param pika.connection.Connection connection: The closed connection obj
        :param Exception reason: exception representing reason for loss of
            connection.
        """
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
            return
        _logger.warning("Connection closed, reconnecting because: %s", reason)
        self.reconnect()

    def on_channel_closed(self, channel, reason) -> None:
        """
        Invoked by pika when RabbitMQ unexpectedly closes the channel.
        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.

        :param pika.channel.Channel: The closed channel
        :param Exception reason: why the channel was closed
        """
        _logger.warning("Channel %s was closed: %s", channel, reason)
        self.close_connection()

    def setup_queue(self, queue) -> None:
        """
        Setup the queue on RabbitMQ by invoking the Queue.Declare RPC
        command.

        :param str|unicode queue_name: The name of the queue to declare.
        """
        _logger.debug("Creating queue: %s", queue)
        self._queue = queue
        self._channel.queue_declare(
            queue=self._queue,
            durable=True,
            auto_delete=False,
            arguments={"x-queue-type": "quorum"},
        )

    def quene_bind(self, routing_key: str) -> None:
        """
        Method to bind queue and exchange toggether.
        """
        _logger.debug(
            "Binding %s to %s with %s", self._exchange, self._queue, routing_key
        )
        self._channel.queue_bind(
            queue=self._queue, exchange=self._exchange, routing_key=routing_key
        )

    def setup_exchange(self, exchange) -> None:
        """
        Setup the exchange on RabbitMQ by invoking the Exchange.Declare RPC
        command.

        :param str|unicode exchange_name: The name of the exchange to declare
        """
        _logger.debug("Declaring exhange %s", exchange)
        self._exchange = exchange
        self._channel.exchange_declare(
            exchange=self._exchange,
            durable=True,
            exchange_type="direct",
            auto_delete=False,
            internal=False,
        )

    def start_consuming(self) -> None:
        """This method sets up the consumer by first calling
        add_on_cancel_callback so that the object is notified if RabbitMQ
        cancels the consumer. It then issues the Basic.Consume RPC command
        which returns the consumer tag that is used to uniquely identify the
        consumer with RabbitMQ. We keep the value to use it when we want to
        cancel consuming. The on_message method is passed in as a callback pika
        will invoke when a message is fully received.
        """
        _logger.info("Starting to consume messages")
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self._queue, self.on_message)
        self.was_consuming = True
        self._consuming = True

    def add_on_cancel_callback(self) -> None:
        """
        Add a callback that will be invoked if RabbitMQ cancels the consumer
        for some reason. If RabbitMQ does cancel the consumer,
        on_consumer_cancelled will be invoked by pika.
        """
        _logger.debug("Adding consumer cancel callback")
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame) -> None:
        """
        Invoked by pika when RabbitMQ sends a Basic.Cancel for a consumer
        receiving messages.

        :param pika.frame.Method method_frame: The Basic.Cancel frame
        """
        _logger.info("Consumer canceled, shuting down %s", method_frame)
        if self._channel:
            self._channel.close()

    def on_message(
        self,
        _unused_channel,
        basic_deliver,
        properties,
        body,
    ) -> None:
        """
        Invoked by pika when a message is delivered from RabbitMQ. The
        channel is passed for your convenience. The basic_deliver object that
        is passed in carries the exchange, routing key, delivery tag and
        a redelivered flag for the message. The properties passed in is an
        instance of BasicProperties with the message properties and the body
        is the message that was sent.

        :param pika.channel.Channel _unused_channel: The channel object
        :param pika.Spec.Basic.Deliver: basic_deliver method
        :param pika.Spec.BasicProperties: properties
        :param bytes body: The message body
        """
        body = json.loads(body.decode())
        for record in body["Records"]:
            obj_size = record["s3"]["object"]["size"]
            if obj_size == 0:
                continue
            event = record["eventName"]
            bucket = record["s3"]["bucket"]["name"]
            obj_key = record["s3"]["object"]["key"]
            _logger.debug(
                "Bucket: %s event: %s file: %s size: %s",
                bucket,
                event,
                obj_key,
                obj_size,
            )
            action = self.__bucket_event(event=event)
            key = check_object(obj_key)
            if action == "download":
                if isinstance(key, dict):
                    self._download_remapped(bucket=bucket, data=key)
                else:
                    _ = self._s3_client.download_object_v2(  # type: ignore[union-attr]
                        bucket=bucket, s3_obj=key, local_path=key
                    )

            if action == "remove":
                if isinstance(key, dict):
                    self._remove_remapped(bucket=bucket, data=key)
                else:
                    self._s3_client.remove_object(  # type: ignore[union-attr]
                        bucket=bucket, path=obj_key
                    )
        self.acknowledge_message(basic_deliver.delivery_tag)

    def _remove_remapped(self, bucket, data: dict) -> None:
        """
        Remove remmaped object from active and database

        :param str bucket: Bucket name
        :param dict data: Dictionary containing remapping info
        :rtype: None
        """
        _, local_path, message = remmaping_message(
            action="remove", remap=data, bucket=bucket
        )
        self._s3_client.remove_object(bucket=bucket, path=local_path)  # type: ignore[union-attr]
        self._mp_data_queue.put_nowait(message)  # type: ignore[union-attr]

    def _download_remapped(self, bucket: str, data: dict) -> None:
        """
        Method to download and remap object

        :param str bucket: Bucket name
        :param dict data: Dictionary containing remapping info
        :rtype: None
        """
        s3_obj, local_path, message = remmaping_message(
            action="download", remap=data, bucket=bucket
        )
        dl_status = self._s3_client.download_object_v2(  # type: ignore[union-attr]
            bucket=bucket, s3_obj=s3_obj, local_path=local_path
        )
        if dl_status:
            self._mp_data_queue.put_nowait(message)  # type: ignore[union-attr]

    def __bucket_event(self, event: str) -> str:
        """
        Method to parse bucket event
        :param str event: Event that was received
        :raises ValueError: if event unknow
        :return: Parsed action to execute
        """
        e_split = event.split(":")
        if e_split[0].lower() == "objectsynced" and e_split[1].lower() == "create":
            return "download"
        if e_split[0].lower() == "objectsynced" and e_split[1].lower() == "delete":
            return "remove"
        if e_split[0].lower() == "objectcreated":
            return "download"
        if e_split[0].lower() == "objectremoved":
            return "remove"
        if e_split[0].lower() == "objectlifecycle":
            return "remove"
        raise ValueError(f"Event: {event} unknow")

    def acknowledge_message(self, delivery_tag) -> None:
        """
        Acknowledge the message delivery from RabbitMQ by sending a
        Basic.Ack RPC method for the delivery tag.

        :param int delivery_tag: The delivery tag from the Basic.Deliver frame
        """
        _logger.debug("Ack message: %s", delivery_tag)
        self._channel.basic_ack(delivery_tag)

    def on_basic_qos_ok(self, _unused_frame):
        """Invoked by pika when the Basic.QoS method has completed. At this
        point we will start consuming messages by calling start_consuming
        which will invoke the needed RPC commands to start the process.

        :param pika.frame.Method _unused_frame: The Basic.QosOk response frame

        """
        _logger.info("QOS set to: %d", self._prefetch_count)
        self.start_consuming()

    def set_qos(self):
        """This method sets up the consumer prefetch to only be delivered
        one message at a time. The consumer must acknowledge this message
        before RabbitMQ will deliver another one. You should experiment
        with different prefetch values to achieve desired performance.

        """
        _logger.debug("Setting prefetch: %s", self._prefetch_count)
        self._channel.basic_qos(
            prefetch_count=self._prefetch_count, callback=self.on_basic_qos_ok
        )
