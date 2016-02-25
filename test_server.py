"""Test Server."""
from server import LightController
from mock import patch, Mock


def test_lightcontroller_is_a_singleton():
    """Test singleton pattern."""
    lc1 = LightController()
    lc2 = LightController()
    assert id(lc1) == id(lc2)


def test_toggle_queues_message():
    """Test clients added when register called."""
    lc = LightController()
    with patch.object(lc, 'queues') as mock_queue:
        lc.toggle('on', 'lounge')
        assert mock_queue.enqueue.called_once_with('client.toggle_lights',
                                                   'on', 'lounge')
