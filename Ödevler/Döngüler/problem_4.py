"""

Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları
"toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın
ve ekrana "toplam değişkenini" bastırın.

"""

toplam = 0

while True:
    girdi = input("Sayı(Çıkmak için 'q' ya basın):")
    if(girdi == "q"):
        break
    else:
        sayi = int(girdi)
        toplam += sayi
        print(toplam)
