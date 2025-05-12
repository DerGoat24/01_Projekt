import random
würfelzahl = random.randint(1, 6)
print("du hast eine", würfelzahl, "geworfen")

Abfrage = input("Sind alle Figuren im Haus? (ja/nein)")
Anzahlwurf = 0
while True:
    if Abfrage == "nein": 

        if  würfelzahl == 6:
            antwort= input("Ist mindestens eine Figur im Haus? (ja/nein)")

            if antwort == "ja":
                antwort2 = input("Ist das Startfeldfrei? (ja/nein)")

                if antwort2 == "ja":
                    print("Du kannst eine Figur ins Spiel bringen")
                    
                else:
                    print("Du musst die Figur auf dem Startfeld bewegen")
                    
            if antwort == "nein":
                print("ziehe die Figur um die Augenzahl nach vorne")
                

        else:
            print("bewege die Figur um die Augenzahl Feld nach vorne")
            break
    

    if Abfrage == "ja":
        
        if würfelzahl == 6:
                print("Du darfst deine Figur auf das Startfeld bewegen")
                
                
        else:
                
                if Anzahlwurf == 3:
                    break

                else:
                    print("neuer Versuch")
                


        Anzahlwurf = Anzahlwurf + 1
