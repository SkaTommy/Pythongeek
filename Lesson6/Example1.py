# 1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
class TrafficLight:
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<3:
            for el in TrafficLight._colors :
                print(el)
                i+=1
                time.sleep(1)

traffic = TrafficLight()
traffic.running()