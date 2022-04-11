# Доработка игры "Отгадай число" из главы 3. Теперь в ней нашла применение функция ask_number()
LOW = 1
HIGH = 100

def ask_number(question, low, high):
    number = None
    while number not in range(low,high):
        number = int(input(question))
        if number not in range(low,high):
            print("Вы не попали в диапазон 1-100.")
    return number

print("\t\t\tДобро пожаловать в программу \"Отгадай число\"!")
print("\nЯ загадаю число от 1 до 100, Вам нужно его отгадать.")
print("Итак, начнём.")
import random
the_number = random.randint(1,100)
count = 0
guess = ask_number("Введите число: " , LOW , HIGH)
while True:
    count +=1
    if guess == the_number:
        break
    if guess > the_number:
        guess = int(input("меньше\n.Ваше число: "))
    else:
        guess = int(input("больше\n.Ваше число: "))
print("Поздравляю! Вы отгадали число!")
print("Было загадано число: " , the_number)
print("Количество Ваших попыток: " , count)
input("\nНажмите Enter, чтобы выйти.")
