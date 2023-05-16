"""
Armstrong sayısı olup olmadığını bulma
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve
oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Sadece 3 ve 4 basamaklı sayılarda Armstrong sayısı hesaplanır

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

sayi = int(input("Hesaplanacak sayıyı girin:"))

if (sayi % 1000 == sayi):
    a = sayi // 100 #birinci basamak
    b = (sayi // 10) % 10 # ikinci basamak
    c = sayi % 10 #üçüncü basamak
    if(sayi == a**3 + b**3 + c**3):
        print("{} sayısı üç basamaklı bir Armstrong sayısıdır".format(sayi))
    else:
        print("Bu bir armstrong sayısı değildir")
else:
    a = sayi // 1000 #birinci basamak
    b = ((sayi // 100) % 100) % 10#ikinci basamak
    c = (sayi // 10) % 10 #üçüncü basamak
    d = sayi % 10 #dördüncü basamak
    if (sayi == a **4 + b**4 + c**4 + d**4):
        print("{} sayısı dört basamaklı bir Armstrong sayısıdır".format(sayi))
    else:
        print("Bu bir armstrong sayısı değildir")

