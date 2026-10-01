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

# Top bar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root, image=TopImage).pack()

dockImage=PhotoImage(file="Images/dock.png")
Label(root, image=dockImage, bg="#32405B").place(x=30, y=25)

noteImage=PhotoImage(file="Images/note.png")
Label(root, image=noteImage, bg="#32405B").place(x=30, y=25)

heading=Label(root, text="My Tasks", font="monospace 20 bold", fg="white", bg="#32405B")
heading.place(x=130, y=20)

root.mainloop()