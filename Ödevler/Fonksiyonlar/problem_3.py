def ekok(sayi1, sayi2):

    for i in range(1, sayi2 + 1):
        for j in range(1, sayi1 + 1):
            if (sayi2 * j == sayi1 * i):
                return(sayi2 * j)
                break



a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))

print("Bu iki sayının EKOK'u: {}".format(ekok(a, b)))





