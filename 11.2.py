class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = nopeus

    def kulje(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

    def tulosta_tiedot(self):
        print(f"{self.rekisteritunnus}: Nopeus: {self.nopeus} km/h, Matka: {self.matkamittari} km")

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Bensatankki: {self.bensatankki} litraa")


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aseta_nopeus(150)
polttomoottoriauto.aseta_nopeus(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

sahkoauto.tulosta_tiedot()
print()
polttomoottoriauto.tulosta_tiedot()
