from tkinter import *
def print_text():
	lab_text['text'] = var.get()

root = Tk()
var = StringVar()
l_frame = Frame(root)
r_frame = Frame(root)
l_frame.pack(side=LEFT)
r_frame.pack(side=LEFT)

lab_text = Label (r_frame)

batton1 = Radiobutton(l_frame, text = 'Дима', variable=var, value='+79814214955', indicatoron=0, command=print_text)
batton2 = Radiobutton(l_frame, text = 'Даня', variable=var, value='+79814214956', indicatoron=0, command=print_text)
batton3 = Radiobutton(l_frame, text = 'Ваня', variable=var, value='+79814214957', indicatoron=0, command=print_text)
batton1.pack(fill=X)
batton2.pack(fill=X)
batton3.pack(fill=X)
lab_text.pack(fill=X)
root.mainloop()