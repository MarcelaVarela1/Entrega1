import dash
from dash import html
import dash_bootstrap_components as dbc
import math
from dash.dependencies import Input, Output


#se importa el front 
from fronted.fronted import layout
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout


@app.callback(
    Output('ResultadoOperacion' , 'children'),
    Input('EntradaCohesion', 'value'),
    Input('EntradaSobreCarga', 'value'),
    Input('EntradaBase', 'value'),
    Input('EntradaPesoEspecifico', 'value'),
    Input('EntradaAnguloFriccion', 'value'),
)

def Calculoq(EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion):
    # Check if any of the inputs are None
    if None in (EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion):
        return "Error: Ingrese todos los datos"
       
    resultado = EntradaCohesion * EntradaSobreCarga * EntradaBase * EntradaPesoEspecifico * EntradaAnguloFriccion
    return 'La sobre carga es: ' + str(resultado)

    
if __name__ =='__main__':
    app.run_server(debug=True)
    