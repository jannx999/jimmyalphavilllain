# 
zahl1 = int(input("Hier zahl von 1 bis 100 eingben:"))
if zahl1 >= 0 and zahl1 <= 20:
    print("Die Zahl",zahl1,"liegt im ersten intervall von 0-20")
if zahl1 >= 21 and zahl1 <= 40:
    print("Die Zahl",zahl1,"liegt im zweiten intervall von 21-40")
if zahl1 >= 41 and zahl1 <= 60:
    print("Die Zahl",zahl1,"liegt im dritten intervall von 41-60")
    if zahl1%2 == 0:
        print("Ihre Zahl ist grade")
    else:
        print("Ihre Zahl ist ungerade")
if zahl1 >= 61 and zahl1 <= 80:
    print("Die Zahl",zahl1,"liegt im vierten intervall von 61-80")
if zahl1 >= 81 and zahl1 <= 100:
    print("Die Zahl",zahl1,"liegt im fünften intervall von 81-100")
