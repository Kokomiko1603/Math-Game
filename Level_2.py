from tkinter import *
from PIL import Image, ImageTk

class Level2(Frame):
    def __init__( self, parent, controller ):
        super().__init__(parent, background = "#b3ebf2")
        self.controller = controller