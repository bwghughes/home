"""Client for toggling lights."""
import time
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


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


def toggle_lights(key, state):
    """Toggle lights."""
    log.info("Toggling lights {} for key {}".format(state, key))

    for attempt in range(3):
        log.info("Attempt {} of 3: Sending '{}' command to switch {}..."
                 .format(attempt, state, key))
        if state == 'on':
            switch_on(key)
        elif state == 'off':
            switch_off(key)
        time.sleep(1)
