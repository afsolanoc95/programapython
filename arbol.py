class Nodo_N():
    def __init__(self, valor):
        self.valor=valor
        self.hijos=[]
        
def agregarElemento(arbol, elemento, elementoPadre):
    buscar(arbol, elementoPadre).hijos.append(Nodo_N(elemento));
    
def buscar(arbol, elemento):
    if arbol.valor == elemento:
        return arbol
    return buscar_hijos(arbol.hijos,elemento)

def buscar_hijos(hijos,valor):
    if hijos==[]:
        return False

    return buscar(hijos[0],valor) or buscar_hijos(hijos[1:],valor)
    
def profundidad(arbol):
    printElement(arbol.valor)
    for hijo in arbol.hijos:
        profundidad (hijo)
        
def printElement(valor):
    print valor
a=['a','ab','ac','abel','abeta','abalia','acacia']

arbol = Nodo_N(a[0])
print(arbol.hijos)
agregarElemento(arbol,a[1],a[0])
agregarElemento(arbol,a[2],a[0])

def escogencia(valor):
    
        
    if valor==arbol.hijos[0].valor or encoger(valor)==arbol.hijos[0].valor:
        agregarElemento(arbol,valor,a[1])
    if valor==arbol.hijos[1].valor or encoger(valor)==arbol.hijos[1].valor:
        agregarElemento(arbol,valor,a[2])
    
    
def encoger(valor):
    if valor==arbol.hijos[0].valor or valor==arbol.hijos[1].valor:
        return valor
    else:
        return encoger(valor[:len(valor)-1])
   

escogencia(a[6])
escogencia(a[4])
escogencia(a[3])
escogencia(a[5])

profundidad(arbol)
