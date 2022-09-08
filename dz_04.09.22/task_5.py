# 5. Реализуйте алгоритм перемешивания списка.
from random import randint

start_list = list(range(1,10))
answer_list = []
i = 9

while i > 0:
    i = i - 1
    num = randint(0,i)
    answer_list.append(start_list[num])
    start_list.pop(num)


print(f'Ваш паремешанный список: {answer_list}')








