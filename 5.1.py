import random

heitot = int(input("anna kuutioiden määrä"))
summa = 0
for x in range(heitot):
    silmäluku = random.randint(1, 6)
    print(silmäluku)
    summa += silmäluku

print("Heittojen summa on:", summa)