
class Bilgisayar():

    def __init__(self, pc_durum = "Kapalı", pc_ses = 0, isletim_sistemi = "Windows", uygulamalar = ["Hesap Makinesi", google = ["YouTube", "LinkedIN", "Udemy", "Netflix", "Mail", "Medium"], "Kamera"], ram = 16, islemci = "i7", cekirdek = 6, ekran_boyutu = "15,6"):
        
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
            cevap = input("Ses kapatma: X\nSes kısma: -\nSes arttırma: +")

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

    def __str__(self):
        return "Bilgisayar durumu: {}\nSes düzeyi: {}\nİşletim sistemi: {}\nRam: {}\nİşlemci: {}\nÇekirdek: {}\nEkran boyutu: {}".format(self.pc_durum, self.pc_ses, self.isletim_sistemi, self.ram, self.islemci, self.cekirdek, self.ekran_boyutu)

















