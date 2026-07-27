from marshmallow import validate
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
        validate=validate.Range(
            min=0,
            error="Reps cannot be negative."
        )
    )

    sets = ma.auto_field(
        required=True,
        validate=validate.Range(
            min=1,
            error="Sets must be at least 1."
        )
    )

    duration_seconds = ma.auto_field(
        required=True,
        validate=validate.Range(
            min=0,
            error="Duration cannot be negative."
        )
    )