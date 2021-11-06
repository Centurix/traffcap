from .root import root_router
from .incoming import incoming_router
from .endpoints import endpoints_router


__all__ = [
    "routers"
]


routers = [
    root_router,
    incoming_router,
    endpoints_router
]
