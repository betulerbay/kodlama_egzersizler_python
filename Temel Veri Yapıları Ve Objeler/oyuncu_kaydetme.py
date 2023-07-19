print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takim = input("Oyuncunun Takımı:")

bilgiler = [ad, soyad, takim]  #listeye attık

print("Bilgiler Kaydediliyor...")

print("Oyuncu Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı: {} \n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Bilgiler Kaydedildi...")