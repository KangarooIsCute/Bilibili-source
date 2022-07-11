# 构造函数 constructor
class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("__init__ is run")

jack = Student("jack.ma",12,"male")
pony = Student("pony.ma",13,"male")
# 参数不能少

print(jack.name)
print(pony.name)