"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os

    # Ruta del archivo original
    file_path = 'files/input/solicitudes_de_credito.csv'

    # Ruta para guardar el archivo limpio
    output_dir = 'files/output'
    output_path = os.path.join(output_dir, 'solicitudes_de_credito.csv')

    # Leer el archivo CSV con el separador correcto
    data = pd.read_csv(file_path, sep=';', encoding='utf-8')




    # Eliminar registros con valores faltantes
    data = data.dropna()
    data_cleaned=data.copy()

    # Eliminar la columna innecesaria
    data_cleaned = data.drop(columns=["Unnamed: 0"])


    data_cleaned['monto_del_credito'] = data_cleaned['monto_del_credito'].replace({'\$': '', ',': '', ' ': ''}, regex=True)
    data_cleaned['barrio'] = data_cleaned['barrio'].str.replace('_', ' ').str.replace('-', ' ')
    data_cleaned['idea_negocio'] = data_cleaned['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ')
    data_cleaned['línea_credito'] = data_cleaned['línea_credito'].str.replace('-', ' ').str.replace('_', ' ')


    # # Normalizar valores de texto
    data_cleaned['sexo'] = data_cleaned['sexo'].str.lower().str.strip()
    # # Normalizar valores de texto
    data_cleaned['tipo_de_emprendimiento'] = data_cleaned['tipo_de_emprendimiento'].str.lower().str.strip()
    # # Normalizar valores de texto
    data_cleaned['línea_credito'] = data_cleaned['línea_credito'].str.lower().str.strip()
    # # Normalizar valores de texto
    data_cleaned['idea_negocio'] = data_cleaned['idea_negocio'].str.lower().str.strip()
    # # Normalizar valores de texto
    data_cleaned['barrio'] = data_cleaned['barrio'].str.lower()



    def es_convertible_a_entero(valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False

    # Filtrar el DataFrame para mantener solo los registros convertibles a entero
    data_cleaned = data_cleaned[data_cleaned['comuna_ciudadano'].apply(es_convertible_a_entero)]

    #Ordenar fecha
    data_cleaned['fecha_de_beneficio'] = data_cleaned['fecha_de_beneficio'].str.replace("-","/").str.strip()


    def ordenarfecha(fecha_de_beneficio):
        if int(fecha_de_beneficio.split("/")[0])>31:
            return pd.to_datetime(fecha_de_beneficio, format='%Y/%m/%d')
        else:
            return pd.to_datetime(fecha_de_beneficio, format='%d/%m/%Y')
        
    data_cleaned['fecha_de_beneficio'] = data_cleaned['fecha_de_beneficio'].apply(ordenarfecha)

    # Limpiar 'monto_del_credito' y barrio: eliminar caracteres especiales 
    # data_cleaned["monto_del_credito"] = (
    #     data_cleaned["monto_del_credito"]
    #     .str.replace("[^0-9]", "", regex=True)
    #     .astype(float)
    #  )


    #castear las columnas
    data_cleaned['monto_del_credito'] = data_cleaned['monto_del_credito'].astype(float)
    data_cleaned['comuna_ciudadano'] = data_cleaned['comuna_ciudadano'].astype(int)
    data_cleaned['estrato'] = data_cleaned['estrato'].astype(int)
    data_cleaned['barrio'] = data_cleaned['barrio'].astype(str)


    # # Eliminar registros duplicados
    data_cleaned = data_cleaned.drop_duplicates()

    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Guardar el archivo limpio
    data_cleaned.to_csv(output_path, index=False, sep=';')

if __name__ == '__main__':
    print(pregunta_01())

