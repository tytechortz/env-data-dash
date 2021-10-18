import dash
from dash import html
import dash_core_components as dcc
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

def river_App():
    return get_river_header()