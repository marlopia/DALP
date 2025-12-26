from flask import Flask
from controllers.todo_controller import todo_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"  # en producción, usa variable de entorno

    # Registro del controlador (Blueprint)
    app.register_blueprint(todo_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
