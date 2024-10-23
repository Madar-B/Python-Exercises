
def kulje(self,tunnit):
    self.tunnit = tunnit
    self.kuljettuMatka = self.atmNopeus * self.tunnit
    return self.kuljettuMatka
    def __str__(self):
     return f"Auton nopeus on {self.atmNopeus} ja kulkema matka on {self.kuljettuMatka} "

mercedes = Auto("ABC-123","142 km/h")
mercedes.nopeudenMuutos(30)
mercedes.nopeudenMuutos(70)
mercedes.nopeudenMuutos(50)
print(mercedes)
mercedes.nopeudenMuutos(-200)
mercedes.kulje(30)
print(mercedes)