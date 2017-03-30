def palindromas(x):
    if (len(x)==1 or len(x)==0):
        return "true"
    else:
        if(x[0]==x[len(x)-1]):
            return palindromas(x[1:-1])
    return "false"

frase = input('Ingrese una frase:') 
print (palindromas(frase))