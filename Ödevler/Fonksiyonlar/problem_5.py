def pisagor():


    for a in range(1, 101):
        for b in range (1, 101):
            if (((a ** 2 + b ** 2) ** 0.5) % 1 == 0):
                print("{} {} {} pisagor üçlüsüdür".format(a, b, int((a ** 2 + b ** 2) ** 0.5)))



print(pisagor())

