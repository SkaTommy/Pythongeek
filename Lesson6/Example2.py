# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина),
# width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.

# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    weigth = 25.0
    thickness = 0.05
    allThickness = 5

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def metrkv(self):
        metrvk = self.thickness * self.length * self.width * self.weigth / 1000 ** 2
        print('Потребуется {} тонн асфальта для 1 кв.м дороги.'.format(metrvk))

    def totalmass(self):
        totalmass = self.allThickness * self.length * self.width * self.weigth /1000
        print('Потребуется {} тонн асфальта для всей дороги.'.format(totalmass))

length = input('Введите длинну дороги в метрах: ')
width = input('Введите ширину дороги в метрах: ')

road_to_village = Road(length, width)
road_to_village.metrkv()
road_to_village.totalmass()


