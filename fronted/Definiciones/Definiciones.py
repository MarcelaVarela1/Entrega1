import dash 
from dash import html
import dash_bootstrap_components as dbc

Definiciones = dbc.Container([
    dbc.Row([
        dbc.Col('Conceptos', md= 8, style={'background-color':'Blue'}),
        html.Br(), html.Br(),
        dbc.Col('Ecuación metodo de Terzaghi', md= 4, style={'background-color':'yellow'}), 
        html.Br(), html.Br(),
    ])
])