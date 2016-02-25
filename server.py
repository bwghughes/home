"""Lightcontroller server allows licnets to register for lights to control."""
import time
import logging

from redis import Redis
from rq import Queue

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class LightController(object):
    """Lightcontroller object."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implement singleton pattern."""
        if not cls._instance:
            cls._instance = super(LightController, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        """Init."""
        log.info("Initliazing....")
        self.q = Queue(connection=Redis())
        self.clients = []

    def register(self, client):
        """Register clients."""
        log.info("Register client {}".format(client))
        self.clients.append(client)
        pass

    def publish(self, room):
        """Queue messages."""
        self.q.enqueue('client.toggle_lights', 'lounge')

    def run(self):
        """Run the server."""
        while True:
            log.info("Checking for events...")
            time.sleep(1)


def main():
    """Main method."""
    lc = LightController()
    lc.run()


if __name__ == '__main__':
    main()
