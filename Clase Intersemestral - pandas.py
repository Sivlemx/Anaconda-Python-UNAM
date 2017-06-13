# Python Zen
print("""
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    Plano es mejor que anidado.
    Disperso es mejor que denso.
    La legibilidad cuenta.
    Los casos especiales no son tan especiales como para quebrantar las reglas.
    Aunque lo práctico gana a la pureza.
    Los errores nunca deberían dejarse pasar silenciosamente.
    A menos que hayan sido silenciados explícitamente.
    Frente a la ambigüedad, rechaza la tentación de adivinar.
    Debería haber una -y preferiblemente sólo una- manera obvia de hacerlo.
    Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés.
    Ahora es mejor que nunca.
    Aunque nunca es a menudo mejor que ya mismo.
    Si la implementación es difícil de explicar, es una mala idea.
    Si la implementación es fácil de explicar, puede que sea una buena idea.
    Los espacios de nombres son una gran idea ¡Hagamos más de esas cosas!
""")

print("""
¿Por qué usar Python como herramienta para el análisis estadístico?

R es un lenguaje dedicado a las estadísticas. 

Python es un lenguaje de propósito general con módulos de estadística. 

R tiene más funciones de análisis estadístico que Python y sintaxis especializadas. 

Sin embargo, cuando se trata de desarrollar análisis complejos que mezclan

Estadística --> Archivos de Imágenes
            --> Archivos de Sonido
            --> Archivo de Texto
            --> Pruebas Psicométricas, Neurociencias, Psicología Experimental (psicopy)
            --> Análisis de Experimentos Físicos
            --> Análisis de Experimentos Químicos
            --> Imágenes de Resonancia Magnética
            --> Bioinformática
            --> Análisis Financiero
            --> Psicología Organizacional
            --> etc

                            Python lo realiza sin problemas. 
                            
                       -- Leguaje de programación de alto nivel--
                                 -- Interpretado --
                               -- Escritura dinámica --
                             - Orientado a objetos (POO) --

(Recuerda, es un programa con el que se desarrolla programas,
 es "OMNIPRESENTE") 

""")

print(
      """
      ¿Qué es pandas?
            --> Librería de Python para análisis de datos.
            --> Estructuras de datos con un "montón" de funciones.
                -> Manejo de etiquetas.
                -> Análisis de Series de Tiempo.
                -> Manejo de datos faltantes.
                -> Operaciones relacionados.
      """)

print(
      """
      pandas.DataFrame: 
          Módulo de pandas. 
          DataFrame = analogia pythonica del marco de datos de R.
          
          Es el equivalente de Python de la tabla de hojas de cálculo. 
          Es diferente de una matriz numpy 2D, ya que ha nombrado columnas, 
          puede contener una mezcla de diferentes tipos de datos por columna,
          selección de índices y columnas por "str" e "int", así como también
          tiene tablas dínamicas.
        
      """)
    
##########################################################################################

import pandas as pd

#### DataFrame desde cero
## Los diccionarios deben contener el mismo número de "values"

## 1ra Forma
nomb = ['Sutano', 'Perengano', 'Fulanita', 'Sutanita']
seme = ['cuarto', 'cuarto', 'sexto', 'sexto']
sexo = ['hombre', 'hombre', 'mujer', 'mujer']
edad = [21, 23, 21, 24]
esta = [1.60, 1.65, 1.50, 1.75]

lista_etiquetas = ['Nombre', 'Semestre', 'Sexo', 'Edad', 'Estatura']
lista_columnas = [nomb, seme, sexo, edad, esta]

comprimido = list(zip(lista_etiquetas, lista_columnas))
print(comprimido)

clase = dict(comprimido)

clase = pd.DataFrame(clase)
print(clase)

## 2da Forma

clase = {'Semestre':['cuarto', 'cuarto', 'sexto', 'sexto'],
         'Sexo':['hombre', 'hombre', 'mujer', 'mujer'],
         'Edad':[21, 23, 21, 24],
         'Estatura':[1.60, 1.65, 1.50, 1.75],
         'Nombre':['Sutano', 'Perengano', 'Fulanita', 'Sutanita']}

clase = pd.DataFrame(clase)
print(clase)

## Crear nueva(s) columna(s)
clase['Universidad'] = ['UNAM', 'UVM', 'UNAM', 'De la Vida'] 
print(clase)

peso = [70, 80, 65, 55]
clase['Peso'] = peso
print(clase)

clase['Deporte'] = ['Correr', 'Nadar', 'Trotar', 'Brincar']

