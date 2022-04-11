# Программа выводит список слов в случайном порядке. Без повторений
import random
guess = ["Генератор" , "Рефрежератор" , "Абстракция" , "Манипуляция" , "Гипотиза" , "Инжекция" , "Анатотивность" , "Параметризация" , "Калориметризация" , "Дисперсия" , "Креогенность"]
print("Вот представленный список слок:")
for a in guess:
    print(a)
print("\nА вот этот же список в случайной последовательности:")
len_guess = int(len(guess))
while True:
    i = int(random.randrange(0,len_guess))
    word = guess[i]
    del guess[i]
    print(word)
    len_guess -= 1
    if len_guess == 0:
        break
input("\n\nНажмите Enter, чтобы выйти.")
