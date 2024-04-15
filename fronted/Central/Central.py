import dash
from dash import html
import dash_bootstrap_components as dbc

Central = dbc.Container([
    dbc.Row([
        dbc.Col('Tio de cimentación',md=8,style={'background-color':'blue'}),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        dbc.Col('Imagen referencia',md=4),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
    ])
])