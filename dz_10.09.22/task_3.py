# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_min_max(input_list, output_list):
    for i in range(len(input_list)):
        value = round(input_list[i] % 1, 3)
        if value != 0:
            output_list.append(value)
    
    return (max(output_list) - min(output_list))

my_list = [1.1, 1.2, 3.1, 5, 10.01]
answer_list = []

print(diff_min_max(my_list, answer_list))
