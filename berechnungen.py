from datetime import datetime

# Berechnung von Schaltjahren
def berechne_schaltjahre(geburtsjahr):
    schaltjahre = 0

    # Alle Jahre seit Geburtsjahr durchlaufen und Schaltjahre zählen
    for jahr in range(geburtsjahr, datetime.now().year + 1):
        if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
            schaltjahre += 1

    return schaltjahre