#This file contains a program for working with the second level of the game my_game

def second_level():
    print("Добро пожаловать на второй уровень!")
    print("Здесь вы можете ввести свою строку и метод, программа выведет итоговую строку")
    print("1 - метод, который выведет индекс первого элемента какой-то подстроки в строке")
    print("2 - метод, который заменит подстроку в вашей строке на другую подстроку,которую вы сами введете")
    print("3 - метод, который посчитает все элементы вхождения подстроки в строке")
    print("Если вы выбрали 1 и ввели строку ПрИВеТ МиР, а потом МиР:")
    sub = str("ПрИВеТ МиР")
    sub_2 = str("МиР")
    print(f"Программа выведет: {sub.find(sub_2)}")
    print("Если вы выбрали 2 и ввели ПрИВеТ МиР, потом МиР, потом Школа")
    print(f"Программы выведет: ПрИВеТ Школа")
    print(f"Если вы выбрали 3 и ввели: ПрИВеТ МиР, потом И")
    print("Программа выведет: 1")
    flag = bool(True)

    while flag:
        print("Введите метод 1, 2, 3, для выхода введите 4")
        method = str(input())

        if method == "1":
            print("Введите строку")
            str_inp1 = str(input())
            print("Введите подстроку,индекс которой ищем")
            str_inp2 = str(input())
            if (str_inp1.find(str_inp2) == -1):
                print("Элемент не найден")
            else:
                print(f"Индекс вашей подстроки --> {str_inp1.find(str_inp2)}")

        elif method == "2":
            print("Введите строку")
            str_inp1 = str(input())
            print("Введите подстроку, которую надо заменить")
            str_inp2 = str(input())
            print("Введите строку, на которую меняем вашу подстроку")
            str_inp3 = str(input())
            print(str_inp1.replace(str_inp2, str_inp3))

        elif method == "3":
            cnt = int(0)
            print("Введите строку")
            str_inp1 = str(input())
            print("Введите элемент, количество вхождений которого считаем")
            str_inp2 = str(input())
            for s in str_inp1:
                if s == str_inp2:
                    cnt = cnt + 1
            print(f"Количество вхождений --> {cnt}")

        elif method == "4":
            print("Вы вышли из уровня")
            flag = False
            return

        else:
            print("Вы ввели несуществующий метод")


