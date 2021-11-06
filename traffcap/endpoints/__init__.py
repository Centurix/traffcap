from time import time
from base64 import b64encode


__all__ = [
    "generate_code"
]


async def generate_code() -> str:
    """
    Generate an endpoint code
    """
    return b64encode(str(int(time() * 1000)).encode())[:-2].decode()
