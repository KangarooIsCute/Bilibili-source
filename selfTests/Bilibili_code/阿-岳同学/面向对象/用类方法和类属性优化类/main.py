"""
2022-7-12
by JerryQiu
"""
from typing import *
from random import choice


class Person:
    _FirstName = ["邱", "李", "张", "王", "俞", "傅", "戚", "应"]
    _LastName = ["三", "建国", "鹏", "宇航", "超", "子航"]

    def __init__(self, name):
        self.name = name
    def say(self):
        print(f"大家好我叫{self.name}")

    @classmethod
    def createMan(cls):
        return cls(choice(cls._FirstName) + choice(cls._LastName))
    def __str__(self):
        return f"【{self.name}】"
    def __repr__(self):
        return f"【{self.name}】"


def main():
    arr = [Person.createMan() for _ in range(100)]
    print(arr)
    return None

if __name__ == '__main__':
    main()
