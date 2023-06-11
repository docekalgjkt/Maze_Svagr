import tkinter as tk
from tkinter import font
import random
from tkinter import filedialog



def open_folder():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "r") as file:
            maze = [line.strip() for line in file]
            

def start_game():
    level = level_var.get()
    robot_position = position_var.get()
    print("Level:", level)
    print("Robot position:", robot_position)
    maze = create_maze()
    display_maze(maze)
  


def stop_game():
    print("Game stopped")

main= tk.Tk()
main.title("Herní menu")
main.geometry("1200x750")  
button_font = font.Font(size=15, weight = 'bold')

menu_frame = tk.Frame(main)
menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

level_label = tk.Label(menu_frame, text="Výběr úrovně bludiště", font = button_font)
level_label.pack(pady=0)

level_var = tk.StringVar(menu_frame)
level_var.set("Úroveň 1")

level_dropdown = tk.OptionMenu(menu_frame, level_var, "Úroveň 1", "Úroveň 2", "Úroveň 3")
level_dropdown.config(font=button_font)
level_dropdown.pack(pady=35)


maze_button = tk.Button(menu_frame, text="Výběr bludiště", font = button_font, bg = "dark orange", fg = "black", command = open_folder)
maze_button.pack(pady=60)


position_label = tk.Label(menu_frame, text="Poloha robota", font = button_font)
position_label.pack(pady=0)

position_var = tk.StringVar(menu_frame)
position_var.set("0, 0")

position_entry = tk.Entry(menu_frame, textvariable=position_var, font = button_font)
position_entry.pack(pady=35)



button_frame = tk.Frame(menu_frame)
button_frame.pack(pady=35)

start_button = tk.Button(button_frame, text="Start", command=start_game, fg="dark green", bg="lime", font = button_font)
start_button.pack(side=tk.LEFT,pady=50)

stop_button = tk.Button(button_frame, text="Stop", command=stop_game, fg="dark red", bg="red", font = button_font)
stop_button.pack(side=tk.LEFT,pady=80)

separator = tk.Canvas(main, width=2, height=750, bg="black")
separator.pack(side=tk.LEFT)

game_frame = tk.Frame(main, bg="white")
game_frame.pack(fill=tk.BOTH, expand=True)


canvas = tk.Canvas(main, width=750, height=750, bg="white")
canvas.pack()






def create_maze():
    selected_option = level_var.get()
    if selected_option == "Úroveň 1":
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    elif selected_option == "Úroveň 2":
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    elif selected_option == "Úroveň 3":
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
    available_positions = []
    for row in range(1, len(maze) - 1):
        for col in range(1, len(maze[0]) - 1):
            if maze[row][col] == 0:
                available_positions.append((row, col))


    if available_positions:
        start_row, start_col = random.choice(available_positions)
        maze[start_row][start_col] = 2
        available_positions.remove((start_row, start_col))

    if available_positions:
        end_row, end_col = random.choice(available_positions)
        maze[end_row][end_col] = 3

    return maze



def display_maze(maze):
    canvas.delete("maze")
    cell_size = 75
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            if maze[row][col] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="maze")
            elif maze[row][col] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green", tags="maze")
                canvas.create_oval(x1, y1, x2, y2, fill="gray", outline="black")
                robot_x = col
                robot_y = row
                robot_position = f"{robot_x+1}, {robot_y+1}"
                position_var.set(robot_position)
            elif maze[row][col] == 3:
                canvas.create_rectangle(x1, y1, x2, y2, fill="red", tags="maze")

            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="maze")







main.mainloop()
