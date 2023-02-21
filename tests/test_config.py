import pytest
from json import JSONDecodeError
from contextlib import nullcontext as does_not_raise
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


## LOAD tests

def test_load(valid_config):
    assert valid_config != {}

def test_invalid_load(invalid_test_file):
    with pytest.raises(FileNotFoundError):
        Config(invalid_test_file)

def test_malformed_load(malformed_test_file):
    with pytest.raises(JSONDecodeError):
        Config(malformed_test_file)




## SET tests

### FUNC tests

@pytest.mark.parametrize('keys, orig_val, expected_val, expected_except', [
    ('test', 'test', 'test2', does_not_raise()),
    (('nestedTest', 'test'), 'test', 'test2', does_not_raise()),
    ('get', 'test', 'test2', does_not_raise()),
    ('badNestedTest', 'test', 'test2', pytest.raises(KeyError)),
    (None, None, None, pytest.raises(KeyError)),
    ((), None, None, pytest.raises(KeyError)),
    ([], None, None, pytest.raises(KeyError))
])

def test_set_by_func(valid_config, keys, orig_val, expected_val, expected_except):
    with expected_except:
        v = valid_config.get(keys)
        valid_config.set(keys, value=expected_val)

        assert v == orig_val and valid_config.get(keys) != orig_val and valid_config.get(keys) == expected_val

### KEY tests

def test_key_set(valid_config):
    v = valid_config['test']
    valid_config['test'] = 'test2'

    assert v == 'test' and valid_config['test'] != 'test' and valid_config['test'] == 'test2'




## GET tests

### FUNC tests

@pytest.mark.parametrize('keys, expected_result, expected_except', [
    ('test', 'test', does_not_raise()),
    ('nestedTest', { 'test': 'test' }, does_not_raise()),
    (('nestedTest', 'test'), 'test', does_not_raise()),
    (('nestedTest2', 'nested', 'test'), 'test', does_not_raise()),
    ('get', 'test', does_not_raise()),
    (None, None, pytest.raises(KeyError)),
    ((), None, pytest.raises(KeyError)),
    ([], None, pytest.raises(KeyError))
])

def test_get_by_func(valid_config, keys, expected_result, expected_except):
    with expected_except:
        v = valid_config.get(keys)

        assert v == expected_result

### KEY tests

@pytest.mark.parametrize('keys, expected_result, expected_except', [
    ('test', 'test', does_not_raise()),
    ('nestedTest', { 'test': 'test' }, does_not_raise()),
    (('nestedTest', 'test'), 'test', does_not_raise()),
    (('nestedTest2', 'nested', 'test'), 'test', does_not_raise()),
    ('get', 'test', does_not_raise()),
    (None, None, pytest.raises(KeyError)),
    ((), None, pytest.raises(KeyError)),
    ([], None, pytest.raises(KeyError))
])

def test_get_by_key(valid_config, keys, expected_result, expected_except):
    with expected_except:
        if type(keys) == str or type(keys) == type(None):
            v = valid_config[keys]
        elif type(keys) == tuple:
            fk = ()

            if len(keys) > 0:
                fk = keys[0]

            v = valid_config[fk]

            for k in keys[1:]:
                v = v[k]
        elif type(keys) == list:
            fk = []

            if len(keys) > 0:
                fk = keys[0]

            v = valid_config[fk]

            for k in keys[1:]:
                v = v[k]
        else:
            assert 1 == 2

        assert v == expected_result




## DELETE tests

### FUNC tests

@pytest.mark.parametrize('keys, expected_except', [
    ('test', does_not_raise()),
    (('nestedTest', 'test'), does_not_raise()),
    (('nestedTest2', 'nested', 'test'), does_not_raise()),
    ('badDelete', pytest.raises(KeyError)),
    (None, pytest.raises(KeyError)),
    ((), pytest.raises(KeyError)),
    ([], pytest.raises(KeyError))
])

def test_delete_by_func(valid_config, keys, expected_except):
    with expected_except:
        if type(keys) == str or type(keys) == type(None):
            valid_config.delete(keys)

            assert keys not in valid_config
        else:
            valid_config.delete(keys)

            no_last_keys = keys[:-1]

            assert keys not in valid_config.get(no_last_keys)

### KEY tests

def test_key_delete(valid_config):
    del valid_config['test']

    assert 'test' not in valid_config

def test_key_nested_delete(valid_config):
    del valid_config['nestedTest']['test']

    assert 'test' not in valid_config['nestedTest']