import pandas as pd
import numpy as np
import plotly.graph_objects as go

path = "C:/Users/Fer/TESIS_ARCHIVOS/TESIS_AIRE/MP_Forecasting/mp_forecasting/data/interim"

datos = pd.read_csv(path + '/DINAC_CERRITO.csv', index_col='FECHA_HORA_UTC')

print(datos.head())

# creamos la figura
fig = go.Figure()

# elegimos los parametros x e y desde nuestro dataframe
fig.add_trace(
    go.Scatter(x = list(datos.index), y = list(datos.BANDERA), mode = 'lines'))

# titulo

fig.update_layout( title_text = "CERRITO - DATOS PRESENTES (0) VS FALTANTES (-1)")

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1d",
                     step="day",
                     stepmode="backward"),
                dict(count=7,
                     label="1w",
                     step="day",
                     stepmode="backward"),
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
    

)

# fig.update_traces(visible = False)
fig.show()
