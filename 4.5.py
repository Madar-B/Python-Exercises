
käyttäjäTunnus = "python"
salasana = "rules"
annaKäyttäjätunnus = input("anna käyttäjätunnus")
annaSalasana = input("anna salasana")

for x in range(5):
    if annaKäyttäjätunnus != käyttäjäTunnus and annaSalasana != salasana:
        print("väärä käyttäjätunnus tai salasana")
        annaKäyttäjätunnus = input("anna käyttäjätunnus")
        annaSalasana = input("anna salasana")

if annaKäyttäjätunnus == käyttäjäTunnus and annaSalasana == salasana:
    print("pääsy sallittu")

else:
    print("pääsy evätty")