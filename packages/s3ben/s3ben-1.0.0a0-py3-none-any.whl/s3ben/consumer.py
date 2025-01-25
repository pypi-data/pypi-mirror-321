"""
Consumer module
"""

import multiprocessing
import signal
from logging import getLogger
from typing import Optional

from typing_extensions import TypeAlias

from s3ben.helpers import signal_handler
from s3ben.rabbit import MqConnection, RabbitMQ
from s3ben.s3 import BackupLocations, S3Config

_logger = getLogger(__name__)

Queue: TypeAlias = multiprocessing.Queue


def run_consumers(
    manager: multiprocessing.managers.SyncManager, consumers: int
) -> None:
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    try:
        consumers_proc: list = create_consumer_list(consumers)

        # for _ in range(consumers):
        #     _logger.debug("Starting consumer")
    except (KeyboardInterrupt, SystemExit):
        for c in consumers:
            c.terminate()


def create_consumer_list(n_consumers: list) -> list:
    """
    Create a list of consumer processes
    """


class Consume:
    """
    MQ consumer class
    """

    def __init__(self, locations: BackupLocations, s3_config: S3Config) -> None:
        self.locations = locations
        self.s3_config = s3_config
        self._mq: Optional[RabbitMQ] = None
        self._mq_queue: Optional[str] = None

    def start_consumer(
        self, mq_conn: MqConnection, mq_queue: str, data_queue: Queue
    ) -> None:
        """
        Start rabbitMQ consumer
        """
        self._mq = RabbitMQ(conn_params=mq_conn)
        self._mq_queue = mq_queue
        while True:
            try:
                s3_client = self.s3_config.client()
                self._mq.consume(queue=self._mq_queue, s3_client=s3_client)
            except (KeyboardInterrupt, SystemExit):
                _logger.debug("Stopping mq")
                self._mq.stop()
                break
