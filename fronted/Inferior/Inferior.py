import dash 
from dash import html,dcc
import dash_bootstrap_components as dbc

Inferior = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([

            html.H2("Toma de Datos"),
                html.Label('A. Cohesión (c)  [N/m^2]'),
                dcc.Input(type='number' , value= "0", id= "entradacohesión"),
                html.Label(id = 'Salidacohesión'),
                html.Br(),

            
                html.Label('B. Sobrecarga (q)  [N]'), 
                dcc.Input(type='number' , value= "0", id= "entradasc"),
                html.Label(id = 'Salidasc'),
                html.Br(),

                html.Label('C. Base       (B)  [m]'),
                dcc.Input(type='number' , value= "0", id= "entradabase"),
                html.Label(id = 'Salidabase'),
                html.Br(),

                html.Label('D. Peso específico (γ) [Kg/m^3]'), 
                dcc.Input(type='number' , value= "0", id= "entradape"),
                html.Label(id = 'Salidape'),
                html.Br(),

                html.Label('E. Ángulo de Ficción (Φ) [°]'), 
                dcc.Input(type='number' , value= "0", id= "entradaaf"),
                html.Label(id = 'Salidaaf'),
                html.Br(),

            ])
            
            , md= 7, style={'background-color':'#FFF0F5'}),
        html.Br(), html.Br(),


        dbc.Col('Resultado q', md= 5, style={'background-color':'#FFF0F5'}), 



    
    ])
])