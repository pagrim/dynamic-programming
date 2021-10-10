from primitive_calculator import PrimitiveCalculator

pc = PrimitiveCalculator([lambda x: x*2, lambda x: x*3, lambda x: x+1])


def test_find_min_operations_base():
    assert (pc._find_min_operations([[1, 2, 3], [1, 3]], 2, 3) == [1, 3])
    #assert(pc._find_min_operations([], 1, 1) == [1])
    #assert(pc._find_min_operations([], 1, 3) == [1, 3])
