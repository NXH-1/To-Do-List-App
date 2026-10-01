import tkinter
from tkinter import *

root = Tk()
root.title("Neil's-To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# Helper Function
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

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