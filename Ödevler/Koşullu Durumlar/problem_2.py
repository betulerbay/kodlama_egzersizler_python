a = int(input("A sayısını Girin:"))
b = int(input("B sayısını Girin:"))
c = int(input("C sayısını Girin:"))

if (a > b):
    if (a > c):
        print("a en büyüktür")
elif (b > a):
    if (b > c):
        print("b en büyüktür")
elif (c > a):
    if (c > b):
        print("c en büyüktür")
else:
    print("Hepsi birbirine eşittir")

