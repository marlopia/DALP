import os
from dotenv import load_dotenv
from flask import Flask, flash, json, redirect, render_template, request, url_for


app = Flask(__name__)
load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")

os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        task_list = json.load(f)
else:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)
    task_list = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tareas", methods=["GET", "POST"])
def tareas():
    if request.method == "POST":
        texto = request.form.get("texto", "").strip()
        if texto:
            new_task = {"id": get_next_id(), "texto": texto, "done": False}
            task_list.append(new_task)
            save_tasks()
            flash(f"Tarea '{texto}' creada", "success")

    return render_template("tareas.html", tareas=task_list)


@app.route("/api/tarea_toggle/<int:id>", methods=["POST"])
def tarea_toggle(id):
    for tarea in task_list:
        if tarea["id"] == id:
            tarea["done"] = not tarea["done"]
            save_tasks()
            if tarea["done"]:
                flash(f"Tarea '{tarea['texto']}' marcada como hecha", "info")
            else:
                flash(f"Tarea '{tarea['texto']}' marcada como pendiente", "info")
            break
    return redirect(url_for("tareas"))


def save_tasks():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(task_list, f, indent=2, ensure_ascii=False)


def get_next_id():
    if task_list:
        return max(t["id"] for t in task_list) + 1
    return 0


if __name__ == "__main__":
    app.run(debug=True)
