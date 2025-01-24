import os

import pytest

from ..config import get_config_value, has_config_value


def test_has_config_value():
    assert not has_config_value('something')
    assert has_config_value('something', config={'something': 'asdf'})


def test_get_config_value():
    assert get_config_value('something', config={'something': 'asdf'}) == 'asdf'


def test_get_config_value_missing():
    """An error should be thrown when a setting is not present."""
    with pytest.raises(KeyError):
        assert get_config_value('something', config={}) == 'asdf'


def test_get_config_value_missing_default():
    """A default value can be used when a setting is missing."""
    assert get_config_value('something', config={}, default='asdf') == 'asdf'


def test_get_config_value_env_variable():
    """An environment variable should be used when available."""
    os.environ['SOMETHING'] = 'asdf'
    assert get_config_value('SOMETHING', config={}) == 'asdf'
    del os.environ['SOMETHING']


def test_get_config_value_env_variable_priority():
    """An environment variable should take priority over the config."""
    os.environ['SOMETHING'] = 'asdf'
    assert get_config_value('SOMETHING', config={'SOMETHING': 'lala'}) == 'asdf'
    del os.environ['SOMETHING']
