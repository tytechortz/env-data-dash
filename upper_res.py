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
                        html.H6(children='Drought'),
                        href='/drought'
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

def ur_App():
    return html.Div([
        get_river_header(),
        get_nav_bar(),
        get_emptyrow(),
        html.Div([
            html.H3('Upper Colorado River Reservoir Storage', style={'text-align': 'center'})
        ],
            className='row'
        ),
        html.Div([
            html.Div([
                dcc.Graph(
                    id='bm-levels',
                ),
            ],
                className='four columns'
            ),
            html.Div([
                dcc.Graph(
                    id='navajo-levels',
                ),
            ],
                className='four columns'
            ),
            html.Div([
                dcc.Graph(
                    id='fg-levels',
                ),
            ],
                className='four columns'
            ),

        ],
            className='row'
        ),
        dcc.Interval(
        id='interval-component',
        interval=500*1000, # in milliseconds
        n_intervals=0
        ),
        dcc.Store(id='blue-mesa-water-data'),
        dcc.Store(id='navajo-water-data'),
        dcc.Store(id='fg-water-data'),
        dcc.Store(id='ur-water-data'),
    ])

app.layout = ur_App