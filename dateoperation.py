import calendar
import datetime

def todaydate():
    today = datetime.date.today()
    cal = calendar.Calendar(firstweekday=0)  # creazione del calendario personalizzato e setta la monday come primo giorno della settimana
    this_month = cal.monthdayscalendar(today.year, today.month)  # Ottenere i giorni del mese corrente come lista di settimane
    return today