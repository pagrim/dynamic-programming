import pytest

from primitive_calculator import PrimitiveCalculator, MemoItem

pc = PrimitiveCalculator([lambda x: x // 2, lambda x: x // 3, lambda x: x - 1],
                         [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x > 1])


def test__find_min_operations_base():
    assert (pc._find_min_operations(2) == {1: MemoItem(0, -1), 2: MemoItem(1, 0)})
    pc.clear_memo()


def test__find_min_operations():
    assert (pc._find_min_operations(6) == {1: MemoItem(0, -1), 2: MemoItem(1, 0), 3: MemoItem(1, 1), 4: MemoItem(2, 0),
                                           5: MemoItem(3, 2), 6: MemoItem(2, 0)})
    pc.clear_memo()


@pytest.mark.parametrize(('target', 'exp_num_ops', 'exp_trace'), [
    (9, MemoItem(2, 1), [1, 3, 9]),
    (8, MemoItem(3, 0), [1, 2, 4, 8]),
])
def test_find_min_operations(target, exp_num_ops, exp_trace):
    assert (pc.find_min_operations(target=target) == exp_num_ops)
    assert pc.backtrace(target) == exp_trace
    pc.clear_memo()


@pytest.mark.parametrize(('target', 'exp_num_ops'), [
    (96234, 14)
])
def test_large_min_operations(target, exp_num_ops):
    assert (pc.find_min_operations(target=target).num_ops == exp_num_ops)
    backtrace = pc.backtrace(target)
    assert(len(backtrace) == exp_num_ops + 1)
    pc.clear_memo()

