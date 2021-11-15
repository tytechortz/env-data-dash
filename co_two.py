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

def co2_App():
    return html.Div([
        get_river_header(),
        get_nav_bar(),
        get_emptyrow(),
        html.Div([
            html.Div([
                html.H3('Atmospheric CO2 Concentration', style={'text-align': 'center'})
            ],
                className='row'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='co2-levels',
                        # figure=fig
                    ),
                ],
                    className='nine columns'
                ),
                html.Div([
                    html.Div(id='max-co2-layout'),
                    html.Div(id='current-co2-layout'),
                    html.Div(id='avg-co2-layout'),
                ],
                    className='three columns'
                ),
            ],
                className='row'
            ),
            html.Div([
                html.Div([
                    html.Div(id='co2-month-selector'),
                ],
                    className='two columns'
                ),
            ],
                className='row'
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='monthly-co2-levels',
                        # figure=fig
                    ),
                ],
                    className='nine columns'
                ),
            ],
                className='row'
            ),
            html.Div([
                dcc.Interval(
                    id='interval-component',
                    interval=60000,
                    n_intervals=0
                ),
            ]),
        ]),
        dcc.Store(id='CO2-data'),
        dcc.Store(id='CO2-month-data'),
    ])



app.layout = co2_App