import tkinter
from tkinter import *

root = Tk()
root.title("Neil's-To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# App icon
top_icon = PhotoImage(file="Images/image.png")
root.iconphoto(False, top_icon)

root.mainloop()

# Top bar
