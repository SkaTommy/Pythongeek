# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = str
    surname = str
    position = str
    price = int
    bonus = int
    def __init__(self, name, surname, position, price, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.price = price
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, price, bonus):
        super().__init__(name, surname, position, price, bonus)
    def get_full_name(self):
        return self.name + ' ' +self.surname
    def get_full_profit(self):
        self.__income = {'profit': self.price, 'bonus': self.bonus}
        return self.__income


manager = Position('Иван', 'Говнов', 'manager', 500, 100)
full_profit = manager.get_full_profit()
print(manager.get_full_name(), 'Profit: ' + str(full_profit['profit']), 'Bonus: ' + str(full_profit['bonus']))

