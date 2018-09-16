# coding: utf-8
def test_func0():
    assert (1,2,3) == (1,2,3)

# テスト対象外(pytest.ini を参照)
def notTest_func0():
    assert (1,2,3) == (1,2,4)
    