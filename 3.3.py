#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("mikä on sukupuolesi?")
arvo = int(input("mikä on hemoglobiiniarvosi?"))

if sukupuoli == " nainen" and arvo < 117 :
    print("hemoglobiinisi on alhainen")

elif sukupuoli == " nainen" and arvo > 175 :
    print("hemoglobiinisi on korkea")

elif sukupuoli == " nainen" and arvo > 117 and arvo < 175:
    print("hemoglobiinisi on normaali")

if sukupuoli == " mies" and arvo < 134:
    print("hemoglobiinisi on alhainen")

elif sukupuoli == " mies" and arvo > 195 :
    print("hemoglobiinisi on korkea")

elif sukupuoli == " mies" and arvo > 134 and arvo < 195:
    print("hemoglobiinisi on normaali")