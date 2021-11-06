from .repository_service_provider import start_repository_service_provider
from .logging_service_provider import start_logging_service_provider


__all__ = [
    "start_service_providers"
]


async def start_service_providers() -> None:
    """
    Bootstrap and check environment variables up front
    """
    await start_logging_service_provider()
    await start_repository_service_provider()
