# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число N: '))
i = 1

while i < n + 1:
    answer = (1 + 1/i)**i
    print(f'{i}: {answer}')
    i += 1

