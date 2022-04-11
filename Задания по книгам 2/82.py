# Телевизор
# Программа имитирует телевизор как объект, с возможностями вводить
# номер канала, а также увеличивать и уменьшать громкость.
class Tv(object):
    def __init__(self, number = 0, volume = 0):
        print("Вас приветствует программа TV.")
        self.number = number
        self.volume = volume
    def channel(self, number = 0):
        while number == 0:
            number = input("Введите номер канала(1-99): ")
            if number.isdigit():
                number = int(number)
            else:
                print("Некорректный ввод. Повторите попытку.")
                number = 0
            if number == 0 or number > 99:
                print("Некорректный ввод. Повторите попытку.")
                number = 0
        print("Канал", number, "поставлен.")
    def volumes(self, volume = 0):
        while volume == 0:
            volume = input("Введите уровень громкости(0-100): ")
            if volume.isdigit():
                volume = int(volume)
            else:
                print("Некорректный ввод. Повторите попытку.")
                volume = 0
            if volume > 100:
                print("Некорректный ввод. Повторите попытку.")
                volume = 0
        print("Уровень", volume, "поставлен.")
    def talk(self):
        print("Ваш канал сейчас: ")
        print(self.number)
        print("Уровень громкости: ")
        print(self.volume)
def main():
    television = Tv()
    print("""
    Меню пульта
    0 - Выйти
    1 - Выбрать канал
    2 - Установить уровень громкости
    """)
    choice = None
    while choice != "0":
        choice = input("Выберите пункт из меню: ")
        if choice == "0":
            print("Завершение программы.")
        elif choice == "1":
            television.channel()
        elif choice == "2":
            television.volumes()
        else:
            print("Некорректный ввод. Повторите попытку.")
main()
input("\n\nНажмите Enter, чтобы выйти.")