from flask import Flask, render_template, request
from pandas import DataFrame
from random import randint


app = Flask(__name__)
app.df = DataFrame({
    'Name': ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h'),
    'Rating': (randint(0, 100) for _ in range(11)),
})


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/data-slider")
def data_slider():
    df = app.df
    lower_limit = int(request.values.get('lower_limit', df['Rating'].mode()))
    filtered = df[df['Rating'] >= lower_limit]
    return render_template(
        "data-slider.html",
        lower_limit=lower_limit,
        df_table=filtered.to_html(),
        minimum=df["Rating"].min(),
        maximum=df["Rating"].max(),
        total=filtered.shape[0],
    )


if __name__ == '__main__':
    app.run(debug=True)
