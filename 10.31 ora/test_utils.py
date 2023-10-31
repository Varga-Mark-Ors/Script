from utils import duplaz, is_palindrom

def test_duplaz():
    assert duplaz(4) == 8
    assert duplaz(0) == 0
    assert duplaz(20) == 40
    assert duplaz(-2) == -4
    assert duplaz(-100) == -200
    
def test_is_palindrom():
    assert is_palindrom("Alma") == False
    assert is_palindrom("ollo") == True
    assert is_palindrom("kekes") == False
    assert is_palindrom("") == True
    assert is_palindrom("   ") == True