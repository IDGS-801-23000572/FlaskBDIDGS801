from flask import Flask, render_template
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g

from config import DevelopmentConfig
import forms
from models import db, Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.route("/alumnos")
def alumnos():
	return render_template("alumnos.html")

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
