from tkinter import *
def c(kod, cc):
	emp.delete(0, END)
	emp.insert(0, kod)
	lab['text'] = cc
root = Tk()
root.resizable(False, False)

lab = Label(width=30)
lab.pack()
emp = Entry(width=30, justify=CENTER)
emp.pack()

colour = {'#ff0000': 'Красный',
		  '#ff7d00': 'Оранжевый',
		  '#ffff00': 'Желтый',
		  '#00ff00': 'Зеленый',
		  '#007dff': 'Голубой',
		  '#0000ff': 'Синий',
		  '#7d00ff': 'Фиолетовый'}

for i in colour:
	c_k = lambda kod=1, cc=colour[i]:c(kod,cc)
	button = Button(background=i, activebackground = i, command = c_k, width =30)
	button.pack()

root.mainloop()