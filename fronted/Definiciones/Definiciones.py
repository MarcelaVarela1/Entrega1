import dash 
from dash import html
import dash_bootstrap_components as dbc


Definiciones = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
    html.H1("TITULO1"),
    html.H1("TITULO1"),
    html.H1("TITULO1"),
    html.H1("TITULO1"),
    html.H1("TITULO1"),
            ])
            
            , md= 8, style={'background-color':'pink'}),
       
        dbc.Col('Ecuación metodo de Terzaghi', md= 4, style={'background-color':'yellow'}), 
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        
    ])
])