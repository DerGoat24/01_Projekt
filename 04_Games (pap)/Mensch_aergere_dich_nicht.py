kartenstapel = ["gr7", "gl2", "+4"]
while len (kartenstapel) != 0 : 
    print(kartenstapel)
    kartenstapel.pop(0)
    aktuelleKarte = kartenstapel.pop(0)

    if aktuelleKarte == "+4" :
        print("+4 kann gespielt werden")
        break
if len(kartenstapel) != 0 :
    print("Kartenstapel ist leer")


