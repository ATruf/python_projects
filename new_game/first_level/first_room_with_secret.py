from random import randint

def casino_stavki(card, inp, weapon): # Функция ставок в казино
    # Интерфейс для разработчика
    print("     STAVKI       ")

    print("Поставьте свое оружие, деньги или предмет!")
    while(True):
        print(f"Ваш арсенал: {weapon}")
        print("Выберите предмет, который вы готовы потерять!")
        print(f"Введите число от 1 до {len(weapon)}")
        while True:
            user_input = input('Введите целое число: ')

            try:
                num = int(user_input)

                if 1 <= num <= len(weapon):
                    chosen_item = weapon[num - 1]
                    
                    # Проверка на то, чтобы элемент не был отрицательным числом
                    if isinstance(chosen_item, (int, float)) and chosen_item < 0:
                        print("Ошибка! Отрицательные числа нельзя сдать в казино.")
                        print(f"Введите число строго от 1 до {len(weapon)}")
                        continue
                        
                    print(f'Отлично! Вы ввели число: {num}')
                    print("")
                    break  # Выходим из цикла, так как преобразование прошло успешно
                else:
                    print(f"Введите число строго от 1 до {len(weapon)}")
            except ValueError:
                print('Ошибка! Попробуйте еще раз.\n')

        random_num1 = randint(1, 10)
        if (random_num1 >= 1 and random_num1 < 5): # Игрок выиграл
            print("Вы выиграли")
            weapon.append(random_num1 * 5)
            print(f"Ваш арсенал: {weapon}")
            print("Введите 1 для выхода!")
            inp_stavki = str(input())
            if inp_stavki == "1" or inp_stavki.lower() == "exit":
                return "exit" # Сигнал главному меню на выход из казино

        else: # Игрок проиграл
            print("Вы проиграли")
            weapon.pop(num - 1)
            print(f"Остаток вашего снаряжения: {weapon}")
            print("Для выхода из казино введите 2, для продолжения - 1")
            inp_stavki_for_exit = str(input())
            if inp_stavki_for_exit == "1":
                return "continue" # Сигнал главному меню запустить ставки заново
            else:
                return "exit"


def casino_sum_nums(card, inp, weapon):
    # Интерфейс для разработчика
    print("     SUM NUMS     ")

    if(len(weapon) == 0):
                weapon.append("пиво")
                weapon.append("stone")
                print("Подарок от казино!")
                print("Вы получили пиво и камень!!")
    
    # Сразу забираем пиво или другую вещь)))
    if(len(weapon) != 0):
        print(f"Вы потеряли {weapon[0]}((")
        weapon.pop(0)

    sum = int(0)

    while(True):
        print("Нажмите 1 для добавления к текущему еще числа")
        print("Если сумма больше 20, вы можете вывести их")
        print("Для этого введите 2")
        inp_str2 = str(input())

        if inp_str2 == "1":
            random_num = randint(1, 10)
            sum += random_num
            print(f"К вашему счету добавилось {random_num}; итоговая сумма {sum}")

            if sum > 25:
                print("Вы проиграли")
                print("Нажмите 1 для выхода из казино и 2 для перехода в меню казино") 
                str_inp = str(input())
                if str_inp == "1":
                    return "exit"
                else:
                    return "continue"

        if inp_str2 == "2":
            if(sum > 25):
                print("Вы проиграли")
                print("Нажмите 1 для выхода из казино и 2 для перехода в меню казино") 
                str_inp = str(input())
                if str_inp == "1":
                    return "exit"
                else:
                    return "continue"

            elif (sum >= 20 and sum <= 25):
                print(f"ВЫ ВЫИГРАЛИ {sum} МОНЕТ")
                weapon.append(sum)
                return "exit"

            else:
                print(f"Ваша сумма {sum}")
                print("Сумма слишком мала((")


def casino_inp(card, inp, weapon):
    # Интерфейс для разработчика
    print("       IN CASINO         ")
    print("                         ")

    print("Вы попали в казино!")
    print("Тут вы можете попробовать выиграть оружие, монеты или ключ")
    
    while True: # Наш главный управляющий цикл внутри казино
        print("Вариант игр:")
        print("1. Ставка")
        print("Вы ставите оружие или монеты и надеетесь выиграть ключ")
        print("Чем больше вы ставите, тем выше шанс на победу")
        print("2. Вы пытаетесь выбить 20 - 25 с помощью рандомного выбора чисел")
        print("Вы можете забрать не менее 20 монет, при этом если сумма ваших чисел будет больше 25 - вы ничего не получите")
        print("Введите 1 или 2 для выбора режима, для выхода 3 вы отдаете первую вещь из вашего списка")
        print(f"Ваши вещи: {weapon}")
        
        choice = str(input())
        if choice == "1":
            if len(weapon) >= 1:
                print("Ура! Вы выбрали ставки!")
                status = casino_stavki(card, inp, weapon)
                if status == "exit":
                    return # Полностью покидаем казино и возвращаемся на карту
            else:
                print("Введите заново (Возможно, для выбора ставок у вас мало вещей)")

        elif choice == "2":
            print("Ура! Вы выбрали сумму цифр")
            status = casino_sum_nums(card, inp, weapon)
            if status == "exit":
                return # Полностью покидаем казино и возвращаемся на карту

        elif choice == "3":
            if len(weapon) != 0:     
                print("Вы потеряли:")
                print(weapon[0])
                weapon.pop(0)
                print("Вы вышли из казино")
                return 
            else:
                print("Вы нищий")
                print("К сожалению, вы не сможете выйти из казино сразу)))")
        else:
            print("Введите заново (Возможно, для выбора ставок у вас мало вещей)")


def Secret(card, inp, weapon):
    # Интерфейс для разработчика
    # print("   IN SECRET ROOM   ")
    # print("               ")
    # print(card)
    # print(inp)
    # print(weapon)

    room_types = ["casino", "weapon", "money+", "money-", "start"]
    random_num = 0

    if room_types[random_num] == "casino":
        casino_inp(card, inp, weapon)