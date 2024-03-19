import pandas as pd

# Leer el archivo Excel
data = pd.read_excel('datos-Eval-2.xlsx')

# Obtener los encabezados
encabezados = data.columns.tolist()

# Obtener los valores del DataFrame como una lista de listas
lista = data.values.tolist()

# Solicitar al usuario que ingrese un número
num = int(input("Ingrese un número: "))

# Imprimir los encabezados
for encabezado in encabezados:
  print(f'{encabezado:<15}', end=' ')
print()

# Recorrer la lista y imprimir los elementos
for fila in lista:
  for elemento in fila:
    if elemento == num:
      # Imprimir el elemento en rojo si es igual al número ingresado por el usuario
      print('\033[31m' + f'{str(elemento):<15}' + '\033[0m', end=' ')
    else:
      # Imprimir el elemento normalmente si no es igual al número ingresado por el usuario
      print(f'{str(elemento):<15}', end=' ')
  print()