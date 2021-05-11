run = int(input("Ежедневнй пробег в км?: "))
distance = int(input("Цель дистанции в км?: "))
current_run = 0
count_day = 0
while True:
    count_day += 1
    print("%s-день:" % count_day, "%.2f" % run)
    if run > distance:
        break
    run = run * 1.10
print("На %s день" % count_day, "результат будет достигнут не менее %s км" % distance)

