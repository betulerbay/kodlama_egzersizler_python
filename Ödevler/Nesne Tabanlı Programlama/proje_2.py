import time

class Bilgisayar():

    def __init__(self, pc_durum = "Kapalı", pc_ses = 0, isletim_sistemi = "Windows", uygulamalar =["Google", "Hesap Makinesi", "Kamera"], ram = 16384, islemci = "i7", cekirdek = 6, ekran_boyutu = "15,6"):
        
        self.pc_durum = pc_durum

        self.pc_ses = pc_ses
    
        self.uygulamalar = uygulamalar

        self.isletim_sistemi = isletim_sistemi

        self.ram = ram
        
        self.islemci = islemci

        self.cekirdek = cekirdek

        self.ekran_boyutu = ekran_boyutu

    def pc_ac(self):
        if (self.pc_durum == "Açık"):
            print("Bilgisayar açık")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum = "Açık"

    def pc_kapat(self):
        if (self.pc_durum == "Kapalı"):
            print("Bilgisayar kapalı")
        else:
            print("Bilgisayar kapanıyor...")
            self.pc_durum = "Kapalı"

    def ses_ayari(self):

        while True:
            cevap = input("Ses kapatma: X\nSes kısma: -\nSes arttırma: +\n")

            if (cevap == "-"):
                if (self.pc_ses != 0):
                
                    self.pc_ses -= 1
                    print("Ses:", self.pc_ses)
            elif (cevap == "+"):

                self.pc_ses += 1
                print("Ses:", self.pc_ses)

            elif (cevap == "X"):

                self.pc_ses = 0
                print("Ses:", self.pc_ses)

            elif (cevap == "exit"):
                break

            else:
                print("Geçersiz bir komut kullandınız")

    def uygulama_indir(self, uygulama_ismi):

        boyut = int(input("İndireceğiniz uygulamanın boyutunu giriniz:"))

        if (self.ram - boyut >= 0):

            print("Uygualama indiriliyor...")
        
            time.sleep(2)
            self.uygulamalar.append(uygulama_ismi)
            self.ram -= boyut

            print("Uygulama indirildi\n Kalan alanınız: {}".format(self.ram))
        else:
            print("Bu uygulamayı indirmek için yeterli alanınız yok!")

    def uygulama_sil(self, uygulama_ismi):

        boyut = int(input("Kaldırmak istediğiniz uygulamanın boyutunu giriniz:"))

        self.uygulamalar.remove(uygulama_ismi)
        self.ram += boyut

        print("Uygulama kaldırılıyor...")
        time.sleep(2)
        print("Kalan alanınız: ", self.ram)

    def __str__(self):
        return "Bilgisayar durumu: {}\nSes düzeyi: {}\nBulunan Uygulamalar: {}\nİşletim sistemi: {}\nRam: {}\nİşlemci: {}\nÇekirdek: {}\nEkran boyutu: {}".format(self.pc_durum, self.pc_ses, self.uygulamalar, self.isletim_sistemi, self.ram, self.islemci, self.cekirdek, self.ekran_boyutu)


pc = Bilgisayar()

print("""
Bilgisayar Modeli:

1_ Bilgisayarı Açma

2_ Bilgisayarı Kapama

3_ Ses düzeyi değiştirme

4_ Uygulama indirme

5_ Uygulama silme

6_ Bilgisayar Bilgileri

Çıkmak için 'q' ya basın
""")

while True:
    islem = input("İşlemi Seçiniz:")

    if (islem == "q"):
        print("İşlem sonlandırılıyor...")
        break
    
    elif (islem == "1"):
        pc.pc_ac()

    elif (islem == "2"):
        pc.pc_kapat()

    elif (islem == "3"):
        pc.ses_ayari()

    elif (islem == "4"):
        isim = input("İndireceğiniz uygulamanın ismi?")
        pc.uygulama_indir(isim)
    
    elif (islem == "5"):
        isim = input("Kaldıracağınız uygulama?")
        pc.uygulama_sil(isim)

    elif (islem == "6"):
        print(pc)

    else:
        print("Geçersiz işlem girdiniz!")
















