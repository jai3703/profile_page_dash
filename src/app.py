import dash
from dash import dcc
from dash import html

# Create a Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='My Portfolio'),

    # Navigation bar
    html.Div(children=[
        html.Div(children='Home'),
        html.Div(children='About'),
        html.Div(children='Projects'),
        html.Div(children='Contact'),
    ]),

    # Main content area
    html.Div(children=[
        html.Div(children=[
            html.H2(children='About Me'),
            html.P("Welcome to my portfolio website. I'm passionate about data science and web development."),
            html.P("I have experience in Python, machine learning, web development, etc."),
        ]),

        html.Div(children=[
            html.H2(children='My Projects'),
            # Placeholder for project cards or links
        ]),

        html.Div(children=[
            html.H2(children='Contact Me'),
            html.P("Feel free to reach out to me via email at example@example.com."),
        ]),
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
