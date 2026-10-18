#Import package levels
from levels import level_1 as l1
from levels import level_2 as l2
from levels import level_3 as l3
from levels import level_4 as l4
from levels import level_5 as l5

#Приветствие и выбор уровня
print("Добро пожаловать в игру")

while(True):
    print("Выберите уровень игры от 1 до 5")
    print("Нажмите 6 для выхода")
    level_num = str(input())

    def level_select(level_num):
        if level_num == "1":
            l1.first_level()

        elif level_num == "2":
            l2.second_level()

        elif level_num == "3":
            l3.third_level()

        elif level_num == "4":
            l4.fourth_level()

        elif level_num == "5":
            l5.fifth_level()
            
    if level_num == "6":
        print("Вы вышли из игры")
        break

    else:
        level_select(level_num)

