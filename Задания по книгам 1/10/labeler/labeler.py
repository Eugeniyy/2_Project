# Это я метка
# Показывает применение меток
from tkinter import *
root = Tk()
root.title("Это я, метка")
root.geometry("400x100")
# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
# создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")
lbl.grid()
# старт событийного цикла
root.mainloop()