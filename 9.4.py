
import random

class Auto:
    def __init__(self,rekkari):
        self.kuljettuMatka = 0
        self.rekkari = rekkari
        self.huippunopeus = random.randint(100,200)
        self.atmNopeus = 0

    def kiihdytä(self, muutoskmh):
        if muutoskmh < 0:
            self.atmNopeus -= abs(muutoskmh)
        if muutoskmh > 0:
            self.atmNopeus += muutoskmh
        if self.atmNopeus < 0:
            self.atmNopeus = 0
        if self.atmNopeus > self.huippunopeus:
            self.atmNopeus = self.huippunopeus
        return
    def kulje(self,tunnit):
        self.kuljettuMatka = tunnit * self.atmNopeus
        return
    def __str__(self):
        return f"Auton rekkari: {self.rekkari} tämänhetkinen nopeus:{self.atmNopeus}, auton huippunopeus: {self.huippunopeus} auton kuljettu matka {self.kuljettuMatka}"

autot = []
for x in range(1,11):
    auto = Auto(f"ABC-{x}")
    autot.append(auto)

while any(auto.kuljettuMatka < 10000 for auto in autot):
    for auto in autot:
        auto.kulje(1)
        auto.kiihdytä(random.randint(-10, 15))

for auto in autot:
    print(auto)