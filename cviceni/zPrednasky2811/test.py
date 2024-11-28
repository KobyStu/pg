from aplikace import soucet,test_fibonachi
from zkouska  import pozpatku
from zkouska2 import operace

def test_soucet_2():
    assert soucet(1,1) == 2

def test_soucet_3():
    assert soucet(1,2) == 3

def test_fibonachi_5():
    assert test_fibonachi(5) == [1,1,2,3,5]

def test_pozpatku():
    pass

def test_operace():
    pass