from flask import Flask, render_templates

app = Flask(__name__)
app.secret_key = "replace later"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_templates("index.html")


if __name__ = "__main__":
    app.run(debug=True)