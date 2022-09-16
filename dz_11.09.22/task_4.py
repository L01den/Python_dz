# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2, 4, 5 - генерятся рандомно
# стперень x - задаёт пользователь и она уменьшаеться
from random import randint

def random_factor(k, min = 0, max = 101) -> list:
    for i in range(k+1):
        my_list.append(random.randint(min, max))
    return my_list
    
# def equality(my_list, k):
#     for i in range(len(my_list):
        

k = int(input('Введите степень числа '))
my_list = []
    
    
print(random_factor(k))

my_list.insert(0, (f'{my_list[0]}x^{k} +'))







# def equality(my_list, k):
#     while i < len(my_list):
#         my_list.insert(i, (f'{my_list[i]}x^{k} +'))
#         k -= 1
#         i += 1
#     return my_list
