
galloonat = int(input("anna galloonat"))
def bensaLitroiksi(galloonat):
    litrat = galloonat * 3.785
    print(f"Tämä on:{litrat} litraa")
    return litrat

litroiksi = bensaLitroiksi(galloonat)

while litroiksi > 0:
    galloonat = int(input("anna galloonat"))
    litroiksi = bensaLitroiksi(galloonat)
print("Syötit negatiivisen luvun")