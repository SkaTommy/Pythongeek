# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def myData(myName, mySurmane, myYear, myCity, myEmail, myPhone):
    myList = myName + ' ' + mySurmane + ' ' + myYear + ' ' + myCity + ' ' + myEmail + ' ' + myPhone
    return myList



myName = input('Введите ваше имя: ')
mySurmane = input('Введите вашу фамилию: ')
myYear = input('Введите год рождения: ')
myCity = input('Введите ваш город: ')
myEmail = input('Введите ваш email: ')
myPhone = input('Введите номер телефона: ')


print(myData(myName, mySurmane, myYear, myCity, myEmail, myPhone))