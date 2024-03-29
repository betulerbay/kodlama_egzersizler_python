"""Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını 
dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***"""


liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgen_mi(demet):
    a = demet[0]
    b = demet[1]
    c = demet[2]

    if (a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False
    
    
print(list(filter(ucgen_mi, liste)))