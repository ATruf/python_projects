from start_window_package import start_window as p1
from start_window_package import generate as gen1
from first_level import first_go as f1
from first_level import first_choice as f1_ch
#from first_level import ____

level = p1.start() #Определяем, на какой уровень хочет идти человек

# if level == "1":
card = gen1.generate(str(level)) #Формируем карту для уровня


inp = [0, 0]  
weapon = []
game_running = True

#Запускаем блок работы с первым уровнем
while game_running:
    # Шаг 1: Игрок выбирает направление и меняет координату (inp)
    f1.Go(card, inp, weapon)
    
    # Шаг 2: Обрабатываем комнату, в которую наступил игрок
    f1_ch.choice(inp, card, weapon)
    
    if "WIN" in weapon:
        break