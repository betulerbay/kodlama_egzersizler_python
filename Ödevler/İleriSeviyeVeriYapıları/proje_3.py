"""Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. 
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

*İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*"""

with open ("mailler.txt", "r", encoding= "utf-8") as file:
    
    for satır in file:
        satır = satır[:-1]
        if (satır.endswith(".com") == True and satır.find("@") != -1):
            print(satır)
