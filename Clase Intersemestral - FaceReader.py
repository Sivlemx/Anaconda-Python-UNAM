import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sujeto = 'sujeto1.txt'

df = pd.read_csv(sujeto)

df = pd.read_csv(sujeto, sep='\t')

df = pd.read_csv(sujeto, sep='\t', header=6)

df.info()

dftiempo = pd.to_datetime(df.iloc[:, 0]).dt.time.to_frame().rename(columns={'Video Time':'Tiempo'})

df1 = df.iloc[:, 1:11] 
df1.info()

df2 = df.iloc[:, -3:-2]
df2.info()

df3 = df1.join(df2)
df3.info()
 
df4 = df3.replace('FIT_FAILED', np.nan)
df4.info()

df5 = df4.replace('FIND_FAILED', np.nan)
df5.info()

df6 = df5.replace('NotAnalyzed', np.nan)
df6.info()

df7 = df6.replace('Unknown Heart Rate', np.nan).astype(float) 
df7.info()

df8 = df7.rename(columns={'Neutral':'Neutral',
                          'Happy':'Felicidad',
                          'Sad':'Tristeza',
                          'Angry':'Enojo',
                          'Surprised':'Sorpresa',
                          'Scared':'Miedo',
                          'Disgusted':'Asco',
                          'Contempt':'Desprecio',
                          'Valence':'Valencia',
                          'Heart Rate':'Frec Cardíaca',
                          'Arousal':'Activación'}) 

sujeto1 = dftiempo.join(df8).dropna(how='any').set_index('Tiempo').assign(Sujeto='Suejto1')
sujeto1.info()

sujeto1.to_csv('Sujeto1.csv', sep=',')

#############################################################################
# 1.- Trabajar a sujeto2 y sujeto3
# 2.- Obtener los Descriptivos por sujeto y por emoción
# 3.- Obtener los descriptivos por sujeto de todas las emociones
# 4.- Graficar cada emoción
# 5.- Graficar las emociones con valencias positivas
# 6.- Graficar las emociones con valencias negativas

sujeto1.iloc[:, 0:9].plot()













