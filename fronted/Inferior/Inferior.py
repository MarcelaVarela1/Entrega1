import dash  #Se importa la libreria de Dash
from dash import html,dcc # Importa el módulo html de Dash para poder utilizar etiquetas HTML.
import dash_bootstrap_components as dbc # Importa Dash Bootstrap Components que proporciona componentes basados en Bootstrap para Dash.

# Se Define un contenedor central que encapsula todo el contenido de esta sección.
Inferior = dbc.Container([ # Se define un contenedor.
    dbc.Row([ # Se Crea una fila usando.Las filas son usadas para agrupar horizontalmente columnas.
        dbc.Col(
            html.Div([

            html.H2("Toma de Datos", style={'text-align': 'center'}),
                html.Label('A. Cohesión (c)  [N/m^2]'),
                dcc.Input(type='number', id= "EntradaCohesion",placeholder="Ingrese valor cohesión"),
                html.Br(),

            
                html.Label('B. Sobrecarga (q)  [N]'), 
                dcc.Input(type='number', id= "EntradaSobreCarga",placeholder="Ingrese valor Sobrecarga"),
                html.Br(),

                html.Label('C. Base       (B)  [m]'),
                dcc.Input(type='number' , id= "EntradaBase",placeholder="Ingrese valor Base"),
                html.Br(),

                html.Label('D. Peso específico (γ) [Kg/m^3]'), 
                dcc.Input(type='number' , id= "EntradaPesoEspecifico",placeholder="Ingrese valor Peso Específico"),
                html.Br(),

                html.Label('E. Ángulo de Ficción (Φ) [°]'), 
                dcc.Input(type='number', id= "EntradaAnguloFriccion",placeholder="Ingrese Ángulo Fricción"),
                html.Br(),
            ])
            
            , md= 7, style={'background-color':'#FFF0F5'}),
        html.Br(), html.Br(),

        
        dbc.Col(
            html.Div([
                html.H1("El Resultado de la Carga Ultima es:", style={'text-align': 'center'}),
                html.Label( id = 'ResultadoOperacion')

            ])
            
            , md= 5, style={'background-color':'#FFF0F5'}),     
    ])
])