import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', name="Benson Sanga")

@app.route("/dilara")
def dilara():
    return render_template('index.html', name=datetime.datetime.now())

@app.route("/forloop")
def forloop():
    names=["benson", "dilara", "beril", "gizem"]
    return render_template('index02.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)