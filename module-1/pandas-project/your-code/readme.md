El proyecto está dividido en las siguientes actividades:

1. Importing data (Extract)

2. Data cleaning (Transform)
- Cambiar nombres de las columnas
- Consultar columnas con muchos nulls y eliminarlas
- Eliminar columnas que tienen valores similares

3. Data manipulation (Transform)
- Realizar consultas filtrando los datos de algunas de las columnas, respondiendo a preguntas como "¿en qué país hay más ataques de tiburones mortales?"
- Crear columna y poner morning, afternoon, etc. en función de la hora (time)

4. Exporting data (Load)
- Exportar un csv con el dataframe limpio
- Exportar una imagen con una gráfica de algunos de los cálculos realizados

Está planteado de esta forma sobre todo de cara al proyecto de pipelines, en el que lo dividiré en diferentes clases (Extractor, Transformer...) con las distintas funciones, como importar un archivo, eliminar espacios en blanco, eliminar columnas que tengas más del 90% nulls, exportar un archivo, etc.