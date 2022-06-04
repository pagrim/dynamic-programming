import pytest

from primitive_calculator import PrimitiveCalculator

pc = PrimitiveCalculator([lambda x: x // 2, lambda x: x // 3, lambda x: x - 1],
                         [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x > 1])


def test__find_min_operations_base():
    assert (pc._find_min_operations([3], 1) == [1, 3])
    assert (pc._find_min_operations([], 1) == [1])
    pc.clear_memo()


def test__find_min_operations():
    assert (pc._find_min_operations([6], 3) == [1, 3, 6])
    pc.clear_memo()


@pytest.mark.parametrize(('target', 'exp_res'), [
    (9, [1, 3, 9]),
    (8, [1, 2, 4, 8]),
    (96234, [])
])
def test_find_min_operations(target, exp_res):
    assert (pc.find_min_operations(target=target) == exp_res)
    pc.clear_memo()
