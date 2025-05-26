from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/verbs")
def verbs():
    return render_template("pages/verbs/index.html")


@app.route("/flashcards")
def flashcards():
    return render_template("pages/flashcards.html")


@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)


@app.route("/data/<path:path>")
def data_files(path):
    return send_from_directory("data", path)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
    
