number = int(input("Введите целое число: "))
max_num = number%10
number = number//10
while number > 0:
    if number%10 > max_num:
        max_num = number%10
    number = number//10
print(max_num)