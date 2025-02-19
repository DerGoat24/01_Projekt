#Operation = input("""bitte geben sie eine rechenoperation ein:"Add" für Addition, "Sub" für Subtraktion, "Mul" für Multiplikation, "Div" für Division""")   

Operation = input ("bitte geben sie eine rechenoperation ein:Add für Addition, Sub für Subtraktion, Mul für Multiplikation, Div für Division")   


while Operation != "exit":
    match Operation:

        case "Add":
            ZahlA = int(input("bitte geben sie eine Zahl A ein"))
            ZahlB = int(input("bitte geben sie eine Zahl B ein"))
            ergebnis = (ZahlA) + (ZahlB)
            print(f"Die Summe aus {ZahlA} und {ZahlB} ist",(ergebnis))               
            
        
        case "Sub":
            ZahlA = int(input("bitte geben sie eine Zahl A ein"))
            ZahlB = int(input("bitte geben sie eine Zahl B ein"))
            ergebnis = (ZahlA) - (ZahlB)
            print(f"Die Differenz aus {ZahlA} und {ZahlB} ist",(ergebnis))
            

        case "Mul":
            ZahlA = int(input("bitte geben sie eine Zahl A ein"))
            ZahlB = int(input("bitte geben sie eine Zahl B ein"))
            ergebnis = (ZahlA) * (ZahlB)
            print(f"Das Produkt aus {ZahlA} und {ZahlB} ist",(ergebnis))
            
        case "Div":
            ZahlA = int(input)
            
            while (ZahlA) == 0:
                
                print("bitte geben sie eine Zahl ungleich 0 ein")

                eingabe = input("bitte Zahl A eingeben")
                ZahlA = int(eingabe)

                ZahlB = int(input ("bitte Zahl B eingeben"))

            while (ZahlB) == 0: 
                
                print("bitte geben sie eine Zahl ungleich 0 ein")

                eingabe = input("bitte geben sie eine Zahl B eingeben")
                ZahlB = int(eingabe)
                

                ergebnis = (ZahlA)/(ZahlB)
                print(f"Der Quotient aus {ZahlA} und {ZahlB} ist",(ergebnis))
    Operation = input ("bitte geben sie eine rechenoperation ein:Add für Addition, Sub für Subtraktion, Mul für Multiplikation, Div für Division")   

    