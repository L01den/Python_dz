import random 

def check(count) -> int:  
    temp = False
    while temp == False:
            if (count > 0) and (count < 29):
                return count
                temp = True
            else:
                count = int(input(('Введите число от 1 до 28: ')))

# def game(candy, player, name):
#     player = int(input(f'Ходит {name}: '))
#     candy -= check(player)
#     name = name
#     return candy
    

name_1 = 'игрок'                                                    
name_2 = 'Бот' 
player_1 = 0
# name_1 = input('Введите имя игрока: ')                      

# lot = random.randint(1, 2)

candy = 2021
while candy > 0:
    if candy > 0:
        player_1 = int(input(f'Ходит {name_1}: '))
        candy -= check(player_1)
        name = name_1
    if candy > 0:
        player_2 = random.randint(1, 28)
        print(f'Ходит бот: {player_2}')
        candy -= player_2
        name = name_2


        
print(f'Победитель {name}!!!')
                         


