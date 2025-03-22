from flask import Flask
app = Flask(__name__)
@app.route('/<name>')
def index(Chris):
    return '<h1>Hola {}!<h1>' . format (name)