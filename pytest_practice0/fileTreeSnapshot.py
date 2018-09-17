# coding: utf-8
import os
import sys

# 指定したパス以降のファイルのツリー構成を記録（ちょうてきとう）
def getFileTreeSnapshot(path):
    result=''
    
    # 指定したpathが存在するか確認
    if os.path.exists(path) is False and os.path.isdir(path) is False: return result

    # path以下のファイルをフルパスで取得
    for root, dirs, files in os.walk(path):
        if root.find('.git') != -1: continue
        result+='::'+os.path.abspath(root).replace('\\','/')
        for filename in files:
            if os.path.abspath(filename).find('.git') != -1: continue
            result+='::'+os.path.abspath(filename).replace('\\','/')

    return result
