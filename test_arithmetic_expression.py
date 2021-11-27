import pytest
from arithmetic_expression import ArithmeticExpression, Expression

@pytest.fixture
def mock_ae():
    return ArithmeticExpression([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+'])

@pytest.fixture
def mock_ae_calculated(mock_ae):
    return mock_ae.calculate()

def test__calculate(mock_ae):
    assert(mock_ae._calculate(0, 2) == (-10, 4))

def test_calculate_min_max(mock_ae):
    assert(mock_ae.calculate_min_max() == (-94, 200))

def test_retrace(mock_ae_calculated):
    assert(mock_ae_calculated.retrace('max', 200) == '5-((8+7)*(4-(8+9)))')

def test__retrace1(mock_ae_calculated):
    assert(mock_ae_calculated._retrace(Expression(0, 0), 'min', 5) == '5')

def test__retrace2(mock_ae_calculated):
    assert(mock_ae_calculated._retrace(Expression(3, 5), 'min', -13) == '(4)-((8)+(9))')
