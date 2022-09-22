# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = int(input('Введите число '))

num_list = []
i = 2
value = n
while i < value:
    if n % 2 == 0:
        num_list.append(2)
        n /= 2
        i += 1
    elif n % i == 0:
        num_list.append(i)
        n /= i
        i += 1
    elif (i == value - 1) and (len(num_list) == 0):
        num_list.append(value)
    else:
        i += 1

print(num_list)


