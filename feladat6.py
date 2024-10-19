def beolvas(szoveg):
    szam = int(input(szoveg))
    return szam

def hat():
    a = beolvas("Add meg az első számot: ")
    b = beolvas("Add meg a második számot: ")
    c = beolvas("Add meg a harmadik számot: ")

    if a > 0 and b > 0 and c > 0:
        if a < c + b and b < a + c and c < a + b:
            print("Bla")
        else:
            print("Nem szerkeszthető")
    else:
        print("Hiba")
