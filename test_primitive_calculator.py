from primitive_calculator import PrimitiveCalculator

pc = PrimitiveCalculator([lambda x: x//2, lambda x: x//3, lambda x: x-1], [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x > 1])


def test__find_min_operations_base():
    assert(pc._find_min_operations([3], 1) == [1, 3])
    assert (pc._find_min_operations([], 1) == [1])
    pc.clear_memo()


def test__find_min_operations():
    assert(pc._find_min_operations([6], 3) == [1, 3, 6])
    pc.clear_memo()


def test_find_min_operations_9():
    assert(pc.find_min_operations(9) == [1, 3, 9])
    pc.clear_memo()

def test_find_min_operations_8():
    assert(pc.find_min_operations(8) == [1, 2, 4, 8])
    pc.clear_memo()