## Colocar Índice
clase.index = ['Su', 'Pe', 'Fu', 'Sut'] # Iniciales en clase
print(clase)

## Cambiar a propiedad de categoría las categorías
clase.Sexo = clase.Sexo.astype('category')
clase.Deporte = clase.Deporte.astype('category')
clase.Universidad = clase.Universidad.astype('category')

clase.info()

### Index y Selección de Datos
# Corchetes Rectos
# Métodos Avanzados = "*.loc"  "*.iloc"
clase['Edad']
clase['Estatura']
clase['Deporte']
clase['Nombre']

type(clase['Edad'])
type(clase['Estatura'])
type(clase['Deporte'])
type(clase['Nombre'])

clase[['Edad']]
clase[['Estatura']]
clase[['Deporte']]
clase[['Nombre']]

type(clase[['Edad']])
type(clase[['Estatura']])
type(clase[['Deporte']])
type(clase[['Nombre']])

clase[['Peso', 'Categoría_IMC']]

clase[1:3]

## Método "*.loc"
# Filas
clase.loc['Pe']
clase.loc[['Pe']]
clase.loc[['Pe', 'Fu', 'Sut']]
# Filas y Columnas
clase.loc[[1, 2, 3], ['Peso', 'Categoría_IMC']]
#Todas las Filas
clase.loc[:, ['Peso', 'Categoría_IMC']]

## Método "*.iloc"
# Filas
clase.iloc[1]
clase.iloc[[1]]
clase.iloc[[1, 2, 3]]
# Filas y Columnas
clase.iloc[[1, 2, 3], [6, 9]]
#Todas las Filas
clase.iloc[:, [6, 9]]

import numpy as np

### Nueva columna

# imc = peso / estatura ** 2

clase['IMC'] = clase['Peso'] / clase['Estatura'] ** 2

## Nueva columna de Clasificación de Índice de Masa Corporal
#        <16.00 -- Infrapeso: Delgadez Severa
# 16.00 - 16.99 -- Infrapeso: Delgadez moderada
# 17.00 - 18.49 -- Infrapeso: Delgadez aceptable
# 18.50 - 24.99 -- Peso Normal
# 25.00 - 29.99 -- Sobrepeso
# 30.00 - 34.99 -- Obeso: Tipo I
# 35.00 - 40.00 -- Obeso: Tipo II
#        >40.00 -- Obeso: Tipo III

## Filtar en toda la base de datos
infrapeso = clase[clase['IMC'] < 18.50]
normal = clase[np.logical_and(clase['IMC'] > 18.50, clase['IMC'] < 24.99)]
sobrepeso = clase[np.logical_and(clase['IMC'] > 25., clase['IMC'] < 29.99)]
obeso = clase[clase['IMC'] > 30.]

df = infrapeso.assign(Categoría_IMC = 'Infrapeso')
df1 = normal.assign(Categoría_IMC = 'Normal').append(df)
df2 = sobrepeso.assign(Categoría_IMC = 'Sobrepeso').append(df1)
clase = obeso.assign(Categoría_IMC = 'Obeso').append(df2)

clase.Categoría_IMC = clase.Categoría_IMC.astype('category')

## Ordenar por Edad
#clase = clase.sort_values('Edad')

## Exportar a CSV
clase.to_csv('Clase_Anaconda.csv', sep=',')

## Exportar a Excel
clase.to_excel('Clase_Anaconda.xls')
clase.to_excel('Clase_Anaconda.xlsx')


## Importar archivo CSV
clase = pd.read_csv('Clase_Anaconda.csv', sep=',')

## Bucle For
clase = pd.read_csv('Clase_Anaconda.csv', sep=',', index_col=0)

for val in clase:
    print(val)

for sujeto, valores in clase.iterrows():
    print(sujeto)
    print(valores)

for sujeto, valores in clase.iterrows():
    print(sujeto + ': ' + valores['Nombre'])

## Agregar columna con For
## Y función "*.apply()"
for sujeto, valores in clase.iterrows():
    clase.loc[sujeto, 'No._Letras'] = len(valores['Nombre'])
print(clase)

clase['No. Letras'] = clase['Nombre'].apply(len)
print(clase)

clase = clase.drop('No._Letras', axis=1)

## Índices y Columnas
type(clase)

clase.shape

clase.columns

type(clase.columns)

clase.index

clase.head()
clase.head(2)

clase.tail()
clase.tail(2)

clase.info()

#### Graficar lo que se tenga que graficar
import matplotlib.pyplot as plt

edades = clase['Edad'].values
plt.plot(edades)
plt.show()

