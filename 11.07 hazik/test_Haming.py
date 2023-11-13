import Hamingtav

def test_hamingtav():
    assert Hamingtav.hamingtav("toned", "roses") == 3
    assert Hamingtav.hamingtav("tone", "roses") == 0
    assert Hamingtav.hamingtav("ollo", "alma") == 3
    assert Hamingtav.hamingtav("toned", "") == 0
    assert Hamingtav.hamingtav("", "") == 0