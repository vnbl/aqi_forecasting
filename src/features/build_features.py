
# Turn raw data into features for modeling

import numpy
import pandas

"""

Original dataset

10 streams (one per station)

FECHA | HORA |  MP1  |  MP2_5  |  MP10  |   TEMPERATURA  |  HUMEDAD RELATIVA  | PRESION  | BATERIA

Target dataset

FECHAHORA | ESTACION | ANHO | MES | DIA | HORA | MINUTO |  MP1  |  MP2_5  |  MP10  |   TEMPERATURA  |  HUMEDAD RELATIVA  | PRESION  | AQI_10  | AQI_2_5  |  TRAFICO | DIA_SEM


"""
def build_station(df, station):
    
    set_col_names(df)
    date_features(df)
    aqi_features(df)
    traffic_features(df)

    df[ESTACION] = station



def set_col_names(df):

    df.columns = ['FECHA', 'HORA', 'MP1', 'MP2_5', 'MP10', 'TEMPERATURA', 'HUMEDAD', 'PRESION', 'BATERIA']

    #return df

def date_features(df):
    
    # aqui poner el codigo que se uso originalmente para poner el feature fechahora.
    

def aqi_features(df):

    # aqui poner el codigo usado originalmente para poner los features de AQI.

def traffic_features(df):

    # aqui poner el codigo usado originalmente para transformar los features de tráfico.




