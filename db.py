def Saving(str1: str, str2: str, number_phone: int, str3: str):
    path = 'text2.txt'
    with open(path, 'a') as file:
        file.write(f'\n{str1}\n{str2}\n{number_phone}\n{str3}')



def get_base():
    with open ('text1.txt', 'r') as file:
        return file.readlines()
        
def find_base(Book, Find):
    i = 0
    while (i != -1):
        i = Book.find(Find, i)
        print



