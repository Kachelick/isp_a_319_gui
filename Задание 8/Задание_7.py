from tkinter import *


def evb():
    t['width'] = en1.get()
    t['height'] = en2.get()


def ev1(event):
    t['width'] = en1.get()
    t['height'] = en2.get()


def ev2(event):
    t['bg'] = 'white'


def ev3(event):
    t['bg'] = 'lightgrey'


root = Tk()
root.title('8')
root.resizable(False, False)

f1 = Frame()
f11 = Frame(f1)
f12 = Frame(f1)
f3 = Frame()

en1 = Entry(f11, width=4)
en2 = Entry(f11, width=4)

en1.bind('<Return>', ev1)
en2.bind('<Return>', ev1)

b = Button(f12, text='Изменить', command=evb)

t = Text(f3, width=25, height=12, bg='lightgrey')
t.bind('<FocusIn>', ev2)
t.bind('<FocusOut>', ev3)

f1.pack()
f11.pack(side=LEFT)
f12.pack(side=LEFT)
f3.pack()
en1.pack()
en2.pack(side=LEFT)
b.pack(side=LEFT)
t.pack()

root.mainloop()
