
joukko = set()
nimi = input("Syötä nimi")

while nimi != "":
    if nimi in joukko:
         print("Aiemmin syötetty nimi")
         nimi = input("Syötä nimi")
    else:
        print("Uusi nimi")
        joukko.add(nimi)
        nimi = input("Syötä nimi")

print("Syötit tyhjän merkkijonon")

for x in joukko:
    print(x)