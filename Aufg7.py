# Eingabe der Benutzerdaten
koerperGroesse = int(input("Geben Sie Ihre Größe in 'm' an: "))
# Berechnung BMI [Body Mass Index]
bmi = int(input("Geben Sie Ihr Gewicht in 'kg' an: ")) /(koerperGroesse*2)
bmi = bmi*100
print("Ihr BMi beträgt:", bmi)
# Deutung des BMI
ergebnisAusgabe1 = "Laut WHO-Einteilung zum BMI haben Sie"
if bmi<18.5:
    ergebnisAusgabe2="Untergewicht."
elif bmi>=18.5 and bmi<25:
    ergebnisAusgabe2="Normalgewicht."
elif bmi>=25 and bmi<30:
    ergebnisAusgabe2="Übergewicht."
elif bmi>=30 and bmi<35:
    ergebnisAusgabe2="starkes Übergewicht (Adipositas Grad I)."
elif bmi>=35 and bmi<40:
    ergebnisAusgabe1="Adipositas Grad II."
elif bmi>=40:
    ergebnisAusgabe2="Adipositas Grad III."
print(ergebnisAusgabe1,ergebnisAusgabe2)
