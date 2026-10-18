#В данной комнате можно получить подарок
from random import randint
def Box(card, inp, weapon):
    #Интерфейс для разработчика
    # print("   IN ROOM BOX   ")
    # print("                 ")

    print("Вы попали в комнату-сюрприз")
    print("Тут вы можете выбрать:")
    print("1. Сразу получить случайный подарок")
    print("2. Попытаться улучшить оружие")
    print("3. Купить в магазине за монеты оружие или зелье")
    print("Введите цифру для выбора")
    inp_type = str(input())

    if inp_type == "1": #Сразу получить подарок 
        random1 = int(randint(1, 10))
        if random1 >= 1 and random1 <= 7:
            if "sword" in weapon:
                weapon.append("Heal")
                print("Вы получили зелье здоровья!(Heal)")
                print("Вы вышли и больше не сможете сюда заходить!")
                for ind, i in enumerate(card): #Меняем клетку 
                    if inp[0] == i[1] and inp[1] == i[2]:
                        card[ind] = ["B1", i[1], i[2]]
                        return

            if "sword" not in weapon:
                weapon.append("sword")
                print("Вы получили меч!")
                print("Вы вышли и больше не сможете сюда заходить!")
                for ind, i in enumerate(card): #Меняем клетку 
                    if inp[0] == i[1] and inp[1] == i[2]:
                        card[ind] = ["B1", i[1], i[2]]
                        return

        else:
            print("Вы ничего не получили(")
            print("Вы вышли и больше не сможете сюда заходить!")
            for ind, i in enumerate(card): #Меняем клетку 
                if inp[0] == i[1] and inp[1] == i[2]:
                    card[ind] = ["B1", i[1], i[2]]
                    return

    elif inp_type == "2":
        random1 = int(randint(1, 10))
        if "sword" in weapon:
            if random1 >= 1 and random1 <= 7:
                weapon.append("sharpened blade")#!!!!!!!!! Заточенное лезвие
                print("Вы получили заточенное лезвие")
                print("Вы вышли и больше не сможете сюда заходить!")
                for ind, i in enumerate(card): #Меняем клетку 
                    if inp[0] == i[1] and inp[1] == i[2]:
                        card[ind] = ["B1", i[1], i[2]]
                        return

            else:
                print("Вы ничего не получили(")
                print("Вы вышли и больше не сможете сюда заходить!")
                for ind, i in enumerate(card): #Меняем клетку 
                    if inp[0] == i[1] and inp[1] == i[2]:
                        card[ind] = ["B1", i[1], i[2]]
                        return
                    
        else:
            print("Вам нечего улучшать")        
            print("Вы вышли и больше не сможете сюда заходить!")
            for ind, i in enumerate(card): #Меняем клетку 
                if inp[0] == i[1] and inp[1] == i[2]:
                    card[ind] = ["B1", i[1], i[2]]
                    return

    else:
        print("Вы в магазине!")
        print("Цены:")
        print("1. Меч - 50")
        print("2. Зелье здоровья - 40")
        print("3. Палка-ковырялка - 10")

        total_sum = sum(x for x in weapon if type(x) is int)
        if (total_sum >= 0):
            print(f"Сумма денег - {total_sum}")

        else:
            print("Вы нищий")


        print("Если вы выберете вещь, на которую у вас нет денег - это ваши проблемы))")
        print("Введите номер покупки")
        inp_choice = str(input())

        if inp_choice == "1" and total_sum >= 50:
            weapon.append("sword")
            weapon.append(-50)
            print("Вы купили меч!")

        elif inp_choice == "2" and total_sum >= 40:
            weapon.append("Heal")
            weapon.append(-40)
            print("Вы купили зелье здоровья!")

        elif inp_choice == "3" and total_sum >= 10:
            weapon.append("kovyryalka")
            weapon.append(-10)
            print("Вы купили ковырялку!")

        else:
            print("Вы ничего не купили!")

    print("Вы вышли!")
    for ind, i in enumerate(card): #Меняем клетку 
        if inp[0] == i[1] and inp[1] == i[2]:
            card[ind] = ["B1", i[1], i[2]]
            return
    
    
        
