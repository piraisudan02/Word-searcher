from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Word Search Game")

class Solution:
    def exist(self, board, word):
        def search(i, j, ind, seen, path):
            if ind == len(word):
                return True, path
            if (i, j) in seen or i < 0 or j < 0 or i == len(board) or j == len(board[0]) or word[ind] != board[i][j]:
                return False, []
            seen.add((i, j))
            path.append((i, j))
            up, up_path = search(i - 1, j, ind + 1, seen, path[:])
            right, right_path = search(i, j + 1, ind + 1, seen, path[:])
            down, down_path = search(i + 1, j, ind + 1, seen, path[:])
            left, left_path = search(i, j - 1, ind + 1, seen, path[:])
            seen.remove((i, j))
            if up:
                return True, up_path
            elif right:
                return True, right_path
            elif down:
                return True, down_path
            elif left:
                return True, left_path
            else:
                return False, []

        for i in range(len(board)):
            for j in range(len(board[0])):
                found, path = search(i, j, 0, set(), [])
                if found:
                    return True, path
        return False, []

def validate_grid(grid):
    letters = set()
    for row in grid:
        for cell in row:
            value = cell.get()
            if not value or len(value) != 1 or not value.islower():
                return False
            letters.add(value)
    return True

def search_word(event=None):  # Updated to accept an event argument with a default value of None
    word = word_entry.get()
    if grid and validate_grid(grid):
        found, path = solution.exist(grid_to_list(grid), word)
        if found:
            messagebox.showinfo("Word Found", f"The word '{word}' is found in the grid!")
            create_grid_gui(path)
        else:
            messagebox.showinfo("Word Not Found", f"The word '{word}' is not found in the grid.")
    else:
        messagebox.showerror("Invalid Grid", "Please create a valid grid before searching for a word.")

def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(StringVar())
        grid.append(row)
    return grid

def create_grid_gui(path=None):  # Modified to accept path argument with a default value of None
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    global grid, grid_window, search_button, word_entry
    grid = create_grid(rows, cols)
    grid_window = Toplevel(root,bg="black")
    grid_window.title("Word Search Grid")
    cell_width = 40
    cell_height = 40
    window_width = cols * (cell_width + 4)  # 4 for padding
    window_height = rows * (cell_height + 4) + 100  # Extra space for entry and button
    grid_window.minsize(window_width, window_height)
    frame = Frame(grid_window, highlightthickness=1, padx=30, pady=30, bg="black")  # Set background color to green
    frame.pack(fill=BOTH, expand=True)

    def ValidateNumber(p):
        if (p.islower() or p == "") and len(p) < 2:
            return True
        return False

    reg = frame.register(ValidateNumber)

    # Function to change border color to red if cell is in the path
    def set_border_color(cell, i, j):
        if path and (i, j) in path:
            cell.config(highlightbackground="red", highlightthickness=2,bg="orange")
        else:
            cell.config(highlightbackground="black", highlightthickness=1,bg="orange")
        cell.config(bg="orange", fg="black")  # Set entry background color to black and text color to green

    for i in range(rows):
        for j in range(cols):
            entry = Entry(frame, width=2, bg="orange", textvariable=grid[i][j], validate="key", validatecommand=(reg, "%P"))
            entry.grid(row=i, column=j, padx=2, pady=2)
            set_border_color(entry, i, j)

    word_label = Label(grid_window, text="Enter word to search:", bg="black", fg="orange")  # Set label background to green and text color to black
    word_label.pack(pady=10)

    word_entry = Entry(grid_window, bg="orange", fg="black")  # Set entry background color to black and text color to green
    word_entry.pack()

    search_button = Button(grid_window, text="Search Word", command=search_word, bg="black", fg="orange")  # Set button background to green and text color to black
    search_button.pack(pady=5)

    def clear_grid():
        for i in range(rows):
            for j in range(cols):
                grid[i][j].set("")  # Clearing the grid values

    clear_button = Button(grid_window, text="Clear Grid", command=clear_grid, bg="black", fg="orange")  
    clear_button.pack(pady=1)

    # Bind the <Return> event to the word_entry widget
    word_entry.bind("<Return>", search_word)

    # Center the window
    grid_window.update_idletasks()
    screen_width = grid_window.winfo_screenwidth()
    screen_height = grid_window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    grid_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

def grid_to_list(grid):
    return [[cell.get() for cell in row] for row in grid]

# messagebox.showinfo("Help", "1) Enter the number of rows and columns in these boxes.\n2) Give the characters in the grids.\n3)Enter only one character in a grid.\n4) Enter the search word.")

def validate_row_entry():
    value = rows_entry.get()
    if value.isdigit() and int(value) > 0:
        return True
    else:
        messagebox.showerror("OOPS!!","Enter validate row. U can only enter number above 0.")
        return False

def validate_col_entry():
    value = cols_entry.get()
    if value.isdigit() and int(value) > 0:
        return True
    else:
        messagebox.showerror("OOPS!!","Enter validate column. U can only enter number above 0.")
        return False

def validate_and_create_grid():
    if validate_row_entry() and validate_col_entry():
        create_grid_gui()

root.configure(bg="black", height=2000)
root.geometry("290x80")
root.resizable(False, False)

solution = Solution()
grid = None
grid_window = None
word_search_window = None

rows_label = Label(root, fg="orange", bg="black", text="Enter number of rows:")
rows_label.grid(row=0, column=0)
rows_entry = Entry(root, fg="black", bg="orange")
rows_entry.grid(row=0, column=1)

cols_label = Label(root, fg="orange", bg="black", text="Enter number of columns:")
cols_label.grid(row=1, column=0)
cols_entry = Entry(root, fg="black", bg="orange")
cols_entry.grid(row=1, column=1)

create_button = Button(root, fg="orange", bg="black", text="Create Grid", command=validate_and_create_grid)
create_button.grid(row=2, columnspan=2)

root.mainloop()
