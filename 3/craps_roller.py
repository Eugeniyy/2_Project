# Игральные кубики
# Демонстрирует генерацию случайных чисел
import random
# создаем случайные числа из диапазона 1 - 5
one = random.randint(1, 5)
two = random.randrange(5) + 1
total = one + two
print("При Вашем броскае выпало" , one , "и" , two , "очков, в сумме" , total)
input("\n\nНажмите Enter, чтобы выйти.")
