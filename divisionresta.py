def DivisionResta (numero1,numero2):
    if numero2 > numero1:
        return 0
    else:
        return DivisionResta(numero1-numero2,numero2)+1   
print(DivisionResta(35,5))