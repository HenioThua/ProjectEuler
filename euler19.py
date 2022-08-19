from datetime import datetime, timedelta 
data = datetime(1900,12,31)
incremento = timedelta(days = 1)
data_final = datetime(2000,12,31)
contador = 0
while data != data_final:
    if data.day == 1 and data.isoweekday() == 7:
        contador+=1 
    data = data + incremento
print(contador)
    




