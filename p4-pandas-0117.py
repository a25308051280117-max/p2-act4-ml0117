import pandas as pd
import numpy as np
# Matias lopez NC 0117
n_filas=5
n_columnas=5
tag_columna=tuple('ABCDE') #etiquetas para columnas de una tupla
print(tag_columna)
matriz=np.random.randint(1,6,size=(n_filas,n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros alaterorios conprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df=pd.DataFrame(matriz,columns= tag_columna)
print("-----La tabla o dataframe----NC= 0117")
print(df)
print("----- Matias lopez NC 0117-------")










