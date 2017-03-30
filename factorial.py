def numeroFactorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero* numeroFactorial(numero-1)
    
print(numeroFactorial(8))