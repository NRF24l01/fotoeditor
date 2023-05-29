import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from effects import *


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Image filters")

        self.original_image = Image.open(filedialog.askopenfilename())
        self.filtered_image = self.original_image.copy()

        self.img_label = tk.Label(self.master)
        self.img_label.pack()
        self.update_image()

        self.filters = [{"name": "Grayscale", "func": self.grayscale_filter}]
        for f in self.filters:
            filter_button = tk.Button(self.master, text=f["name"], command=f["func"])
            filter_button.pack()

    def update_image(self):
        img_tk = ImageTk.PhotoImage(self.filtered_image)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def grayscale_filter(self):
        self.filtered_image = blasck_white(self.filtered_image)
        self.update_image()


root = tk.Tk()
app = App(root)
root.mainloop()