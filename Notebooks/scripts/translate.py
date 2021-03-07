"""
Uno de los puntos principales a solucionar en la limpieza de datos fue estandarizar el idioma de todos los países; ya que al tener distintos idiomas los CSV resulta complicado
poder ejecutar operaciones debido a que el nombre de los países en su traducción español-inglés no es la misma. Para poder realizar esta tarea tomamos como apoyo
una de las principales aplicaciones de traducción hoy en día, el traductor de google.
El primer paso para tener acceso a la aplicación, es necesario instalar el paquete google_trans_new el cual se añade al ejecutar en una ventana de comandos la siguiente linea:
- pip install google_trans_new
Se debe asegurar sea el paquete que termina en new ya que hay una librería similar la cual ya no cuenta con soporte. 
"""
# Importamos las liberías necesarias
from pandas import DataFrame, read_csv
from google_trans_new import google_translator

# Definicion de la variable global translator
translator = google_translator()


def get_df_translated(url: str) -> DataFrame:
    """
    Función para leer csv desde una URL y retorna un DataFrame con los nombres de los paises traducidos
    :param url: Enlace hacia el csv
    :return: DataFrame
    """
    df = read_csv(url) #Lectura de CSV
    regs = df.Country.count() #Contamos la cantidad de registros en la columna 'Country' para servir como delimitador de la función for
    # Usamos un for para traducir uno a uno los países, el parámetro lang_tgt nos indica el idioma al que queremos llegar y lang_src el de origen
    for i in range(0, regs):
        df.Country[i] = translator.translate(df.Country[i], lang_tgt='es', lang_src='en') 
    return df


def translate_df(df: DataFrame) -> DataFrame:
    """
    Función para traducir directamente un DataFrame
    :param df: DataFrame a traducir
    :return: DataFrame
    """
    regs = df.Country.count() #Contamos la cantidad de registros en la columna 'Country' para servir como delimitador del for
   # Usamos un for para traducir uno a uno los países, el parámetro lang_tgt nos indica el idioma al que queremos llegar y lang_src el de origen
    for i in range(0, regs):
        df.Country[i] = translator.translate(df.Country[i], lang_tgt='es', lang_src='en')
    return df
