from edit_distance import EditDistance

def test__calculate():
    ed1 = EditDistance('app', 'happen')
    assert(ed1._calculate(2, 2) == 2)

def test_calculate():
    assert(EditDistance('ab', 'ab').calculate() == 0)
    assert(EditDistance('short', 'ports').calculate() == 3)
    assert(EditDistance('editing', 'distance').calculate() == 5)
