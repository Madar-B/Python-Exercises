
def kiihdytä(self,muutoskmh):
    if muutoskmh > 0:
        self.atmNopeus += muutoskmh
    if muutoskmh < 0:
        self.atmNopeus -= abs(muutoskmh)
    if self.atmNopeus < 0:
        self.atmNopeus = 0
    if self.atmNopeus > self.huippunopeus:
        self.atmNopeus = self.huippunopeus
def __str__(self):
    return f"Auton rekkari on {self.rekkari} ja nopeus {self.atmNopeus}"