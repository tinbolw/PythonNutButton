import tkinter as tk
from playsound import playsound

root = tk.Tk()
nutCanvas = tk.Canvas()
nutButton = tk.Button(root, text = "Nut Button", width=10, height=5, command=lambda: (playsound('nut sound effect.mp3')))
nutButton.pack()
root.mainloop()
