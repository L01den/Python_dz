# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: ')) 
num_list = []

num = 1
i = 1
while i < n + 1:
    match i:
        case 1:
            num_list.append(num)
            i += 1
        case _:
            num *= i
            num_list.append(num)
            i += 1
print(num_list)