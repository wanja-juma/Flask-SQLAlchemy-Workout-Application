from extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id")
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id")
    )

    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # Child → Parent
    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    def __repr__(self):
        return (
            f"<WorkoutExercise "
            f"Workout={self.workout_id}, "
            f"Exercise={self.exercise_id}>"
        )