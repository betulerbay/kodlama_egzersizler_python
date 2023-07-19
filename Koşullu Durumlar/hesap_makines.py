print("""**********************

Hesap Makinesi Programı

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi


*****************
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

işlem = input("İşlemi Giriniz:") #işlem sonucunu string olarak alıyoruz!! Girdi string olarak alınacak !!

if işlem == "1" :
    print("{} + {} = {}".format(a, b, a + b))
elif işlem == "2" :
    print("{} - {} = {}".format(a, b, a - b))
elif işlem == "3" :
    print("{} * {} = {}".format(a, b, a * b))
elif işlem == "4" :
    print("{} / {} = {}".format(a, b, a / b))
else:
    print("Geçersiz İşlem")
