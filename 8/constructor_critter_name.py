# Зверюшка с атрибутами
# Показывает создание атрибутов объекта и доступ к ним
class Critter(object):
    ###Виртуальный питомец"""
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.namee = name
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.namee + "\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.namee, "\n")
# основная часть
crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name:")
print(crit1.name)
input("\n\nНажмите Enter, чтобы выйти.")