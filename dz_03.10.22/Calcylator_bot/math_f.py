import math

def do_it(x, y, operat):
    if operat == '+':
        return summ(x, y)
    elif operat == '-':
        return subtraction(x, y)
    elif operat == '*':
        return multiply(x, y)
    elif operat == '/':
        return division(x, y)
    elif operat == '**':
        return degree(x, y)
    

def summ(a: int, b: int) ->int:
    return a + b

def subtraction(a: int, b: int) ->int:
    return a - b

def multiply(a: int, b: int) ->int:
    return a * b

def division(a: int, b: int) ->float:
    return a / b

def degree(a: int, b: int):
    return a ** b



def example(data: str) ->float:
    my_list = list(data.split())
    return my_list


# Может быть доделаю для неограниченного числа перемнных
# def do_it(operat, *args):
#     if operat == '+':
#         return summa(*args)
#     elif operat == '-':
#         return subtraction(*args)
#     elif operat == '*':
#         return multiply(*args)
#     elif operat == '/':
#         return division(*args)
#     elif operat == '**':
#         return degree(*args)
#     elif operat == '^':
#         return square_root(*args)
    
# def summa(*args) ->int:
#     sum = 0
#     for n in args:
#         sum += n
#     return sum 

# def subtraction(*args) ->int:
#     subt = args[0]
#     n = 1
#     while n < len(args):
#         subt -= args[n]
#         n += 1
#     return subt

# def multiply(*args) ->int:
#     mult = 0
#     for n in args:
#         mult *= n
#     return mult 

# def division(*args) ->float:
#     div = args[0]
#     n = 1
#     while n < len(args):
#         div /= args[n]
#         n += 1
#     return div

# def degree(*args):
#     deg = args[0] ** args[1]
#     return deg 
    
# def square_root(*args) ->float:
#     return math.sqrt(args[0])    

# print(do_it('^', 25))
