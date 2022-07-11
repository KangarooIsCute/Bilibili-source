# 模块 module
# PYTHONPATH 环境变量

import student as s
print(s.my_name)

def foo():
    import sys
    print(sys.path)

# dir
print(dir())
print(dir(s))