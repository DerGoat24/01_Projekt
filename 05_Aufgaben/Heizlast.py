

def Werte():
    print("Gib die Maße für den Raum an:")
    laenge = int(input("Länge in mm: "))
    breite = int(input("Breite in mm: "))
    hoehe = int(input("Höhe in mm: "))
    aussen = int(input("Außentemperatur in °C: "))
    innen = int(input("Innertemperatur in °C: "))

    Volumen =laenge * breite * hoehe *0.001

    dt = int (innen) - int (aussen)

    return Volumen, dt


def Berechnung ():
    P = Volumen * dt * 0.24
    return P

Volumen, dt = Werte()

P2 =Berechnung()

if dt <0:
    print ("Die Innentemperatur ist niedriger als die Außentemperatur")

print (f"die Temperaturdifferenz ist {dt}°C")


print (f"Die Heizlast beträgt {P2} kW")

