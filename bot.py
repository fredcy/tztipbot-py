import configparser
import json
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
    username=config.get("client", "username")
    password=config.get("client", "password")
    print(f"username={username}")

    token = client.login(username=username, password=password)
    print(f"token={token}")
    return client


def on_event(room, event):
    print(f"room={room} event={json.dumps(event, indent=4)}")


if __name__ == "__main__":
    client = init()

    room_alias = "#TezosConcerns:matrix.org"
    room = client.join_room(room_alias)
    room.add_listener(on_event)

    client.start_listener_thread()

    while True:
        msg = input()
        if msg == "/quit":
            break
        else:
            room.send_text(msg)
