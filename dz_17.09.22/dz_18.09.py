n = int(input('Введите число N: '))
# i = 1

# while i < n + 1:
#     answer = (1 + 1/i)**i
#     print(f'{i}: {answer}')
#     i += 1
my_list = map(int, range(1, n+1))  
new_list = [((1 + 1/i)**i) for i in my_list] 

print(new_list)
