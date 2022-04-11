# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):
    ###Виртуалный питомец"""
    def __init__(self,name,hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    def __str__(self):
        hunger = str(self.hunger)
        boredom = str(self.boredom)
        rep = "Вы ввели команду разработчика.\n"
        rep += "Текущие параметры:\n"
        rep += "Голод:" + hunger + "\nТоска:" + boredom
        return rep
    @ property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать, чтобы хорошо"
        else:
            m = "ужасно"
        return m
    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()
    def eat(self, food = 4):
        if 0 < food <= 9:
            food = int(input("Введите количество порций. От 1 до 9 По умолчанию 4:"))
        else:
            print("Вы ввели неккоректное количество порций. По умолчанию установлено 4.")
            food == 4
        if food > 3:
            print("Спасибо!!!")
        else:
            print("Спасибо.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        if 0 < fun <= 9:
            fun = int(input("Введите количество минут, которые потратите на игру с питомцем. От 1 до 9. По умолчанию 4."))
        else:
            print("Вы ввели некорректное число минут. По умолчанию установлено 4.")
            fun = 4
        if fun > 3:
            print("Уиии!")
        else:
            print("Спасибо.")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
def main():
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print("""
        Моя заерюшка
        0 - Выйти
        1 - Узнать о самочувствии
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
        choice = input("Ваш выбор: ")
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == "4":
            print(crit)
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нету пункта", choice)

main()
input("\n\nНажмите Enter, чтобы выйти.")