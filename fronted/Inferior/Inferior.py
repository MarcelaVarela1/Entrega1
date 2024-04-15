import dash 
from dash import html
import dash_bootstrap_components as dbc

Inferior = dbc.Container([
    dbc.Row([
        dbc.Col('Entrada de datos', md= 4, style={'background-color':'Green'}),
        html.Br(), html.Br(),
        dbc.Col('Resultado q', md= 5, style={'background-color':'yellow'}), 
        html.Br(), html.Br(),
        dbc.Col('Imagen resultado', md= 3, style={'background-color':'grey'}), 
        html.Br(), html.Br(),
    ])
])