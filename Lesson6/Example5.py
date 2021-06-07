from time import sleep

class TrafficLight:
    __color = ""
    def running(self):
        modes = {"red   ": 7, "yellow": 2, "green ": 5}
        # modes = {"yellow": 7, "red   ": 2, "green ": 5} #раскомментировать для проверки последовательности цветов
        check_mode = []
        for __color, time in modes.items():
            self.__color = __color
            check_mode.append(self.__color)
            print(f"\n{self.__color}  ", end="")
            for delay in range(time):
                print(".", end="")
                sleep(1)
        if check_mode == ['red   ', 'yellow', 'green ']:
            print(f"\n\nПоследовательность цветов верная")
        else:
            print(f"\n\nПоследовательность цветов нарушена")
            exit()

first_on_street = TrafficLight()

for iteration in range(5):
    print(f"\nИтерация {iteration}")
    first_on_street.running()
