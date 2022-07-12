"""
2022-7-12
by JerryQiu
"""
def robot(oldFunc):
    def newFunc(name):
        oldFunc(name[::-1])

    return newFunc

@robot
def hello(name: str):
    print(f"Hello {name}")

hello("Jack")