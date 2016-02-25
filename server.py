"""Lightcontroller server allows licnets to register for lights to control."""
import os
import logging
from redis import Redis
from rq import Queue
from threading import Thread
from flask import Flask, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


ROOMS = ['kitchen', 'lounge', 'bedroom']


class LightController(Thread):
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
        Thread.__init__(self, *args, **kwargs)
        self.queues = {}
        self.conn = Redis(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'),
                          password=os.getenv('REDIS_PASSWORD'))
        self.queue = Queue('lights', connection=self.conn)

    def toggle(self, key, state):
        """Queue messages."""
        self.queue.enqueue('client.toggle_lights', key, state)

    def run(self):
        """Run the server."""
        log.info("LightController server running...")
        while True:
            pass


@app.route("/<key>/<state>", methods=['POST'])
def toggle(key, state):
    """Toggle."""
    log.info('Recieved toggle request for {}'.format(key))
    lc = LightController()
    lc.toggle(key, state)
    return jsonify(dict(status='OK'))


def start_controller():
    """Proc to start controller thread."""
    log.info('Starting LightController...')
    lc = LightController()
    lc.run()


if __name__ == '__main__':
    start_controller()
