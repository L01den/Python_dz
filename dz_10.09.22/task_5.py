# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# Fn = F(n-1) + F(n-2)
# негафибоначи Fn = F(n+2)−F(n+1)

def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите число '))
normal_fib = []
negariv_fib = []

for j in range(1, n + 1):
    if j % 2 == 0:
        negariv_fib.append(fibonacci(j) * -1)
    else:    
        negariv_fib.append(fibonacci(j))
negariv_fib.reverse()
negariv_fib.append(0)
    
for j in range(1, n + 1):
    normal_fib.append(fibonacci(j))
    
negariv_fib.extend(normal_fib)
print(negariv_fib)
