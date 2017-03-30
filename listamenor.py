def menor(lista):
    if len(lista) == 1:       
        return [lista[0][lista[0].index(min(lista[0]))]]
    else:
        return [lista[0][lista[0].index(min(lista[0]))]]+menor(lista[1:])

print (menor([[1,-5,3], [100,10,9], [5,8,10]]))