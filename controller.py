import db, gui
def button_click():
    a = gui.Choice()
    if (a == 1):
        family = gui.Family_input()
        name = gui.Name_input()
        phone = gui.Phone_input()
        description = gui.Description_input()
        db.Saving(family, name, phone, description)
    elif (a == 2):
        book = db.get_base()
        print(book)
    elif(a == 3):
        book = db.get_base()
        b = gui.Choice_find()
        find1 = gui.Find(b)
        if (b == 1):
            len1 = len(find1)
            for i in range (len(book)):
                str1 = ""
                for j in range (len1):
                    str1+=book[i][j]
                if (find1 == str1):
                    print(book[i], book[i+1], book[i+2], book[i+3])
    # elif (b == 2):
    #     find = gui.Name_input()
    # elif (b == 3):
    #     find = gui.Phone_input()
    # elif (b == 4):
    #     find = gui.Description_input()

    
