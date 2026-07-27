from marshmallow import validate
from extensions import ma
from models import Workout


class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        include_fk = True

    duration_minutes = ma.auto_field(
        required=True,
        validate=validate.Range(
            min=1,
            max=300,
            error="Workout duration must be between 1 and 300 minutes."
        )
    )

    date = ma.auto_field(required=True)

    notes = ma.auto_field()