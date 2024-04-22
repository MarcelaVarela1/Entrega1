import dash #Se importa la libreria de Dash
from dash import html # Importa el módulo html de Dash para poder utilizar etiquetas HTML.
import dash_bootstrap_components as dbc # Importa Dash Bootstrap Components que proporciona componentes basados en Bootstrap para Dash.

# Se define un contenedor.
Definiciones = dbc.Container([
    dbc.Row([ # Se Crea una fila usando.Las filas son usadas para agrupar horizontalmente columnas.
        dbc.Col(
            html.Div([ # Se crea un contenedor genérico que en este caso contiene un título.
    html.H1("CONCEPTOS IMPORTANTES"), # Título principal
    html.H3("Cohesión"), # Subtítulo para el tema de cohesión.
     # Párrafo explicativo sobre qué es la cohesión en suelos.
    html.P("La cohesión en suelos es una propiedad que describe la capacidad de las partículas de suelo para mantenerse unidas o adherirse entre sí."),
    html.H3("Sobre Carga"),# Subtítulo para el tema de sobre carga.
    # Párrafo explicativo sobre qué es la sobrecarga en suelos.
    html.P("La sobrecarga en suelos se refiere a la presión adicional ejercida sobre el suelo que puede afectar su comportamiento geotécnico"),
    html.H3("Peso Específico γ"), # Subtítulo para el peso específico.
    # Párrafo explicativo sobre el peso específico del suelo.
    html.P("El peso específico del suelo, también conocido como peso unitario o densidad del suelo, es una medida de la masa de un determinado volumen de suelo.  Se expresa en unidades de peso por unidad de volumen, generalmente en kN/m³"),
    # Subtítulo para el tema de sobre ancho.
    html.H3("B"),
    html.P("Ancho Zapata"),
    html.H3("Factores de Capacidad de Carga"),
    # Párrafos explicativos detallando cada factor y su relevancia.
    html.P("Son coeficientes que se utilizan en la ecuación de capacidad de carga última de suelos para determinar la capacidad de carga de una cimentación en una masa de suelo."),
    html.P("Nc (Factor de capacidad de carga por cohesión): Este factor se relaciona con la cohesión del suelo. "),
    html.P("Nq (Factor de capacidad de carga por presión neta): Este factor se refiere a la presión neta del suelo sobre la cimentación. "),
    html.P("Nγ (Factor de capacidad de carga por peso unitario): Este factor se relaciona con el peso unitario del suelo sobre la cimentación."),
    html.H3("Ángulo de fricción Φ"),# Subtítulo para el ángulo de fricción.
    # Párrafo explicativo sobre qué es el ángulo de fricción y su importancia.
    html.P("Este ángulo se define como el ángulo de inclinación máxima a la cual una superficie de suelo puede soportar una carga sin que se produzca un deslizamiento o falla. Es un indicador de la fricción entre las partículas del suelo, y su valor está influenciado por las propiedades de los materiales del suelo, como el tamaño y la forma de las partículas, la compactación y el contenido de humedad."),


            ])
            
            , md= 12, style={'background-color':'#F0FFFF'}),
       

        
    ])
])