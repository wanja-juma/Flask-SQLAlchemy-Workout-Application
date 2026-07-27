from sqlalchemy.orm import validates

from extensions import db


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    equipment_needed = db.Column(
        db.Boolean,
        nullable=False
    )

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        back_populates="exercises",
        viewonly=True
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty.")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        if not value or not value.strip():
            raise ValueError("Category cannot be empty.")
        return value.strip().title()

    def __repr__(self):
        return f"<Exercise {self.name}>"