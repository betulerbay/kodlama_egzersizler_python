""""futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe 
ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. 
Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın."""

with open("takımlar.txt", "r", encoding= "utf-8") as file:

    gs = []
    fb = []
    bjk = []

    for satir in file:

        satir = satir[:-1]

        satir_el = satir.split(" , ")

        if satir_el[1] == "Fenerbahçe":
            
            fb.append(satir + "\n")
        
        elif satir_el[1] == "Beşiktaş":

            bjk.append(satir + "\n")
        
        else:

            gs.append(satir + "\n")

with open("gs.txt", "w", encoding= "utf-8") as file:

    for i in gs:

        file.write(i)

with open("bjk.txt", "w", encoding= "utf-8") as file1:

    for i in bjk:

        file1.write(i)

with open("fb.txt", "w", encoding= "utf-8") as file2:

    for i in fb:

        file2.write(i)