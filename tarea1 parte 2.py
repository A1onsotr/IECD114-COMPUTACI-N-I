import os
import pandas as pd

os.chdir("C:/Users/A/Desktop/Tarea1")

df = pd.read_csv(filepath_or_buffer = "AgeHeightWeight.csv", sep = ",", index_col=False)


weight = df['Weight'] # 'pandas.core.series.Series'>

height = df['Height']


# convertir altura en metros
height_m = []    # altura en metros
for f in range(len(height)):
    m = height[f]/100
    height_m.append(m)




IMC = []

for f in range(len(weight)):
    val_imc = weight[f]/(height_m[f]**2)
    val_imc = round(val_imc,2)
    IMC.append(val_imc)
    
    
#print(IMC)

#CLASIFICACIONES
#clasificaciones sacadas de la siguiente pagina web:
#https://www.cdc.gov/healthyweight/spanish/assessing/index.html#:~:text=Si%20su%20IMC%20es%20menos,dentro%20del%20rango%20de%20obesidad.

clas = [] 


for f in range(len(IMC)):
    if IMC[f] < 18.5 :
        clas.append('Bajo Peso')
    else:
        if IMC[f] < 25.0:
            clas.append('Peso Normal')
        else:
            if IMC[f] < 30:
                clas.append('Sobrepeso')
            else:
                clas.append('Obesidad')
                        
        
#print(len(p_b)+len(p_n)+len(p_s)+len(p_o1)+len(p_o2)+len(p_o3))

# ESTETÍCA
df.columns = ['Genero','Altura (cm)','Peso (kg)']

genero = df['Genero']

for f in range(len(genero)):
    if genero[f] == 'Male':
        genero[f] = 'Hombre'
    if genero[f] == 'Female':
        genero[f] = 'Mujer'
print(genero)

df.pop('Genero')           
df.insert(loc=0, column='Genero',value = genero)
print(df)  

# AGREGADOS DE NUEVAS COLUMNAS
col_name = ['IMC','Clasificación']
col_value = [IMC, clas]

df.insert(loc= 3, column= 'IMC' ,value = IMC)
df.insert(loc= 4, column= 'Clasificación' ,value = clas)
    

df.to_csv("AgeHeightWeight_modificado.csv", sep = ";", header = True, index = False)
