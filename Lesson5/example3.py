# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

file = open('emloyers.txt', 'r')
list = file.readlines()
employers = dict()
for el in list:
    data = el.split(' ')
    employers[data[0]] = float(data[1])
print('Зарплата меньше 20000 руб: ')
for name, salary in employers.items():
    if salary < 20000:
        print(name)

averageSalary = sum(employers.values()) / \
                len(employers)
print('Средняя величина дохода сотрудника: ' + str(averageSalary))