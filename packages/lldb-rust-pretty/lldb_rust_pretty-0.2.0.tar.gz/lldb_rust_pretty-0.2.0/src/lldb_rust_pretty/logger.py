import logging
from datetime import datetime, timezone
from logging import DEBUG, LogRecord, Logger, StreamHandler, getLogger
from typing import Optional

NAME = 'lldb-rust-pretty'

class Formatter(logging.Formatter):
    def formatTime(self, record: LogRecord, datefmt: Optional[str] = None) -> str:
        return datetime.fromtimestamp(record.created, timezone.utc).astimezone().isoformat(sep="T", timespec="milliseconds")

def get_logger() -> Logger:
    return getLogger(NAME)

def _init():
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    handler.setFormatter(Formatter('%(asctime)s %(levelname)-5s %(name)s: %(message)s'))
    logger = get_logger()
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

_init()
