"""Client for toggling lights."""
import time
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def toggle_lights(state, room):
    """Toggle lights."""
    log.info("Toggling lights in {}".format(room))
    # TODO - put in energenie code.
    for attempt in range(3):
        log.info("Attempt {} of 3: Sending '{}' command to switch..."
                 .format(attempt, state))
        time.sleep(1)
