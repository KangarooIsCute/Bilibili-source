from tkinter import *
def xinlabel():
    global xin
    s = Label(xin, text='完成')
    s.pack()
xin = Tk()
b1 = Button(xin, text='下一步', command=xinlabel)
b1.pack()
xin.mainloop()