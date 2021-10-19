import dash
from dash import html
from dash import dcc
from colorado_river import get_river_header, get_nav_bar, get_emptyrow

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True

def ur_App():
    return html.Div([
        get_river_header(),
        get_nav_bar(),
        get_emptyrow(),
    ])

app.layout = ur_App