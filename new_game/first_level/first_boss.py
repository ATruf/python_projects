#В данном блоке игрок должен побелить босса 
from random import randint

def Boss_Portala(card, inp, weapon):
    #Интерфейс для разработчика
    # print("    BOSS    ")
    # print("            ")

    print("Сейчас вы сразитесь с боссом!")
    print("Он обитает в подвале МИСИСа")
    print("Всего у него 100 здоровья")
    print("Меч наносит 70 урона")
    print("Камень наносит 30 урона")
    print("Палка-ковырялка наносит 20 урона")
    print("Острое лезвие увеличивает урон в 2 раза")
    print("Зелье исцеления спасает от мощного удара")
    print(f"Ваше снаряжение - {weapon}")

    damage = int(0)
    for i in weapon:
        if i == "sword":
            damage += 70
        elif i == "stone":
            damage += 30
        elif i == "kovyryalka":
            damage += 20

    if "sharpened blade" in weapon:
        damage *= 2

    
    print(f"Cумма вашего оружия - {damage}")
    if("Heal" in weapon):
        if(damage >= 100):
            print("Вы победили!!!")
            weapon.append("boss_ring") 
            return

        else:
            print("У вас слабое оружие((")
            print("Возвращайтесь после прокачки")
            return

    else:
        random_num = randint(1, 3)
        if random_num == 1:
            print("Босс нанес мощный удар и вы потеряли сознание( ")
            print("Приходите в след раз!")        
            return

        if damage >= 100:
            print("Вы победили!!!")
            weapon.append("boss_ring") 
            return

        elif damage < 100:
            print("У вас слабое оружие((")
            print("Возвращайтесь после прокачки")
            return
