import dash
from dash import html,dcc
import dash_bootstrap_components as dbc





Central = dbc.Container([
    dbc.Row([
        dbc.Col(

            html.Div([
    html.H1("Tipo de Cimentación"),
    dcc.RadioItems(['Cimentación Corrida', 'Cimentación Cuadrada' , 'Cimentación Circular']
        ),

])
                
                          
                ,md=8,style={'background-color':'blue'}),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        dbc.Col('Imagen referencia',md=4),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
        html.Br(), html.Br(),
    ])
])