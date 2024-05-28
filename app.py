import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
import dash_auth

USER_PASS_MAPPING={
    "admin": "password123"
}

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server
auth = dash_auth.BasicAuth(app, USER_PASS_MAPPING)

navbar = dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
    ),
    brand="BROADCAST DASHBOARD",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        dcc.Link(
            html.Div(id="navbar-brand", children=[dbc.NavbarBrand("BROADCAST DASHBOARD")]),
            href="/"
        ),
        dbc.Row(
            [
                dbc.Col(navbar, width={"size": 12, "offset": 0, "order": 1}),
            ],
            className="g-0",
        ),
        dash.page_container
    ],
    fluid=True,
)

# Load custom CSS file
external_css = ["assets/custom.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server()
