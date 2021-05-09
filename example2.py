second_all=int(input("Введите количество секунд: "))
hour=((second_all//3600))%24
minute=(second_all//60)%60
seconds=second_all%60
if minute<10:
    minute=str('0'+str(minute))
else:
    minute=str(minute)
if seconds<10:
    seconds=str('0'+str(seconds))
else:
    seconds=str(seconds)
print(str(hour)+':'+str(minute)+':'+str(seconds))