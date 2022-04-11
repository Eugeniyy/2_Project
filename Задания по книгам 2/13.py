# Автодиллер
price = input("Введите стоимость автомобиля без наценок:")
price = float(price)
tax = float("0.1")
print("Налог - " , tax*100 , "%")
collection = float("0.05")
print("Регистрационный сбор - " , collection*100 , "%")
agent = int("1200")
print("Агентский сбор - " , agent , "р")
transfer = int("3000")
print("Доставка по месту назначение - " , transfer , "р")
print("Окончательная цена автомобиля - " ,\
      price - price*tax - price*collection - agent - transfer , "р")
input("\nНажмите Enter, чтобы выйти.")
