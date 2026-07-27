from flask import Flask

from config import Config
from extensions import db, migrate, ma, cors

# Import models so Flask-Migrate can detect them
from models import Exercise, Workout, WorkoutExercise


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    @app.route("/")
    def home():
        return {
            "message": "Workout Tracker API is running!"
        }, 200

    return app


app = create_app()