from marshmallow import validate
from extensions import ma
from models import Exercise


class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        include_fk = True

    name = ma.auto_field(
        required=True,
        validate=validate.Length(
            min=2,
            max=100,
            error="Exercise name must be between 2 and 100 characters."
        )
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