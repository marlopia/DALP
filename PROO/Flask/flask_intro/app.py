from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", flask_env=app.config.get("FLASK_ENV"))


@app.route("/saluda/<nombre>")
def saluda(nombre):
    return f"Hola {nombre}!"


@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"La suma de {a} y {b} es {a + b}"


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    errores = []
    nombre = ""
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        if len(nombre) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres.")
        if len(mensaje) < 10:
            errores.append("El mensaje debe tener al menos 10 caracteres.")

        if not errores:
            return render_template("contacto_ok.html", nombre=nombre, mensaje=mensaje)

    return render_template(
        "contacto.html", errores=errores, nombre=nombre, mensaje=mensaje
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        if usuario:
            session["user"] = usuario
            return redirect(url_for("perfil"))
        else:
            error = "Debes escribir un nombre de usuario"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/perfil")
def perfil():
    usuario = session.get("user")
    if not usuario:
        return redirect(url_for("login"))
    return render_template("perfil.html", usuario=usuario)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/api/saludo")
def api_saludo():
    nombre = request.args.get("nombre", "mundo")
    return jsonify({"saludo": f"Hola, {nombre}"})


if __name__ == "__main__":
    app.run(debug=True)
