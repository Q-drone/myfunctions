from myfunctions.mathfunctions import add_one, neg, subt, add

def test_add_one():
    assert add_one(0) == 1
    assert add_one(-1) == 0
    assert add_one(1) == 2

def test_neg():
    assert neg(0) == 0
    assert neg(1) == -1
    assert neg(-1) == 1

def test_subt():
    assert subt(0,0) == 0
    assert subt(1,2) == -1
    assert subt(2,1) == 1

def test_add():
    assert add(0,0) == 0
    assert add(1,2) == 3
    assert add(2,1) == 3
    assert add("2","1") == "Please provide number"