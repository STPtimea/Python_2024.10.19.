def beolvas(szoveg):
    szam = int(input(szoveg))
    return szam
def harom():
    a1 = beolvas("Számtani sorozat első eleme (a1):")
    n = beolvas("Elemszám (n):")
    d = beolvas("Differenciál (d): ")

    an = a1 + (n-1)*d
    sn = ((a1 + an) * n) / 2

    print("a1=" + str(a1) + " n=" + str(n) + " d=" + str(d) + " Sn="+str(int(sn)))
    if d > 0:
        print("Alulról korlátos")
    elif d < 0:
        print("Felülről korlátos")
    else:
        print("Állandó")

