import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Page registration
dash.register_page(__name__, path='/', name="bar-graph")

data = pd.read_csv('data.csv')

layout = html.Div([
    html.H1('Bar Graph Page'),
    html.Label('Filter by Gender:'),
    dcc.Dropdown(
        id='gender-dropdown',
        options=[{'label': g, 'value': g} for g in data['gender'].unique()],
        value='All'
    ),
    dcc.Graph(id='bar-graph')
])

@callback(
    Output('bar-graph', 'figure'),
    [Input('gender-dropdown', 'value')]
)
def update_bar(gender):
    if gender == 'All':
        filtered_data = data
    else:
        filtered_data = data[data['gender'] == gender]
    
    fig = px.bar(filtered_data, x="country", y="duration", color="gender")
    return fig