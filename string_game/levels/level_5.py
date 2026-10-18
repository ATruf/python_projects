#This file contains a program for working with the fifth level of the game game_py
import re

def fifth_level():
    print("Добро пожаловать на пятый уровень")
    print("Здесь вы можете ввести строку и получить неочевидный ответ)")
    print("Введите строку")
    str_in = str(input())
    text = " pYtHon,is;AWESome , "

# 1. Удаляем лишние символы пунктуации и приводим к нижнему регистру
    clean_text = re.sub(r"[^\w\s]", " ", text).lower()

# 2. Разбиваем на слова, чтобы избавиться от лишних пробелов, и собираем заново
    result = " ".join(clean_text.split()).capitalize()
    print(result)
    print("Для выхода в выбор уровня введите что-либо")
    str_in2 = str(input())
    return


