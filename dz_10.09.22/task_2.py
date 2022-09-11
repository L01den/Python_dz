# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def compos_couple(enty_list):
    i = 0
    j = -1
    answer_list = []
    while i < len(my_list) / 2:
        answer_list.append(int(my_list[i]) * int(my_list[j]))
        i += 1
        j -= 1
    return answer_list

my_list = [2, 3, 4, 5, 6]

print(compos_couple(my_list))