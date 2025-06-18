import("math")

n =("Nummer zur Überprüfung eingeben")

def prime(n)
    
if n <= 1:
        return False
elif n == 2:
        return True

x == quadratwurzel(n)

i == 2

while i <= x:
    
    if n % i == 0:
        return False
    i += 1 

    else retrun True

print("Die Zahl", n, "ist eine Primzahl." if prime(n) else "Die Zahl", n, "ist keine Primzahl.")
    