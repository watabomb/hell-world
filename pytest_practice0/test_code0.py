# coding: utf-8
import maya.standalone
maya.standalone.initialize()

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

import fileTreeSnapshot as ft
@pytest.mark.run_mark1
def test_func2():
    path='c:/users/watab/source/hell-world'
    log=ft.getFileTreeSnapshot(path)

    # ダミーでファイルを追加
    with open('c:/users/watab/source/hell-world/test.txt','w') as f: f.write('hoge\n')

    # 異なるファイル構成であることからエラー検知（多分）
    assert ft.getFileTreeSnapshot(path)==log
