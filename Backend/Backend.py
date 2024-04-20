"""
Nycole Valentina Wiesner Cod. 20222579031
Angie Marcela Varela Cod. 20222579035
"""

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math

@app.callback(
    Output('lo que se ponga en output','Children'),
    Input('lo que se puso en input', 'value')
)
def CargaUltima('lo que se puso en input'):
    calculo = 