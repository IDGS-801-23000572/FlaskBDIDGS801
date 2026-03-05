from flask import Flask, redirect, render_template, request, url_for

from flask import g
from . import alumnos
import forms
from models import db, Alumnos


@alumnos.route('/listadoAlumn')
def listadoAlumn():
	create_formn=forms.UserForm2(request.form)
	alumnos=Alumnos.query.all()
	return render_template("/alumnos/listadoAlumn.html", form=create_formn, alumn=alumnos)

@alumnos.route("/agregarAlumnos", methods=['GET','POST'])
def agergarAlumnos():
	create_form=forms.UserForm2(request.form)
	if request.method== 'POST':
		alum=Alumnos(nombre=create_form.nombre.data,
			   		apellidos=create_form.apellidos.data,
					email=create_form.email.data,
					telefono=create_form.telefono.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for("alumnos.listadoAlumn"))
	return render_template("alumnos/agregarAlumnos.html", form=create_form)

@alumnos.route("/detallesAlumnos")
def detalles():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono = alum1.telefono
	return render_template("alumnos/detallesAlumnos.html",id=id, nombre=nombre, apellidos=apellidos, email=email, telefono = telefono)

@alumnos.route("/editarAlumnos", methods=['GET','POST'])
def editar():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(alum1.nombre)
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
	if request.method== 'POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id=id
		alum1.nombre=str.rstrip(create_form.nombre.data)
		alum1.apellidos=create_form.apellidos.data
		alum1.email=create_form.email.data
		alum1.telefono=create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for("alumnos.listadoAlumn"))
	return render_template("alumnos/editarAlumnos.html", form=create_form)

@alumnos.route("/eliminarAlumnos", methods=['GET','POST'])
def eliminar():
	create_form=forms.UserForm2(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.email.data = alum1.email
			create_form.telefono.data = alum1.telefono
			return render_template("alumnos/eliminarAlumnos.html", form=create_form)
	if request.method == 'POST':
		id = create_form.id.data
		alum  = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		if alum:
			db.session.delete(alum)
			db.session.commit()
		return redirect(url_for('alumnos.listadoAlumn'))
	return render_template("alumnos/eliminarAlumnos.html", form=create_form)
