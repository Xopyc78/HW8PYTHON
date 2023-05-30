def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def change() -> None:
    """Изменяет или удаляет выбранный контакт."""
    with open('book.txt', 'r', encoding='utf-8') as book:
        data=book.readlines()
        data=list(enumerate(data))
    print(data)
    n=int(input("Какую строку по номеру вы хотите отредактировать?"))
    mode=input("Удалить -набери 1, изменить- набери 2")
    if mode=="1":
        data.remove(data[n])
    elif mode=="2":
        data[n]=(input("Введите правильный ФИО")+" | "+input("Введите правильный номер телефона"))
    with open('book.txt', 'w', encoding='utf-8') as book:
        new_data=''
        for i in data:
            new_data+=str(i)
        book.writelines(new_data)
    