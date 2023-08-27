##############################################################################
##    TAREA 1: PARTE N°1   ###################################################
##############################################################################

import os
import pandas as pd
import numpy as np
os.chdir('C:/Users/A/Desktop/Tarea1')
df = pd.read_csv("starbucks.csv")
ranking = np.arange(1,78,1)

#calorias
df = df.sort_values(by=['calories'], ascending=True)

df.insert(loc= 2 , column= 'ranking calories' ,value = ranking)

#fat 
df = df.sort_values(by=['fat'], ascending=True)

df.insert(loc= 4 , column= 'ranking fat' ,value = ranking)

#carb
df = df.sort_values(by=['carb'], ascending=True)

df.insert(loc= 6 , column= 'ranking carb' ,value = ranking)

# fiber
df = df.sort_values(by=['fiber'], ascending=True)

df.insert(loc= 8 , column= 'ranking fiber' ,value = ranking)

#protein

df = df.sort_values(by=['protein'], ascending=True)

df.insert(loc= 10 , column= 'ranking protein' ,value = ranking)

df = df.sort_values(by=['type'], ascending=True)

df.to_csv("starbucks_modificado.csv", sep = ";", header= True, index = False )