from tkinter import Tk, Canvas

row = 10
column = 10
hlavni = Tk()
w = Canvas(hlavni, width=506, height=506)

a = 5

c = 5


for i in range(11):
    w.create_line(a ,5, c, 505)
    w.create_line(5,a,505,c)
    a += 50
    c += 50
    w.create_line(5, 5, 505, 5, width= 10)
    w.create_line(5, 505, 505, 505, width= 10)
    w.create_line(5, 5, 5, 505, width= 10)
    w.create_line(505, 5, 505, 505, width= 10)



w.pack()
hlavni.mainloop()