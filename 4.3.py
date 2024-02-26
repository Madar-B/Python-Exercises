
mainitutLuvut = []
luku = str(input("anna luku"))
while luku != "":
    mainitutLuvut.append(luku)
    luku = str(input("anna luku"))
print(mainitutLuvut)
print("pienin luku on:", min(mainitutLuvut), "," , "suurin luku on:" , max(mainitutLuvut))
