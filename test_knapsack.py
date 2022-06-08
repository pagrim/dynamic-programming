from knapsack import KnapsackWithRepetition, KnapsackNoRepetition, MemoItem
import pytest

@pytest.fixture
def kswr_example():
    return KnapsackWithRepetition([6, 3, 4, 2], [30, 14, 16, 9], 10)


def test_calc_max_value_kswr(kswr_example):
    assert(kswr_example.calc_max_value() == MemoItem(48, [1, 0, 0, 2], 4))


@pytest.mark.parametrize(("weights", "values", "capacity", "exp_res"),[
    ([6, 3, 4, 2], [30, 14, 16, 9], 10, MemoItem(46, [1, 0, 1, 0], 4)),
    ([1, 4, 8], [1, 4, 8], 10, MemoItem(9, [1, 0, 1], 8)),
])
def test_calc_max_value_ksnr(weights, values, capacity, exp_res):
    ksnr = KnapsackNoRepetition(weights, values, capacity)
    assert(ksnr.calc_max_value() == exp_res)
