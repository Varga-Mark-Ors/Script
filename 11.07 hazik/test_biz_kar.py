import Bizonyoskarakterek

def test_valid():
    assert Bizonyoskarakterek.valid("Alma") == "A"
    assert Bizonyoskarakterek.valid("Bananos Fa") == "BF"
    assert Bizonyoskarakterek.valid("Alma", chars="abcdefg") == "a"
    assert Bizonyoskarakterek.valid("Fa eger", chars="abcdefg") == "aeger"