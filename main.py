from utils import add, sub, div, mul

def test_add():
    assert add(2,2) == 4
    assert add(2,-5) == -3

def test_sub():
    assert sub(2,2) == 0
    assert sub(2,-5) == 7

def test_div():
    assert div(2,2) == 1
    assert div(2,-5) == -0.4

def test_mul():
    assert mul(2,2) == 4
    assert mul(2,-5) == -10