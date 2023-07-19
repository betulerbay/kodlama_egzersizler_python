
class animals():
    def __init__(self, hayvan_ismi, ayak_sayisi, beslenme_türü, üreme_sekli):
        
        self.hayvan_ismi = hayvan_ismi

        self.ayak_sayisi = ayak_sayisi

        self.beslenme_türü = beslenme_türü

        self.üreme_sekli = üreme_sekli

    def __str__(self):
        return "{}, {} ayak sayısına sahiptir. {} olarak beslenir. {} ürer".format(self.hayvan_ismi, self.ayak_sayisi, self.beslenme_türü, self.üreme_sekli)
    

hayvan1 = animals("İnek", 4, "Otobur", "Doğurarak")

print(hayvan1)

class kus(animals):
    pass

hayvan2 = kus("Ördek", 2, "etobur", "yumurtlayarak")

print(hayvan2)