import json

def savecalendar(calendar_data):
    # Salvare il calendario in un file JSON
    with open('calendar.json', 'w') as json_file:
        json.dump(calendar_data, json_file, indent=4)
    print("Calendario salvato in 'calendar.json'")
    
def loadcalendar():
    try:
        # Caricare il calendario dal file JSON
        with open('calendar.json', 'r') as json_file:
            calendar_data = json.load(json_file)
        print("Calendario caricato da 'calendar.json'")
        return calendar_data
    except json.JSONDecodeError:
        print("Errore nel caricamento del calendario ")