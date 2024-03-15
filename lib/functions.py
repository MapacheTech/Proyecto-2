#pip3 install pandas openpyxl
import pandas as pd

archivo = 'datos-Eval-2.xlsx'
data = pd.read_excel(archivo)

# Convertir el DataFrame a una lista
lista = [data.columns.values.tolist()] + data.values.tolist()

# Aplanar la lista de listas en una sola lista
lista_plana = [item for sublist in lista for item in sublist]

for i in lista:
  if [i] == 77:
    print(f' \033[31m{i}\033[om]')
  else:
    print(i)