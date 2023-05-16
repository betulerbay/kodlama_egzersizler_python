a = int(input("Bir a sayısı girin:"))
b = int(input("Bir b sayısı girin:"))

print("a = {}, b ={}".format(a, b))

a, b = b, a

print("a = {}, b = {}".format(a, b))