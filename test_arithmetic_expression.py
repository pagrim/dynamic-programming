from arithmetic_expression import ArithmeticExpression
import pytest
from unittest.mock import patch
from operator import sub


@pytest.fixture
def example_expr():
    return ArithmeticExpression([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+'])


def test_fetch_operate(example_expr):
    example_expr.min_memo[3, 4] = 5
    assert(example_expr.fetch_operate(min, 3, 4) == 5)


@patch('arithmetic_expression.ArithmeticExpression.min_max')
def test_get_combinations(mm_min_max, example_expr):

    def mock_min_max(i, j):
        if i == 2 and j == 3:
            res = (10, 5)
        elif i == 4 and j == 4:
            res = (3, 7)
        else:
            res = None
        return res

    mm_min_max.side_effect = mock_min_max
    exp_result = [2, -2, 7, 3]
    assert(example_expr.get_combinations(2, 4, 3) == exp_result)


def test_calculate_max(example_expr):
    assert(example_expr.calculate_max() == 200)
