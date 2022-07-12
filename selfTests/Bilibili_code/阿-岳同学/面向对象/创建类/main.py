"""
2022-7-12
by JerryQiu
"""



class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def plus(self, v):
        self.x += v.x
        self.y += v.y


def main():
    v1 = Vec(2, 2)
    print(v1)
    v2 = Vec(1, 1)
    v1.plus(v2)
    print(v1)
    print(v1.x)
    return None



if __name__ == '__main__':
    main()
