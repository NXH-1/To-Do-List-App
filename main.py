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

# Main
frame=Frame(root,width=400,height=50, bg="white")
frame.place(x=0, y=180)

## Where you enter text
task=StringVar()
task_entry=Entry(frame, width=18, font="monospace 20", bd=0, bg="white", justify="left", textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame, text="Add", font="monospace 20 bold", width=6, bg="#5A95FF", fg="#fff", bd=0)
button.place(x=290, y=0)




root.mainloop()