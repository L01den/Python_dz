n = int(input('Введите число N: '))
new_list = [((1 + 1/i)**i) for i in (map(int, range(1, n+1)))]  # решение в 3 строки
print(new_list)

# print([((1 + 1/i)**i) for i in (map(int, range(1, n+1)))])    # и решение в 2 строки


