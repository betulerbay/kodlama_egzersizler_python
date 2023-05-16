
sys_kullanici_adi = "berbay"
sys_parola = "12345"
giris_hakki = 3


while True:
    kullanici_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (kullanici_adı != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -= 1
    elif (kullanici_adı == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı...")
        giris_hakki -= 1
    elif (kullanici_adı != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakki -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı!")
        break
    if (giris_hakki == 0):
        print("Giriş hakkınız bitti...")
        break
