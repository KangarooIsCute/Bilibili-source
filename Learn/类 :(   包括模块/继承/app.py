# 继承 inheritance
class Person:
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

class Student(Person):   #继承，创建一个类，类的名字后面加一个括号，里面填着你要继承的类
    def who_am_i(self):
        print(f'i am a student,{self.get_name()}')
    def learn(self):
        print("i am learning")

class Teacher(Person):
    def teach(self):
        print("i am teaching")

jack = Student("jack.ma",23,"male")
jack.who_am_i()
jack.learn()