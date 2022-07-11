my_name= "jack.ma"

list_name = ["jack.ma", "pony.ma", "robin.li"]


def who_am_i(name):
    print(f'my name is {name}')
class Student:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def who_am_i(self):
        print(f'i am a person,{self.__name}|{self.__age}|{self.__sex}')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex