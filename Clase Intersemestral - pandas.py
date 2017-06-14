## https://github.com/Sivlemx/Anaconda-Python-UNAM

# Python Zen
print("""
          -->  Python Zen  <--
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
# http://pandas.pydata.org/pandas-docs/stable/index.html

import numpy as np
# https://docs.scipy.org/doc/numpy/user/quickstart.html

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
peso = [67, 56, 69, 55, 65, 51, 47, 90, 52, 56, 82, 104, 89, 65, 60]
estatura = [1.74, 1.60, 1.71, 1.60, 1.70, 1.60, 1.53, 1.73, 1.60, 1.60, 1.76, 1.80, 1.78, 1.72, 1.52]

# Cambiar Macho=Hombre y Hembra=Mujer
clase = {'Semestre':['Sexto', 'Sexto', 'Sexto', 'Sexto', 'Cuarto', 'Egresada', 'Segundo', 'Cuarto', 'Sexto', 'Sexto', 'Titulado', 'Doctorante', 'Egresada', 'Sexto', 'Egresada'],
         'Sexo':['Mujer', 'Mujer', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Mujer', 'Hombre', 'Mujer', 'Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer'],
         'Edad':[23, 20, 21, 22, 25, 23, 19, 20, 21, 20, 25, 34, 22, 21, 24],
         'Estatura':[1.74, 1.60, 1.71, 1.60, 1.70, 1.60, 1.53, 1.73, 1.60, 1.60, 1.76, 1.80, 1.60, 1.72, 1.52],
         'Nombre':['Gisela', 'Valeria', 'Alfredo', 'Gabriela', 'Pako', 'Samantha', 'Valeria', 'Mario', 'Elizabeth', 'Sam', 'Christian', 'Javier', 'Leslie', 'Rodrigo', 'Yuna']}

clase = pd.DataFrame(clase)
print(clase)

## Crear nueva(s) columna(s)
clase['Universidad'] = ['UNAM', 'UNAM', 'UNAM', 'UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM','UNAM'] 
print(clase)

peso = [67, 56, 69, 55, 65, 51, 47, 90, 52, 56, 82, 104, 55, 65, 60]
clase['Peso'] = peso
print(clase)

clase['Deporte'] = ['Natación', 'Volley', 'Basquetball', 'Tae Kwon Do', 'Soccer', 'Soccer', 'Basquetball', 'Basquetball', 'Natación', 'Tennis', 'Hapkido', 'Hapkido', np.nan, 'Basquetball', 'Tocho']

## Colocar Índice
clase.index = ['GB', 'VC', 'AL', 'GC', 'PT', 'SA', 'VG', 'IG', 'EN', 'SM', 'CD', 'JV', 'LZ', 'RG', 'ID'] # Iniciales en clase
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

clase[['Deporte', 'Nombre']]

clase[1:3]

## Método "*.loc"
# Filas
clase.loc['GC']
clase.loc[['GC']]
clase.loc[['LZ', 'EN', 'GB']]
# Filas y Columnas
clase.loc[['PT', 'CD', 'ID'], ['Deporte', 'Nombre']]
#Todas las Filas
clase.loc[:, ['Deporte', 'Nombre']]

## Método "*.iloc"
# Filas
clase.iloc[1]
clase.iloc[[1]]
clase.iloc[[1, 2, 3]]
# Filas y Columnas
clase.iloc[[1, 2, 3], [6, 7]]
#Todas las Filas
clase.iloc[:, [6, 7]]

## Ejercicio
# Utilizar = *.loc[Edad, Estatura, Peso] de JV, SA, CD
# En 2 tipos = Series de Tiempo y DataFrame
clase.loc[['JV', 'SA', 'CD'], ['Edad', 'Estatura', 'Peso']]
clase.loc[['JV', 'SA', 'CD'], :]
clase.loc[:, 'Edad']
clase.loc[:, 'Estatura']
clase.loc[:, 'Peso']

clase.loc[:, ['Edad']]
clase.loc[:, ['Estatura']]
clase.loc[:, ['Peso']]

clase.columns
clase.index
clase.axes

# Utilizar = *.iloc[Edad, Estatura, Peso] de JV, SA, CD
# En 2 tipos = Series de Tiempo y DataFrame

clase.iloc[[11, 5, 10], [0, 1, 6]]
clase.iloc[[11, 5, 10], :]
clase.iloc[:, 0]
clase.iloc[:, 1]
clase.iloc[:, 6]

clase.iloc[:, [0]]
clase.iloc[:, [1]]
clase.iloc[:, [6]]



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

clase.info()
## Ordenar por Edad
clase = clase.sort_values('Edad')

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


## Exportar a CSV
clase.to_csv('Clase_Anaconda.csv', sep=',', encoding='utf-8')
clase.to_csv('Clase_Anaconda1.csv', sep='\t', encoding='utf-8')
clase.to_csv('Clase_Anaconda2.csv', sep=';', encoding='utf-8')


## Exportar a TXT
clase.to_csv('Clase_Anaconda.txt', sep=',')

## Exportar a Excel
clase.to_excel('Clase_Anaconda.xls')
clase.to_excel('Clase_Anaconda.xlsx')
##########################################################

## Importar archivo CSV
clase = pd.read_csv('Clase_Anaconda.csv', sep=',')

help(pd.read_csv)

clase = pd.read_csv('Clase_Anaconda.csv', sep=',', index_col=0)

## Bucle For

for valores in clase:
    print(valores)

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

##
clase['# Letras en el Nombre'] = clase['Nombre'].apply(len)
print(clase)

clase = clase.drop('No._Letras', axis=1)

## Ejercicio
# 1.- Fijate en el ejemplo de arriba
# 2.- Crea una columna llamada "Letras UNAM" con valores del número de letras
# 3.- Avisa que ya lo hiciste
# 4.- Esa columna que creaste, borrala












clase['Letras UNAM'] = clase['Universidad'].apply(len)
clase = clase.drop('Letras UNAM', axis=1)
clase = clase.drop(['No._Letras', '# Letras en el Nombre'], axis=1)


################################################################

clase['Sexo']
clase[['Sexo']]

clase['Sexo'].unique()
clase[['Sexo']].nunique()

#### Estadística Descriptiva
print("""
      Estadística Descriptiva:
          
          “Es el estudio que incluye la obtención, organización, 
          presentación y descripción de información numérica”. 
""")

## Medidas de Tendencia Central = media, mediana, moda
clase[clase['Sexo'] == 'Mujer']['Estatura'].mean() # Media
clase[clase['Sexo'] == 'Mujer']['Estatura'].median() # Mediana
clase[clase['Sexo'] == 'Mujer']['Estatura'].mode() # Moda

## Medidas de Dispersión = Rango, Desviación Estándar, Varianza
clase[clase['Sexo'] == 'Mujer']['Estatura'].max() # Máximo
clase[clase['Sexo'] == 'Mujer']['Estatura'].min() # Mínimo
clase[clase['Sexo'] == 'Mujer']['Estatura'].std() # Desviación Estándar
clase[clase['Sexo'] == 'Mujer']['Estatura'].var() # Varianza

clase[clase['Sexo'] == 'Mujer']['Estatura'].sem() # Error Estándar

clase[clase['Sexo'] == 'Mujer'][['Estatura', 'Peso']].describe() # Datos Descriptivos 

#Correlación (method='pearson')
clase[clase['Sexo'] == 'Mujer'].corr()

## Ejercicio
# 1.- Obtener la media de la Edad y el IMC de solo los hombres 
# 2.- Obtener la desviación estandar de la Edad y el IMC de solo los hombres
# 3.- Obtener el mínimo de la Edad y el IMC de solo los hombres
# 4.- Obtener el máximo de la Edad y el IMC de solo los hombres
# 5.- Obtener la correlación de la Edad y el IMC de solo los hombres


### Función Groupby
clase['Sexo'].unique()

clase.groupby('Sexo').mean()
clase.groupby('Sexo').median()
clase.groupby('Sexo').mode()

clase.groupby('Sexo').max()
clase.groupby('Sexo').min()
clase.groupby('Sexo').std()
clase.groupby('Sexo').var()

clase.groupby('Sexo').sem()

clase.groupby('Sexo').describe()

clase.groupby('Sexo').corr()

clase.describe()
clase.corr()
#############################################################
#### Análisis Cualitativo
# Factores e individuales
clase['Sexo'].unique()

# Descriptiva por categoría
clase['Sexo'].describe()

# Observando índices y columnas
clase.axes

# Filtrando por categorías
mujeres = clase[clase['Sexo'] == 'Mujer']
hombres = clase[clase['Sexo'] == 'Hombre']

mujeres.describe()
hombres.describe()
############################################################################################
#### Graficar lo que se tenga que graficar
import matplotlib.pyplot as plt
# https://matplotlib.org/index.html

edades = clase['Edad'].values

plt.hist(edades)
plt.hist(edades, 5)
plt.hist(edades, 10)

plt.plot(edades)
plt.show()

x = clase['Peso'].values
y = clase['Estatura'].values
plt.scatter(x, y)
plt.show()
##########################################################################################
## Graficando con la propia librería de pandas
edades1 = clase['Edad']

edades1.plot.hist()
edades1.plot.hist(alpha=0.5)

edades1.plot()

clase.plot.scatter(x='Peso', y='Estatura')

ax = clase[clase['Sexo'] == 'Mujer'].plot.scatter(x='Peso', y='Estatura', color='Red', label='Mujeres')
clase[clase['Sexo'] == 'Hombre'].plot.scatter(x='Peso', y='Estatura', color='Blue', label='Hombres', ax=ax)

help(pd.DataFrame.boxplot)

clase.boxplot('Peso', 'Sexo', grid=False)

clase.groupby('Sexo')['Peso'].describe()

pd.plotting.scatter_matrix(clase[['Peso', 'Estatura', 'IMC']])

######################################################################################
import seaborn as sns
# http://seaborn.pydata.org/index.html
sns.pairplot(clase, vars=['Peso', 'Estatura', 'IMC'], kind='reg')

sns.pairplot(clase, vars=['Peso', 'Estatura', 'IMC'], kind='reg', hue='Sexo')

sns.lmplot(y='Peso', x='Estatura', data=clase)

sns.stripplot(x='Peso', y='Estatura', hue='Sexo', data=clase)

sns.stripplot(x='Categoría_IMC', y='IMC', hue='Sexo', data=clase)

###########################################################################################
### Estadística Inferencial
import scipy.stats as sps
# https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats

peso_mujer = clase[clase['Sexo'] == 'Mujer']['Peso']
peso_hombre = clase[clase['Sexo'] == 'Hombre']['Peso']
sps.ttest_ind(peso_mujer, peso_hombre)




