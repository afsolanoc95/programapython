def multiplicacionSuma(numero1,numero2):
    if numero2==0:
        return 0
    else:
        return numero1+multiplicacionSuma(numero1,numero2-1)
    
print(multiplicacionSuma(5,1))