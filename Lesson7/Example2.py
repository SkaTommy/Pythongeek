# Реализовать проект расчета суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на
# практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике
# работу декоратора @property.

class Dress:

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat(self):
        return self.size / 6.5 + 0.5

    def get_jacket(self):
        return self.height * 2 + 0.3

    property
    def get_full(self):
        return str(f'Общая площадь ткани: ' f' {(self.size / 6.5 + 0.5)  + (self.height * 2 + 0.3)}')


class Coat(Dress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.get_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Для пальто: {self.get_coat}'


class Jacket(Dress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.get_jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'На костюм: {self.get_jacket}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat.get_full())
print(coat)
print(jacket)



