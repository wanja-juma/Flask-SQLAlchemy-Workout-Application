from marshmallow import fields, validate

from extensions import ma
from models import Workout


class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        include_fk = True

    duration_minutes = ma.auto_field(
        required=True,
        validate=validate.Range(min=1, max=300)
    )

    date = ma.auto_field(required=True)

    notes = ma.auto_field()

    workout_exercises = fields.Nested(
        "WorkoutExerciseSchema",
        many=True,
        exclude=("workout",)
    )