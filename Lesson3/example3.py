# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

#1.Принимает на ввод 3 позиционных аргумента
#2.Сравнивает между собой находя 2 наибольшие
#3.Возвращает сумму наибольших

arg1 = int(input("Введите первый аргумент: "))
arg2 = int(input("Введите второй аргумент: "))
arg3 = int(input("Введите третий аргумент: "))

def mySum(arg1, arg2, arg3):
    nums = [arg1, arg2, arg3]
    nums.sort(reverse=True)
    return sum(nums[0:2])

print(mySum(arg1, arg2, arg3))