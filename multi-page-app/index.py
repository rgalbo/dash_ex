from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from app import server

from dashboards import home, dash1, dash2


app.layout = html.Div(
    [dcc.Location(id='url', refresh=False), html.Div(id='page-content')]
)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash1':
        return dash1.layout
    elif pathname == '/dash2':
        return dash2.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