edades1 = clase['Edad']
edades1.plot()
plt.show()

clase.loc[:, ['IMC', 'Peso']].plot()







###########################################################################################


#### Base de datos "iris" ############################################################
from urllib.request import urlretrieve

url = 'https://github.com/Sivlemx/Anaconda-Python-UNAM'
urlretrieve(url, 'iris.csv')
iris_csv = 'iris.csv'
print(iris_csv)
print(type(iris_csv))

df_csv = pd.read_csv(iris_csv, sep=',')
print(df_csv)
print(type(df_csv))

url = 'https://github.com/Sivlemx/Anaconda-Python-UNAM'
urlretrieve(url, 'iris.xlsx')
iris_xlsx = 'iris.xlsx'
print(iris_xlsx)
print(type(iris_xlsx))

df_xlsx = pd.ExcelFile(iris_xlsx)
print(df_xlsx.sheet_names)
df1 = df_xlsx.parse('iris') # --> 1ra opción
df2 = df_xlsx.parse(0) # --> 2da opción
print(df1)
print(type(df1))
print(df2)
print(type(df2))
########################################################################################
#### Indices y Columnas
print(df1.shape)

print(df1.columns)
print(type(df1.columns))

print(df1.index)
print(type(df1.index))
########################################################################################
#### Dividiendo filas y columnas
## comando "iloc" y "loc"
primeras_filas = df1.iloc[:5, :]
print(primeras_filas)

ultimas_filas = df1.iloc[-5:, :]
print(ultimas_filas)

iloc_columnas = df1.iloc[:, :3]
print(iloc_columnas)

loc_columnas = df1.loc[:, :'petal_length']
print(loc_columnas)
########################################################################################
#### comando "head()" y "tail()"
print(df1.head())
print(df1.head(10))
print(df1.head(20))

print(df1.tail())
print(df1.tail(10))
print(df1.tail(20))
#########################################################################################
#### comando "info()"
print(df1.info())
########################################################################################
#### comando "unique()"
print(df1['name'])

print(df1['name'].unique())
#########################################################################################
#### Estadística Descriptiva
print("""
      Estadística Descriptiva:
          
          “Es el estudio que incluye la obtención, organización, 
          presentación y descripción de información numérica”. 
""")

## Medidas de Tendencia Central = media, mediana, moda
df1[df1['name'] == 'versicolor']['sepal_length'].mean() # Media
df1[df1['name'] == 'versicolor']['sepal_length'].median() # Mediana
df1[df1['name'] == 'versicolor']['sepal_length'].mode() # Moda

## Medidas de Dispersión = Rango, Desviación Estándar, Varianza
df1[df1['name'] == 'versicolor']['sepal_length'].max() # Máximo
df1[df1['name'] == 'versicolor']['sepal_length'].min() # Mínimo
df1[df1['name'] == 'versicolor']['sepal_length'].std() # Desviación Estándar
df1[df1['name'] == 'versicolor']['sepal_length'].var() # Varianza

df1[df1['name'] == 'versicolor']['sepal_length'].sem() # Error Estándar







df1[df1['name'] == 'versicolor'].describe()

df1.describe()




## Estadística Parámetrica
## Estadística No Parámetrica
## Correlación
## Regresión Lineal



print("""
      Esatdística Inferencial:
          “La inferencia estadística es una técnica mediante la cual se 
          obtienen generalizaciones o se toman decisiones en base a una 
          información parcial o completa obtenida mediante 
          técnicas descriptivas”. 
""")
#########################################################################################
#### comando "groupby"
groupby_name = df1.groupby('name')

for name, value in groupby_name['sepal_length']:
    print((name, value.mean()))

groupby_name.mean()
groupby_name.median()
groupby_name.mode() # Groupby no da la moda
groupby_name.std()
groupby_name.sem()

groupby_name.boxplot()
df1[df1['name'] == 'setosa'].boxplot()
df1[df1['name'] == 'versicolor'].boxplot()
df1[df1['name'] == 'virginica'].boxplot()

### Plotear datos
import matplotlib.pyplot as plt

pd.plotting.scatter_matrix(df1[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
df1[df1['name'] == 'versicolor']['sepal_length'].plot()
df1[df1['name'] == 'versicolor']['sepal_length']
df1[df1['name'] == 'versicolor']['sepal_length']
df1[df1['name'] == 'versicolor']['sepal_length']
df1[df1['name'] == 'versicolor']['sepal_length']

df1[df1['name'] == 'versicolor'].plot.scatter('sepal_length', 'petal_length')



