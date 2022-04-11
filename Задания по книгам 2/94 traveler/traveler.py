# Traveler - путешественник
import random

class Universe(object):
    def __init__(self):
        self.worlds = []
        self.MAP = ["Field", "Forest", "Pond", "Lake", "Dense Forest", "Hamlet", "Meadows", "Mushroom glade", "Hill", "Mountain", "Cave"]
    def create_the_worlds(self):
        complexity = None
        while complexity not in ("1", "2", "3"):
            complexity = input("Выберите уровень сложности мира(1-3): ")
            if complexity == "1":
                self.count = 4
            elif complexity == "2":
                self.count = 7
            elif complexity == "3":
                self.count = 11
            else:
                print("Выбранный уровень сложности не существует.")
        self.rand = random.randint(0, self.count)
        print("Создаю миры.")
        print("Вот список созданных миров:")
        for i in range(self.count):
            self.worlds.append(self.MAP[i])
            print(self.worlds[i], end = "")
            if i < self.count - 1:
                print(end = ", ")
            else:
                print()
    def show_all_the_worlds(self):
        print("Список всех миров:")
        for i in range(self.count):
            print(self.worlds[i], end = "")
            if i < self.count - 1:
                print(end = ", ")
            else:
                print()
    def first_world(self):
        self.rand = random.randint(0, self.count)
        rand = int(self.rand)
        worlds = self.worlds
        world = str(worlds[rand])
        return world
class Player(object):
    def __init__(self, name, world, worlds, maps):
        self.name = name
        self.world = world
        self.worlds = worlds
        self.MAP = maps
        self.len_worlds = len(worlds) - 1
        print("Вас зовут", self.name, end = ".\n")
        print("Вы находитесь в", self.world, end = ".\n")
    def __str__(self):
        print("Текущий игрок и его местоположение:")
        print(self.name, "\t", self.world)
    def move(self):
        print("Текущий мир:", self.world)
        world = str(self.world)
        i = self.MAP.index(world)
        a = i - 1
        if a < 0:
            a = self.len_worlds
        b = i + 1
        if b > self.len_worlds:
            b = 0
        print("Доступные миры:", "\n1.", self.worlds[a],"\n2.", self.worlds[b])
        move_in_world = None
        while move_in_world not in ("1", "2"):
            move_in_world = input("Куда хотите переместиться? Выберите мир(1-2): ")
            if move_in_world == "1":
                self.world = self.worlds[a]
            elif move_in_world == "2":
                self.world = self.worlds[b]
            else:
                print("Недопустимый ввод. Повторите попытку.")
        print("Ваш текущий мир:", self.world)

def main():
    print("\t\t\tВас приветствует игра \"Путешественник\".")
    print("\tПрограмма выбирает случайного персонажа и создаёт определенный мир.")
    universe = Universe()
    universe.create_the_worlds()
    name = input("\nВведите имя путешественника: ")
    player = Player(name, universe.first_world(), universe.worlds, universe.MAP)
    choice = None
    while choice != "0":
        print("""
        0 - Выйти из игры
        1 - Список всех миров
        2 - Перейти в ближайший мир
        """)
        choice = input("Выбери один из пунков: ")
        if choice == "0":
            print("Спасибо, что посетили наши миры. Всего доброго.")
            break
        elif choice == "1":
            universe.show_all_the_worlds()
        elif choice == "2":
            player.move()
        else:
            print("Недопустимый ввод. Повторите попытку.")

main()
input("Нажмите Enter, чтобы выйти.")