# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
my_list_size = int(input('Введите количество элементов списка: '))
for i in range(0, my_list_size):
    el = input('Введите значение элемента: ')
    my_list.append(el)
i = 0
x = 0 if len(my_list) % 2 == 0 else 1
while i < len(my_list) - x:
    cur = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = cur
    i += 2
print(my_list)
