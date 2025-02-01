import pandas as pd
import numpy as np

# Leer el archivo CSV
df = pd.read_csv('movies.csv', encoding='cp1252')

# Función para calcular estadísticas básicas
def analizar_peliculas(df):
   """
   Analiza el conjunto de datos de películas y retorna estadísticas principales
   
   Args:
   df (pandas.DataFrame): DataFrame con datos de películas
   
   Returns:
   dict: Diccionario con estadísticas calculadas
   """
   
   # Estadísticas básicas
   stats = {
       'total_peliculas': len(df),
       'presupuesto_promedio': df['budget'].mean(),
       'ingresos_promedio': df['revenue'].mean(),
       'duracion_promedio': df['runtime'].mean(),
       'calificacion_promedio': df['voteAvg'].mean()
   }
   
   # Conteo de idiomas
   idiomas = df['originalLanguage'].value_counts().head()
   stats['idiomas_principales'] = idiomas.to_dict()
   
   return stats

# Ejecutar análisis
estadisticas = analizar_peliculas(df)

# Imprimir resultados
print("=== Resumen del Dataset ===")
print(f"Total películas: {estadisticas['total_peliculas']}")
print(f"\nPromedios:")
print(f"Presupuesto: ${estadisticas['presupuesto_promedio']:,.2f}")
print(f"Ingresos: ${estadisticas['ingresos_promedio']:,.2f}")
print(f"Duración: {estadisticas['duracion_promedio']:.2f} minutos")
print(f"Calificación: {estadisticas['calificacion_promedio']:.2f}/10")

print("\nIdiomas principales:")
for idioma, cantidad in estadisticas['idiomas_principales'].items():
   print(f"- {idioma}: {cantidad}")