kuhaPituus = int(input("anna kuhan pituus"))
puuttuvaPituus = 37 - kuhaPituus
if kuhaPituus >= 37:
    print("Hyvä saalis!")
else:
    print("Kuha on alamittainen")
print("Kuhan pituudesta puuttuu:", puuttuvaPituus, "cm")