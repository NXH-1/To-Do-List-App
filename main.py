import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Neil's-To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def openTaskFile():
    with open("tasklist.txt", "r") as file:
        tasks = file.readlines()

    for task in tasks:
        if task != "\n":
            task_list.append(task.strip())
            listbox.insert(END, task.strip())

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

# Main (Text Entry Box)
frame=Frame(root,width=400,height=50, bg="white")
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame, width=18, font="monospace 20", bd=0, bg="white", justify="left", textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame, text="Add", font="monospace 20 bold", width=6, bg="#5A95FF", fg="#fff", bd=0)
button.place(x=290, y=0)


# Listbox
frame1=Frame(root, bd=3, width=700, height=280, bg="#32405B")
frame1.pack(pady=(160, 0))

listbox=Listbox(frame1, font="monospace 12", width=40, height=16, bg="#32405B", fg="white", cursor="hand2", selectbackground="#5A95FF")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# Delete Button
Delete_icon=PhotoImage(file="Images/delete.png")
Button(root, image=Delete_icon, bd=0).pack(side=BOTTOM, pady=13)

root.mainloop()