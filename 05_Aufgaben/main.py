from Temperaur import c_to_K, c_to_f

c = float (input("gib die Aktuele Tmeperatur an: "))

f = c_to_f(c)
k = c_to_K(c)


print (f"Die Temperatur in Fahrenheit ist {f}°F")
print (f"Die Temperatur in Kelvin ist {k}K")

