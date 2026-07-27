from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    __table_args__ = (
        CheckConstraint("sets > 0", name="check_sets_positive"),
        CheckConstraint("reps >= 0", name="check_reps_positive"),
        CheckConstraint(
            "duration_seconds >= 0",
            name="check_duration_seconds_positive"
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    reps = db.Column(
        db.Integer,
        nullable=False
    )

    sets = db.Column(
        db.Integer,
        nullable=False
    )

    duration_seconds = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    @validates("sets")
    def validate_sets(self, key, value):
        if value <= 0:
            raise ValueError(
                "Sets must be greater than zero."
            )
        return value

    @validates("reps")
    def validate_reps(self, key, value):
        if value < 0:
            raise ValueError(
                "Reps cannot be negative."
            )
        return value

    @validates("duration_seconds")
    def validate_duration(self, key, value):
        if value < 0:
            raise ValueError(
                "Duration cannot be negative."
            )
        return value

    def __repr__(self):
        return (
            f"<WorkoutExercise "
            f"Workout={self.workout_id}, "
            f"Exercise={self.exercise_id}>"
        )