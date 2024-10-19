import math
def ot():

    szam = int(input("Adj meg egy számot 40, 95 között: "))
    if szam < 40 or szam > 95:
        print("HIBA")
    else:
        szam = str(szam)
        print(szam[0])

    # megoldás számolással --> elosztjuk 10-el és kerekítünk

    #2. megoldás
    szam = int(szam)
    print(str(int(szam/10)))

    #3. megoldás
    szam = int(szam)
    print(str(math.floor(szam/10)))

