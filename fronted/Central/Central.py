import dash
from dash import html,dcc
import dash_bootstrap_components as dbc





Central = dbc.Container([
    dbc.Row([
        dbc.Col(

            html.Div([
    html.H2("Seleccione tipo de Cimentación a diseñar:"),
    dcc.RadioItems(['Cimentación Corrida', 'Cimentación Cuadrada' , 'Cimentación Circular']
        ),

])
                
                          
                ,md=4,style={'background-color':'#F0FFF0'}),
        
        dbc.Col(
            html.Div([
    html.H2("Formula metodo Terzagui"),
    html.H3("Cimentación Corrida"),
    html.P("qu= C*Nc+q*Nq+1/2*B*γ*Nγ"),

    html.H3("Cimentación Cuadrada"),
    html.P("qu= 1.3*C*Nc+q*Nq+0.3*B*γ*Nγ"),

    html.H3("Cimentación Circular"),
    html.P("qu= 1.3*C*Nc+q*Nq+0.4*B*γ*Nγ"),
 ])
            
            ,md=4,style={'background-color':'#F0FFF0'}),

        dbc.Col('Imagenes referencia de tipo de cimentación', md= 4, style={'background-color':'#F0FFF0'}),
        
    ])
])