import pytest
from test_data import data


def test_one_plus_one():
    assert 1 + 1 == 2


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as ex:
        num = 1 / 0

    assert 'division by zero' in str(ex.value)


@pytest.mark.parametrize('a, b, result', data.numbers)
def test_multiply_numbers(a, b, result):
    assert result == a * b
