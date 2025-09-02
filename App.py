from tkinter import *
from tkinter import ttk
from Menu import MainMenu
from Level_1 import Level1
from Level_2 import Level2
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self):
        # Creating a window, self = root
        super().__init__()
        self.title("Mathfight")
        self.geometry("600x700")

        self.container = Frame(self)
        self.container.pack(fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, Level1, Level2):
            frame = F( parent = self.container, controller = self )
            self.frames[F.__name__] = frame
            frame.grid( row = 0, column = 0, sticky = "nsew" )
        
        self.show_frame("MainMenu")
        
    def show_frame( self, page_class ):
        frame = self.frames[ page_class ]
        frame.tkraise()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()