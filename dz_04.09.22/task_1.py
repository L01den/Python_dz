# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.  
#     *Пример:*
#     - 0,56 -> 11
    
num = input('Введите число: ') 
sum = 0
i = 0
while i < len(num):
    match num[i]:
        case '0' | '.':
            i += 1
        case _:
            sum += int(num[i])
            i += 1
print(sum, len(num))  


