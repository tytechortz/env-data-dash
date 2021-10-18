
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from homepage import Homepage
import time
from colorado_river import river_App

today = time.strftime("%Y-%m-%d")
print(today)

app = dash.Dash(name=__name__, 
                title="Environnmental Data Dashboard",
                assets_folder="static",
                assets_url_path="static")

application = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/den-temps':
        return temp_App()
    elif pathname == '/ice':
        return ice_App()
    elif pathname == '/colorado-river':
        return river_App()
    elif pathname == '/co2':
        return co2_App()
    else:
        return Homepage()






if __name__ == '__main__':
    application.run(debug=True, port=8050)