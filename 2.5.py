# leiviskä 8500 g# luoti 13,3 g
# naula 425,6 g
leiviskät = int(input("anna leiviskät"))
luodit = int(input("anna luodit"))
naulat = int(input("naulat"))
summaG= leiviskät * 8500 + luodit * 13.3 + naulat + 425.6
kiloina = summaG / 1000
grammaJäännös = summaG // 1000
print((f"Yhteispaino on {kiloina:2.0f} kiloa"), (f"ja {grammaJäännös:2.0f} grammaa"))