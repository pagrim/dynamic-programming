from distance import EditDistance, LongestCommonSubsequence


def test_ED__calculate():
    ed1 = EditDistance('app', 'happen')
    assert(ed1._calculate(2, 2) == 2)


def test_ED_calculate():
    assert(EditDistance('ab', 'ab').calculate() == 0)
    assert(EditDistance('short', 'ports').calculate() == 3)
    assert(EditDistance('editing', 'distance').calculate() == 5)


def test_LCS_calculate():
    assert(LongestCommonSubsequence('275', '25').calculate() == 2)
    assert(LongestCommonSubsequence('7', '1234').calculate() == 0)
    assert(LongestCommonSubsequence('2783', '5287').calculate() == 2)
