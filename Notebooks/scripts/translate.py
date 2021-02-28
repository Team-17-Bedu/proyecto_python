"""
Para tener acceso al paquete google_trans_new es necesario ejecutar en una ventana de comandos la siguiente linea
 - pip install google_trans_new
"""

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
    df = read_csv(url)
    regs = df.Country.count()
    for i in range(0, regs):
        df.Country[i] = translator.translate(df.Country[i], lang_tgt='es', lang_src='en')
    return df


def translate_df(df: DataFrame) -> DataFrame:
    """
    Función para traducir directamente un DataFrame
    :param df: DataFrame a traducir
    :return: DataFrame
    """
    regs = df.Country.count()
    for i in range(0, regs):
        df.Country[i] = translator.translate(df.Country[i], lang_tgt='es', lang_src='en')
    return df
