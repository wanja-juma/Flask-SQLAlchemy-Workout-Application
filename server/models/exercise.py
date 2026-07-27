from extensions import db


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    category = db.Column(db.String(100))

    equipment_needed = db.Column(db.Boolean)

    def __repr__(self):
        return (
            f"<Exercise "
            f"id={self.id}, "
            f"name='{self.name}', "
            f"category='{self.category}'>"
        )