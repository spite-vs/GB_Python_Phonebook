import csv

headers = ['№', 'Name', 'Surname', 'Phone', 'Email']


def name_data():
    return input('Имя: ')


def surname_data():
    return input('Фамилия: ')


def phone_data():
    return input('Номер телефон: ')


def email_data():
    return input('Адрес электронной почты: ')


def index():
    with open('phonebook.csv', 'r', encoding='utf-8', newline='') as pb:
        reader = csv.DictReader(pb)
        var = list(reader)
        if len(var) == 1:
            return 1
        return int(var[-1]["№"])+1


def err():
    print('\nКриворукий мудила, давай ещё раз')


def end():
    print('\nНу и гуляй\n')


def wrt(dt):
    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as pb:
        writer = csv.DictWriter(pb, fieldnames=headers)
        writer.writeheader()
        writer.writerows(dt)


def input_data():
    buffer = f'{index()},{name_data()},{surname_data()},{phone_data()},{email_data()}\n'
    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as pb:
        pb.write(buffer)
    print('\n<<< Записал >>>')


def delete_data():
    data = print_data()
    number = int(input('\nИз какой записи удаляем: '))
    while number < 1 or number > len(data):
        err()
        number = int(input('\nИз какой записи удаляем: '))
    key_data = {'2': 'Name', '3': 'Surname',
                '4': 'Phone', '5': 'Email'}
    print(f'\n{data[number-1]["№"]:>3}. {data[number-1]["Surname"]:15} {data[number-1]["Name"]:10}: тел. {data[number-1]["Phone"]}, e-mail: {data[number-1]["Email"]}')
    print('\nЧё удаляем?\n\n1. Всю запись\n2. Имя\n3. Фамилия\n4. Телефон\n5. E-mail\n6. Я передумал')
    com = input("Введите номер операции: ")
    while com < '1' or com > '6':
        err()
        print(
            'Чё удаляем?\n1. Всё\n2. Имя\n3. Фамилия\n4. Телефон\n5. E-mail\n6. Я передумал')
        com = input("Введите номер операции: ")
    if com == '6':
        end()
    elif com == '1':
        del data[number-1]
        for i in range(number-1, len(data)):
            if i == 0:
                data[0]['№'] = 1
                continue
            data[i]['№'] = int(data[i-1]['№'])+1
        wrt(data)
        print('\n<<< Удалил >>>')
    else:
        data[number-1].pop(key_data[com], None)
        wrt(data)
        print('\n<<< Удалил >>>')


def put_data():
    data = print_data()
    number = int(input('\nКакую запись будем менять: '))
    while number < 1 or number > len(data):
        err()
        number = int(input('\nКакую запись будем менять: '))
    key_data = {'2': 'Name', '3': 'Surname',
                '4': 'Phone', '5': 'Email'}
    key_operation = {'2': name_data, '3': surname_data,
                     '4': phone_data, '5': email_data}
    print(f'\n{data[number-1]["№"]:>3}. {data[number-1]["Surname"]:15} {data[number-1]["Name"]:10}: тел. {data[number-1]["Phone"]}, e-mail: {data[number-1]["Email"]}')
    print('\nЧё меняем?\n\n1. Всю запись\n2. Имя\n3. Фамилия\n4. Телефон\n5. E-mail\n6. Я передумал')
    com = input("Введите номер операции: ")
    while com < '1' or com > '6':
        err()
        print(
            'Чё меняем?\n1. Всё\n2. Имя\n3. Фамилия\n4. Телефон\n5. E-mail\n6. Я передумал')
        com = input("Введите номер операции: ")
    if com == '6':
        end()
    elif com == '1':
        for i in key_data:
            data[number-1][key_data[i]] = key_operation[i]()
        wrt(data)
        print('\n<<< Поменял >>>')
    else:
        data[number-1][key_data[com]] = key_operation[com]()
        wrt(data)
        print('\n<<< Поменял >>>')


def print_data():
    with open('phonebook.csv', 'r', encoding='utf-8', newline='') as pb:
        reader = csv.DictReader(pb)
        var = list(reader)
        print()
        for i in var:
            print(
                f'{i["№"]:>3}. {i["Surname"]:15} {i["Name"]:10}: тел. {i["Phone"]}, e-mail: {i["Email"]}')
        print()
        return var


def search_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as pb:
        reader = csv.reader(pb)
        search_word = input('\nЧё ищем: ')
        var = list(
            filter(lambda x: search_word.lower() in ' '.join(x).lower(), reader))
        print(f'\nНайдено {len(var)} записей:\n')
        for i in var:
            print(
                f'{i["№"]:>3}. {i["Surname"]:15} {i["Name"]:10}: тел. {i["Phone"]}, e-mail: {i["Email"]}')
        print()


command = ''
operation = {'1': input_data, '2': delete_data, '3': put_data,
             '4': print_data, '5': search_data, '6': end}
while command != '6':
    print('\nВас приветствует доброжелательный телефонный справочник. Чё хотел?\n1. Записать\n2. Удалить\n3. Поменять\n4. Вывести\n5. Найти\n6. Покинуть чудо-программу')
    command = input("Введите номер операции: ")

    operation.get(command, err)()
