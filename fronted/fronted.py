import dash
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Col('Central',md=12,style={'background-color':'red'}),
    dbc.Col('Definiciones',md=12,style={'background-color':'red'}),
    dbc.Col('Inferior',md=12,style={'background-color':'red'}),
    dbc.Col('Superior1',md=12,style={'background-color':'red'}),

])