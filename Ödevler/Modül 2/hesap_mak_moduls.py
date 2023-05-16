def toplama(a, b):
    """
    Verilen değerler toplamını döndürür

    """
    return a + b

def bölme(a, b):
    """
    Verilen değerlerin bölümünü verir

    """
    return a / b

def carpma(a, b):
    """
    Verilen değerlerin çarpımını verir

    """
    return a * b

def cıkarma(a, b):
    """
    Verilen değerlerin birbirinden farkını verir

    """
    return a - b

def us_alma(a, b):
    """
    a ^ b değerini verir

    """
    return a ** b

def faktoriyel(a):
    """
    Verilen sayının faktöriyelini bulur

    """
    if (a == 0 or a == 1):
        fak = 1
    else:
        fak = 1
        while (a != 1):
            fak *= a
            a -= 1
    return fak

def karekok(a):
    """
    Verilen sayının karekökünü alır

    """
    return a ** (0.5)
















