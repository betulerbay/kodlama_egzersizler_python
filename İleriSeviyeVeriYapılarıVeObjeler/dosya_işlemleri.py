class Dosya ():

    def __init__(self, dosya_adı):
        with open ("metin.txt", "r", encoding= "utf-8") as file:

            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.yalın_kel = list()

            for kelime in kelimeler:
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")
                kelime = kelime.strip(",")

                self.yalın_kel.append(kelime)

    def kelime_bul(self, arama):

        konum = list()
        say = 1
        for kelime in self.yalın_kel:
            if (kelime == arama):
                konum.append(say)
            
            say += 1

        if (len(konum) == 0):
            print("Dosyada böyle bir kelime yok!")

        else:
            print("{} kelimesi dosyada şuralarda bulunuyor. \n{}".format(arama, konum))


    def kelime_histogramı(self):

        kelime_frekansi = dict()
        kelime_kumesi = set ()

        for kelime in self.yalın_kel:

            kelime_kumesi.add(kelime)
            if (kelime in kelime_frekansi):
                kelime_frekansi[kelime] += 1
            else:
                kelime_frekansi[kelime] = 1

        print("Kelimelerin frekansı....")

        for i, j in kelime_frekansi.items():
            print(" {} kelimesi metinde {} defa geçiyor".format(i, j))

        print("Tüm kelimeler")

        for i in kelime_kumesi:
            print(i)
            print("*****************")



dosya = Dosya("metin.txt")

print("""*************
      
Dosya İşlemleri

1. Tüm kelime frekansı

2. Kelime ara
      
Çıkış için 'q' ya basın.
      
""")
      
while True:
    islem = input("İşlem: ")

    if (islem == "q"):
        print("Programdan çıkılıyor...")
        break
    elif (islem == "1"):
        dosya.kelime_histogramı()
    elif (islem == "2"):
        kelime = input("Aranacak kelimeyi girin:")
        dosya.kelime_bul(kelime)
    else:
        print("Geçersiz işlem!")