# 3.Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

num_list = [1, 1, 2, 3, 4, 5, 5] 
answer = set()

for i in range(len(num_list)):
    answer.add(num_list[i])


for i in range(len(num_list)):
    count = 0
    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            count += 1
    if count > 1:
        answer.discard(num_list[i])

print(answer)
