import math
def ketto():
     szam = int(input("Adj meg egy hárojegyű,5-telosztható számot: "))
     if (((szam > 99) and (szam < 1000)) or ((szam < -99) and (szam > -1000))) and (szam % 5 == 0):
        negyzet = szam ** 2
        print(negyzet)
     else:
        print("HIBA: A megadott szám nem megfelelő")

