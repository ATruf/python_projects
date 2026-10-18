#This file contains a program for working with the fourth level of the game my_game

def fourth_level():
    print("Добро пожаловать на третий уровень")
    print("Здесь вы можете ввести метод, строки, программа выдаст ответ")
    print("1 - метод, который покажет, строка состоит только из цифр или нет") #isdigit
    print("2 - метод, который удаляет с начала и конца строки пробелы и специальные символы") #strip
    print("3 - метод, который покажет, строка состоит только из букв или нет") #isalpha
    print("Если вы выберете 1 и введете строку 1234:")
    print("Выведется: Строка состоит только из цифр")
    print("Если вы выберете 2 и введете строку ___1234 3425345_____ ")
    print("Выведется: 1234 3425345")    
    print("Если вы выберете 3 и введете строку 1asdedf")
    print("Выведется: Строка состоит не только из цифр")

    flag = True
    while flag:
        print("Введите метод 1, 2, 3 или для выхода введите 4")
        method = str(input())

        if method == "1": #isdigit
            print("Введите строку")
            str_inp1 = str(input())
            if str_inp1.isdigit():
                print("В вашей строке только цифры")
            else:
                print("В вашей строке не только цифры")

            
        elif method == "2": #strip
            print("Введите строку")
            str_inp1 = str(input())
            print(f"Итоговая строка без пробелов с начала и конца:{str_inp1.strip()}")
            
            
        elif method == "3": #isalpha
            print("Введите строку")
            str_inp1 = str(input())
            if str_inp1.isalpha():
                print("В вашей строке только буквы")
            else:
                print("В вашей строке не только цифры")
            
        elif method == "4":
            print("Вы вышли с уровня")
            flag = False
            return

        
        else:
            print("Вы ввели что-то не то")

