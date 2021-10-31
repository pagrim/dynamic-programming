from arithmetic_expression import ArithmeticExpression
import pytest
from unittest.mock import patch


@pytest.fixture
def example_expr():
    return ArithmeticExpression([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+'])


def test_fetch_operate(example_expr):
    example_expr.min_memo[3, 4] = 5
    assert(example_expr.fetch_operate(min, 3, 4) == 5)


@patch('arithmetic_expression.ArithmeticExpression.min_max')
def test_get_combinations(example_expr, mm_min_max):
    mm_min_max.return_value = 88
    exp_result = None
    assert(example_expr.get_combinations(2, 4, 3) == exp_result)
