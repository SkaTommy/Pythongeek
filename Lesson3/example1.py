# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(arg1, arg2):
    return arg1 / arg2

def getDivident():
    return int(input('Введите делимое: '))

def getDivider():
    prompt = 'Введите делитель: '
    divider = int(input(prompt))
    while divider == 0:
        divider = int(input(prompt))
    return divider

print(division(getDivident(), getDivider()))



