# Счет в ресторане

from tkinter import *

class Application(Frame):
    """ Основная рамка. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Основные элементы на рамке. """
        self.bun = BooleanVar()
        self.bread = BooleanVar()
        self.flatbread = BooleanVar()
        self.shurpa = BooleanVar()
        self.chuchvara = BooleanVar()
        self.uygur_meat = BooleanVar()
        self.lagman = BooleanVar()
        Label(self,
            text = "Меню ресторана"
            ).grid(row = 0, column = 1, sticky = W)
        Label(self,
            text = "Выберите несколько блюд:"
            ).grid(row = 1, column = 1, sticky = W)
        Label(self,
            text = "Выпечка"
            ).grid(row = 2, column = 0, sticky = W)
        Checkbutton(self,
            text = "Булочка(20р)",
            variable = self.bun
            ).grid(row = 3, column = 0, sticky = W)
        Checkbutton(self,
            text = "Хлеб(15р)",
            variable = self.bread
            ).grid(row = 3, column = 1, sticky = W)
        Checkbutton(self,
            text = "Лепешка Тандыр(30р)",
            variable = self.flatbread
            ).grid(row = 3, column = 2, sticky = W)
        Label(self,
            text = "Традиционные восточные блюда",
            ).grid(row = 4, column = 0, sticky = W)
        Checkbutton(self,
            text = "Шурпа с курицей(250р)",
            variable = self.shurpa
            ).grid(row = 5, column = 0, sticky = W)
        Checkbutton(self,
            text = "Чучвара(300р)",
            variable = self.chuchvara
            ).grid(row = 5, column = 1, sticky = W)
        Checkbutton(self,
            text = "Мясо по-уйгурски(270р)",
            variable = self.uygur_meat
            ).grid(row = 6, column = 0, sticky = W)
        Checkbutton(self,
            text = "Лагман(270р)",
            variable = self.lagman
            ).grid(row = 6, column = 1, sticky = W)
        Button(self,
            text = "Счет",
            command = self.expense
            ).grid(row = 8, column = 2, sticky = E)
        self.text_score = Text(self, width = 55, height = 4, wrap = WORD)
        self.text_score.grid(row = 7, column = 0, columnspan = 3)
    def expense(self):
        score = 0
        text = "Ваш заказ:\n"
        if self.bun.get():
            score += 20
            text += " булочка,"
        if self.bread.get():
            score += 15
            text += " хлеб,"
        if self.flatbread.get():
            score += 30
            text += " лепешка Тандыр,"
        if self.shurpa.get():
            score += 250
            text += " шурпа с курицей,"
        if self.chuchvara.get():
            score += 300
            text += " чучвара,"
        if self.uygur_meat.get():
            score += 270
            text += " мясо по-уйгруски,"
        if self.lagman.get():
            score += 270
            text += " лагман,"
        text = text[0:-1]
        text += "\nСчет: " + str(score)
        self.text_score.delete(0.0, END)
        self.text_score.insert(0.0, text)

# основная часть программы
root = Tk()
root.title("Ресторан")
app = Application(root)
root.mainloop()