import pytest


# region int
def test_int_properties(obj: int = 10) -> None:
    assert isinstance(obj, int)
    assert str(obj).isdigit()
    assert 10 == obj
    assert obj ** 2 == 100
    assert str(obj) == '10'
    assert '01'.isdigit() is True
    assert int('01') == 1


@pytest.mark.parametrize('first_multiplier, second_multiplier,excepted_result', [
    (1, 2, 2), (2, 7, 14), (1, 0, 0), (0, 0, 0),
    (12, 2, 24), (1, 1, 1), (2, 4, 8), (3, 6, 18)
])
def test_times(
        first_multiplier: int,
        second_multiplier: int,
        excepted_result: int
) -> None:
    assert first_multiplier * second_multiplier == excepted_result


@pytest.mark.parametrize('numerator, exception', [
    (1, ZeroDivisionError), (15, ZeroDivisionError),
    ('12', TypeError), ('45', TypeError)
])
def test_divided_by_zero(
        numerator: int,
        exception: type(BaseException),
        denominator: int = 0
) -> None:
    with pytest.raises(exception):
        assert numerator / denominator == exception


# some more test
def test_even_number() -> None:
    values = [0, 3, 4, 7, 2, 5, 8]
    assert any(value % 2 == 0 for value in values) is True
    assert all(value % 2 == 0 for value in values) is False
    assert all(value % 2 == 0 for value in values[0::2]) is True
    assert all(value % 2 == 1 for value in values[1:7:4]) is True


# endregion


# region dict
def test_dict_properties(obj: dict = None) -> None:
    if obj is None:
        obj = {'first_value': 0, 'second_value': 1}
    assert isinstance(obj, dict)
    assert obj.keys()
    assert 'first_value' in obj
    assert ('first_value', 0) in obj.items()
    assert 1 in obj.values()
    assert obj.copy() == obj
    assert len(obj) == 2
    assert obj.get('second_value') == 1
    assert obj.clear() is None
    assert len(obj) == 0


@pytest.mark.parametrize('key, value', [
    ('test', 'value'), ('first', 1)
])
def test_keys_and_values(
        key: float | int | str,
        value: float | int | str,
) -> None:
    obj = {key: value}
    assert key, value in obj.items()
    assert key in obj.keys()
    assert value in obj.values()
    assert {key: value} == obj
    assert dict([(key, value)]) == {key: value}


@pytest.mark.parametrize('key, value', [
    (0, 1), ('0', '1'), ('William', 23),
    ('on', True), ('off', False)
])
def test_key_error(
        key: int | str,
        value: int | str | bool,
        exception=KeyError
) -> None:
    keys = [2, '14', 'John', 'turn']
    values = [4, '0', 15, 'left']
    obj = dict(zip(keys, values))
    with pytest.raises(exception):
        assert obj[key]
        assert key in obj.keys()
        assert value in obj.values()
        assert key, value in obj.items()
        assert key in obj

# endregion
