import dash
from dash import html
from dash import dcc
from colorado_river import get_river_header, get_emptyrow
import requests


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True

def get_nav_bar():
    navbar = html.Div([
        html.Div([
            html.Div([], className='col-2'),
            html.Div([
                dcc.Link(
                    html.H6(children='Home'),
                    href='/homepage'
                )
            ],
                className='col-2',
                style={'text-align': 'center'}
            ),
            html.Div([], className = 'col-2')
        ],
            className = 'row',
            style = {'background-color' : 'dark-green',
                    'box-shadow': '2px 5px 5px 1px rgba(0, 100, 0, .5)'}
        ),
    ])

    return navbar
def get_snow_header():

    header = html.Div([

        # html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.H2(
                'Colorado Snowpack Data',
                className='twelve columns',
                style={'text-align': 'center'}
            ),
        ],
            className='row'
        ),
    ])

    return header

def snow_App(): 
    return html.Div([
        get_snow_header(),
        get_nav_bar(),
        html.Div([
            html.H3('STUFF')
        ],
            className='row'
        ),
]) 

app.layout = snow_App