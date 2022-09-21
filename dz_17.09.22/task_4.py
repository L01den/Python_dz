# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaffffcc
# a3f4c2

def rle_compression(input_str) -> str:
    output_list = []
    i = 0
    while i < len(input_str):
        a = input_str.find(input_str[i])
        b = input_str.rfind(input_str[i])
        output_list.append(f'{input_str[i]}{b-a+1}')
        output_str = ''.join([str(i) for i in output_list])
        i = b + 1
    return output_str

def rle_unpacking(input_str) -> str:
    new_list = []
    i = 0
    j = 1
    while i < len(input_str):
        new_list.append(input_str[i]*int(input_str[j]))
        output_str = ''.join([str(i) for i in new_list])
        i += 2
        j += 2
    return output_str


with open('Homeworke/dz_17.09.22/input_str.txt', 'r') as in_str:
    for line in in_str.readlines():
        with open('Homeworke/dz_17.09.22/output_str.txt', 'w') as on_str:
            on_str.write(rle_compression(line))
    
with open('Homeworke/dz_17.09.22/output_str.txt', 'r') as on_str:
    for line in on_str.readlines():
        with open('Homeworke/dz_17.09.22/input_str2.txt', 'w') as in_str2:
            in_str2.write(rle_unpacking(line))


   
        









