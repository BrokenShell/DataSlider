from flask import Flask, render_template, request
from pandas import DataFrame


app = Flask(__name__)

# placeholder data
DATA = DataFrame({
    'Name': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    'Rating': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
})


def custom_filter(slider_value: str) -> DataFrame:
    """ Filter for specifying data """
    rate = int(slider_value)
    return DATA[DATA['Rating'] >= rate]


@app.route("/")
@app.route("/index")
def index():
    """ Standard index """
    return render_template("index.html")


@app.route("/data-slider")
@app.route("/data-slider", methods=['GET'])
def data_slider():
    """ Recursive GET """
    val = request.args.get('val')
    if val is not None:
        return render_template(
            "data-slider.html", val=val, find=custom_filter)
    else:
        return render_template("data-slider.html")


if __name__ == '__main__':
    app.run(debug=True)
