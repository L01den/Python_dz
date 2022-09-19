# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_str = 'Мы неабв очень любим Питон иабв Джавуабв !'.split()

# print(' '.join([word for word in my_str if 'абв' not in word]))

import random 


# a, b = 1, 0
# while True:   
#     try:
#         print(a/b)
#         print("Это не будет напечатано")
#         print('10'+10)
#     except TypeError:
#         print("Вы сложили значения несовместимых типов")
#     except ZeroDivisionError:
#         b = int(input("Введите число "))

# count = int(input(f'Ходит: '))

# temp = False
# while temp == False:
#     try:
#         if (count > 0) and (count < 29):
#             print(count)
#             temp = True
#         else:
#             count = int(input(('Введите число от 1 до 28: ')))
#     except ValueError:
#         count = input(('Введите число от 1 до 28: '))
lot = random.randint(1, 2) 
print(lot)