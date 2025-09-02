from tkinter import *
from PIL import Image, ImageTk
import random

class Level1(Frame):
    def generate_task(self):

        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, 100)

        if num1 >= num2:
            self.number_1.config(text = num1)
            self.number_2.config(text = num2)
        else:
            self.number_1.config(text = num2)
            self.number_2.config(text = num1)

        list = ["+", "-"]
        self.operator.config(text = random.choice(list))
    
    def check_answer(self):

        user_answer = int(self.input_box.get())
        num1 = int(self.number_1.cget("text"))
        num2 = int(self.number_2.cget("text"))
        op = self.operator.cget("text")
        answer = num1 + num2 if op == "+" else num1 - num2

        if user_answer == answer:
            self.point_counter += 1
            self.input_box.delete(0, END)
            self.generate_task()
        else:
            self.point_counter -= 1
            self.input_box.delete(0, END)

        self.points.config(text = "Points: " + str(self.point_counter))

    def reset_points(self):
        self.point_counter = 0
        self.points.config(text="Points: 0")


    def __init__( self, parent, controller ):
        super().__init__(parent, background = "#b3ebf2")
        self.controller = controller

        self.title = Image.open("pixelarts/solve_message.png").resize((240, 60), Image.Resampling.NEAREST)
        self.title = self.title.convert("RGBA")
        self.title = ImageTk.PhotoImage(self.title)

        title_label = Label(self, image=self.title, bg="#b3ebf2", borderwidth=0, highlightthickness=0)
        title_label.place(relx = 0.5, rely = 0.2, anchor = 'center')

        self.point_counter = 0
        self.points = Label(self, text="Points: " + str(self.point_counter), font=("Fixedsys", 20, "bold"), bg="#b3ebf2")
        self.points.place(relx = 0.5, rely = 0.4, anchor = 'center')

        self.number_1 = Label(self, text = "" , font=("Fixedsys", 20, "bold"), bg="#b3ebf2")
        self.number_1.place(relx = 0.4, rely = 0.5, anchor = 'center')

        self.operator = Label(self, text = "", font=("Fixedsys", 20, "bold"), bg="#b3ebf2")
        self.operator.place(relx = 0.5, rely = 0.5, anchor = 'center')

        self.number_2 = Label(self, text = "", font=("Fixedsys", 20, "bold"), bg="#b3ebf2")
        self.number_2.place(relx = 0.6, rely = 0.5, anchor = 'center')

        self.generate_task()

        self.input_box = Entry(self, font=("Fixedsys", 20, "bold"), bg="#b3ebf2")
        self.input_box.place(relx = 0.5, rely = 0.6, anchor = 'center')

        ok_button = Button(self, text = "OK", font=("Fixedsys", 20, "bold"), command = self.check_answer)
        ok_button.place(relx = 0.5, rely = 0.7, anchor = 'center')

        back_button = Button(self, text="Back to Menu", command=lambda: ( self.reset_points(), controller.show_frame("MainMenu")))
        back_button.place(relx=0.1, rely=0.9, anchor="w")
        
        