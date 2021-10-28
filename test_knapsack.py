from knapsack import KnapsackWithRepetition, WeightsValue
import pytest

@pytest.fixture
def kswr_example():
    return KnapsackWithRepetition([6, 3, 4, 2], [30, 14, 16, 9], 10)


def test_compute_value(kswr_example):
    assert(kswr_example.compute_value([1, 1, 1, 0]) == 60)


def test__calc_max_value(kswr_example):
    assert(kswr_example._calc_max_value([1, 0, 0, 0], 4) == WeightsValue([1, 0, 0, 2], 48))


def test_calc_max_value(kswr_example):
    assert(kswr_example.calc_max_value() == WeightsValue([1, 0, 0, 2], 48))
