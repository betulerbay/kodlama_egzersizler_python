def ebob():
    a = int(input("Birinci sayıyı girin:"))
    b = int(input("İkinci sayıyı girin:"))

    i = 1

    if (a > b):
        while (i <= b):
            if (a % i == 0 and b % i == 0):
                ebob = i
            i += 1
    else:
        while (i <= a):
            if (a % i == 0 and b % i == 0):
                ebob = i
            i += 1

    return ebob


print("EBOB: {}".format(ebob()))




