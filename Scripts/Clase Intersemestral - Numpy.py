print(
      """
      ¿Qué es Numpy?
          --> Librería para arreglar números.
          --> Maneja diferentes tipos de datos.
          --> Cambia, crea, adjunta y elimina.
          --> Necesario para Data Science
              --> Operaciones matematicas sobre lo que existe.
              --> Es rápido y simple de usar.
              """)


lista1 = [1, 2, 3]
lista2 = [3, 2, 1]
lista1 + lista2

peso = [67, 56, 69, 55, 65, 51, 47, 90, 52, 56, 82, 104, 89, 65, 60]
estatura = [1.74, 1.60, 1.71, 1.60, 1.70, 1.60, 1.53, 1.73, 1.60, 1.60, 1.76, 1.80, 1.78, 1.72, 1.52]

IMC = peso / estatura ** 2

import numpy as np

np_lista1 = np.array(lista1)
np_lista2 = np.array(lista2)
np_lista1 + np_lista2

np_estatura = np.array(estatura)
np_peso = np.array(peso)
IMC = np_peso / np_estatura ** 2

type(np_estatura)
type(np_peso)

## Nueva columna de Clasificación de Índice de Masa Corporal
#        <16.00 -- Infrapeso: Delgadez Severa
# 16.00 - 16.99 -- Infrapeso: Delgadez moderada
# 17.00 - 18.49 -- Infrapeso: Delgadez aceptable
# 18.50 - 24.99 -- Peso Normal
# 25.00 - 29.99 -- Sobrepeso
# 30.00 - 34.99 -- Obeso: Tipo I
# 35.00 - 40.00 -- Obeso: Tipo II
#        >40.00 -- Obeso: Tipo III

## Operadores Booleanos
IMC < 18.50
np.logical_and(IMC > 18.50, IMC < 24.99)
np.logical_and(IMC > 25., IMC < 29.99)
IMC > 30.

## Numpy Array 2D
np_2d = np.array([[67, 56, 69, 55, 65, 51, 47, 90, 52, 56, 82, 104, 89, 65, 60],
                  [1.74, 1.60, 1.71, 1.60, 1.70, 1.60, 1.53, 1.73, 1.60, 1.60, 1.76, 1.80, 1.78, 1.72, 1.52]])

np_2d.shape

# Localizar datos
np_2d[0]
np_2d[0][2]
np_2d[0, 2]

np_2d[:, 1:3]
np_2d[1, :]

### Numpy: Estadística Básica
np_2d

np.mean(np_2d[0, :])

np.median(np_2d[0, :])

np.corrcoef(np_2d[0, :], np_2d[1, :])

np.sum(np_2d[0, :])

np.std(np_2d[0, :])

## Bucle For
for val in IMC:
    print(val)

variables = np.array([np_estatura, np_peso])

for valores in variables:
    print(valores)

for valores in np.nditer(variables):
    print(valores)

