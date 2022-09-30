def Choice():
    print ("Выберите действие: 1 - добавить запись, 2 - выдать весь справочник, 3 - поиск в книге")
    return int(input()) 

def Choice_find():
    print ("Выберите действие: 1 - найти по фамилии")
    return int(input())

def Family_input():
    return input('Введите фамилию: ')

def Name_input():
    return input('Введите имя: ')

def Phone_input():
    return input('Введите номер телефона: ')

def Description_input():
    return input('Введите описание: ')

def Find(a):
    print ("Введите поисково слово: ")
    if (a != 3):
        return input()
    else:
        return int(input())