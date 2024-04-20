import dash 
from dash import html,dcc
import dash_bootstrap_components as dbc

Inferior = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
            html.H2("Toma de Datos"),
            html.P("A. Cohesión (c)  [N/m^2]"),
        dcc.Input(type='number' , value= "0", id= "entrada"),

            html.P("B. Sobrecarga (q)  [N]"),
        dcc.Input(type='number' , value= "0", id= "entrada"),

            html.P("C. Base (B)  [m]"),
        dcc.Input(type='number' , value= "0", id= "entrada"),
    
            html.P("D. Peso específico (γ)  [Kg/m^3]"),
        dcc.Input(type='number' , value= "0", id= "entrada"),
    
             html.P("E. Ángulo de Ficción (Φ)  [Kg/m^3]"),
        dcc.Input(type='number' , value= "0", id= "entrada"),


            ])
            
            , md= 4, style={'background-color':'#FFF0F5'}),
        html.Br(), html.Br(),
        dbc.Col('Resultado q', md= 5, style={'background-color':'#FFF0F5'}), 
        html.Br(), html.Br(),
        dbc.Col('Imagen resultado', md= 3, style={'background-color':'#FFF0F5'}), 
        html.Br(), html.Br(),
    ])
])