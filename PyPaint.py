from tkinter import *

# Make Main Window
wd = Tk()
wd.geometry("700x700")
wd.title("PyPaint")

# Close the Window
def close():
    wd.quit()
    wd.destroy()

# Menu
mnbar = Menu(wd)

mn = Menu(mnbar, tearoff=0)
mn.add_command(label="New")
mn.add_command(label="Open")
mn.add_separator()
mn.add_command(label="Exit", command=close)
mnbar.add_cascade(label="Main", menu=mn)

wd.config(menu=mnbar)
wd.mainloop()