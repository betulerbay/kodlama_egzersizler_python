def muko(sayi):

    i = 1
    toplam = 0

    while (i < sayi):
        if (sayi % i == 0):
            toplam += i
        i += 1
        if (i == sayi - 1):
            if (toplam == sayi):
                return 1
            else:
                return 0

i = 1

while i < 1001:
    if muko(i) == 1:
        print("{}, ".format(i))
    i += 1
