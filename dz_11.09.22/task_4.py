# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2, 4, 5 - генерятся рандомно
# стперень x - задаёт пользователь и она уменьшаеться
import random 

def random_factor(k, min = 0, max = 101) -> list:
    for i in range(k+1):
        my_list.append(random.randint(min, max))
    return my_list
    
def equality(k):
    for i in range(len(my_list)):
        if i!= (len(my_list) - 1):
            output_lits.insert(i, (f'{my_list[i]}*x^{k} +'))
            k -= 1
        else:
            output_lits.insert(i, (f'{my_list[i]} = 0'))
    return output_lits
        
k = int(input('Введите степень числа '))
my_list = []  
output_lits = []
    
random_factor(k)

with open('Homeworke/dz_11.09.22/answer.txt', 'w') as an:
    an.write(' '.join(equality(k)))






# def equality(my_list, k):
#     while i < len(my_list):
#         my_list.insert(i, (f'{my_list[i]}x^{k} +'))
#         k -= 1
#         i += 1
#     return my_list
