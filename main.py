import io
from base64 import b64encode

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


def main():
    app = Dash(__name__)

    buffer = io.StringIO()

    df = pd.read_csv("data/sale.csv")

    fig = px.bar(
        df,
        x="date",
        y="sales",
        # color="smoker",
        barmode="group",
        facet_row="area",
        facet_col="weekday",
        category_orders={"weekday": df["weekday"].unique().tolist(), "area": df["area"].unique().tolist()},
    )

    fig.write_html(buffer)

    html_bytes = buffer.getvalue().encode()
    encoded = b64encode(html_bytes).decode()

    app.layout = html.Div(
        [
            dcc.Graph(id="graph", figure=fig),
        ]
    )

    fig.write_html("html/viewer.html")
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
