# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

numOfMonth = 0
while numOfMonth > 12 or numOfMonth < 1:
    numOfMonth = int(input("Введите номер месяца: "))
seasons = {
    'Зима': {12, 1, 2},
    'Весна': {3, 4, 5},
    'Лето': {6, 7, 8},
    'Осень': {9, 10, 11}
}
for key, val in seasons.items():
    for num in val:
        if num == numOfMonth:
            print(key)
            break
