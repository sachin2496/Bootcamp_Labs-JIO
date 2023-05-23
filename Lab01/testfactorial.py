from factorial import compfactorial

obj = compfactorial()

def test_something():
    assert obj.compute(5) == 120
    assert obj.compute(6) == 720
    assert obj.compute(7) == 5040
    assert obj.compute(11) == 39916800
    
