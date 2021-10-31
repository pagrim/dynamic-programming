from knapsack import KnapsackWithRepetition, WeightsValue
import pytest

@pytest.fixture
def kswr_example():
    return KnapsackWithRepetition([6, 3, 4, 2], [30, 14, 16, 9], 10)


def test_valid_weight(kswr_example):
    assert(kswr_example.valid_weight(2, 2))


def test_fetch_options(kswr_example):
    assert(kswr_example.fetch_options(2) == [(0, 9)])


def test__calc_max_value(kswr_example):
    assert(kswr_example._calc_max_value(4) == 18)


def test_calc_max_value(kswr_example):
    assert(kswr_example.calc_max_value() == 48)
