# 类函数 class function
# 类方法 class method
class Student:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def print_info(self):
        print(f'{self.__name}-{self.__age}-{self.__sex}')
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
jack = Student("jack.ma",13,"male")
print(jack.get_name())
jack.set_name("pony")
# print(jack.__name)
jack.print_info()
# print_info(jack)