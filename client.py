"""Client for toggling lights."""
import time
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

try:
    from energenie import switch_on, switch_off
except ImportError:
    log.error("No energenie installed.")
    switch_on = lambda x: x
    switch_off = lambda x: x


client_map = {'kitchen': [2], 'lounge': [2, 3]}


def toggle_lights(state, room):
    """Toggle lights."""
    log.info("Toggling lights in {}".format(room))
    # TODO - put in energenie code.
    for attempt in range(3):
        for sock in client_map.get(room):
            log.info("Attempt {} of 3: Sending '{}' command to switch {}..."
                     .format(attempt, state, sock))
            if state == 'on':
                switch_on(sock)
            elif state == 'off':
                switch_off(sock)
            time.sleep(1)
