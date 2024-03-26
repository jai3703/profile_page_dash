# import required libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_extensions as de
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Create a Dash app
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY])

#Instatntiate server
server = app.server

# Define the layout of the app

navigation_bar = dbc.NavbarSimple(
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
    color="primary",
    dark=True,
    fluid=True
)

intro_banner = html.Div(style={ 'background-image': 'radial-gradient(600px at 357px 3406px, rgba(29, 78, 216, 0.15), transparent 80%)', 
                             'background-size': 'cover', 'background-repeat': 'no-repeat',
                             'background-position': 'center', 'height': '80vh'},
                      children=[
                          dmc.Center(
                              style={"height": "100%", "width": "100%"},
                              children=[
                                  dmc.Blockquote(
                                      "Everything we hear is an opinion, not a fact. "
                                      "Everything we see is a perspective, not the truth.",
                                      cite="- Marcus Aurelius , Meditations",
                                      ),
                                  dmc.Anchor("Click now!", href="https://mantine.dev/"),
                                  ],
                                  )
                                  ]
                                  )

left_card =dbc.Card(
    [ dbc.CardBody(
            [   html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H5("Hello, I am", className="card-title"),
                
                html.H1(html.B("Jai Kumar Pandey")),
                html.P([
                    html.H4("Data Scientist"),
                    html.Br(),
                    "I primarily work on complex manufacturing related data and develop end to end solutions.",
                    html.Br(),
                    "I also have strong interest and grasp on optimization"
                     " and simulation techniques and have used a combination of both to solve network optimization problems."] ,
                    className="card-text",
                ),
            ],
            style={"height":'100%', 'display':'inline',
                   'align-items':'center','whiteSpace': 'pre-wrap',
                   'color':'white',
                   'fontFamily':'inter'
                   #'justify-content':'center'
                   }
        ),
    ],
    style={"height":'100%',
           'display':'flex' ,
           'align-items':'center', 
           'justify-content':'center',
           'backgroundColor':'#0f172a'},
)

right_card =dbc.Card(
    [
        dbc.CardImg(src="/assets/profile_pic.jpg",top=False)
    ],
    style={"height":'100%'},
)

custom_layout_trial = dbc.Container(
    children= [
        dbc.Row(children=[
            dbc.Col(width=8,
                    children=[left_card]),
            dbc.Col(width=4,children=[right_card])
        ])
    ],
    style={'height':'100vh'},
    fluid=True
)
app.layout = html.Div(children=[
    navigation_bar,
    html.Hr(),
    custom_layout_trial
    #intro_banner
],style={'backgroundColor':'#0f172a'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
