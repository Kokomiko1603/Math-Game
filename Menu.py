from tkinter import *
from PIL import Image, ImageTk
from Level_1 import Level1
from Level_2 import Level2

class Menu(Frame):
    def __init__( self, parent, controller ):
        super().__init__(parent, background = "#b3ebf2")
        self.controller = controller

        self.title = Image.open("pixelarts/mathfight_menu.png").resize((250, 80), Image.Resampling.NEAREST)
        #self.title = self.title.resize((250, 250), Image.Resampling.LANCZOS)
        self.title = self.title.convert("RGBA")
        self.title = ImageTk.PhotoImage(self.title)


        title_label = Label(self, image=self.title, bg="#b3ebf2", borderwidth=0, highlightthickness=0)
        #title_label.pack()
        title_label.place(relx = 0.5, 
                   rely = 0.2,
                   anchor = 'center')
        #title_label.grid(row=1, column=10)

        self.level_1 = Image.open("pixelarts/level_1_button.png").resize((150, 50), Image.Resampling.NEAREST)
        self.level_1 = self.level_1.convert("RGBA")
        self.level_1 = ImageTk.PhotoImage(self.level_1)
        level_1_label = Button(self, text = "Level 1", image = self.level_1, bg = "#b3ebf2", highlightthickness=0, borderwidth=0, activebackground="#b3ebf2", command = lambda: self.controller.show_frame(Level1) ).place(relx = 0.5, rely = 0.45, anchor = "center")

        self.level_2 = Image.open("pixelarts/level_2_frame.png").resize((150, 50), Image.Resampling.NEAREST)
        self.level_2 = self.level_2.convert("RGBA")
        self.level_2 = ImageTk.PhotoImage(self.level_2)
        level_2_label = Button(self, text = "Level 2", image = self.level_2, bg = "#b3ebf2", highlightthickness=0, borderwidth=0, activebackground="#b3ebf2", command = lambda: self.controller.show_frame(Level2)).place(relx = 0.5, rely = 0.6, anchor = "center")
