# Escriba una rotate que gire una matriz bidimensional (una matriz) ya sea en sentido horario o
# antihorario 90 grados y devuelva la matriz rotada.
# La función acepta dos parámetros: una matriz y una cadena que especifica la dirección o
# rotación. La dirección será "clockwise"o "counter-clockwise".
# Aquí hay un ejemplo de cómo se usará su función:
# var matrix = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]];
# rotate(matrix, "clockwise"); // Would return [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# Para ayudarlo a visualizar la matriz rotada, aquí está formateada como una cuadrícula:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
# Girado en sentido contrario a las agujas del reloj se vería así:
# [[3, 6, 9],
#  [2, 5, 8],
#  [1, 4, 7]]

import numpy as np  

def pedir_numero():
    while True:
        try:
            n = int(input("Introduce un número para determinar el orden de la matriz: "))
            return n
        except ValueError:
            print("Error. Introduce un número entero")

def matriz(n):
    return np.random.randint(1, 100, size=(n, n))

def rotar_clockwise(matriz):
    return np.rot90(matriz)

def rotar_anticlockwise(matriz):
    matrix1 = np.rot90(matriz)
    matrix2 = np.rot90(matrix1)
    matrix3 = np.rot90(matrix2)
    return matrix3


if __name__ == '__main__':
    n = pedir_numero()
    matrix = matriz(n)
    print(matrix, '\n')
    print(rotar_clockwise(matrix), '\n')
    print(rotar_anticlockwise(matrix))