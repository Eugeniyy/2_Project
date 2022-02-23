# Программа отгадай число от 1 до 100
# Человек загадывает число от 1 до 100, компьютер пытается его отгадать
# В конце программы выводится загаданное число человеком и количество попыток компьютера
print("\t\t\tВас приветствует программа \"Отгадай число\".")
print("\nЗагадайте число от 1 до 100, а я попытаюсь его отгадать.")
import random
number = int(input("Не волнуйтесь, я не буду смотреть.\n"))
while True:
    if number >= 0 and number <= 100:
        break
    else:
        number = int(input("Повторите попытку. Видимо Вы не попали в диапозон от 0 до 100.\n"))
number_two = 0
count = 0
digit = random.randint(1,100)
while True:
    number_two = digit
    if number > digit:
        digit = random.randint(number_two,number)
        if digit == number_two:
            continue
        print("Похоже, Ваше число ,больше.")
        print(digit , "!")
        input("Нажмите Enter.")
    elif number < digit:
        digit = random.randint(number,number_two)
        if digit == number_two:
            continue
        print("Чтож, Ваше число меньше. Хм.")
        print(digit , "!")
        input("Нажмите Enter.")
    else:
        break
    count += 1
print("Видимо я угадал! Ваше число: " , number)
if count == 1:
    word = "попытка."
elif count == 2 or count == 3 or count == 4:

    word = "попытки."
elif count == 0 or count >= 5 and count <= 9:
    word = "попыток."
print("На всё у меня ушло всего то" , count , word)
input("\nНажмите Enter, чтобы выйти.")
