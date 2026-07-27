from extensions import ma
from marshmallow import fields, validate
from models import Exercise


class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        include_fk = True

    name = ma.auto_field(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    category = ma.auto_field(
        required=True,
        validate=validate.OneOf(
            [
                "Strength",
                "Cardio",
                "Core",
                "Flexibility",
                "Balance"
            ]
        )
    )

    equipment_needed = ma.auto_field(required=True)

    # populated later to avoid circular references
    workout_exercises = fields.Nested(
        "WorkoutExerciseSchema",
        many=True,
        exclude=("exercise",)
    )