from extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Date)

    duration_minutes = db.Column(db.Integer)

    notes = db.Column(db.Text)

    def __repr__(self):
        return (
            f"<Workout "
            f"id={self.id}, "
            f"date={self.date}, "
            f"duration={self.duration_minutes} minutes>"
        )