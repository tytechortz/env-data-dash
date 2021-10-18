import dash
from dash import html
from dash import dcc
import pandas as pd
import time
import json
import requests
from datetime import datetime, date


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True

capacities = {'Lake Powell Glen Canyon Dam and Powerplant': 24322000, 'Lake Mead Hoover Dam and Powerplant': 26134000, 'FLAMING GORGE RESERVOIR': 3788700, 'NAVAJO RESERVOIR': 1708600, 'BLUE MESA RESERVOIR': 940800, 'Powell Mead Combo': 50456000, 'UR': 6438100}

def get_river_header():

    header = html.Div([

        # html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.H2(
                'Colorado River Water Storage',
                className='twelve columns',
                style={'text-align': 'center'}
            ),
        ],
            className='row'
        ),
    ])

    return header

def get_emptyrow(h='15px'):
    """This returns an empty row of a defined height"""

    emptyrow = html.Div([
        html.Div([
            html.Br()
        ], className = 'col-12')
    ],
    className = 'row',
    style = {'height' : h})

    return emptyrow

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
                        html.H6(children='Upper Reservoirs'),
                        href='/ur'
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
    

def river_App():
    return html.Div([
        get_river_header(),
        get_nav_bar(),
        get_emptyrow(),
        html.Div([
            html.Div([
                dcc.Loading(
                id="loading-powell",
                type="default",
                children=html.Div(dcc.Graph(id='powell-levels'))),
            ],
                className='four columns'
            ),
            html.Div([
                dcc.Loading(
                id="loading-mead",
                type="default",
                children=html.Div(dcc.Graph(id='mead-levels'))),
            ],
                className='four columns'
            ),
            html.Div([
                dcc.Loading(
                id="loading-combo",
                type="default",
                children=html.Div(dcc.Graph(id='combo-levels'))),
            ],
                className='four columns'
            ),
        ],
            className='row'
        ),
    ])

app.layout = river_App