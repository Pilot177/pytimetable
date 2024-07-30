import calendar
import datetime
import json

today = datetime.date.today()

cal = calendar.Calendar(firstweekday=0)  # creazione del calendario personalizzato e setta la monday come primo giorno della settimana

# Ottenere i giorni del mese corrente come lista di settimane
this_month = cal.monthdayscalendar(today.year, today.month)


calendar_data = {
    "year": today.year,
    "month": today.month,
    "weeks": this_month
}

# Salvare il calendario in un file JSON
with open('calendar.json', 'w') as json_file:
    json.dump(calendar_data, json_file, indent=4)

print("Calendario salvato in 'calendar.json'")