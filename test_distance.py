from distance import EditDistance, LongestCommonSubsequence


def test_ed__calculate_1():
    ed1 = EditDistance(['app', 'happen'])
    assert (ed1._calculate([2, 2]) == 2)


def test_ed__calculate_2():
    ed1 = EditDistance(['s', 'p'])
    assert (ed1._calculate([1, 1]) == 1)


def test_ed_substitution_cost_1():
    ed1 = EditDistance(['app', 'happen'])
    assert (ed1.get_substitution_cost([1, 1]) == 1)


def test_ed_substitution_cost_2():
    ed1 = EditDistance(['ports', 'short'])
    assert (ed1.get_substitution_cost([1, 1]) == 1)


def test_ed_get_next_costs_1():
    ed1 = EditDistance(['ab', 'ab'])
    assert (ed1.get_next_costs([2, 2], [[2, 1], [1, 2], [1, 1]]) == [1, 1, 0])


def test_ed_get_next_costs_2():
    ed1 = EditDistance(['app', 'happen'])
    assert (ed1.get_next_costs([2, 2], [[2, 1], [1, 2], [1, 1]]) == [1, 1, 1])


def test_ed_get_next_costs_3():
    ed1 = EditDistance(['ports', 'short'])
    assert (ed1.get_next_costs([2, 2], [[2, 1], [1, 2], [1, 1]]) == [1, 1, 1])


def test_ed_calculate_1():
    assert (EditDistance(['ab', 'ab']).calculate() == 0)


def test_ed_calculate_2():
    assert (EditDistance(['short', 'ports']).calculate() == 3)


def test_ed_calculate_3():
    assert (EditDistance(['editing', 'distance']).calculate() == 5)


def test_lcs_calculate():
    assert (LongestCommonSubsequence('275', '25').calculate() == 2)
    assert (LongestCommonSubsequence('7', '1234').calculate() == 0)
    assert (LongestCommonSubsequence('2783', '5287').calculate() == 2)
