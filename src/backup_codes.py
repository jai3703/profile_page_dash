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




import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_extensions as de
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Create a Dash app
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# Define the layout of the app

app_header = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("HOME", href="#")),
        dbc.NavItem(dbc.NavLink("PORTFOLIO", href="#")),
        dbc.NavItem(dbc.NavLink("CONTACT", href="#")),
        dbc.NavItem(dbc.NavLink("RESUME", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("P1", header=True),
                dbc.DropdownMenuItem("P2", href="#"),
                dbc.DropdownMenuItem("P3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="PROJECTS",
        ),
    ],
    brand="WELCOME",
    color="secondary",
    dark=True,
    style={'color':'black'}
)

url = 'https://lottie.host/3c1b3811-cf6d-4f69-aa88-095bf40f62ab/7kGlbm7O2I.json'
options = dict(loop=True, autoplay=True,width = '90%',height='50%')


home_page_background = dmc.Grid(
    [
        dmc.Col(
            [
                #dmc.Space(className='main-space', h=15),
                de.Lottie(url=url, options=options, isClickToPauseDisabled=True),
                dmc.Stack(
                    children=[
                        dmc.Title('A little bit about me..', style={'color': 'white'}, align='center'),
                        dmc.Center(
                            [
                                dmc.Text(
                                    children=[
                                        "I am Data scientist with specialization in Manufacturing Domain "
                                        "I am also equally passionate about Simulation and Optimization"
                                    ],
                                    style={'color': 'white', 'width': '50%'},
                                    align='center',
                                    id='main-text'
                                ),
                            ]
                        ),
                        dcc.Link(
                            [
                                dmc.Button(
                                    'Projects',
                                    id='start-btn',
                                    variant='outline',
                                    color='white',
                                    size='lg',
                                    uppercase=True,
                                    rightIcon=DashIconify(icon='ion:rocket-outline', width=30)
                                ),
                                
                            ],
                            href='#'
                        )
                    ],
                    align='center',
                    className='stack-left-container',
                    spacing=30,
                    mt=-170
                )
            ],
            md=12, lg=8
        ),
        dmc.Col(
            [
                dmc.Center(
                    className='right-container',
                    id='right-container',
                    children=[
                        dmc.Loader(
                            color="blue",
                            size="md",
                            variant="oval"
                        ),
                    ]
                ),
            ], md=12, lg=4
        ),
    ],
    id='home-grid',
    style={'backgroundColor':'#deddd8','height':'100vh'},
    className='hide'
)

app.layout = html.Div(children=[
    app_header,
    home_page_background
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
