def SumaDigitos(numero):
    if numero==0:
        return numero
    else:
        return SumaDigitos(numero/10)+(numero%10)
print(SumaDigitos(15))