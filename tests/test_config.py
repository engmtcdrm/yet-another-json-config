import pytest
from json import JSONDecodeError
from config import Config, MissingConfigFileException

@pytest.fixture
def valid_config():
    conf = Config('./tests/test.json')
    return conf

@pytest.fixture()
def invalid_test_file():
    return './tests/doesnotexist.json'

@pytest.fixture()
def malformed_test_file():
    return './tests/malformed_test.json'

def test_load(valid_config):

    assert valid_config != {}

def test_invalid_load(invalid_test_file):
    with pytest.raises(FileNotFoundError):
        conf = Config(invalid_test_file)

def test_malformed_load(malformed_test_file):
    with pytest.raises(JSONDecodeError):
        conf = Config(malformed_test_file)

def test_set(valid_config):
    v = valid_config['test']
    valid_config.set('test', value='test2')

    assert v == 'test' and valid_config['test'] != 'test' and valid_config['test'] == 'test2'

def test_set2(valid_config):
    v = valid_config['test']
    valid_config['test'] = 'test2'

    assert v == 'test' and valid_config['test'] != 'test' and valid_config['test'] == 'test2'

def test_nested_set(valid_config):
    v = valid_config['nestedTest']['test']
    valid_config.set('nestedTest', 'test', value='test2')

    assert v == 'test' and valid_config['nestedTest']['test'] != 'test' and valid_config['nestedTest']['test'] == 'test2'

def test_bad_nested_set(valid_config):
    with pytest.raises(KeyError):
        valid_config.set('badNestedTest', 'test', value='test2')

def test_get(valid_config):
    v = valid_config.get('test')

    assert v == 'test'

def test_empty_get(valid_config):
    with pytest.raises(KeyError):
        valid_config.get()

def test_get2(valid_config):
    v = valid_config['test']

    assert v == 'test'

def test_nested_get(valid_config):
    v = valid_config.get('nestedTest')

    assert v == { 'test': 'test' }

def test_nested_val_get(valid_config):
    v = valid_config.get('nestedTest', 'test')

    assert v == 'test'

def test_dbl_nested_val_get(valid_config):
    v = valid_config.get('nestedTest2', 'nested', 'test')

    assert v == 'test'

def test_nested_get2(valid_config):
    v = valid_config['nestedTest']

    assert v == { 'test' : 'test'}

def test_nested_get3(valid_config):
    v = valid_config['nestedTest']['test']

    assert v == 'test'

def test_delete(valid_config):
    valid_config.delete('test')

    assert 'test' not in valid_config

def test_delete2(valid_config):
    del valid_config['test']

    assert 'test' not in valid_config

def test_nested_delete(valid_config):
    valid_config.delete('nestedTest', 'test')

    assert 'test' not in valid_config['nestedTest']

def test_nested_delete2(valid_config):
    del valid_config['nestedTest']['test']

    assert 'test' not in valid_config['nestedTest']

def test_bad_delete(valid_config):
    with pytest.raises(KeyError):
        valid_config.delete('badDelete')

def test_empty_str_delete(valid_config):
    with pytest.raises(KeyError):
        valid_config.delete('')

def test_empty_call_delete(valid_config):
    with pytest.raises(KeyError):
        valid_config.delete()