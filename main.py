import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Neil's-To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# Helper Function

# App icon
top_icon = PhotoImage(file="Images/image.png")
root.iconphoto(False, top_icon)

# Top bar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root, image=TopImage).pack()

dockImage=PhotoImage(file="Images/dock.png")
Label(root, image=dockImage, bg="#32405B").place(x=30, y=25)


noteImage=Image.open("Images/note.png")
resize_noteImage=noteImage.resize((50, 50), Image.Resampling.LANCZOS)
noteImage=ImageTk.PhotoImage(resize_noteImage)
Label(root, image=noteImage, bg="#32405B").place(x=30, y=15)

heading=Label(root, text="My Tasks", font="monospace 20 bold", fg="white", bg="#32405B")
heading.place(x=130, y=20)

root.mainloop()