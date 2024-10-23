class Auto:
    def __init__(self,rekkari,huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.kuljettuMatka = 0
        self.atmNopeus = 0
    def __str__(self):
        return f"Auton rekkari on: {self.rekkari} , huippunopeus: {self.huippunopeus} , kuljettu matka: {self.kuljettuMatka} ja tämänhetkinen nopeus: {self.atmNopeus}"

mercedes = Auto("ABC_123", "142 km/h")
print(mercedes)