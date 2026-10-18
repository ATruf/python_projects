
#В этом блоке мы рассматриваем, есть ли у человека ключ и победил ли он босса. Если есть и он победил - он выходит, если нет - печально  

def Portal(card, inp, weapon):
    #Интерфейс для разработчика
    # print("   IN PORTAL   ")
    # print("               ")

    print("Вы оказались в портале!")
    if "Key" in weapon and "boss_ring" in weapon:
        print("Поздравляем! Игра окончена, вы вышли из портала")
        weapon.append("WIN")
        return
    
    elif "Key" in weapon and "boss_ring" not in weapon:
        print("Победите босса и возвращайтесь!")
        return

    elif "boss_ring" in weapon and "ring" not in weapon:
        print("Найдите ключ и возвращайтесь!")
        return

    else:
        print("Найдите ключ и победите босса! Далее возвращайтесь")
        return 