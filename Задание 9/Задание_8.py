from tkinter import *

root = Tk()
root.title('9')
root.resizable(False, False)

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_polygon(100, 40, 40, 90, 157, 90, fill='lightblue')

c.create_rectangle(60, 80, 140, 170,
                   fill='lightblue',
                   outline='lightblue'
                   )

c.create_oval(150, 5, 190, 40, width=2,
              fill='orange',
              outline='orange'
              )

for i in range(20):
    c.create_arc(i*10, 120, i*10 + 100, 270,
                 start=190, extent=-40,
                 style=ARC, outline='green',
                 width=2)

root.mainloop()
