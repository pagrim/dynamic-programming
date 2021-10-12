from edit_distance import EditDistance

ed = EditDistance('app', 'happen')

def test__calculate():
    assert(ed._calculate(2, 2) == 2)
