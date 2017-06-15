import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sps
import statsmodels.api as sm

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

df6 = df5.replace('Unknown Heart Rate', np.nan).astype(float) 
df6.info()

df7 = df6.rename(columns={'Neutral':'Neutral',
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

sujeto1 = dftiempo.join(df7).dropna(how='any').set_index('Tiempo').assign(Sujeto='Suejto1')
sujeto1.info()

sujeto1.to_csv('Sujeto1.csv', sep=',')

#############################################################################
# 1.- Trabajar a sujeto2 y sujeto3
# 2.- Obtener los Descriptivos por sujeto de 1 por 1
# 3.- Obtener los descriptivos por sujeto
# 4.- 

sujeto1.iloc[:, 0:9].plot()
