# list erstellen
personendaten =[]
# Eingabe der daten
personendaten.insert(0, "Jannik")
personendaten.insert(1, "Schwepe")
personendaten.insert(2, "Kleenskamp")
personendaten.insert(3, "6")
personendaten.insert(4, "26129")
personendaten.insert(5, "Oldenburg")
# löschen der hausnummer
personendaten.pop(3)
# neue hausnummer einfügen
personendaten.insert(3, 21)
# ausgabe
print(personendaten)
