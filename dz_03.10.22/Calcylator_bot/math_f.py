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
    # elif operat == '^':
    #     return square_root(x)


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

# def square_root(a: int) ->float:
#     return math.sqrt(a)


def example(data: str) ->float:
    my_list = list(data.split())
    return my_list

