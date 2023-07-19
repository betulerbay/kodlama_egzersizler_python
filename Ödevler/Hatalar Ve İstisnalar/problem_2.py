def cift_mi(a):
    if (a % 2 == 0):
        return a
    else:
        raise ValueError
    

liste = [745,34,34,23,455,323,63,23,2,4,52,65,76,100]


for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass