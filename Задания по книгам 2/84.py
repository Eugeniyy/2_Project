# Зооферма
# Программа создаёт обитателей зоофермы, за которой пользователю нужно следить

import random

class Critter(object):
    count = 0
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.count += 1
        if Critter.count == 1:
            print("Привет! Я живу на твоей ферме. Меня зовут", self.name, end=".\n")
        if Critter.count == 2:
            print("Привет! Я тоже живу на твоей ферме. А меня зовут", self.name, end=".\n")
        if Critter.count == 3:
            print("Привет! Меня зовут", self.name, ".И я живу на твоей ферме.")
    def __str__(self):
        hunger = str(self.hunger)
        boredom = str(self.boredom)
        condition = "Текущее состояние питомца " + self.name + ":"
        condition += "\n" + "Голод: " + hunger
        condition += "\n" + "Тоска: " + boredom
        return condition
    def pass_time(self):
        r = random.randint(1,3)
        self.boredom += r
        r = random.randint(1,3)
        self.hunger += r
    def eat(self, food = 4):
        print("Сколько Вы хотите дать порций еды", self.name, "?(1-10порций):")
        food = input()
        if food.isdigit():
            food = int(food)
        else:
            print("Вы ввели некорректное значение. По умолчанию установлено 4")
            food = 4
        if food == 0 or food > 10:
            print("Вы ввели некорректное число. По умолчанию установлено 4")
            food = 4
        self.hunger -= food
        print("Спасибо!")
    def game(self,fun = 4):
        print("Сколько Вы хотите уделить времени", self.name, "?(1-10минут):")
        fun = input()
        if fun.isdigit():
            fun = int(fun)
        else:
            print("Вы ввели некорректное значение. По умолчанию установлено 4")
            fun = 4
        if fun == 0 or fun > 10:
            print("Вы ввели некорректное число. По умолчанию установлено 4")
            fun = 4
        self.boredom -= fun
        print("Спасибо!")
    def talk_eat(self):
        print("Похоже твой питомец", self.name, "хочет кушать. Пора его покормить.")
    def talk_game(self):
        print("Твой питомец", self.name, "скучает. Пора с ним поиграть.")
    def return_critter(self):
        self.hunger = 0
        self.boredom = 0
def main():
    print("\t\t\tВас приветствует зооферма!")
    print("Программа создаст 3 животных, за которыми Вам нужно будет ухаживать.")
    print("Вы заходите на зооферму.")
    crit_jasy = Critter("Jasy")
    crit_nancy = Critter("Nancy")
    crit_jhon = Critter("Jhon")
    choice = None
    while choice != 0:
        print("""
        Список Ваших возможностей:
        0 - Выйти
        1 - Узнать состояние всех животных
        2 - Покормить всех питомцев
        3 - Покормить конкретного питомца
        4 - Программа развлечений для всех питомцев
        5 - Программа развлечений для конкретного питомца
        """)
        choice = input("Ваш выбор: ")
        if choice == "0":
            print("Спасибо, что посетили нашу ферму! О всех животных будет заботиться программа")
            print("во время Вашего отсутствия!\nУдачи!")
            crit_jasy.return_critter()
            crit_nancy.return_critter()
            crit_jhon.return_critter()
            break
        elif choice == "1":
            print(crit_jasy)
            print(crit_nancy)
            print(crit_jhon)
            crit_jasy.pass_time()
            crit_nancy.pass_time()
            crit_jhon.pass_time()
        elif choice == "2":
            crit_jasy.eat()
            crit_nancy.eat()
            crit_jhon.eat()
            crit_jasy.pass_time()
            crit_nancy.pass_time()
            crit_jhon.pass_time()
        elif choice == "3":
            name = None
            while not name:
                name = input("Введите имя питомца(Jasy, Nancy или Jhon): ")
                name = name.capitalize()
                print(name)
                if name == "Jasy" or name == "Nancy" or name == "Jhon":
                    continue
                else:
                    print("На данной ферме нету", name, ". Повторите попытку. Либо нажмите Enter, чтобы выйти.")
                    name = None
                if name == "":
                    break
            if name == "Jasy":
                crit_jasy.eat()
            elif name == "Nancy":
                crit_nancy.eat()
            elif name == "Jhon":
                crit_jhon.eat()
            crit_jasy.pass_time()
            crit_nancy.pass_time()
            crit_jhon.pass_time()
        elif choice == "4":
            crit_jasy.game()
            crit_nancy.game()
            crit_jhon.game()
            crit_jasy.pass_time()
            crit_nancy.pass_time()
            crit_jhon.pass_time()
        elif choice == "5":
            name = None
            while not name:
                name = input("Введите имя питомца(Jasy, Nancy или Jhon): ")
                name = name.capitalize()
                print(name)
                if name == "Jasy" or name == "Nancy" or name == "Jhon":
                    continue
                else:
                    print("На данной ферме нету", name, ". Повторите попытку. Либо нажмите Enter, чтобы выйти.")
                    name = None
                if name == "":
                    break
            if name == "Jasy":
                crit_jasy.game()
            elif name == "Nancy":
                crit_nancy.game()
            elif name == "Jhon":
                crit_jhon.game()
            crit_jasy.pass_time()
            crit_nancy.pass_time()
            crit_jhon.pass_time()
        else:
            print("Некорректный ввод. Повторите попытку.")
        if crit_jasy.hunger > 20 or crit_jasy.boredom > 20 or crit_nancy.hunger > 20 or crit_nancy.boredom > 20 or crit_jhon.hunger > 20 or crit_jhon.boredom > 20:
            if crit_jasy.hunger > 20 or crit_jasy.boredom > 20:
                print("Похоже Jasy нездоровится. Я заберу питомцев и приведу их в порядок.")
            if  crit_nancy.hunger > 20 or crit_nancy.boredom > 20:
                print("Похоже Nancy нездоровится. Я заберу питомцев и приведу их в порядок.")
            if crit_jhon.hunger > 20 or crit_jhon.boredom > 20:
                print("Похоже Jhon нездоровится. Я заберу питомцев и приведу их в порядок.")
            crit_jasy.return_critter()
            crit_nancy.return_critter()
            crit_jhon.return_critter()
            print("В следующий раз постарайтесь лучше следить за питомцами.\n Удачи!")
            break
        if crit_jasy.hunger > 10:
            crit_jasy.talk_eat()
        if crit_nancy.hunger > 10:
            crit_nancy.talk_eat()
        if crit_jhon.hunger > 10:
            crit_jhon.talk_eat()
        if crit_jasy.boredom > 10:
            crit_jasy.talk_game()
        if crit_nancy.boredom > 10:
            crit_nancy.talk_game()
        if crit_jhon.boredom > 10:
            crit_jhon.talk_game()

main()
input("Нажмите Enter, чтобы выйти.")