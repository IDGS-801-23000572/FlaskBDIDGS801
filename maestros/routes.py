from . import maestros
import forms
from flask import Flask, redirect, render_template, request, url_for
from models import db, Maestros

		
@maestros.route('/perfil/<nombre>')
def perfil(nombre):
	return f"Perfil de {nombre}"

@maestros.route('/listadoMaes')
def listadoMaes():
	create_formn=forms.UserForm3(request.form)
	maestros=Maestros.query.all()
	return render_template("/maestros/listadoMaes.html", form=create_formn, maes=maestros)

@maestros.route("/agregarMaestros",methods=['GET','POST'])
def agergarMaestros():
    create_form=forms.UserForm3(request.form)
    if request.method== 'POST':
        maes=Maestros(nombre=create_form.nombre.data,
                    apellidos=create_form.apellidos.data,
                    especialidad=create_form.especialidad.data,
                    email=create_form.email.data)
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.listadoMaes'))
    return render_template("maestros/agregarMaestros.html", form=create_form)

@maestros.route("/detallesMaestros", methods=['GET','POST'])
def detalles():
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula')
		nombre=maes1.nombre
		apellidos=maes1.apellidos
		especialidad = maes1.especialidad
		email=maes1.email
	return render_template("maestros/detallesMaestros.html",matricula=matricula, nombre=nombre, apellidos=apellidos,especialidad=especialidad ,email=email)

@maestros.route("/editarMaestros", methods=['GET','POST'])
def editar():	
	create_form=forms.UserForm3(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=str.rstrip(maes1.nombre)
		create_form.apellidos.data=maes1.apellidos
		create_form.especialidad.data=maes1.especialidad
		create_form.email.data=maes1.email
	if request.method== 'POST':
		matricula=create_form.matricula.data
		maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maes1.matricula=matricula
		maes1.nombre=str.rstrip(create_form.nombre.data)
		maes1.apellidos=create_form.apellidos.data
		maes1.especialidad=create_form.especialidad.data
		maes1.email=create_form.email.data
		db.session.add(maes1)
		db.session.commit()
		return redirect(url_for('maestros.listadoMaes'))
	return render_template("maestros/editarMaestros.html", form=create_form)

@maestros.route("/eliminarMaestros", methods=['GET','POST'])
def eliminar():
	create_form=forms.UserForm3(request.form)
	if request.method == 'GET':
		matricula = request.args.get('matricula')
		maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes:
			create_form.matricula.data = maes.matricula
			create_form.nombre.data = maes.nombre
			create_form.apellidos.data = maes.apellidos
			create_form.especialidad.data = maes.especialidad
			create_form.email.data = maes.email
			return render_template("maestros/eliminarMaestros.html", form=create_form)
	if request.method == 'POST':
		matricula = create_form.matricula.data
		maes= db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes:
			db.session.delete(maes)
			db.session.commit()
		return redirect(url_for('maestros.listadoMaes'))
	return render_template("maestros/eliminarMaestros.html", form=create_form)
