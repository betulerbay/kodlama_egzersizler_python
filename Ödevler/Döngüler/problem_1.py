"""Mükemmel sayı olup olmadığını bulma
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
  Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""


sayi = int(input("Hesaplanacak sayıyı girin:"))
i = 1
toplam = 0


while (i < sayi):
    if (sayi % i == 0):
        toplam += i
    if (i == sayi - 1):
        if(toplam == sayi):
            print("{} sayısı bir mükemmel sayıdır".format(sayi))
        else:
            print("{} sayısı mükemmel olmayan bir sayıdır".format(sayi))
    #print("toplam: {} i:{}".format(toplam, i))
    #print(i)
    i += 1
