"""Test Server."""
from server import LightController
from mock import patch, Mock


def test_lightcontroller_is_a_singleton():
    """Test singleton pattern."""
    lc1 = LightController()
    lc2 = LightController()
    assert id(lc1) == id(lc2)


def test_register_adds_clients():
    """Test clients added when register called."""
    lc = LightController()
    with patch.object(lc, 'clients') as mock_clients:
        mock_client = Mock()
        lc.register(mock_client)
        assert mock_clients.append.called_once_with(mock_client)


def test_publish_queues_message():
    """Test clients added when register called."""
    lc = LightController()
    with patch.object(lc, 'q') as mock_queue:
        lc.publish('lounge')
        assert mock_queue.enqueue.called_once_with('client.toggle_lights',
                                                   'lounge')
