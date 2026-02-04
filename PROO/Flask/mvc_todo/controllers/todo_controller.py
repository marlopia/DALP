from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import TodoService, ValidationError

todo_bp = Blueprint("todo", __name__)

# Repositorio en memoria (para el ejercicio). En un proyecto real lo inyectarías.
service = TodoService()


@todo_bp.get("/")
def index():
    items = service.repo.list_all()
    complete = service.total_complete()
    return render_template("index.html", items=items, complete=complete)


@todo_bp.get("/nuevo")
def new_form():
    return render_template("todo_form.html")


@todo_bp.post("/nuevo")
def create():
    title = request.form.get("title", "")
    priority = request.form.get("priority", "")
    try:
        service.create_todo(title, priority)
        flash("Tarea creada ✅", "success")
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return render_template("todo_form.html", title=title, priority=priority), 400


@todo_bp.post("/toggle/<int:index>")
def toggle(index: int):
    try:
        service.toggle_todo(index)
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return redirect(url_for("todo.index")), 400


@todo_bp.post("/delete/<int:index>")
def delete(index: int):
    try:
        service.delete_todo(index)
        flash("Tarea eliminada 🗑️", "success")
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return redirect(url_for("todo.index")), 400


@todo_bp.get("/saludo/<string:nombre>")
def saludo(nombre: str):
    try:
        name = service.validate_name(nombre)
        return render_template("saludo.html", nombre=name)
    except ValidationError as e:
        flash(str(e), "error")
        return redirect(url_for("todo.index")), 400
