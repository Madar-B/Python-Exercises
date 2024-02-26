import random

def nopanHeitto():
    return random.randint(1,6)

heitto = nopanHeitto()

while heitto != 6:
    heitto = nopanHeitto()
    print(heitto)