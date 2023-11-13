import Median

def test_test():
    assert Median.test([1, 2, 3, 4, 5]) == 3
    assert Median.test([3, 1, 2, 5, 3]) == 3
    assert Median.test([1, 300, 2, 200, 1]) == 2
    assert Median.test([3, 6, 20, 99, 10, 15]) == 12.5