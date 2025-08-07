from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        # Creating a window, self = root
        super().__init__()
        self.title("Mathfight")
        self.geometry("600x700")

        self.container = Frame(self)
        self.container.pack(fill = "both", expand = True)

        self.frames = {}

        for F in ():
            frame = F( parent = self.container, controller = self )
            self.frames[F] = frame
            frame.grid( row = 0, column = 0, sticky = "nsew" )
        
    def show_frame( self, page_class ):
        frame = self.frames[ page_class ]
        frame.tkraise()
    