"""
2022-7-11
by JerryQiu
"""
a = float(3)
b = float(4)
c = float(5)

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(area)
