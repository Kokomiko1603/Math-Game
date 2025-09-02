from tkinter import *
from PIL import Image, ImageTk
import random

class Level2(Frame):
    def generate_task(self):

        list = ["*", ":"]
        operator = random.choice(list)
        self.operator.config(text = operator)

        num1 = random.randrange(0, 10)

        if operator == "*":
            self.number_1.config(text = num1)
            self.number_2.config(text = random.randrange(0, 10))
        else:
            solution = random.randrange(0, 10)
            self.number_1.config(text = num1*solution)
            self.number_2.config(text = num1)
    
    def check_answer(self):

        user_answer = int(self.input_box.get())
        num1 = int(self.number_1.cget("text"))
        num2 = int(self.number_2.cget("text"))
        op = self.operator.cget("text")
        answer = num1 * num2 if op == "*" else num1 // num2

        if user_answer == answer:
            self.point_counter += 1
            self.input_box.delete(0, END)
            self.generate_task()
        else:
            self.point_counter -= 1
            self.input_box.delete(0, END)

        self.points.config(text = "Points: " + str(self.point_counter))

       


    def __init__( self, parent, controller ):
        super().__init__(parent, background = "#b3ebf2")
        self.controller = controller

        self.title = Image.open("pixelarts/solve_message.png").resize((240, 60), Image.Resampling.NEAREST)
        self.title = self.title.convert("RGBA")
        self.title = ImageTk.PhotoImage(self.title)

        title_label = Label(self, image=self.title, bg="#b3ebf2", borderwidth=0, highlightthickness=0)
        title_label.place(relx = 0.5, rely = 0.2, anchor = 'center')

        self.point_counter = 0
        self.points = Label(self, text = "Points: " + str(self.point_counter), bg="#b3ebf2")
        self.points.place(relx = 0.4, rely = 0.4, anchor = 'center')

        self.number_1 = Label(self, text = "" , bg="#b3ebf2")
        self.number_1.place(relx = 0.4, rely = 0.5, anchor = 'center')

        self.operator = Label(self, text = "", bg="#b3ebf2")
        self.operator.place(relx = 0.5, rely = 0.5, anchor = 'center')

        self.number_2 = Label(self, text = "", bg="#b3ebf2")
        self.number_2.place(relx = 0.6, rely = 0.5, anchor = 'center')

        self.generate_task()

        self.input_box = Entry(self, bg="#b3ebf2")
        self.input_box.place(relx = 0.5, rely = 0.6, anchor = 'center')

        ok_button = Button(self, text = "OK", command = self.check_answer)
        ok_button.place(relx = 0.5, rely = 0.7, anchor = 'center')
        
        