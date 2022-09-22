# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. 
#     Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. 
#     За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход. 
    
#     a) Добавьте игру против бота
    
#     b) Подумайте как наделить бота "интеллектом"
#     (Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?)
import random 

def error_checking(count, name) -> int: 
    while True:
        count = input(f'Ходит {name}: ')
        try:
            if (int(count) > 0) and (int(count) < 29):
                return int(count)
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print('Дурак введи число от 1 до 28')
        

flag = input('Начать игру против бота, нажмите +. Или нажмите -')

name_1 = input('Введите имя игрока: ')
if flag == '+': name_2 = 'Бот' 
else: name_2 = input('Введите имя второго игрока: ')  
player_1 = 0
player_2 = 0
candy = 2021                    

lot = random.randint(0, 1)
if lot == 1:
    while candy > 0:
        if candy > 0:
            candy -= error_checking(player_1, name_1)
            name = name_1
        if candy > 0:
            if flag == '+':     
                player_2 = random.randint(1, 28)
                print(f'Ходит бот: {player_2}')
                candy -= player_2
                name = name_2
            else:
                candy -= error_checking(player_2, name_2)
                name = name_2
else:
    while candy > 0:
        if candy > 0:
            if flag == '+':     
                player_2 = random.randint(1, 28)
                print(f'Ходит бот: {player_2}')
                candy -= player_2
                name = name_2
            else:
                candy -= error_checking(player_2, name_2)
                name = name_2
        if candy > 0:
            candy -= error_checking(player_1, name_1)
            name = name_1


        
print(f'Победитель {name}!!!')

