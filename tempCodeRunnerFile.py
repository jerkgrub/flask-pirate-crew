from flask import Flask, render_template, session, request, redirect, url_for
# from pirates import Pirate

app = Flask(__name__)
app.secret_key = "flaskProject"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
