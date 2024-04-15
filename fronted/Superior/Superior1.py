import dash
from dash import html
import dash_bootstrap_components as dbc

Superior1 = dbc.Container([
    dbc.Row([
        dbc.Col('Diseña cimetación',md=8,style={'background-color':'blue'}),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        dbc.Col('Logo',md=4),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
    ])
])