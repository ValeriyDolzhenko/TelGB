from data_create import name_data, surname_data, phone_data, address_data
from data_read import get_name_first, get_surname_first, get_name_second, get_surname_second, get_address_first, get_address_second, get_phone_first, get_phone_second

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open ('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open ('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из первого файла:')
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        print(''.join(data_first))


    print('Вывожу данные из второго файла:')
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(''.join(data_second))


def change_data():
    is_first_file = True
    contact = []
    print('Введите фамилию или имя для изменения данных: \n')
    name = str(input())
    #обрабатываем первый файл
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    index = 0
    for i in range(int((len(data_first)+1)/5)):
        if name == get_name_first(i+1) or name == get_surname_first(i+1):
            index = i+1
            contact.append([get_name_first(index), get_surname_first(index), get_phone_first(index), get_address_first(index)])
            break
    ##если индекс не найден (равен нулю) - обрабатываем второй файл:
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    for i in range(int(len(data_second)/4)):
        if name == get_name_second(i+1) or name == get_surname_second(i+1):
            index = i+1
            contact.append([get_name_second(index), get_surname_second(index), get_phone_second(index), get_address_second(index)])
            is_first_file = False
            break
    #проверяем индекс: если нулевой - контакт не найден
    if index == 0:
        print("По заданным данным контакт не найден")
        return
    print("Найденный контакт:")
    print(*contact)
    print("Введите новые данные:")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    if is_first_file:
        data_first[(index-1)*5] = name + '\n'
        data_first[(index-1)*5+1] = surname + '\n'
        data_first[(index-1)*5+2] = phone + '\n'
        data_first[(index-1)*5+3] = address + '\n'
        with open ('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.truncate()
            f.writelines(data_first)
    else:
        data_second[(index-1)*4] = name
        data_second[(index-1)*4+1] = surname
        data_second[(index-1)*4+2] = phone
        data_second[(index-1)*4+3] = address
        for i in range(len(data_second)):
            if data_second[i] != "\n" and data_second[i] != "":
                if (i+1) % 4 == 0:
                    data_second[i] = data_second[i] + '\n'
                else:    
                    data_second[i] = data_second[i] + ';'
        with open ('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.truncate()
            f.writelines(data_second)

def delete_data():
    is_first_file = True
    contact = []
    print('Введите фамилию или имя для удаления данных: \n')
    name = str(input())
    #обрабатываем первый файл
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    index = 0
    for i in range(int((len(data_first)+1)/5)):
        if name == get_name_first(i+1) or name == get_surname_first(i+1):
            index = i+1
            contact.append([get_name_first(index), get_surname_first(index), get_phone_first(index), get_address_first(index)])
            break
    ##если индекс не найден (равен нулю) - обрабатываем второй файл:
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    for i in range(int(len(data_second)/4)):
        if name == get_name_second(i+1) or name == get_surname_second(i+1):
            index = i+1
            contact.append([get_name_second(index), get_surname_second(index), get_phone_second(index), get_address_second(index)])
            is_first_file = False
            break
    #проверяем индекс: если нулевой - контакт не найден
    if index == 0:
        print("По заданным данным контакт не найден")
        return
    print("Удаляемый контакт:")
    print(*contact)
    if is_first_file:
        data_first[(index-1)*5] = ""
        data_first[(index-1)*5+1] = ""
        data_first[(index-1)*5+2] = ""
        data_first[(index-1)*5+3] = ""
        data_first[(index-1)*5+4] = ""
        with open ('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.truncate()
            f.writelines(data_first)
    else:
        data_second[(index-1)*4] = ""
        data_second[(index-1)*4+1] = ""
        data_second[(index-1)*4+2] = ""
        data_second[(index-1)*4+3] = ""
        for i in range(len(data_second)):
            if data_second[i] != "\n" and data_second[i] != "":
                if (i+1) % 4 == 0:
                    data_second[i] = data_second[i] + '\n'
                else:    
                    data_second[i] = data_second[i] + ';'
        with open ('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.truncate()
            f.writelines(data_second)
    
