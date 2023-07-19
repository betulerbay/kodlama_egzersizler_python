boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki = kilo / (boy * boy)

if (bki < 18.5):
    print("Zayıfsınız.Çokça yemek yiyin!!")
elif (bki < 25):
    print("Normal kilodasınız. Böyle Takılın :)")
elif (bki < 30):
    print("Fazla kilolusun")
else:
    print("Üzgünüm bunu dediğim için ama OBEZSİN")

