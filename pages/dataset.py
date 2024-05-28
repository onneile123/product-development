import pandas as pd
import dash
from dash import html, dash_table, dcc, callback
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Page registration
dash.register_page(__name__, path='/dataset', name="dataset")

df = pd.read_csv('data.csv')

# Page layout (goes under the page container in the dash_app.py)
layout = html.Div(
    children=[
        html.H3("dataset page"),
        dcc.Dropdown(
            id='duration-sort', options=['Ascending', 'Descending'], value='Ascending'),
        dcc.Graph(id='table', figure={})
])

@callback(
    Output('table', 'figure'),
    [Input('duration-sort', 'value')]
)
def update_table(sort):
    if sort == 'Ascending':
        df_sorted = df.sort_values(by='duration')
    else:
        df_sorted = df.sort_values(by='duration', ascending=False)

    fig = go.Figure(
    data=[
        go.Table(
            header=dict(values=list(df_sorted.columns),
                        fill_color='white',
                        font=dict(color='black', size=12),
                        align='left'),
            cells=dict(values=[df_sorted[col] for col in df_sorted.columns],
                       fill_color='white',
                       font=dict(color='black', size=10),
                       align='left'))
    ],
    layout=go.Layout(width=1450,height=600))
    return fig