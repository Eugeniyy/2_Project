# Программа отгадай число
# Новая реализация с графическим интерфейсом

from tkinter import *

class Application(Frame):
    """ Основная рамка. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.number_comp = random.randint(1, 100)
    def create_widgets(self):
        """ Основные элементы внутри рамки. """
        Label(self,
            text = "Я загадал число от 1 до 100. Попробуйте его отгадать."
            ).grid(row = 0, column = 0, columnspan = 1, sticky = W)
        Label(self,
            text = "Введите число(1-100):"
            ).grid(row = 1, column = 0, sticky = W)
        self.number_us = Entry(self)
        self.number_us.grid(row = 2, column = 0, sticky = W)
        self.display = Text(self, width = 40, height = 2, wrap = WORD)
        self.display.grid(row = 4, column = 0, columnspan = 1)
        Button(self,
            text = "Ввод",
            command = self.game
            ).grid(row = 3, column = 0, sticky = W)
    def game(self):
        display_text = ""
        number_user = ""
        number_use = self.number_us.get()
        for i in number_use:
            if i.isdigit():
                number_user += i
        number_user = int(number_user)
        if number_user > 100:
            display_text = "Вы не попали в диапазон, попробуйте ещё раз."
        else:
            if number_user < self.number_comp:
                display_text = "Мое число больше."
            elif number_user > self.number_comp:
                display_text = "Мое число меньше."
            else:
                display_text = "Поздравляю! Вы угадали!"
        self.display.delete(0.0, END)
        self.display.insert(0.0, display_text)

# основная часть
import random
root = Tk()
root.title("Отгадай число")
root.geometry("350x140")
app = Application(root)
root.mainloop()