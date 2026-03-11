from . import cursos
import forms
from flask import redirect, render_template, request, url_for
from models import db, Curso, Alumnos, Maestros
import forms
from sqlalchemy.orm import joinedload


@cursos.route('/listadoCursos')
def listadoCursos():
    create_form = forms.UserForm4(request.form)
    cursos_list = Curso.query.options(joinedload(Curso.maestro)).all()
    return render_template("cursos/listadoCursos.html", form=create_form, cursos=cursos_list)

@cursos.route("/agregarCursos", methods=['GET', 'POST'])
def agregarCursos():
    create_form = forms.UserForm4(request.form)
    if request.method == 'POST':
        nuevo_curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))
    return render_template("cursos/agregarCursos.html", form=create_form)


@cursos.route("/detallesCursos", methods=['GET'])
def detalles():
    id = request.args.get('id')
    curso = Curso.query.get(id)
    return render_template("cursos/detallesCursos.html", 
                           id=curso.id, 
                           nombre=curso.nombre, 
                           descripcion=curso.descripcion,
                           maestro_nombre=f"{curso.maestro.nombre}")

@cursos.route("/editarCursos", methods=['GET', 'POST'])
def editar():   
    create_form = forms.UserForm4(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        curso = Curso.query.get(id)
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id
        maestro_actual = f"{curso.maestro.nombre}"      
        return render_template("cursos/editarCursos.html", form=create_form, maestro_actual=maestro_actual)
    if request.method == 'POST':
        id = create_form.id.data
        curso = Curso.query.get(id)
        if curso:
            curso.nombre = create_form.nombre.data
            curso.descripcion = create_form.descripcion.data
            curso.maestro_id = create_form.maestro_id.data
            db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))

@cursos.route("/eliminarCursos", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm4(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        curso = Curso.query.get(id)
        if curso:
            create_form.id.data = curso.id
            create_form.nombre.data = curso.nombre
            create_form.descripcion.data = curso.descripcion
            
    if request.method == 'POST':
        id = create_form.id.data
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        if curso:
            db.session.delete(curso)
            db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))
    return render_template("cursos/eliminarCursos.html", form=create_form)

@cursos.route("/alumnosCursos")
def gestion():
    create_form=forms.UserForm2(request.form)
    id=request.args.get('id')
    curso = Curso.query.get(id)
    alumnos_curso = curso.alumnos
    alumnos_disponibles = Alumnos.query.filter(~Alumnos.cursos.any(Curso.id==id)).all()

    return render_template("cursos/alumnosCursos.html", form=create_form,alumnos_curso=alumnos_curso,alumnos_disponibles=alumnos_disponibles, curso=curso)

@cursos.route("/agregarAlumno")
def agregaralumno():
    id_alumno = request.args.get('alumno')
    id_curso = request.args.get('curso')

    alumno = Alumnos.query.get(id_alumno)
    curso = Curso.query.get(id_curso)

    if alumno and curso:
        curso.alumnos.append(alumno)
        db.session.commit()
    return redirect(url_for('cursos.gestion', id=id_curso))

@cursos.route("/eliminarAlumno")
def eliminaralumno():
    id_alumno = request.args.get('alumno')
    id_curso = request.args.get('curso')

    alumno = Alumnos.query.get(id_alumno)
    curso = Curso.query.get(id_curso)

    if alumno and curso:
        curso.alumnos.remove(alumno)
        db.session.commit()
    return redirect(url_for('cursos.gestion', id=id_curso))