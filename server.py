"""Lightcontroller server allows licnets to register for lights to control."""
import logging
from redis import Redis
from rq import Queue
from threading import Thread
from flask import Flask, render_template, jsonify
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
        self.conn = Redis()
        for room in ROOMS:
            self.queues[room] = Queue(room, connection=self.conn)

    def toggle(self, state, room):
        """Queue messages."""
        self.queues.get(room).enqueue('client.toggle_lights', state, room)

    def run(self):
        """Run the server."""
        log.info("LightController server running...")
        while True:
            pass


@app.route("/")
def hello():
    """Index."""
    return render_template('index.html', rooms=ROOMS)


@app.route("/<room>/toggle/<state>", methods=['POST'])
def toggle(room, state):
    """Toggle."""
    log.info('Recieved toggle request for {}'.format(room))
    lc = LightController()
    lc.toggle(state, room)
    return jsonify(dict(status='OK'))


def start_controller():
    """Proc to start controller thread."""
    log.debug('Starting LightController...')
    lc = LightController()
    lc.run()
    logging.debug('Stopping LightController...')


def main():
    """Main method. Starts server and LC thread."""
    start_controller()


if __name__ == '__main__':
    main()
