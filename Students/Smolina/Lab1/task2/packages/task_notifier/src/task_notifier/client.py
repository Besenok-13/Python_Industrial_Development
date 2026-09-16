import httpx


def configure_transport() -> None:
    client = httpx.Client(proxy=None)
    client.close()
