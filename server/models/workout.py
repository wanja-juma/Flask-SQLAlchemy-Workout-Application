from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    __table_args__ = (
        CheckConstraint(
            "duration_minutes > 0",
            name="check_duration_positive"
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(
        db.Date,
        nullable=False
    )

    duration_minutes = db.Column(
        db.Integer,
        nullable=False
    )

    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        back_populates="workouts",
        viewonly=True
    )

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError(
                "Workout duration must be greater than zero."
            )
        return value

    def __repr__(self):
        return f"<Workout {self.id}>"