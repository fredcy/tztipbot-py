import configparser
import logging
import pprint
from matrix_client.client import MatrixClient

logger = logging.getLogger("tztipbot")

def init():
    config = configparser.ConfigParser()
    config.read("tztipbot.cfg")
    homeserver = config.get("server", "host")
    print(f"homeserver={homeserver}")

    client = MatrixClient(homeserver)
    token = client.login(username=config.get("client", "username"),
                         password=config.get("client", "password"))
    print(token)


if __name__ == "__main__":
    init()
