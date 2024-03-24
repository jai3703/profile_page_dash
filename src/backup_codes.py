html.Div(children=[
    dbc.Row(children=[
        dbc.Col(width=4,children=[html.Font('JAI PANDEY',style={'margin-left': '100px'})]),
        dbc.Col(width=6,children=[html.Ul(children = [
            html.Li(html.A('HOME',href='#')),
            html.Br(),
            html.Li(html.A('PORTFOLIO',href='#')),
            html.Li(html.A('CONTACT',href='#')),
            html.Li(html.A('Resume',href='#'))
            ],style= {'display':'flex','list-style-type': 'none','margin-inline': '35px'}),
            ]),
    ],style = {'font-size': '90%',
    'font-weight': '400',
    'letter-spacing': '1px',
    'color': 'black',
    'margin-inline': '35px',
    'font-family': 'Montserrat',
    'list-style-type': 'none',
    'display':'flex'
    }
    )
], 
style={'background-color': '#dde0db', 'padding': '10px 0'})