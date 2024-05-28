import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Page registration
dash.register_page(__name__, path='/pie-chart', name="pie-chart")

data = pd.read_csv('data.csv')

layout = html.Div([
    html.H1('Pie Chart Page'),
    html.Label('Filter by Sport:'),
    dcc.Dropdown(
        id='sport-dropdown',
        options=[{'label': s, 'value': s} for s in data['game'].unique()],
        value='All'
    ),
    dcc.Graph(id='pie-chart')
])

@callback(
    Output('pie-chart', 'figure'),
    [Input('sport-dropdown', 'value')]
)
def update_pie(sport):
    if sport == 'All':
        filtered_data = data
    else:
        filtered_data = data[data['game'] == sport]


    fig = px.pie(filtered_data, values='duration', names='country', title='Duration by Country')
    return fig