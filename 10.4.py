import random

class Auto:
    def __init__(self, nimi, nopeus, matka=0):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = matka

    def kulje(self):
        self.matka += self.nopeus

    def __str__(self):
        return f"{self.nimi}: Nopeus: {self.nopeus} km/h, Matka: {self.matka} km"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.choice([-10, 0, 10])
            auto.nopeus += nopeuden_muutos
            if auto.nopeus < 0:
                auto.nopeus = 0
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.nimi}")
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        print("-" * 45)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

autot = [
    Auto("Auto 1", random.randint(100, 200)),
    Auto("Auto 2", random.randint(100, 200)),
    Auto("Auto 3", random.randint(100, 200)),
    Auto("Auto 4", random.randint(100, 200)),
    Auto("Auto 5", random.randint(100, 200)),
    Auto("Auto 6", random.randint(100, 200)),
    Auto("Auto 7", random.randint(100, 200)),
    Auto("Auto 8", random.randint(100, 200)),
    Auto("Auto 9", random.randint(100, 200)),
    Auto("Auto 10", random.randint(100, 200)),
]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

print("\nKilpailu päättynyt!")
kilpailu.tulosta_tilanne()
