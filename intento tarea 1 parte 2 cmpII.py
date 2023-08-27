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
#https://obtienearchivo.bcn.cl/obtienearchivo?id=repositorio/10221/32699/2/BCN_Goldstein_La_obesidad_como_enfermedad__final2.pdf
#en la pagina 2 item 1

p_b = [] #bajo peso

p_n = [] #normal peso

p_s = [] #sobre peso

p_o1 = [] #obesidad 

p_o2 = [] #obesidad grado 2

p_o3 = [] #obesidad grado 3


for f in range(len(IMC)):
    if IMC[f] < 18.5 :
        p_b.append(IMC[f])
    else:
        if IMC[f] < 25.0:
            p_n.append(IMC[f])
        else:
            if IMC[f] < 30:
                p_s.append(IMC[f])
            else:
                if IMC[f] < 35:
                    p_o1.append(IMC[f])
                else:
                    if IMC[f] < 40:
                        p_o2.append(IMC[f])
                    else:
                        p_o3.append(IMC[f])
                        
        
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
col_name = ['IMC','Bajo Peso', 'Normal', 'Sobrepeso', 'Obesidad','Obesidad Grado II', 'Obesidad Grado III']
col_value = [IMC, p_b, p_n, p_s, p_o1, p_o2, p_o3]
for f in range(3,10):
    df.insert(loc= f, column= col_name[f] ,value = col_value[f])
    
print(df)


               
