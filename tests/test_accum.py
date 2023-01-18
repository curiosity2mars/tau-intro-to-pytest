import pytest
from stuff.accum import Accumulator


@pytest.fixture
def accum():
    yield Accumulator()
    print("Test passed OK")


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_five(accum):
    accum.add(5)
    assert accum.count == 5
    

@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add(2)
    accum.add(4)
    assert accum.count == 6


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as ex:
        accum.count = 10
        