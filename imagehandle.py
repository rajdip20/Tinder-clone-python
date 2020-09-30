from tkinter import *
from tkinter import filedialog
import shutil, os

root = Tk()

filename = filedialog.askopenfilename(initialdir="/images", title="Somrhting")

source = Label(root, text=filename).pack()

print(filename)

shutil.copyfile(filename, "C:\\Users\\user\\PycharmProjects\\tinder\\images\\cnn.png")

root.mainloop()
