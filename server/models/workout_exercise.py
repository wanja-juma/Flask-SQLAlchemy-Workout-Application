from extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer)

    exercise_id = db.Column(db.Integer)

    reps = db.Column(db.Integer)

    sets = db.Column(db.Integer)

    duration_seconds = db.Column(db.Integer)

    def __repr__(self):
        return (
            f"<WorkoutExercise "
            f"id={self.id}, "
            f"workout_id={self.workout_id}, "
            f"exercise_id={self.exercise_id}>"
        )