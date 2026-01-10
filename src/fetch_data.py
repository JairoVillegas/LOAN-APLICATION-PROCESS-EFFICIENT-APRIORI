import os
import pm4py


from .config import ubicacion_datos_crudos_comprimidos #Importamos la direccion personalizada en la que se encuentra el archivo con los datos comprimidos
from . config import ubicacion_datos_crudos_extraidos #Importamos la direccion personalziada en la que queremos que se guarden los datos crudos una vez descomprimidos


def fetch_raw_data(): #Esta funcion descomprime los datos crudos usando procces mining for python (pm4py) desde la direccion personalizada, luego devuelve los datos ya descomprimidos
    datos = pm4py.read_xes(ubicacion_datos_crudos_comprimidos)
    return datos

def save_raw_data():# Esta funcion ejecuta la funcion fetch_raw_data para obtener los datos crudos, luego los vuelve un dataframe, crea la ruta con os y lo guarda en la direccion personalizada indicada
    datos_crudos = fetch_raw_data()
    data_frame = pm4py.convert_to_dataframe(datos_crudos)
    os.makedirs(os.path.dirname(ubicacion_datos_crudos_extraidos), exist_ok=True)
    data_frame.to_csv(ubicacion_datos_crudos_extraidos,index=False)
    return f"Los datos crudos fueron guardados con exito en {ubicacion_datos_crudos_extraidos}"