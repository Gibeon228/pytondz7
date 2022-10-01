import csv

def Saving(str1: str, str2: str, number_phone: int, str3: str):
    path = 'text2.txt'
    with open(path, 'a') as file:
        file.write(f'\n{str1}\n{str2}\n{number_phone}\n{str3}')

def Saving_csv(str1: str, str2: str, number_phone: int, str3: str):
    with open('sw_data_new.csv', 'a') as f:
        writer = csv.writer(f)
        data = [[str1, str2, number_phone, str3]]
        writer.writerows(data)


def get_base_csv():
    with open('sw_data.csv') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print(row)

def get_base():
    with open ('text1.txt', 'r') as file:
        return file.readlines()
        
def find_base(Book, Find):
    i = 0
    while (i != -1):
        i = Book.find(Find, i)
        print


