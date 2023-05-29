import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from effects import *


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("FOTOHREN")

        self.filtered_image = Image.open(filedialog.askopenfilename(filetypes=(("JPG", "*.jpg"),("JPEG", "*.jpeg"))))

        self.img_label = tk.Label(self.master)
        self.img_label.pack()
        self.update_image()

        self.filters = [{"name": "Grayscale", "func": self.grayscale_filter},
                        {"name": "Narko", "func": self.narko_filter},
                        {"name": "Noise", "func": self.noise_filter},
                        {"name": "Color_noise", "func": self.color_noise_filter},
                        {"name": "Hetvertirovanie", "func": self.hetvertirovanie_filter},
                        {"name": "Kek", "func": self.kek_filter},
                        {"name": "Razm", "func": self.razm_filter},
                        {"name": "Rezk", "func": self.rezk_filter},
                        {"name": "Save", "func": self.save}]
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

    def narko_filter(self):
        self.filtered_image = gren_narko(self.filtered_image)
        self.update_image()

    def noise_filter(self):
        self.filtered_image = noise(self.filtered_image)
        self.update_image()

    def color_noise_filter(self):
        self.filtered_image = color_noise(self.filtered_image)
        self.update_image()

    def hetvertirovanie_filter(self):
        self.filtered_image = hetvertirovanie(self.filtered_image)
        self.update_image()
    def kek_filter(self):
        self.filtered_image = kek(self.filtered_image)
        self.update_image()
    def razm_filter(self):
        self.filtered_image = razm(self.filtered_image)
        self.update_image()
    def rezk_filter(self):
        self.filtered_image = kek(self.filtered_image)
        self.update_image()
    def save(self):
        path = filedialog.asksaveasfilename()
        path = path+".jpg"
        print(path)
        self.filtered_image.save(path)

root = tk.Tk()
app = App(root)
root.mainloop()