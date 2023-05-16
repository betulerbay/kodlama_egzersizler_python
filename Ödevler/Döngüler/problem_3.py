"""
1'den 10'a kadar olan sayıların çarpım tablosu
"""
#print(*range(0, 10))
i = 1
j = 1

for i in range(1, 11):
    print("***************************************")
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, i*j))