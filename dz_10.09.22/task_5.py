# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# Fn = F(n-1) + F(n-2)
# негафибоначи Fn = F(n+2)−F(n+1)

# fib_list = []
# i = 0
# n = 8
# while i < n:
#     if i == 0:
#         fib_list.append(0)
#         fib_list.append(1)
#         i += 2
#     else:
#         fib_list.append((fib_list[i - 1]) + (fib_list[i - 2]))
#         i += 1
        
# print(fib_list)
# print(n)


def fibonacci(fib1, fib2):
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        print(fib2, end=' ')

fib1 = 0
fib2 = 1
n = int(input('Введите число '))

fibonacci(fib1, fib2)




def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите число '))
my_list = []
for j in range(1, n):
    my_list.append(fibonacci(j))
print(my_list)
