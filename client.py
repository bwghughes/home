"""Client for toggling lights."""
import os
import time
import redis
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


r = redis.Redis(os.getenv('REDIS_URL'))
client_map = r.hgetall('keymap')


try:
    from energenie import switch_on, switch_off
except ImportError:
    log.error("No energenie installed.")

    def switch_on(num):
        """Dummy function."""
        pass

    def switch_off(num):
        """Dummy function."""
        pass


def toggle_lights(state, room):
    """Toggle lights."""
    log.info("Toggling lights in {}".format(room))

    for attempt in range(3):
        log.info("Attempt {} of 3: Sending '{}' command to switch {}..."
                 .format(attempt, state))
        if state == 'on':
            switch_on(client_map.get(room))
        elif state == 'off':
            switch_off(client_map.get(room))
        time.sleep(1)
