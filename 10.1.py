class Hissi:
    def __init__(self, ekaKerros, vikaKerros):
        self.ekaKerros = int(ekaKerros)
        self.vikaKerros = int(vikaKerros)
        self.atmKerros = int(ekaKerros)

    def ylös(self):
        self.atmKerros += 1
        print("Mennään ylös")
        print(f"Kerros :{self.atmKerros}")
        return self.atmKerros

    def alas(self):
        self.atmKerros -= 1
        print("Mennään alas")
        print(f"Kerros : {self.atmKerros}")
        return self.atmKerros

    def siirry_kerrokseen(self, kerros):
        if kerros < self.atmKerros:
            while kerros != self.atmKerros:
                h.alas()
        if kerros > self.atmKerros:
            while kerros != self.atmKerros:
                h.ylös()


h = Hissi(1, 10)
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(4)