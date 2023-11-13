import NyomtatandoOldalak

def test_oldalak():
    assert NyomtatandoOldalak.oldalak("1-4,7,9,11-15") == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15]
    assert NyomtatandoOldalak.oldalak("1-4,7,9,11-15,10-16") == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15, 10, 11, 12, 13, 14, 15, 16]
    assert NyomtatandoOldalak.oldalak("1") == [1]
    assert NyomtatandoOldalak.oldalak("1-16,16-18") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18]
    
def test_rendez():
    assert NyomtatandoOldalak.rendez([1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15]
    assert NyomtatandoOldalak.rendez([1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15, 10, 11, 12, 13, 14, 15, 16]) == [1, 2, 3, 4, 7, 9, 10, 11, 12, 13, 14, 15, 16]
    assert NyomtatandoOldalak.oldalak([1,1,1,1]) == [1]