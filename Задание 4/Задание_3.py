from tkinter import *
root = Tk()
top = Frame(root)
bot = Frame(root)
top.pack()
bot.pack()
e = Entry(top)
e.pack(side=LEFT)
def op():
	text.delete(1.0,END)
	open_text= open(e.get(), 'r')
	text_o = open_text.readlines()
	for item in text_o:
		text. insert(END, item)
		open_text.close()
def sv():
	save_text = open(e.get(), 'w')
	save_text.writelines(text.get(1.0, END))
	save_text.close()
button_colour1 = Button(top, text = "открыть", command=op)
button_colour1.pack(side=LEFT)
button_colour2 = Button(top, text = "сохранить", command=sv)
button_colour2.pack(side=LEFT)

text = Text(bot, width=30, wrap=WORD)
text.pack(side=LEFT)

scr = Scrollbar(bot, command=text.yview)
scr.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scr.set)
root.mainloop()

