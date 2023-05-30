# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# Простой вариант:
# Пронумеровать контакты и выбрать изменяемый по номеру.

import functions


while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. изменение или удаление')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.change()
    else:
        break