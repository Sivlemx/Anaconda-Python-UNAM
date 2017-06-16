import pandas as pd
import numpy as np

### Abrimos los txt
dfsujeto1 = pd.read_csv('sujeto1.txt', sep='\t', header=6)
dfsujeto2 = pd.read_csv('sujeto2.txt', sep='\t', header=6)
dfsujeto3 = pd.read_csv('sujeto3.txt', sep='\t', header=6)

### Arreglamos el tiempo
dfsujeto1tiempo = pd.to_datetime(dfsujeto1.iloc[:, 0]).dt.time.to_frame().rename(columns={'Video Time':'Tiempo'})
dfsujeto2tiempo = pd.to_datetime(dfsujeto2.iloc[:, 0]).dt.time.to_frame().rename(columns={'Video Time':'Tiempo'})
dfsujeto3tiempo = pd.to_datetime(dfsujeto3.iloc[:, 0]).dt.time.to_frame().rename(columns={'Video Time':'Tiempo'})

### Arreglamos emociones
dfemo1 = dfsujeto1.iloc[:, 1:11] 
dfemo2 = dfsujeto2.iloc[:, 1:11] 
dfemo3 = dfsujeto3.iloc[:, 1:11] 

### Arreglamos Frecuencia Cardíaca
dfcard1 = dfsujeto1.iloc[:, -3:-2]
dfcard2 = dfsujeto2.iloc[:, -3:-2]
dfcard3 = dfsujeto3.iloc[:, -3:-2]
#############################################################################################
### Uniendo bases de Sujeto 1
df1_sujeto1 = dfemo1.join(dfcard1)
df2_sujeto1 = df1_sujeto1.replace('FIT_FAILED', np.nan)
df3_sujeto1 = df2_sujeto1.replace('FIND_FAILED', np.nan)
df4_sujeto1 = df3_sujeto1.replace('NotAnalyzed', np.nan)
df5_sujeto1 = df4_sujeto1.replace('Unknown Heart Rate', np.nan).astype(float) 
df6_sujeto1 = df5_sujeto1.rename(columns={'Neutral':'Neutral',
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

sujeto1 = dfsujeto1tiempo.join(df6_sujeto1).dropna(how='any').set_index('Tiempo').assign(Sujeto='Sujeto1')

df1_sujeto1.info()
sujeto1.info()

sujeto1.to_csv('Sujeto1.csv', sep=',')

########################################################################################################
### Uniendo bases de Sujeto 2
df1_sujeto2 = dfemo2.join(dfcard2)
df2_sujeto2 = df1_sujeto2.replace('FIT_FAILED', np.nan)
df3_sujeto2 = df2_sujeto2.replace('FIND_FAILED', np.nan)
df4_sujeto2 = df3_sujeto2.replace('NotAnalyzed', np.nan)
df5_sujeto2 = df4_sujeto2.replace('Unknown Heart Rate', np.nan).astype(float) 
df6_sujeto2 = df5_sujeto2.rename(columns={'Neutral':'Neutral',
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

sujeto2 = dfsujeto2tiempo.join(df6_sujeto2).dropna(how='any').set_index('Tiempo').assign(Sujeto='Sujeto2')

df1_sujeto2.info()
sujeto2.info()

sujeto2.to_csv('Sujeto2.csv', sep=',')

########################################################################################################
### Uniendo bases de Sujeto 3
df1_sujeto3 = dfemo3.join(dfcard3)
df2_sujeto3 = df1_sujeto3.replace('FIT_FAILED', np.nan)
df3_sujeto3 = df2_sujeto3.replace('FIND_FAILED', np.nan)
df4_sujeto3 = df3_sujeto3.replace('NotAnalyzed', np.nan)
df5_sujeto3 = df4_sujeto3.replace('Unknown Heart Rate', np.nan).astype(float) 
df6_sujeto3 = df5_sujeto3.rename(columns={'Neutral':'Neutral',
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

sujeto3 = dfsujeto3tiempo.join(df6_sujeto3).dropna(how='any').set_index('Tiempo').assign(Sujeto='Sujeto3')

df1_sujeto3.info()
sujeto3.info()

sujeto3.to_csv('Sujeto3.csv', sep=',')
#####################################################################################################
### Juntar las bases de los Sujetos
# 1.- Trabajar a sujeto2 y sujeto3
# 2.- Juntar las bases como apéndices.
df = sujeto1.append(sujeto2)
sujetos = df.append(sujeto3)
#####################################################################################################
### 3.- Obtener los Descriptivos por sujeto y por emoción
neu_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Neutral']].describe()
fel_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Felicidad']].describe()
tri_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Tristeza']].describe()
eno_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Enojo']].describe()
sor_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Sorpresa']].describe()
mie_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Miedo']].describe()
asc_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Asco']].describe()
des_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Desprecio']].describe()
val_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Valencia']].describe()
act_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Activación']].describe()
car_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Frec Cardíaca']].describe()

neu_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Neutral']].describe()
fel_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Felicidad']].describe()
tri_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Tristeza']].describe()
eno_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Enojo']].describe()
sor_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Sorpresa']].describe()
mie_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Miedo']].describe()
asc_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Asco']].describe()
des_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Desprecio']].describe()
val_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Valencia']].describe()
act_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Activación']].describe()
car_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Frec Cardíaca']].describe()

neu_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Neutral']].describe()
fel_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Felicidad']].describe()
tri_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Tristeza']].describe()
eno_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Enojo']].describe()
sor_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Sorpresa']].describe()
mie_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Miedo']].describe()
asc_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Asco']].describe()
des_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Desprecio']].describe()
val_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Valencia']].describe()
act_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Activación']].describe()
car_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Frec Cardíaca']].describe()
######################################################################################################
### 4.- Obtener los descriptivos por sujeto de todas las emociones
desc_sujeto1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'].describe()
desc_sujeto2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'].describe()
desc_sujeto3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'].describe()
######################################################################################################
### 5.- Obtener la correlación de pearson 
###       por sujeto y por emoción
corr_neu_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Neutral']].corr()
corr_fel_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Felicidad']].corr()
corr_tri_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Tristeza']].corr()
corr_eno_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Enojo']].corr()
corr_sor_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Sorpresa']].corr()
corr_mie_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Miedo']].corr()
corr_asc_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Asco']].corr()
corr_des_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Desprecio']].corr()
corr_val_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Valencia']].corr()
corr_act_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Activación']].corr()
corr_car_su1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Frec Cardíaca']].corr()

corr_neu_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Neutral']].corr()
corr_fel_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Felicidad']].corr()
corr_tri_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Tristeza']].corr()
corr_eno_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Enojo']].corr()
corr_sor_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Sorpresa']].corr()
corr_mie_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Miedo']].corr()
corr_asc_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Asco']].corr()
corr_des_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Desprecio']].corr()
corr_val_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Valencia']].corr()
corr_act_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Activación']].corr()
corr_car_su2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Frec Cardíaca']].corr()

corr_neu_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Neutral']].corr()
corr_fel_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Felicidad']].corr()
corr_tri_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Tristeza']].corr()
corr_eno_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Enojo']].corr()
corr_sor_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Sorpresa']].corr()
corr_mie_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Miedo']].corr()
corr_asc_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Asco']].corr()
corr_des_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Desprecio']].corr()
corr_val_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Valencia']].corr()
corr_act_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Activación']].corr()
corr_car_su3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Frec Cardíaca']].corr()
########################################################################################################
### 6.- Obtener la correlación de pearson 
###       por sujeto de todas las emociones
corr_sujeto1 = sujetos[sujetos['Sujeto'] == 'Sujeto1'].corr()
corr_sujeto2 = sujetos[sujetos['Sujeto'] == 'Sujeto2'].corr()
corr_sujeto3 = sujetos[sujetos['Sujeto'] == 'Sujeto3'].corr()
#######################################################################################################
### 7.- Graficar cada emoción
###       (La que mejor consideres y ¿Por qué esa gráfica?)
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Neutral']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Felicidad']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Tristeza']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Enojo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Sorpresa']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Miedo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Asco']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Desprecio']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Valencia']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Activación']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto1'][['Frec Cardíaca']].plot()

sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Neutral']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Felicidad']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Tristeza']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Enojo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Sorpresa']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Miedo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Asco']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Desprecio']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Valencia']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Activación']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto2'][['Frec Cardíaca']].plot()

sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Neutral']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Felicidad']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Tristeza']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Enojo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Sorpresa']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Miedo']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Asco']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Desprecio']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Valencia']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Activación']].plot()
sujetos[sujetos['Sujeto'] == 'Sujeto3'][['Frec Cardíaca']].plot()
########################################################################################
### 8.- Graficar las emociones con valencias positivas
###       (La que mejor consideres y ¿Por qué esa gráfica?)
sujetos[sujetos['Valencia'] > 0].plot()
val_pos = sujetos[sujetos['Valencia'] > 0]
val_pos.iloc[:, 0:9].plot()
#########################################################################################
### 9.- Graficar las emociones con valencias negativas
###       (La que mejor consideres y ¿Por qué esa gráfica?)
sujetos[sujetos['Valencia'] < 0].plot()
val_neg = sujetos[sujetos['Valencia'] < 0]
val_neg.iloc[:, 0:9].plot()



