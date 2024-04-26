import dash #Se importa la libreria de Dash
from dash import html # Importa el módulo html de Dash para poder utilizar etiquetas HTML.
import dash_bootstrap_components as dbc # Importa Dash Bootstrap Components que proporciona componentes basados en Bootstrap para Dash.

# Se define un contenedor.
Superior1 = dbc.Container([ 
    dbc.Row([ # Se Crea una fila usando.Las filas son usadas para agrupar horizontalmente columnas.


        dbc.Col(
            html.Div([ # Se crea un contenedor genérico que en este caso contiene un título.
    html.H1("Diseña tu cimentación SAS"), # Se crea un encabezado de nivel 1 con texto.
    
            ])
    ,md=8,style={'background-color':'#FFEFD5'}),# Crea una columna dentro de la fila. `md=8` indica que la columna usa 8 de 12 columnas en una pantalla de tamaño medio.

        html.Br(), html.Br(), #Espacio de renglon

# Se Define otra columna dentro de la fila. `md=4` indica que esta columna ocupa 4 de 12 columnas posibles en una pantalla de tamaño medio.
        dbc.Col(
        
            html.Div([ # Se crea un contenedor genérico que en este caso contiene un título.
    html.H1("DTC"), #Se genera un titulo.
    
            ])
            
            ,md=4,style={'background-color':'#FFEFD5'}),

        
        html.Br(), html.Br(), #Espacio de renglon
        html.Br(), html.Br(), #Espacio de renglon
    ])
])