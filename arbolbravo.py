from collections import deque
class ARBOL():
    def __init__(self, asignado):
        self.asignado=asignado
        self.hijos=[]
          
def buscar(arbol_nario, elemento):
    if arbol_nario.asignado == elemento:
        return arbol_nario
    return buscar_hijos(arbol_nario.hijos,elemento)

def buscar_hijos(hijos,asignado):
    if hijos==[]:
        return False
    return buscar(hijos[0],asignado) or buscar_hijos(hijos[1:],asignado)

def anadirLetra(arbol_nario, elemento, elementoPadre):
    buscar(arbol_nario, elementoPadre).hijos.append(ARBOL(elemento));
    
def ejecutarAnchoPrimero(arbol_nario, funcion,cola = deque()):
    funcion(arbol_nario.asignado)
    if (len(arbol_nario.hijos) > 0):
        cola.extend(arbol_nario.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(),funcion,cola)  
        
def imprimir(asignado):
    print asignado

a=['a','ab','ac','abel','abeta','abalia','acacia']

arbol_nario = ARBOL(a[0])
anadirLetra(arbol_nario,a[1],a[0])
anadirLetra(arbol_nario,a[2],a[0])

def escogencia(asignado):    
    if asignado==arbol_nario.hijos[0].asignado or encoger(asignado)==arbol_nario.hijos[0].asignado:
        anadirLetra(arbol_nario,asignado,a[1])
    if asignado==arbol_nario.hijos[1].asignado or encoger(asignado)==arbol_nario.hijos[1].asignado:
        anadirLetra(arbol_nario,asignado,a[2])
    
    
def encoger(asignado):
    if asignado==arbol_nario.hijos[0].asignado or asignado==arbol_nario.hijos[1].asignado:
        return asignado
    else:
        return encoger(asignado[:len(asignado)-1])
     
escogencia(a[3])
escogencia(a[4])
escogencia(a[5])
escogencia(a[6])

ejecutarAnchoPrimero(arbol_nario,imprimir)