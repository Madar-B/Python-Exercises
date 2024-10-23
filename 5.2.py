
mainitutLuvut = []
luku = str(input("anna luku"))

while luku != "":
    mainitutLuvut.append(luku)
    luku = str(input("anna luku"))

mainitutLuvut.sort(reverse = True)
print(mainitutLuvut)