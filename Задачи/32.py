# Симулятор статистики монеты орел-решка
print("\t\t\tВас приветствует программа \"Симулятор статистики монеты орел-решка\"")
print("\nПрограмма подбрасывает 100 раз монету и выводит на экран результат выпадения орла и выпадения решки")
count = 1
import random
coin = 0
eagle = 0
tails = 0
while count <= 100:
    coin = random.randint(1,2)
    if coin == 1:
        eagle += 1
    else:
        tails += 1
    count += 1
print("В результате симуляции было получено\nрешек: " , eagle , "\nорлов: " , tails)
input("\nНажмите Enter, чтобы выйти.")
