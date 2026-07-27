from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from extensions import db
from models import Exercise, Workout, WorkoutExercise
from schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema,
)

api_bp = Blueprint("api", __name__)

# EXERCISES

@api_bp.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


@api_bp.get("/exercises/<int:id>")
def get_exercise(id):

    exercise = Exercise.query.get(id)

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    return jsonify(exercise_schema.dump(exercise)), 200


@api_bp.post("/exercises")
def create_exercise():

    json_data = request.get_json()

    if not json_data:
        return jsonify({"error": "Request body is required"}), 400

    try:
        exercise = exercise_schema.load(json_data)

        db.session.add(exercise)
        db.session.commit()

        return jsonify(exercise_schema.dump(exercise)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@api_bp.delete("/exercises/<int:id>")
def delete_exercise(id):

    exercise = Exercise.query.get(id)

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted successfully"}), 200

# WORKOUTS

@api_bp.get("/workouts")
def get_workouts():

    workouts = Workout.query.all()

    return jsonify(workouts_schema.dump(workouts)), 200


@api_bp.get("/workouts/<int:id>")
def get_workout(id):

    workout = Workout.query.get(id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    return jsonify(workout_schema.dump(workout)), 200


@api_bp.post("/workouts")
def create_workout():

    json_data = request.get_json()

    if not json_data:
        return jsonify({"error": "Request body is required"}), 400

    try:

        workout = workout_schema.load(json_data)

        db.session.add(workout)
        db.session.commit()

        return jsonify(workout_schema.dump(workout)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@api_bp.delete("/workouts/<int:id>")
def delete_workout(id):

    workout = Workout.query.get(id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted successfully"}), 200

# WORKOUT EXERCISES

@api_bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):

    workout = Workout.query.get(workout_id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    exercise = Exercise.query.get(exercise_id)

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    json_data = request.get_json()

    if not json_data:
        return jsonify({"error": "Request body is required"}), 400

    json_data["workout_id"] = workout_id
    json_data["exercise_id"] = exercise_id

    try:

        workout_exercise = workout_exercise_schema.load(json_data)

        db.session.add(workout_exercise)
        db.session.commit()

        return jsonify(
            workout_exercise_schema.dump(workout_exercise)
        ), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400