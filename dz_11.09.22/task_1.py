# Вычислить число c заданной точностью d Пример: 
# при d = 0.001, π = 3.141.d=0.001,π=3.141.﻿﻿ 10^{-1} ≤ d ≤10^{-10}10 −1 ≤d≤10 −10 ﻿﻿ 
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Вычислить число c заданной точностью d Пример: при d = 0.001, π = 3.141.d=0.001,π=3.141.﻿﻿
# Задайте 1 натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Задайте 2 последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Задана 3 натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k. Пример: 
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 35.
# Даны два файла, в каждом из которых находится запись многочлена. 

# Задача 4 - сформировать файл, содержащий сумму многочленов.





# fib_list = []
# i = 0
# n = 8
# while i < n:
#     if i == 0:
#         fib_list.append(0)
#         fib_list.append(1)
#         i += 2
#     else:
#         fib_list.append((fib_list[i - 1]) + (fib_list[i - 2]))
#         i += 1
        
# print(fib_list)
# print(n)


def fibonacci(fib1, fib2):
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        print(fib2, end=' ')

fib1 = 0
fib2 = 1
n = int(input('Введите число '))

fibonacci(fib1, fib2)




def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите число '))
my_list = []
for j in range(1, n):
    my_list.append(fibonacci(j))
print(my_list)







def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите число '))
normal_fib = []
negariv_fib = []

for j in range(1, n + 1):
    if j % 2 == 0:
        negariv_fib.append(fibonacci(j) * -1)
    else:    
        negariv_fib.append(fibonacci(j))
negariv_fib.reverse()
    
for j in range(1, n + 1):
    normal_fib.append(fibonacci(j))
    
print(normal_fib)
print(negariv_fib)
