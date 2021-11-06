import os
import logging
from traffcap.exceptions import ServiceProviderConfigurationError
from traffcap.repositories import Repository


async def start_repository_service_provider() -> None:
    db_path = os.getenv("DB_PATH", "sqlite:///traffcap.db")
    if not db_path:
        raise ServiceProviderConfigurationError(
            "Blank 'DB_PATH' provided"
        )

    if not db_path.startswith("sqlite://"):
        raise ServiceProviderConfigurationError(
            "DB_PATH should start with sqlite:///"
        )

    logging.info(f"Setting database path to {db_path!r}")
    Repository.db_path = db_path
    await Repository.upgrade_db()
