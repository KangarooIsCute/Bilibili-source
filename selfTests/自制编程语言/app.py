while True:
    x = input(">>> ")
    if x in globals().keys():
        print(globals() [x])
        continue
    try:
        exec(x)
    except Exception as err:
        print(err)