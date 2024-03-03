import csv
def csvToMat(nombreArchivo):
    mat = []
    with open(nombreArchivo, newline="", encoding="utf-8") as numeros:
        dataNumeros = csv.reader(numeros, delimiter=",")
        for row in dataNumeros:
            mat.append(row)
    return mat
  
def getMat():
    matrix = csvToMat("datos-Eval-2.csv")
    return matrix

def printMat(matriz):
    for j in range(len(matriz)):
      for i in range(len(matriz)):
        print(matriz[j][i], end=" ")
      print("")