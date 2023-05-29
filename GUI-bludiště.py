import tkinter as tk
from tkinter import font
import maze

main = tk.Tk()
w = tk.Canvas(main, width = 240, height = 720)
w.pack()

def msg():
    current_bg = button.cget("bg")
    if current_bg == "lime":
        button.config(bg="red", fg = "dark red")
        print("Hra zahajena")
    elif current_bg == "red":
        button.config(bg="lime", fg = "dark green")
        print("Hra ukončena")


w.create_line(240,0,240,720, width = 5, fill = "black")
button_font = font.Font(size=20, weight = 'bold')
button = tk.Button(main, text = "START", command = msg, fg="dark green", bg="lime", font = button_font)
button.place(x = 20, y = 600, width=200, height=100)

def show():
    label.config(text = clicked.get() )
    print("Úroveň vybrána")
    maze.create_maze()

options = [
    "   Maze 1  ",
    "   Maze 2  ",
    "   Maze 3  ",
    "   Maze 4  ",
    "   Maze 5  ",
    "   Maze 6  ",
    "   Maze 7  "
]

clicked = tk.StringVar()
  
clicked.set("Vyber uroven" )
  
drop = tk.OptionMenu( main , clicked , *options )
drop.place(x = 20, y = 10, width=200, height=100)

level_button = tk.Button( main , text = "Potvrdit" , command = show )
level_button.place(x = 20, y = 110,width=200, height=50)

label = tk.Label(main , text = " " )
label.pack()

w.create_rectangle(240,0,1085,725, fill = "pink")


main.mainloop()
