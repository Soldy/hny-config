import pytest
import config

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def test_init():
    config.init('test/test.conf.json')

def test_string():
    assert config.get('test_string') == "test"

def test_integer():
    assert config.get('test_integer') == 1


