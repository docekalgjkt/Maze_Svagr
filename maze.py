import tkinter as tk

def create_maze():
    row = 10
    column = 10
    main = tk.Tk()
    w = tk.Canvas(main, width=506, height=506)

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
    a = w.create_rectangle(55,5,105,205, fill = "black")
    b = w.create_rectangle(55,255,105,505, fill = "black")
    c = w.create_rectangle(155,55,205,105, fill = "black")
    d = w.create_rectangle(155,105,205,505, fill = "black")
    e = w.create_rectangle(255,5,305,405, fill = "black")
    f = w.create_rectangle(255,455,305,505, fill = "black")
    g = w.create_rectangle(355,5,405,255, fill = "black")
    h = w.create_rectangle(355,305,405,505, fill = "black")
    i = w.create_rectangle(405,5,455,255, fill = "black")
    j = w.create_rectangle(405,305,455,505, fill = "black")
    finish = w.create_rectangle(455, 455, 505, 505, fill = "lime")
    walls = [a,b,c,d,e,f,g,h,i,j]

    w.pack()
    main.mainloop()
