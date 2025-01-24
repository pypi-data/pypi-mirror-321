import os
from loguru import logger as std_logger


LOG_LEVEL = os.getenv("LOG_LEVEL") or "DEBUG"
LOG_PATH = os.getenv("LOG_PATH") or "dev.log"
LOG_ROTATION = os.getenv("LOG_ROTATION") or "2 weeks"

logger = std_logger
logger.add(
    LOG_PATH,
    level=LOG_LEVEL,
    rotation=LOG_ROTATION,
    backtrace=True,
)
