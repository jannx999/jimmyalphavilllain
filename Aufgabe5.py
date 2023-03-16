# list erstellen
personendaten =["Vorname", "Nachname", "Strasse", "Hausnummer", "PLZ", "Wohnort"]
# Eingabe der daten
personendaten.insert(0, "Jannik")
personendaten.insert(1, "Schwepe")
personendaten.insert(2, "Kleenskamp")
personendaten.insert(3, "6")
personendaten.insert(4, "26129")
personendaten.insert(5, "Oldenburg")
# Hausnummer löschen und ausgeben
personendaten.pop (3)
# ausgabe
print(personendaten)
