from sqlite3 import Date
import pandas as pd

#Cargar el conjunto de datos dirtydata.csv
df = pd.read_csv('C:\\Users\\Alfonso\\Dropbox\\python ciencia de datos\\dirtydata.csv')
#Mostrar los 5 primeros registros
print(df.head())
#Mostrar la informaci ́on del conjunto de datos
print(df.info())
#Corregir el formato de la columna fecha
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string)
#Remover celdas vacias o incorrectas
new_df = df.dropna()
print(new_df.to_string())