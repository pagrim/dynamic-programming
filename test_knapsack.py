from knapsack import KnapsackWithRepetition, KnapsackNoRepetition, WeightsValue
import pytest

@pytest.fixture
def kswr_example():
    return KnapsackWithRepetition([6, 3, 4, 2], [30, 14, 16, 9], 10)

@pytest.fixture
def ksnr_example():
    return KnapsackNoRepetition([6, 3, 4, 2], [30, 14, 16, 9], 10)

def test_valid_weight(kswr_example):
    assert(kswr_example.valid_weight(2, 2))


def test_fetch_options(kswr_example):
    assert(kswr_example.fetch_options(2, [0, 0, 0, 0]) == [(0, 9, 3)])


def test__calc_max_value(kswr_example):
    assert(kswr_example._calc_max_value(4, [0, 0, 0, 0]) == 18)


def test_calc_max_value_kswr(kswr_example):
    assert(kswr_example.calc_max_value() == 48)


def test_calc_max_value_ksnr(ksnr_example):
    assert(ksnr_example.calc_max_value() == 46)
