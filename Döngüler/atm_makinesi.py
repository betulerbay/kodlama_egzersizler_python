print("""
*********************************
ATM Makinesine Hoşgeldiniz

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q'ya basın
************************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz:")

    if (islem == "q"):
        print("İşlemler sonlandı")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif (islem == "2"):
        miktar = int (input("Miktarı belirtin:"))
        bakiye += miktar
    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz:"))

        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekilemez!")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem!")















