from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Todo, TodoRepository, ValidationError

todo_bp = Blueprint("todo", __name__)

# Repositorio en memoria (para el ejercicio). En un proyecto real lo inyectarías.
repo = TodoRepository()


@todo_bp.get("/")
def index():
    items = repo.list_all()
    return render_template("index.html", items=items)


@todo_bp.get("/nuevo")
def new_form():
    return render_template("todo_form.html")


@todo_bp.post("/nuevo")
def create():
    title = request.form.get("title", "")
    priority = request.form.get("priority", "")
    try:
        repo.add(Todo(title=title, priority=priority))
        flash("Tarea creada ✅", "success")
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return render_template("todo_form.html", title=title, priority=priority), 400


@todo_bp.post("/toggle/<int:index>")
def toggle(index: int):
    try:
        repo.toggle(index)
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return redirect(url_for("todo.index")), 400


@todo_bp.post("/delete/<int:index>")
def delete(index: int):
    try:
        repo.delete(index)
        flash("Tarea eliminada 🗑️", "success")
        return redirect(url_for("todo.index"))
    except ValidationError as e:
        flash(str(e), "error")
        return redirect(url_for("todo.index")), 400
