# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('Homeworke/dz_11.09.22/example_1.txt', 'r') as e_1:
    e1_list = str(e_1.readline())

with open('Homeworke/dz_11.09.22/example_2.txt', 'r') as e_2:
    e2_list = str(e_2.readline())

answer = f'{e1_list} + {e2_list}'

print(answer)