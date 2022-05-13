import pandas as pd
import matplotlib.pyplot as plt
print("hola Nan")


datos = pd.read_csv('C:\\Users\\Alfonso\\Dropbox\\python ciencia de datos\\surveys.csv')
print(datos)

# The head() method displays the first several lines of a file
datos.head()

#Tipo de dato
print(type(datos))
#Tipos de datos que contiene el dataframe
print(datos.dtypes)
# Echemos un vistazo a las columnas

print(datos.columns)

#lista de todas las especies. La función pd.unique nos dice los distintos valores presentes en la columnaspecies_id.
print(pd.unique(datos['species_id']))

#Podemos calcular algunas estadísticas básica de todos los datos en una columna usando el siguiente comando
print(datos['weight'].describe())

#También podemos extraer una métrica en particular::

print(datos['weight'].min())
print(datos['weight'].max())
print(datos['weight'].mean())
print(datos['weight'].std())
print(datos['weight'].count())
#si nosotros queremos extraer información por una o más variables, por ejemplo sexo,
#podemos usar el método .groupby de Pandas. Una vez que creamos un DataFrame groupby,
#podemos calcular estadísticas por el grupo de nuestra elección.
grouped_data = datos.groupby('sex')
# Estadísticas para todas las columnas numéricas por sexo
print(grouped_data.describe())
# Regresa la media de cada columna numérica por sexo
print(grouped_data.mean())

# Cuenta el número de muestras por especie
species_counts = datos.groupby('species_id')['record_id'].count()
print(species_counts)
#también podemos contar las líneas que tienen la especie “DO”:
datos.groupby('species_id')['record_id'].count()['DO']
# Multiplicar todos los valores de peso por 2

# Aseguremonos de que las imágenes aparezcan insertadas en iPython Notebook
# Creaemos una gráfica de barras

species_counts.plot(kind='bar');
print(datos['weight']*2)


total_count = datos.groupby('plot_id')['record_id'].nunique()
# También grafiquemos eso
total_count.plot(kind='bar');
#plt.show()

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
pd.DataFrame(d)
my_df = pd.DataFrame(d)
#my_df.unstack()
my_df.plot(kind='bar',stacked=True,title="The title of my graph")
plt.show()


