"""Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız 
programı geliştirerek kalanları "kalanlar.txt" 
dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın."""

def not_hesapla(satir):
    
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    ort = vize1 * (3/10) + vize2 * (3/10) + final * (4/10)

    if (ort >= 90):
        harf = "AA"
    elif (ort >= 85):
        harf = "BA"
    elif (ort >= 80):
        harf = "BB"
    elif (ort >= 75):
        harf = "CB"
    elif (ort >= 70):
        harf = "CC"
    elif (ort >= 65):
        harf = "DC"
    elif (ort >= 60):
        harf = "DD"
    elif (ort >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------>" + harf + "\n"


with open("dosya.txt", "r", encoding = "utf-8") as file:

    liste_eklenecekler = []

    for i in file:
        
        liste_eklenecekler.append(not_hesapla(i))

with open("notlar.txt", "w", encoding="utf-8") as file2:

    for i in liste_eklenecekler:

        file2.write(i)

with open("notlar.txt", "r", encoding="utf-8") as file3:

    kalan = []
    gecen = []

    for satir in file3:

        satir = satir[:-1]

        satir_eleman = satir.split("------>")

        if satir_eleman[1] == "AA" or satir_eleman[1] == "BA" or satir_eleman[1] == "BB" or satir_eleman[1] == "CB" or satir_eleman[1] == "CC" or satir_eleman[1] == "DC":

            gecen.append(satir + "\n")

        else:

            kalan.append(satir + "\n")

with open("kalan.txt", "w", encoding= "utf-8") as file4:

    for i in kalan:

        file4.write(i)

with open("gecen.txt", "w", encoding= "utf-8") as file5:

    for i in gecen:

        file5.write(i)
    