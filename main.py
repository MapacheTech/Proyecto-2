from lib import *

numeroAlumno = pedirNumeroAlumno()
nodoRaiz2 = int(numeroAlumno)
archivo = input('Cual es el nombre del archivo a procesar? ')#Usar ruta de acceso
print('')
print('Números en archivo, el rojo es mi número:')
imprimirMatriz(archivo, numeroAlumno)
print('')
print('Arbol armado por extensión:')
nodoRaiz = arbolOrdenado(archivo)
print('')
print('Recorridos de Árbol:')
arrLVR = LVR(nodoRaiz, arr=[])
print(f'In order: {arrLVR}')
arrVLR = VLR(nodoRaiz, arr=[])
print(f'Pre order: {arrVLR}')
arrLRV = LRV(nodoRaiz, arr=[])
print(f'Post order: {arrLRV}')
print('')
print('Árbol armado por ordenamiento:')
nodoArbOrd = arbolNumOrdenado(archivo,nodoRaiz2)
print('')
print('Recorrido del Árbol Ordenado: ')
arr2LRV = LRV(nodoArbOrd, arr=[])
print(arr2LRV)