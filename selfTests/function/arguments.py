"""
2022-7-11
by JerryQiu
"""

def text(*args, end="", sep=" "):
    for i in args:
        print(i, end="", sep=sep)
    if end == "\n":
        print()
    else:
        ...
    return


text("Hello World", "Test_sep")
