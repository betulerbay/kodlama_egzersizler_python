sekil = input("Hesaplanacak şekli girin:")

if (sekil == "Üçgen"):
    a = int(input("Birinci kenar uzunluğu:"))
    b = int(input("İkinci kenar uzunluğu:"))
    c = int(input("Üçüncü kenar uzunluğu:"))
    knr = [a, b, c]
    if (knr[0] + knr[1] > knr[2] and knr[0] + knr[2] > knr[1] and knr[1] + knr[2] > knr[0]):
        if(knr[0] == knr[1] or knr[0] == knr[2] or knr[1] == knr[2]):
            if(knr[0] == knr[1] == knr[2]):
                print("Bu bir eşkenar üçgendir!")
            else:
                print("Bu bir ikizkenar üçgendir!")
        else:
            print("Bu bir çeşitkenar üçgendir!")
    else:
        print("Bu bir üçgen belirtmez!!")

elif (sekil == "Dörtgen"):
    a = int(input("Birinci kenar uzunluğu:"))
    b = int(input("İkinci kenar uzunluğu:"))
    c = int(input("Üçüncü kenar uzunluğu:"))
    d = int(input("Dördüncü kenar uzunluğu:"))
    knr = [a, b, c, d]
    if (knr[0] == knr[1] and knr[0] == knr[2] and knr[0] == knr[3]):
        print("Bu bir kare")
    elif(knr[0] == knr[2] and knr[1] == knr[3]):
        print("Dikdörtgen")
    else:
        print("Dörtgen")


else:
    print("Üzgünüz bu program {} şekli hesaplayamıyor".format(sekil))