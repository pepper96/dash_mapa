import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

import dash
from dash import html,dcc 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv")
de_para = pd.read_csv("https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/estados.csv")

df=pd.merge(df,de_para[["codigo_uf","uf","regiao"]],left_on="codigo_uf",right_on="codigo_uf",how='left')

cores = {
        'Norte': 'rgb(0, 0, 255)',
        'Nordeste': 'rgb(255, 0, 0)',
        'Centro-Oeste': 'rgb(247, 186, 84)',
        'Sudeste': 'rgb(255, 255, 0)',
        'Sul': 'rgb(255, 0, 255)'
    }


#============Layout=================
app.layout = html.Div(children=[
    html.H5("Distribuição de Municípios",className='center-content'),
    dcc.Graph(id='mapa',style={'width':'100%','height':'100vh','margin':0,"padding":0})
], style={'backgroundColor': 'black'})


#===================================================
@app.callback(Output('mapa','figure'),[Input('mapa','id')])
def plota_grafico(_):
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", text='nome', color="regiao",
                            color_discrete_map=cores, size_max=10, zoom=2.3, mapbox_style="carto-darkmatter")

    fig.update_layout(
        legend=dict(font=dict(color='white')),
        plot_bgcolor="rgb(0,0,0)",
        paper_bgcolor="rgb(0,0,0)",
        title_text="Distribuição de Municípios",
        title_font=dict(color='white'))
    
    return fig

#============Runserver===========#
if __name__=='__main__':
    app.run_server(port=8050,debug=True)