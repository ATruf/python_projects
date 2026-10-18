#В данном файле происходит выбор человеком шага, определение его новой координаты и перенаправление на комнату
from first_level import first_choice as f1_ch
#Функция проверки шага
def test(x_y, dir):

    if dir == "W": #Если идем вверх, то итоговая координата по строке больше или равна нулю
        if x_y[0] - 1 >= 0:
            return True
        else:
            return False

    if dir == "S": #Если идем вниз, то итоговая координата по строке меньше или равна 4
        if x_y[0] + 1 <= 4:
            return True
        else:
            return False

    if dir == "A":
        if(x_y[1] - 1 >= 0): # Если идем вправо, то координата по столбцу больше или равна 0
            return True
        else:
            return False

    if dir == "D":
        if(x_y[1] + 1 <= 4): # Если идем влево, то координата по столбцу меньше или равна 4
            return True
        else:
            return False
    
########

def Go(card, inp, weapon):
    #интерфейс для разработчика
    # print("  IN GO  ")
    # print(card)
    # print(inp)
    # print(weapon)
    # print("         ")

    while True: 
        array_for_output = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], ]
        print("Посмотрите на карту. Вы находитесь в X")
                #Вывод массива
        for i in range(5):
             for j in range(5):
                if i == inp[0] and j == inp[1]:
                    array_for_output[i][j] = "X"
                print(array_for_output[i][j],end = " ")
             print()
    
        print("Вы выбираете, куда идти!")
        print("Нажмите W, чтобы идти вверх")
        print("Нажмите S, чтобы идти вниз")
        print("Нажмите A, чтобы идти влево")
        print("Нажмите D, чтобы идти вправо")
        str_inp_go = str(input())

        if str_inp_go in ["W", "w"]:
            if test(inp, "W"):
                inp[0] -= 1
                return
            else:
                print("ВВЕРХ ИДТИ НЕЛЬЗЯ!!!!!")

        if str_inp_go in ["S", "s"]:
            if test(inp, "S"):
                inp[0] += 1
                return
            else:
                print("ВНИЗ ИДТИ НЕЛЬЗЯ!!!!!")

        if str_inp_go in ["A", "a"]:
            if test(inp, "A"):
                inp[1] -= 1
                return
            else:
                print("ВЛЕВО ИДТИ НЕЛЬЗЯ!!!!!")

        if str_inp_go in ["D", "d"]:
            if test(inp, "D"):
                inp[1] += 1
                return
            else:
                print("ВПРАВО ИДТИ НЕЛЬЗЯ!!!!!")

#######