# Компьютерный датчик настроение
# Показывает использование elif
import random
print("Я ощущаю Вашу энергетику. От моего экрана не скрыто ни одно из Ваших чувству.")
print("Итак, Ваше настроение...")
mood = random.randint(1, 3)
if mood == 1:
    #радостное
    print( \
        """
    ----------------
    |              |
    |  O      O    |
    |              |
    |     <        |
    |              |
    |  \       /   |
    |    \___/     |
     ______________
                 """)
elif mood == 2:
    #так себе
    print( \
        """
    ----------------
    |              |
    |  O      O    |
    |              |
    |     <        |
    |              |
    |  ---------   |
    |              |
     ______________
                 """)
elif mood == 3:
    #плохое
    print( \
        """
    ----------------
    |              |
    |  O      O    |
    |              |
    |     <        |
    |              |
    |     --       |
    |   /    \     |
     ______________
                 """)
else:
    print("Не бывает такого настроения! (Должно быть Вы совершенно не в себе.)")
print("...Но это только сегодня.")
input("\n\nНажмите Enter, чтобы выйти.")
