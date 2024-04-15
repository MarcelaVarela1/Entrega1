import dash
from dash import html
import dash_bootstrap_components as dbc


#se importa el front 
from fronted.fronted import layout
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

if __name__ =='__main__':
    app.run_server(debug=True)