# coding: utf-8
import pytest

# pytest -m run_mark0 と指定すると、以下のマークがされた関数のみ評価される
@pytest.mark.run_mark0
def test_func0():
    assert (1,2,3) == (1,2,3)

# assert書かなくても例外が発生すると失敗とみなされる
def test_func1():
    x=1
    y=0
    z=x/y
    return

# テスト対象外(pytest.ini を参照)
def notTest_func0():
    assert (1,2,3) == (1,2,4)
    