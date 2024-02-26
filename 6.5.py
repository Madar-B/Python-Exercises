
lista = [1,2,3,4,5,6,7,8,9]
def funktio(lista):
    print("Tämä on alkuperäinen lista:", lista)
    uusLista= [x for x in lista if x %2 == 0]
    print("Tämä lista on karsittu:",(uusLista))
    return uusLista

funktio(lista)