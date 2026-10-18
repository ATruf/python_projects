#This file contains a program for working with the first level of the game my_game

def first_level():
    #Вывод информации об уровне
    print("Добро пожаловать на первый уровень!")
    print("Здесь вы можете ввести свою строку и метод, программа выведет итоговую строку")
    print("1 - метод upper, он переводит все элементы строки в верхний регистр")
    print("2 - метод lower, он переводит все элементы строки в нижний регистр")
    print("3 - метод capitalize, он переводит первый элемент строки в вехний регистр,а остальные в нижний")
    print("Если вы выбрали 1 и ввели строку ПрИВеТ МиР:")
    print("Программа выведет: ПРИВЕТ МИР")
    print("Если вы выбрали 2 и ввели ПрИВеТ МиР")
    print("Программы выведет: привет мир")
    print("Если вы выбрали 3 и ввели: ПрИВеТ МиР")
    print("Программа выведет: Привет мир")

    flag = bool(True)
    #Получаем на вход строку и обрабатываем
    while flag:
        print("Введите строку")
        str_inp = str(input())
        print("Теперь выберите метод 1, 2 или 3, либо нажмите 4 для выхода")
        method = str(input())

        if method == "1":
            print(f"Ваша строка {str_inp} --> {str_inp.upper()}")
            
        elif method == "2":
            print(f"Ваша строка {str_inp} --> {str_inp.lower()}")
            
        elif method == "3":
            print(f"Ваша строка {str_inp} --> {str_inp.capitalize()}")
            
        elif method == "4":
            print("Отлично,выходим!")
            flag = False;
            return
            
        else:
            print("Вы ввели несуществующий метод")

