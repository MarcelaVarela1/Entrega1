import dash 
from dash import html
import dash_bootstrap_components as dbc

Definiciones = dbc.Container([
    dbc.Row([
        dbc.Col('Conceptos', md= 9, style={'background-color':'Blue'}),
        html.Br(), html.Br(),
        dbc.Col('Imagen Ilustrativa', md= 3, style={'background-color':'yellow'}), 
        html.Br(), html.Br(),
    ])
])