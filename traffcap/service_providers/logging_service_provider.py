import os
import sys
import logging


async def start_logging_service_provider() -> None:
    log_level = os.getenv("LOG_LEVEL", "INFO")

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.getLevelName(log_level))

    logging.info(f"Set logging level to {log_level}")
