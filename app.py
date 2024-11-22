from flask import Flask, render_template
import pandas as pd

file_weapons = pd.read_csv('./weapons.csv')


app = Flask(__name__)

@app.route("/")
def index():
    weapons_list = file_weapons.to_dict(orient='records')
    return render_template("./index.html", result=weapons_list)


if __name__ == "__main__":
    app.run(debug=True)