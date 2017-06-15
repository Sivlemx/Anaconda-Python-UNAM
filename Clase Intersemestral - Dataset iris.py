#### Base de datos "iris" ############################################################
import pandas as pd
import matplotlib.pyplot as plt

iris_csv = 'iris.csv'
print(iris_csv)
print(type(iris_csv))

df_csv = pd.read_csv(iris_csv, sep=',')
print(df_csv)
print(type(df_csv))

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
#### Line Plot
df1.plot(x='sepal_length', y='sepal_width')
plt.show()

#### Scatter Plot
df1.plot(x='sepal_length', y='sepal_width', kind='scatter')
plt.xlabel('Ancho de Sepalo (cm)')
plt.ylabel('Largo de Sepalo (cm)')
plt.show()

#### Boxplot
df1.plot(y='sepal_length', kind='box')
plt.ylabel('Largo de Sepalo (cm)')
plt.show()

#### Histograma
df1.plot(y='sepal_length', kind='hist')
plt.xlabel('Ancho de Sepalo (cm)')
plt.show()

#### Histograma
df1.plot(y='sepal_length', kind='hist', bins=30, range=(4,8), normed=True)
plt.xlabel('Ancho de Sepalo (cm)')
plt.show()


#### Estadística Descriptiva

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

df1[df1['name'] == 'versicolor'].corr()

df1[df1['name'] == 'versicolor'].describe()

df1.describe()



########################################################################################
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

pd.plotting.scatter_matrix(df1[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

### Plotear datos
media = df1.groupby('name')['sepal_length'].mean()
error = df1.groupby('name')['sepal_length'].sem()
media.plot.bar(yerr=error)

errors = df1[df1['name'] == 'versicolor'].sem()

df1[df1['name'] == 'versicolor'].plot()
df1[df1['name'] == 'versicolor'].plot(kind='hist', normed=True, yerr=errors)
df1[df1['name'] == 'versicolor'].plot(kind='bar')
df1[df1['name'] == 'versicolor'].plot(kind='barh')
df1[df1['name'] == 'versicolor'].plot(kind='box')
df1[df1['name'] == 'versicolor'].plot(kind='kde')
df1[df1['name'] == 'versicolor'].plot(kind='area')
df1[df1['name'] == 'versicolor'].plot('sepal_length', 'petal_length', kind='scatter')

df1[df1['name'] == 'versicolor'].plot.scatter('sepal_length', 'petal_length')

