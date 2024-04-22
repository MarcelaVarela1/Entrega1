import dash #Se importa la libreria de Dash
from dash import html
import dash_bootstrap_components as dbc
import math
from dash.dependencies import Input, Output


#se importa el front 
from fronted.fronted import layout
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout


@app.callback(
    Output('ResultadoOperacion', 'children'),
    [Input('EntradaCohesion', 'value'),
     Input('EntradaSobreCarga', 'value'),
     Input('EntradaBase', 'value'),
     Input('EntradaPesoEspecifico', 'value'),
     Input('EntradaAnguloFriccion', 'value'),
     Input('cimentacion-radio', 'value')]
)


def update_output(EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion, selected_value):
   
    if None in (EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion, selected_value):
        return "Por favor, complete todos los campos para calcular la carga última del suelo."

    try:
        EntradaCohesion = float(EntradaCohesion)
        EntradaSobreCarga = float(EntradaSobreCarga)
        EntradaBase = float(EntradaBase)
        EntradaPesoEspecifico = float(EntradaPesoEspecifico)
    except ValueError:
        return "Por favor, asegúrese de que todos los campos numéricos contienen valores válidos."

    if selected_value == 'corrida':
        resultado1 = (float(EntradaCohesion)*1)+(float(EntradaSobreCarga)*1)+(0.5*float(EntradaBase)*float(EntradaPesoEspecifico)*1)
    elif selected_value == 'cuadrada':
        resultado1 = 1.3*float(EntradaCohesion)*1+float(EntradaSobreCarga)*1+0.3*float(EntradaBase)*float(EntradaPesoEspecifico)*1 # operación
    elif selected_value == 'circular':
        resultado1 = 1.3*float(EntradaCohesion)*1+float(EntradaSobreCarga)*1+0.4*float(EntradaBase)*float(EntradaPesoEspecifico)*1   #operación
    else:
        resultado1 = None

    return 'La Carga ultima del suelo cimentación diseñada es: ' + str(resultado1)



if __name__ =='__main__':
    app.run_server(debug=True)
    