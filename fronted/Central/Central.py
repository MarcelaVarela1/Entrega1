import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

Central = dbc.Container([
    dbc.Row([
        dbc.Col(

            html.Div([
    html.H2("Seleccione tipo de Cimentación a diseñar:", style={'text-align': 'center'}),
    html.Br(), html.Br(),
    
    dcc.RadioItems(   id='cimentacion-radio',
            options=[
            {'label': 'Cimentación Corrida', 'value': 'corrida'},
       
            {'label': 'Cimentación Cuadrada', 'value': 'cuadrada'},
           
            {'label': 'Cimentación Circular', 'value': 'circular'},
            
        ],
        value='corrida'  # Valor predeterminado seleccionado
              
        ),
        html.Div(id='output')
])
                                          
                ,md=4,style={'background-color':'#F0FFF0'}),
        
        dbc.Col(
            html.Div([
    html.H2("Formula metodo Terzagui", style={'text-align': 'center'}),
    html.H3("Cimentación Corrida", style={'text-align': 'center'}),
    html.P("qu= C*Nc+q*Nq+1/2*B*γ*Nγ", style={'text-align': 'center'}),

    html.H3("Cimentación Cuadrada", style={'text-align': 'center'}),
    html.P("qu= 1.3*C*Nc+q*Nq+0.3*B*γ*Nγ", style={'text-align': 'center'}),

    html.H3("Cimentación Circular", style={'text-align': 'center'}),
    html.P("qu= 1.3*C*Nc+q*Nq+0.4*B*γ*Nγ", style={'text-align': 'center'}),
 ])
            
            ,md=4,style={'background-color':'#F0FFF0'}),

        dbc.Col('Imagenes referencia de tipo de cimentación', md= 4, style={'background-color':'#F0FFF0'}),
        
    ])
])