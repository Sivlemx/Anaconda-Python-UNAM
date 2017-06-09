# Clase 
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

# imc = peso / estatura ** 2

clase = {'semestre':['cuarto', 'cuarto', 'sexto', 'sexto'],
         'sexo':['hombre', 'hombre', 'mujer', 'mujer'],
         'edad':[21, 23, 21, 24],
         'estatura':[1.60, 1.65, 1.50, 1.75]}

usuarios = pd.DataFrame(clase)
print(usuarios)

## 2da Forma
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

usuarios = pd.DataFrame(clase)
print(usuarios)

## Crear nueva columna
usuarios['Universidad'] = ['UNAM', 'UVM', 'UNAM', 'De la Vida'] 
print(usuarios)

peso = [70, 80, 65, 55]
usuarios['Peso'] = peso
print(usuarios)

## Colocar Índice
usuarios.index = ['A', 'B', 'C', 'D']
print(usuarios)

## Cambiar a propiedad de categoría las categorías
usuarios.Sexo = usuarios.Sexo.astype('category')

usuarios.info()

usuarios['IMC'] = usuarios['Peso']/usuarios['Estatura']**2





## Nueva columna de Clasificación de Índice de Masa Corporal
#        <16.00 -- Infrapeso: Delgadez Severa
# 16.00 - 16.99 -- Infrapeso: Delgadez moderada
# 17.00 - 18.49 -- Infrapeso: Delgadez aceptable
# 18.50 - 24.99 -- Peso Normal
# 25.00 - 29.99 -- Sobrepeso
# 30.00 - 34.99 -- Obeso: Tipo I
# 35.00 - 40.00 -- Obeso: Tipo II
#        >40.00 -- Obeso: Tipo III

import numpy as np

clase_imc = ['Infrapeso', 'Normal', 'Sobrepeso', 'Obeso']

for imc in usuarios['IMC']:
    imc < 18.49
    usuarios['Clase IMC'] = clase_imc[0]
    




for imc in usuarios['IMC']:
    if imc <= 17:
        usuarios['Clase IMC'] = 'Infrapeso'
    elif imc == range(17, 25, 1):
        usuarios['Clase IMC'] = 'Normal'
    elif imc == range(25, 30, 1):
        usuarios['Clase IMC'] = 'Sobrepeso'
    elif imc >= 30:
        usuarios['Clase IMC'] = 'Obeso'
    else:
        print('No aplica')


while usuarios.loc[:, 'IMC'] < np.arange(16, 18.50, 0.000001):
    usuarios['IMC Clas'] = 'Infrapeso'
    print(usuarios)

infrapeso = np.arange(16, 18.50, 0.000001)

for imc in usuarios.loc[:, 'IMC']:
    infrapeso == imc
    print(imc)





infrapeso = np.arange(16, 18.50, 0.000001)

for infrapeso in usuarios.loc[:, 'IMC']:
    print('bajo de peso')
    break


for imc in usuarios['IMC']:
    for i in np.arange(16, 18.50, 0.000001):
        print(i)
        break
    #if imc <= np.arange(16, 18.50):
        #print('infrapeso')
        #usuarios['IMC Clas'] = 'Infrapeso'
    #usuarios['IMC Clas'] = np.arange(16, 18.50, 0.000001)
    print(imc)

if usuarios['IMC'] <= np.arange(16, 18.50, 0.000001):
        usuarios['IMC Clas'] = 'Infrapeso'
    elif usuarios['IMC'] <= np.arange(18.50, 24.99, 0.000001):
        usuarios['IMC Clas'] = 'Normal'
    elif usuarios['IMC'] <= np.arange(24.99, 29.99, 0.000001):
        usuarios['IMC Clas'] = 'Sobrepeso'
    elif usuarios['IMC'] <= np.arange(29.99, 40, 0.000001):
        usuarios['IMC Clas'] = 'Obeso'
    else:
        usuarios['IMC Clas'] == np.nan




for imc in usuarios['IMC']:
    if usuarios['IMC'] <= np.arange(16, 18.50, 0.01):
        usuarios['IMC Clas'] = 'Infrapeso'
    elif usuarios['IMC'] <= np.arange(18.50, 24.99, 0.000001):
        usuarios['IMC Clas'] = 'Normal'
    elif usuarios['IMC'] <= np.arange(24.99, 29.99, 0.000001):
        usuarios['IMC Clas'] = 'Sobrepeso'
    elif usuarios['IMC'] <= np.arange(29.99, 40, 0.000001):
        usuarios['IMC Clas'] = 'Obeso'
    else:
        usuarios['IMC Clas'] == np.nan






###########################################################################################


#### Base de datos "iris" ############################################################
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/Sivlemx/Anaconda-UNAM/master/iris.csv'

urlretrieve(url, 'iris.csv')
iris_csv = 'iris.csv'
print(iris_csv)
print(type(iris_csv))

df_csv = pd.read_csv(iris_csv, sep=',')
print(df_csv)
print(type(df_csv))

url = 'https://github.com/Sivlemx/Anaconda-UNAM/raw/master/iris.xlsx'
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



