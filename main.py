from flask import Flask, render_template, url_for, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)