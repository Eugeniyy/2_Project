# Проигранное сражение
# Показывает тот самый ненавистный нам бесконечный цикл
print("Вашего героя окружила огромная армия троллей.")
print("Смрадными зелеными трупами врагов устланы все окрестные поля.")
print("Одинокий герой достает меч из ножен, готовясь к последней битве в своей жизни.\n")
health = 10
trolls = 0
damage = 3
while health > 0:
    trolls += 1
    health -= damage
    print("Взмахнув мечом, Ваш герой стребляет злобного тролля," \
          "но сам получает повреждение на" , damage , "очков\n")
    print("Остаток жизней Вашего героя: " , health)
print("Ваш герой доблестно сражался и убил" , trolls , "троллей.")
print("Но увы! Он пал на поле боя.")
input("\n\nНажмите Enter, чтобы выйти.")
