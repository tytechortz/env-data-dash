import dash
from dash import html
from dash import dcc
from colorado_river import get_river_header, get_emptyrow

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
        html.Div([
            html.Div([
                html.Div([
                    dcc.Link(
                        html.H6(children='Mead and Powell'),
                        href='/colorado-river'
                    )
                ],
                    className='six columns',
                    style={'text-align': 'center'}
                ),
                html.Div([
                    dcc.Link(
                        html.H6(children='Upper Reservoirs'),
                        href='/ur'
                    )
                ],
                    className='six columns',
                    style={'text-align': 'center'}
                ),
            ],
                className='twelve columns'
            ),
        ],
            className = 'row',
                style = {'background-color' : 'dark-green',
                        'box-shadow': '2px 5px 5px 1px rgba(0, 100, 0, .5)'}
        ),

    ])

    return navbar

def get_temp_header():

    header = html.Div([

        # html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.H2(
                'Denver Climate Data',
                className='twelve columns',
                style={'text-align': 'center'}
            ),
        ],
            className='row'
        ),
    ])

    return header

def dt_App():
    return html.Div([
        get_temp_header(),
        get_nav_bar(),
        get_emptyrow(),
        html.Div([
            html.H3('Denver Central Park Climate Data', style={'text-align': 'center'})
        ],
            className='row'
        ),
        dcc.Interval(
            id='interval-component',
            interval=500*1000, # in milliseconds
            n_intervals=0
        ),
        dcc.Store(id='temp-data'),
])

app.layout = dt_App