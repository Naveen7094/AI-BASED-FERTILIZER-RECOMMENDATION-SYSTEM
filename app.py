from flask import Flask, render_template, request
from model import recommend_fertilizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fertilizer = ""
    if request.method == "POST":
        n = int(request.form["nitrogen"])
        p = int(request.form["phosphorus"])
        k = int(request.form["potassium"])

        fertilizer = recommend_fertilizer(n, p, k)

    return render_template("index.html", result=fertilizer)

if __name__ == "__main__":
    app.run(debug=True)
