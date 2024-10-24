import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailun tilanne: {self.nimi}")
        print(f"{'Rekisteritunnus':<10} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<20} {auto.tämänhetkinen_nopeus:<15} {auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    kilpailu.tulosta_tilanne()

print("\nKilpailu on ohi!")
kilpailu.tulosta_tilanne()
