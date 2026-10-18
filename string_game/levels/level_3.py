#This file contains a program for working with the trird level of the game my_game

def third_level():
    print("Добро пожаловать на третий уровень")
    print("Здесь вы можете ввести метод, строки, программа выдаст ответ")
    print("1 - метод, который выведет подстроки строки по указанному разделителю")
    print("2 - метод, который поставит между введенными строками ваши подстроки")
    print("3 - метод, который принимает строки, которые оканчиваются не на ноль, а затем выдает слова через разделитель")
    print("Если вы выберете 1 и введете строку 1,2,3,4, а разделитель ,:")
    print("Выведется 1 2 3 4")
    print("Если вы выберете 2Б введете строки 1 2 3 4 0, а затем выберете GG")
    print("Выведется 1GGG2GGG3GGG4")    
    print("Если вы выберете 3 и введете слова 1,2,3,4,разделитель , ,а затем GGG")
    print("Выведется 1GGG2GGG3GGG4")

    flag = True
    while flag:
        print("Введите метод 1, 2, 3 или для выхода введите 4")
        method = str(input())

        if method == "1": #Split 
            print("Введите строку")
            str_inp1 = str(input())
            print("Введите разделитель")
            str_inp2 = str(input())
            print(f"Вы ввели строку с разделителем и получили {str_inp1.split(str_inp2)}")

            
        elif method == "2": #Join
            print("Вводите строки, если решите закончить, введите 0")
            str_inp1 = str(input())
            my_list = []
            while str_inp1 != "0":
                print("Если вы ввели все строки, введите 0")
                str_inp2 = str(input())
                my_list.append(str_inp2)
                if str_inp2 == "0":
                    break
            print("Введите разделитель")
            str_inp2 = str(input())
            print(str_inp2.join(my_list))
            
            
        elif method == "3": #Split + Join
            print("Введите строку")
            str_inp1 = str(input())
            print("Введите разделитель")
            str_inp2 = str(input())
            print("Введите, чем вы хотите разделять, вместо прошлого разделителя")
            str_inp3 = str(input())
            print(f"Вы ввели строку {str_inp1}, получили {str_inp3.join(str_inp1.split(str_inp2))}")

            
        elif method == "4":
            print("Вы вышли с уровня")
            flag = False
            return

        
        else:
            print("Вы ввели что-то не то")


