from .root import root_router
from .incoming import incoming_router
from .endpoints import endpoints_router
from .inbound_requests import inbound_requests_router


__all__ = [
    "routers"
]


routers = [
    root_router,
    incoming_router,
    endpoints_router,
    inbound_requests_router
]
