import math
'''def negy():

   n = 1
   k = 1

   if k % 2 == 1 and (n > 0) and (math.pow(2, n) > k):
      # jó eset
      print("Proth-számok: ", end="")
      for n in range(0, 10, 1):
         proth = (k * math.pow(2, n)) + 1
         print(str(proth) + ", ", end="")
      proth = (k * math.pow(2, 10)) + 1
      print(proth)
   else:
      print("HIBA: Nem megfelelő számok!")
      '''

def negy():

   n = 1
   k = 1
   print("Proth-számok: ", end="")

   while n < 10:
      for m in range(1, 100):
         if k % 2 == 1 and 2 ** m > k:
            proth_szam = (k * 2 ** m) + 1
            print(proth_szam, end=", " if n < 10 else "\n")
            n += 1
            if n >= 10:
               break
      k += 2
