import random

tahkojenMäärä = int(input("anna tahkot"))
def nopanHeitto(tahkot):
    return random.randint(1, (tahkot))
heitto = nopanHeitto(tahkojenMäärä)

while heitto != tahkojenMäärä:
    heitto = nopanHeitto(tahkojenMäärä)
    print(heitto)