import random #random bir sayı üretmek için
import time #bir saniye beklemek için

print("""

****************************************
             Sayı Tahmin Oyunu
    1 ile 40 arasında sayıyı tahmin edin
****************************************

""")

rastgele_sayi = random.randint(1, 40)

tahmin_hakki = 7
while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1) #bir saniyeliğine durması için

        print("Daha yüksek bir sayı söyleyin")

        tahmin_hakki -= 1
    elif (tahmin > rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)  # bir saniyeliğine durması için

        print("Daha düşük bir sayı söyleyin")

        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayımız", rastgele_sayi)
        break
    if (tahmin_hakki == 0):
        print("Tahmin hakkınız bitti...")
        print("Sayımız:", rastgele_sayi)
        break
