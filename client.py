"""Client for toggling lights."""
import time
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def toggle_lights(room):
    """Toggle lights."""
    for x in range(3):
        log.info("Toggling lights in {}".format)
        time.sleep(1)
