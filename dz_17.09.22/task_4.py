# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaffffcc
# a3f4c2

my_str = 'aaaffffcc'
output_list = []
i = 6



a = my_str.find(my_str[i])
b = my_str.rfind(my_str[i])
output_list.append(f'{my_str[i]}{b-a+1}')
output_str = ''.join([str(i) for i in output_list])
print(output_str)





# for i in range(len(my_str)):
#     count = 1
#     while my_str[i] == my_str[j]:
#         if my_str[i] == my_str[j]:
#             count += 1
#             j += 1
#             lenn += 1
#         else: 
#             j += 1
#             lenn += 1
#     output_list.append(my_str[i])
#     output_list.append(count)
#     output_str = ''.join([str(i) for i in output_list])
#     i = lenn
#     j = lenn 





