# Рантье (версия без ошибки)
# Демонстрирует type conversion
print(
    """
          Рантье
Программа подсчитывает Ваши ежемесячные расходы. Эту статистику нужно
знать, чтобы у Вас не закончились деньги и Вам не пришлось искать работу.
Введите суммы расходов по всем статьям, перечисленным ниже. Вы богаты -
так не мелочитесь, пишите сумму в долларах, без центов.
    """
    )
car = input("Техническое обслуживание машины 'Ламборгини': ")
car = int(car)
rent = int(input( "Съем роскошной квартиры на Манхэттене: "))
jet = int(input("Apeндa самолета: "))
gifts = int(input ("Подарки: "))
food = int(input("Oбeды и ужины в ресторанах: "))
staff = int(input("Жалованье прислуги (дворецкий. повар. водитель. секретарь): "))
guru = int(input( "Плата личному психоаналитику: "))
games = int(input("Компьютерные игры: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма:", total)
input("\n\nHaжмитe Enteг. чтобы выйти.") 
