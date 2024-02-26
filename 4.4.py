import random

luku = random.randint(1, 10)
arvaus = int(input("arvaa luku 1-10"))

while luku != arvaus:

    if arvaus > luku:
        print("arvaus on liian suuri")
        arvaus = int(input("arvaa luku 1-10"))

    if arvaus < luku:
        print("arvaus on liian pieni")
        arvaus = int(input("arvaa luku 1-10"))

    else:
        print("arvasit oikein")