import pandas as pd
import numpy as np
from urllib.request import urlretrieve
from pandas.tools import plotting

#### Datos Clase Python para Análisis de Datos ###########################################
url = 'https://github.com/Sivlemx/Anaconda-Python-UNAM'
urlretrieve(url, 'iris.csv')

clase = pd.read_csv(url, sep=',', skiprows=6)
print(clase.columns)
print(clase['Sexo'])
print(clase[clase['Sexo'] == 'M']['Estura (cm)'].mean())
print(clase[clase['Sexo'] == 'M'].describe())
print(clase.describe())
por_sexo = clase.groupby('Sexo')
print(por_sexo.mean())
print(por_sexo.median())
por_sexo.boxplot()
plotting.scatter_matrix(clase[['Peso (kg)', 'Estura (cm)', 'Edad']])
#########################################################################################

