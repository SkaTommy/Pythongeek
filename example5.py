revenue_input = int(input("Cумма выручки: "))
costs_input = int(input("Сумма издержек:  "))
profit = revenue_input - costs_input
if profit > 0:
    rent = profit * 100 / revenue_input
    print("Прибыль компании:", profit, "руб")
    print("Рентабельность составляет:", "%.2f" % rent, "%")
    personal = int(input("Численность компании?:  "))
    cash_personal = profit /personal
    print("Прибыль на каждого сотрудника:" "%2.f" % cash_personal)
else:
    print("Компания убыточная!")
