# Задание 1
import math

n = int(input('Введите желаемое количество знаков после заптятой '))
print(str(math.pi)[:n+2])

# Задание 2

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
    else:
        i += 1

print(num_list)




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
    
for j in range(1, n + 1):
    normal_fib.append(fibonacci(j))
    
print(normal_fib)
print(negariv_fib)
