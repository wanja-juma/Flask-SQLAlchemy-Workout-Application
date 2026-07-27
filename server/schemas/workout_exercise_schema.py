from marshmallow import fields, validate

from extensions import ma
from models import WorkoutExercise


class WorkoutExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True

    workout_id = ma.auto_field(required=True)
    exercise_id = ma.auto_field(required=True)

    reps = ma.auto_field(
        required=True,
        validate=validate.Range(min=0)
    )

    sets = ma.auto_field(
        required=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = ma.auto_field(
        required=True,
        validate=validate.Range(min=0)
    )

    exercise = fields.Nested(
        "ExerciseSchema",
        only=(
            "id",
            "name",
            "category",
            "equipment_needed",
        )
    )

    workout = fields.Nested(
        "WorkoutSchema",
        only=(
            "id",
            "date",
            "duration_minutes",
            "notes",
        )
    )