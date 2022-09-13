# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_number(number):
    str_num = ''
    while number != 0:
        str_num += (str(number % 2))
        number //= 2
    bin_num = str_num[::-1]
    return bin_num

num = int(input('Введите число: '))
print(binary_number(num))
