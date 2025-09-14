from flask import Flask
from datetime import datetime


def create_app():
    app = Flask(__name__)

    # --- Configuration ---
    app.config['SECRET_KEY'] = 'change_this_to_a_secure_key'
    app.config['DEBUG'] = True  # à mettre False en production

    # --- Context processor pour l'année ---
    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.now().year}

    # --- Enregistrer les blueprints ---
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
