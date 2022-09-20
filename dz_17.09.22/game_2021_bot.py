import random 

def check(count, name) -> int: 
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
        


# def game(candy, player, name):
#     player = int(input(f'Ходит {name}: '))
#     candy -= check(player)
#     name = name
#     return candy
    

name_1 = 'игрок'                                                    
name_2 = 'Бот' 
player_1 = 0
# name_1 = input('Введите имя игрока: ')                      

lot = random.randint(0, 1)


candy = 100
while candy > 0:
    if candy > 0:
        candy -= check(player_1, name_1)
        name = name_1
    if candy > 0:
        player_2 = random.randint(1, 28)
        print(f'Ходит бот: {player_2}')
        candy -= player_2
        name = name_2


        
print(f'Победитель {name}!!!')
                         


