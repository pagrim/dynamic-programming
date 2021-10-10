from money_change import MoneyChange


def test__change_base():
    mc = MoneyChange([1])
    assert (mc._change([1, 1], 0) == [1, 1])


def test__change():
    mc = MoneyChange([1])
    assert (mc._change([], 2) == [1, 1])


def test_change_1():
    mc = MoneyChange([4, 3, 1])
    assert (mc.change(34) == [4, 4, 4, 4, 4, 4, 4, 3, 3])

def test_change_2():
    mc = MoneyChange([4, 3, 1])
    assert (mc.change(2) == [1, 1])
