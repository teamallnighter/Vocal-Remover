import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess

install = subprocess.call(["pip", "install", "-r", "requirements.txt"])

root = Tk()
messagebox.showinfo("showinfo", "Select an MP3 file on your computer to extract vocals")
root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=[("MP3 File", "*.mp3")])
service = subprocess.call(["python3", "inference.py", "--input", root.filename])
root.mainloop()
