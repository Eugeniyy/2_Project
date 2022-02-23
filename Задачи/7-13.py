# Доработка игры "Отгадай число" из главы 3. Теперь в ней нашла применение функция ask_number()
# А основная часть программы выполняется функцией main()
import random
LOW = 1
HIGH = 100

def ask_number(question, low, high):
    number = None
    while number not in range(low,high):
        number = int(input(question))
        if number not in range(low,high):
            print("Вы не попали в диапазон 1-100.")
    return number
def main():
    print("\t\t\tДобро пожаловать в программу \"Отгадай число\"!")
    print("\nЯ загадаю число от 1 до 100, Вам нужно его отгадать.")
    print("Итак, начнём.")
    the_number = random.randint(1,100)
    count = 0
    guess = ask_number("Введите число: " , LOW , HIGH)
    while True:
        count +=1
        if guess == the_number:
            break
        if guess > the_number:
            guess = ask_number("меньше\nВведите число: " , LOW , HIGH)
        else:
            guess = ask_number("больше\nВведите число: " , LOW , HIGH)
    print("Поздравляю! Вы отгадали число!")
    print("Было загадано число: " , the_number)
    print("Количество Ваших попыток: " , count)

main()
input("\nНажмите Enter, чтобы выйти.")
