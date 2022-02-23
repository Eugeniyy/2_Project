# Генератор персонажа
personal = [
    ["Сила\t\t" , int("10")] ,
    ["Здоровье\t" , int("10")] ,
    ["Мудрость\t" , int("10")] ,
    ["Ловкость\t" , int("10")]
    ]
print("\t\t\tГенератор персонажа.")
print("\nВот начальные характеристики Вашего персонажа:")
for states in personal:
    stat, value = states
    print(stat , value)
input("\n\nНажмите Enter, чтобы продолжить.")
i = 30
n = 1
choice = None
while i > 0:
    print("\nУ Вас есть" , i , "пунктов, чтобы распределить параметры.")
    print("Выберите одну из характеристик:")
    for states in personal:
        stat, value = states
        print(n , stat , value)
        n += 1
    choice = int(input("Ваш выбор: "))
    if choice == 1:
        personal[0][1] += 1
    elif choice == 2:
        personal[1][1] += 1
    elif choice == 3:
        personal[2][1] += 1
    elif choice == 4:
        personal[3][1] += 1
    else:
        choice = int(input("Неверный выбор параметра, повторите попытку: "))
    i -= 1
print("\nВот конечный список параметров:")
for states in personal:
    stat, value = states
    print(stat , value)
input("\n\nНажмите Enter, чтобы выйти.")
