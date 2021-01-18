import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for i in apps:
        label = tk.Label(frame, text=i, bg="gray")
        label.pack()


def runApps():
    for i in apps:
        os.startfile(i)


canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

for i in apps:
    label = tk.Label(frame, text=i)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for i in apps:
        f.write(i + ',')