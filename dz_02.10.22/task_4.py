# Игра против умного бота

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


name_1 = input('Введите имя игрока: ')
name_2 = 'Бот'
player_1 = 0
candy = 136

lot = random.randint(0, 1)
if lot == 1:
    while candy > 0:
        if candy > 0:
            xod = error_checking(player_1, name_1)
            candy -= xod
            name = name_1
        if candy > 21:
            player_2 = 29 - xod
            print(f'Ходит бот: {player_2}')
            candy -= player_2
            name = name_2
        elif candy > 0:
            player_2 = 21
            print(f'Ходит бот: {player_2}')
            candy -= player_2
            name = name_2
else:
    print(f'Ходит бот: 20')
    candy -= 20
    while candy > 0:
        if candy > 0:
            xod = error_checking(player_1, name_1)
            candy -= xod
            name = name_1
        if candy > 0:
            player_2 = 29 - xod
            print(f'Ходит бот: {player_2}')
            candy -= player_2
            name = name_2

print(f'Победитель {name}!!!')
