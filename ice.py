import dash
from dash import html
from dash import dcc
from colorado_river import get_river_header, get_emptyrow

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True

def get_ice_header():

    header = html.Div([
        html.Div([
            html.H3('Arctic Sea Ice Data', style={'text-align': 'center'})
        ],
            className='row'
        ),
        html.Div(id='date-title'),
    ])

    return header

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



def ice_App():
    return html.Div([
        get_ice_header(),
        get_nav_bar(),
        get_emptyrow(),
    ])

app.layout = ice_App