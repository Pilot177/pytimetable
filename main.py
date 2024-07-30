from fileoperation import savecalendar, loadcalendar
from dateoperation import todaydate
from eventoperation import reset

leave = False

while not leave:
    k = str(input())
    
    if k == 'u':
        leave = True
    elif k == 'r':
        reset()
    else:
        print("Comando non valido")