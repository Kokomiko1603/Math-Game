from tkinter import *
from PIL import Image, ImageTk

class Level1(Frame):
    def __init__( self, parent, controller ):
        super().__init__(parent, background = "#b3ebf2")
        self.controller = controller

        self.title = Image.open("pixelarts/solve_message.png").resize((240, 60), Image.Resampling.NEAREST)
        self.title = self.title.convert("RGBA")
        self.title = ImageTk.PhotoImage(self.title)

        title_label = Label(self, image=self.title, bg="#b3ebf2", borderwidth=0, highlightthickness=0)
        title_label.place(relx = 0.5, 
                   rely = 0.2,
                   anchor = 'center')
        
        