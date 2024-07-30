import datetime
import calendar
from fileoperation import savecalendar, loadcalendar
from dateoperation import todaydate

def reset():
    today = todaydate()

    cal = calendar.Calendar(firstweekday=0)  # creazione del calendario personalizzato e setta monday come firstweekday

    calendar_data = {
        today.year : [] 
    }
    
    for i in range(12):
        this_month = cal.monthdayscalendar(today.year, i+1)     # Ottenere i giorni del mese corrente come lista di settimane
        calendar_data[today.year].append(this_month) 
        
        
        
    savecalendar(calendar_data)