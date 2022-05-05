from tkinter import *

def entry1(event):
    list1.insert(0, entry0.get())
    entry0.delete(0, END)

def entry2(event):
    entry0.delete(0, END)
    entry0.insert(0, list1.get(list1.curselection()))
    list1.delete(list1.curselection())

root = Tk()
root.title('7')
root.resizable(False, False)

entry0 = Entry()
entry0.bind('<Return>', entry1)
entry0.grid(column=0, row=0)

list1 = Listbox()
list1.bind('<Double-Button-1>', entry2)
list1.grid(column=0, row=1)

root.mainloop()

