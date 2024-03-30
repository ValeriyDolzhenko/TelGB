def get_name_first(num):
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    return data_first[(num-1)*5].replace('\n', '')

def get_surname_first(num):
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    return data_first[(num-1)*5+1].replace('\n', '')

def get_phone_first(num):
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    return data_first[(num-1)*5+2].replace('\n', '')

def get_address_first(num):
    with open ('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    return data_first[(num-1)*5+3].replace('\n', '')

def get_name_second(num):
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    return data_second[(num-1)*4]

def get_surname_second(num):
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    return data_second[(num-1)*4+1]

def get_phone_second(num):
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    return data_second[(num-1)*4+2]

def get_address_second(num):
    with open ('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = ''.join(f.readlines()).replace('\n', ';').split(';')
    return data_second[(num-1)*4+3]