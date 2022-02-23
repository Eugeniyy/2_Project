# Доработка функции ask_number
# Вызов ещё с одним параметром - кратностью (величиной шага). Шаг по умолчанию равен 1
NUM = 9
MOVE = 1

def ask_number(question, low, high, move):
    """Просит ввести число и диапазона."""
    response = None
    while response not in range(low,high,move):
        response = int(input(question))
    return response

number = ask_number("Введите число из диапозона 0-8: " , 0, NUM, MOVE)
print("Вы ввели:" , number)
input("\n\nНажмите Enter, чтобы выйти.")
