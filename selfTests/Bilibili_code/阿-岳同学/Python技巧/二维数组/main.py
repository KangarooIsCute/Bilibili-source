"""
2022-7-12
by JerryQiu
"""

def create_array2D(w, h):
    arr = []
    for y in range(h):
        line = []
        for x in range(w):
            line.append(0)
            ...
        arr.append(line)
    return arr


def show(arr):
    for line in arr:
        print(line)

def main():
    a1 = create_array2D()
    show(a1)

if __name__ == '__main__':
    main()
