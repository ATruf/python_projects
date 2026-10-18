#Программа для получения ключа при попадании
#Сюда можно попасть всего один раз
from first_level import first_go as f1 

def Key(card, inp, weapon):
    #Интерфейс для разработчика
    # print("   IN KEY   ")
    # print("            ")

    print("Вы получили ключ!")
    print("Больше в эту клетку вы не можете попасть")
    weapon.append("Key")

    for ind, i in enumerate(card): #Меняем клетку 
            if inp[0] == i[1] and inp[1] == i[2]:
                card[ind] = ["K1", i[1], i[2]]
                return
                
    