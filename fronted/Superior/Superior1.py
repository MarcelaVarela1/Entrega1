import dash
from dash import html
import dash_bootstrap_components as dbc

Superior1 = dbc.Container([
    dbc.Row([

        dbc.Col(
            html.Div([
    html.H1("Diseña tu cimentación SAS"),
    
            ])
    ,md=8,style={'background-color':'#FFEFD5'}),

        html.Br(), html.Br(),

        dbc.Col(
        
            html.Div([
    html.H1("DTC"),
    
            ])
            
            ,md=4,style={'background-color':'#FFEFD5'}),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
    ])
])