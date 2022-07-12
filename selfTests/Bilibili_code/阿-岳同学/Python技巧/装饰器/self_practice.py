"""
2022-7-12
by JerryQiu
"""
def reverse_list(oldFunc):
    def newFunc(list):
        oldFunc(list[::-1])

    return newFunc

list = ["Jerry", "Kangaroo", "Tony", "Jack", "Ziqiao"]

@reverse_list
def show_name_list(list):
    print(list)

show_name_list(list)