#В данном файле происходит выбор комнаты в зависимости от координат
from first_level import first_room_with_secret as s_room
from first_level import first_go as go1
from first_level import first_key as key1
from first_level import first_portal as pl1
from first_level import first_box as box1
from first_level import first_boss as boss1

def choice(inp, card, weapon):
    #Интерфейс для разработчика
    # print("   IN CHOICE   ")
    # print("               ")
    # print(card)
    # print(inp)
    # print(weapon)


    flag_room = bool(False)
    for i in card:
        if inp[0] == i[1] and inp[1] == i[2]: #Если мы нашли координату, то выдаем, какой тип комнаты
            type_room = str(i[0])
            flag_room = True
            if type_room == "S": #Если секретная комната
                s_room.Secret(card, inp, weapon)
                return
            
            elif type_room == "K": #Если комната - ключ
                key1.Key(card, inp, weapon) 
                return

            elif type_room == "P": #Если комната - портал
                pl1.Portal(card, inp, weapon)
                return

            elif type_room == "B": #Если комната - это коробка(сюрприз)
                box1.Box(card, inp, weapon)
                return

            elif type_room == "M":
                boss1.Boss_Portala(card, inp, weapon)
                return

            elif type_room == "K1" or type_room == "B1":
                print("Сюда нельзя! Тут вы забрали ключ или были в комнате с подарком")#Убрать дальше
                return
                
    if not flag_room: #Если не нашли комнату, то выдаем пустую комнату
        print("Пустая комната")
        return
