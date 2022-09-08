# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 
from random import randint

n = int(input('Введите число N: '))
num_list = []
i = 0

while i < n:
    num = randint(-n,n)
    num_list.append(num)
    i += 1
    
print(f'Ваш список {num_list}')

first_index = int(input('Введите 1 индекс числа: '))
second_index = int(input('Введите 2 индекс числа: '))

print(f'Ваше произведение = {num_list[first_index] * num_list[second_index]}')