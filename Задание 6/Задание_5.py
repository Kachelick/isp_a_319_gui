from tkinter import *
def a1():
	select = list(list1.curselection())
	select.reverse()
	for i in select:
		list2.insert(END, list1.get(i))
		list1.delete(i)

def a2():
	select = list(list2.curselection())
	select.reverse()
	for i in select:
		list1.insert(END, list2.get(i))
		list2.delete(i)
root = Tk()
root.title('6')
root.resizable(False, False)

list1 = Listbox(selectmode=EXTENDED)
list1.grid(column=0, row=0, rowspan=4)
list2 = Listbox(selectmode=EXTENDED)
list2.grid(column=3, row=0, rowspan=4)
for i in ['apple', 'bananas', 'carrot', 'meat', 'patato']:
	list1.insert(END, i)
but1 = Button(text='>>>', command=a1)
but1.grid(column=2, row=1)
but2 = Button(text='>>>', command=a2)
but2.grid(column=2, row=2)
root.mainloop()