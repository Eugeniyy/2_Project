# Программа принимает текст из пользовательского ввода и печатает его наоборот
print("\t\t\tВас приветствует программа \"Текст наоборот!\"")
word = input("Введите слово, которое нужно написать наоборот: ")
wordlen = int(len(word) - 1)
drow = ""
while wordlen >= 0:
    drow += word[wordlen]
    wordlen -= 1
print("Ваше слово написанное наоборот:" , drow)
input("\n\nНажмите Enter, чтобы выйти.")
