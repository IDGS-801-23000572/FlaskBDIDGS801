from flask import Flask, redirect, render_template, request, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos
from config import DevelopmentConfig
import forms
from models import db, Alumnos

from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
