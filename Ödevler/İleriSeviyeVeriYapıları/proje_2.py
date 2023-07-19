"""şiir.txt" şeklinde bir dosya oluşturun.
Bu dosyanın herbir satırını okuyun. 
Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın."""

from curses.ascii import isupper
from ntpath import join


with open("siir.txt", "r", encoding="utf-8")as file:
    
    siir = file.read()
    kelime = siir.split()
    
    str = ""

    for i in kelime:
        
        if (i.islower() == False):
            str += i[0]
            
            
print(str)







