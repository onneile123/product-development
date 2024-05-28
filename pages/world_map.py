import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Page registration
dash.register_page(__name__, path='/world-map', name="world-map")

data = pd.read_csv('data.csv')

layout = html.Div([
    html.H1('Map Page'),
    html.Label('Filter by Gender:'),
    dcc.Dropdown(
        id='gender-dropdown',
        options=[{'label': g, 'value': g} for g in data['gender'].unique()],
        value='All'
    ),
    dcc.Graph(id='map-graph')
])

@callback(
    Output('map-graph', 'figure'),
    [Input('gender-dropdown', 'value')]
)
def update_map(gender):
    if gender == 'All':
        filtered_data = data
    else:
        filtered_data = data[data['gender'] == gender]
    
    fig = px.choropleth(filtered_data, locations="country", 
                        color="age", hover_name="country", 
                        color_continuous_scale="Viridis", 
                        scope="world", 
                        labels={'age': 'Age'})
    fig.update_layout(legend_title_text='Gender')
    return fig