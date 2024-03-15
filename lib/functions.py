#pip3 install pandas openpyxl
import pandas as pd
from .classes import nodo

inOrder = []
preOrder = []
postOrder = []

def pedirNumeroAlumno():
  numeroAlumno = input('Cuál es mi número? ')
  return numeroAlumno

def imprimirMatriz(archivo, numeroAlumno):
  data = pd.read_excel(archivo)


  lista = [data.columns.values.tolist()] + data.values.tolist()

  for fila in lista:
    for elemento in fila:
      elementoStr = str(elemento).ljust(10)
      if elemento == int(numeroAlumno):
        print(f'\033[31m{elementoStr}\033[0m', end=' ')
      else:
        print(elementoStr, end=' ')
    print()

def agregaNodos(currentNodo, nuevoNumero):
    cola = []
    cola.append(currentNodo)
    
    while cola:          
        currentNodo = cola.pop(0)
        
        if currentNodo.izq is None:
            currentNodo.izq = nodo(nuevoNumero)
            return 0
        if currentNodo.der is None:
            currentNodo.der = nodo(nuevoNumero)
            return 0
        cola.append(currentNodo.izq)
        cola.append(currentNodo.der)
        
    return 0
  
  
def printArbol(Nodo):
    if Nodo is not None:
        nodoPadre = Nodo
        print(nodoPadre.getArbol())
        printArbol(nodoPadre.izq,)        
        printArbol(nodoPadre.der)
    return 0  
  
def arbolOrdenado(archivo):
  data = pd.read_excel(archivo)
  numeros = data.columns.values.tolist() + [item for sublist in data.values.tolist() for item in sublist]
  nodoRaiz = nodo(numeros[0])
  for i in range(1, len(numeros),1):
    agregaNodos(nodoRaiz, numeros[i])
  printArbol(nodoRaiz)
  return nodoRaiz

def LVR(Nodo, arr):

    if Nodo is not None:
        nodoPadre = Nodo
        LVR(nodoPadre.izq, arr)
        arr.append(nodoPadre.valor)
        LVR(nodoPadre.der, arr)
    else:
        pass
    
    return arr

def VLR(Nodo, arr):
    if Nodo is not None:
        nodoPadre = Nodo
        arr.append(nodoPadre.valor)
        LVR(nodoPadre.izq, arr)        
        LVR(nodoPadre.der, arr)
    else:
        pass
    
    return arr

def LRV(Nodo, arr):
    if Nodo is not None:
        nodoPadre = Nodo
        LVR(nodoPadre.izq, arr)        
        LVR(nodoPadre.der, arr)
        arr.append(nodoPadre.valor)        
    else:
        pass
    
    return arr
  
def nodosOrdenados(nodoPadre, newNodo):
    if newNodo.valor < nodoPadre.valor:
        if nodoPadre.izq is None:
            nodoPadre.izq = newNodo
        else:
            nodosOrdenados(nodoPadre.izq, newNodo)
    if newNodo.valor > nodoPadre.valor:
        if nodoPadre.der is None:
            nodoPadre.der = newNodo
        else:
            nodosOrdenados(nodoPadre.der, newNodo)
    pass
  
def arbolNumOrdenado(archivo, nodoRaiz):
  data = pd.read_excel(archivo)
  numeros = data.columns.values.tolist() + [item for sublist in data.values.tolist() for item in sublist]
  primerNodo = nodo(nodoRaiz)
  for i in range(1, len(numeros),1):
    nodosOrdenados(primerNodo, nodo(numeros[i-1]))
  printArbol(primerNodo)
  return primerNodo
