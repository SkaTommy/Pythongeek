# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
import time
class Car():


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print('Машина едет прямо'), time.sleep(1)

    def stop(self):
        print('Машина остановилась'), time.sleep(1)

    def turn(self):
        print('Манина повернула налево')

class Town(Car):

    def town_car(self, speed, color, name, is_police):
        super(Town, self).__init__(speed, color, name, is_police)
        return self.speed + ' ' + self.color + ' '  + self.name + self.is_police
        
class Sport(Car):
    
    def sport_car(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
class Work(Car):
    def workcar(self, speed, color, name, is_police):
        super(Work, self).__init__(speed, color, name, is_police)
    
class Police(Car):

    def police_car(self, speed, color, name, is_police):
        family = True
        super(Police, self).__init__(speed, color, name, is_police)
        self.is_police = family

        if is_police == 'is_police':
            print('Это полицейская машина.')
        else:
            print('Это обычная машина.')


my_road = Car(60, 'red', 'ford', 'is_police')
my_road.go()
my_road.stop()
my_road.turn()
sport_type = Police(70, 'red', 'ford', 'hachback')
sport_type.police_car(70, 'red', 'ford', 'hachback')
sport_type.police_car(70, 'red', 'ford', 'is_police')

