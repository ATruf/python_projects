#В данном файле происходит генерация карты для игрока

"""
Название координат
I - input(start)
K - Key
M - Monster
S - Secret
B - Box
W - Weapon 
P - Portal
"""
import random

def generate(level_inp):
    if (level_inp == "1"):
        #интерфейс для разработчика
        # print("  IN GEN 1 LEVEL  ")
        # print("                  ")

        #Наша карта будет 5 х 5 (5 по вертикали и 5 по коризонтали)
        array_of_occupied_cells = [[0, 0]] #Массив занятых клеток
        array_of_fulls_cells = [["I", 0, 0]] #Массив занятых клеток с учетом типа клетки

#        bosses = int(1)
#        room_with_secret = int(2)
#        room_with_key = int(1)
#        room_with_weapon = int(2)
#        room_with_box = int(3)
        
        #Добавляем комнату с боссами 
        bosses_index = ["M", random.randint(1, 4), random.randint(1, 4)]
        array_of_fulls_cells.append(bosses_index)
        array_of_occupied_cells.append([bosses_index[1], bosses_index[2]]) # Добавляем индексы босса в массив занятых клеток
#        print(bosses_index)

        room_portal_index = ["P", random.randint(1, 4), random.randint(1, 4)]
        while(room_portal_index[1:3] in array_of_occupied_cells):
            room_portal_index = ["P", random.randint(1, 4), random.randint(1, 4)]
        array_of_occupied_cells.append([room_portal_index[1], room_portal_index[2]])
        array_of_fulls_cells.append(room_portal_index)

        #Добавляем комнату с ключами
        room_key_index = ["K", random.randint(1, 4), random.randint(1, 4)]
        while(room_key_index[1:3] in array_of_occupied_cells):
            room_key_index = ["K", random.randint(1, 4), random.randint(1, 4)]

        array_of_occupied_cells.append([room_key_index[1], room_key_index[2]])
        array_of_fulls_cells.append(room_key_index)

        #Добавляем комнаты с сундуками
        box_num = int(0)
        while(box_num < 3):
            room_with_box_index = ["B", random.randint(1, 4), random.randint(0, 4)]
            if (room_with_box_index[1:3] not in array_of_occupied_cells):
                array_of_occupied_cells.append([room_with_box_index[1], room_with_box_index[2]])
                array_of_fulls_cells.append(room_with_box_index)
                box_num += 1

        #Добавляем комнаты с секретами
        secret_num = int(0)
        while(secret_num < 2):
            room_with_secret_index = ["S", random.randint(1, 4), random.randint(0, 4)]
            if (room_with_secret_index[1:3] not in array_of_occupied_cells):
                array_of_occupied_cells.append([room_with_secret_index[1], room_with_secret_index[2]])
                array_of_fulls_cells.append(room_with_secret_index)
                secret_num += 1

        #Добавляем комнаты с оружием
        weapon_num = int(0)
        while(weapon_num < 2):
            room_with_weapon_index = ["W", random.randint(1, 4), random.randint(0, 4)]
            if (room_with_weapon_index[1:3] not in array_of_occupied_cells):
                array_of_occupied_cells.append([room_with_weapon_index[1], room_with_weapon_index[2]])
                array_of_fulls_cells.append(room_with_weapon_index)
                weapon_num += 1


        array_of_fulls_cells.sort()
        #print(array_of_fulls_cells)

        #Заполнение массива для отсмотра ситуаций
        array_for_programmer = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for i in range(5):
            for j in range(5):
                #Если клетка занята
                if ([i, j] in array_of_occupied_cells):
                    #Если отдельный элемент в списке с названием
                    for word in array_of_fulls_cells:
                        if(word[1:3] == [i, j]):
                            array_for_programmer[i][j] = word[0]

         #Вывод массива
        for i in range(5):
            for j in range(5):
                print(array_for_programmer[i][j],end = " ")
            print()
    return array_of_fulls_cells

    #print("STOP")

            
        




        
    
