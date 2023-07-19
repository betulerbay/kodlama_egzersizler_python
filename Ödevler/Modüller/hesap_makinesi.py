import math

while True:
    print("""
    *************************

    1_  Çarpma
    2_  Bölme
    3_  Toplama
    4_  Çıkarma
    5_  Üs alma
    6_  cos(x)
    7_  sin(x)
    8_  tan(x)
    9_  Faktöriyel
    10_ Karekök alma

    !!! ÇIKMAK İÇİN Q YA BASIN !!!
    *************************
    """)
    islem = int(input("Lütfen yapmak istediğiniz işlemin numarasını girin:"))

    if islem == 1:
        a = int(input("İlk sayı:"))
        b = int(input("İkinci sayı:"))
        print("{} x {} = {} ".format(a, b, a*b))
    elif islem == 2:
        a = int(input("İlk sayı:"))
        b = int(input("İkinci sayı:"))
        print("{} / {} = {} ".format(a, b, a / b))
    elif islem == 3:
        a = int(input("İlk sayı:"))
        b = int(input("İkinci sayı:"))
        print("{} + {} = {} ".format(a, b, a + b))
    elif islem == 4:
        a = int(input("İlk sayı:"))
        b = int(input("İkinci sayı:"))
        print("{} - {} = {} ".format(a, b, a - b))
    elif islem == 5:
        a = int(input("Taban:"))
        b = int(input("Üs:"))
        print("{} ^ {} = {} ".format(a, b, pow(a, b)))
    elif islem == 6:
        a = int(input("Açıyı girin:"))
        print("cos{} = {} ".format(a, math.cos(math.radians(a))))
    elif islem == 7:
        a = int(input("Açıyı girin:"))
        print("sin{} = {} ".format(a, math.sin(math.radians(a))))
    elif islem == 8:
        a = int(input("Açıyı girin:"))
        print("tan{} = {} ".format(a, math.tan(math.radians(a))))
    elif islem == 9:
        a = int(input("Faktöriyeli bulunacak sayıyı girin:"))
        print("{}! = {}".format(a, math.factorial(a)))
    elif islem == 10:
        a = int(input("Karekökü alınacak sayıyı girin:"))
        print("{}^(0.5) = {}".format(a, math.sqrt(a)))
    elif islem == "q":
        break
    else:
        print("Yanlış bir tuşa bastınız tekrar deneyin...")

