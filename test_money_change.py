from money_change import MoneyChange

import pytest


def test__change_base():
    mc = MoneyChange([1])
    assert (mc._change([1, 1], 0) == [1, 1])


def test__change():
    mc = MoneyChange([1])
    mc._change([], 2)
    assert (mc.memo[0] == [1, 1])


@pytest.mark.parametrize(('target', 'exp_res'), [
    (34, 9),
    (2, 2)
])
def test_change(target, exp_res):
    mc = MoneyChange([4, 3, 1])
    assert (mc.change(target) == exp_res)
    mc.clear_memo()

