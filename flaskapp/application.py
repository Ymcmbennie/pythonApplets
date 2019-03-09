from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Benson right"

@app.route("/dilara")
def dilara():
    return "Benson found Dilara"