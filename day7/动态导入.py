import importlib
aa = importlib.import_module("lib.aa")      #当我们知道要导入的模块是一个字符串，则可以通过动态导入完成
print(aa.C().name)