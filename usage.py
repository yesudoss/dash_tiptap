import dash_tiptap
import dash
from dash import html, Input, Output

app = dash.Dash(__name__)

mentions = [
    {'id': '1', 'label': 'Phillipp Kühn'},
    {'id': '2', 'label': 'Hans Pagel'},
    {'id': '3', 'label': 'John Doe'},
    {'id': '4', 'label': 'Jacob'},
    {'id': '5', 'label': 'Patrick'},
    {'id': '6', 'label': 'Dixon'},
    {'id': '7', 'label': 'Jason'},
    {'id': '8', 'label': 'Monte'},
    {'id': '9', 'label': 'Nicholas'},
    {'id': '10', 'label': 'Yesu'},
    {'id': '11', 'label': 'John Mathew'},
]

app.layout = html.Div([
    html.H1("Dash Tiptap Mention Component Demo"),
    dash_tiptap.DashTiptap(
        id='input',
        value='<p>Hello!</p>',
        mentions=mentions
    ),
    html.H2("Output"),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return value

if __name__ == '__main__':
    app.run(debug=True, port=8051)