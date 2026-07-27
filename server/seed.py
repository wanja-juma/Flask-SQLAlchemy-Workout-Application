from datetime import date

from app import app
from extensions import db
from models import Exercise, Workout, WorkoutExercise


with app.app_context():

    # Clear existing data
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    db.session.commit()

    print("Previous data deleted.")

    # -------------------------
    # Create Exercises
    # -------------------------

    push_up = Exercise(
        name="Push Up",
        category="Strength",
        equipment_needed=False
    )

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    jumping_jacks = Exercise(
        name="Jumping Jacks",
        category="Cardio",
        equipment_needed=False
    )

    dumbbell_press = Exercise(
        name="Dumbbell Press",
        category="Strength",
        equipment_needed=True
    )

    db.session.add_all([
        push_up,
        squat,
        plank,
        jumping_jacks,
        dumbbell_press
    ])

    db.session.commit()

    print("Exercises created.")

    # -------------------------
    # Create Workouts
    # -------------------------

    workout1 = Workout(
        date=date(2026, 7, 27),
        duration_minutes=45,
        notes="Upper body workout"
    )

    workout2 = Workout(
        date=date(2026, 7, 28),
        duration_minutes=35,
        notes="Core and cardio session"
    )

    workout3 = Workout(
        date=date(2026, 7, 29),
        duration_minutes=60,
        notes="Full body workout"
    )

    db.session.add_all([
        workout1,
        workout2,
        workout3
    ])

    db.session.commit()

    print("Workouts created.")

    # -------------------------
    # Associate Exercises
    # -------------------------

    associations = [

        WorkoutExercise(
            workout=workout1,
            exercise=push_up,
            reps=15,
            sets=4,
            duration_seconds=0
        ),

        WorkoutExercise(
            workout=workout1,
            exercise=dumbbell_press,
            reps=12,
            sets=4,
            duration_seconds=0
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=plank,
            reps=0,
            sets=3,
            duration_seconds=60
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=jumping_jacks,
            reps=20,
            sets=3,
            duration_seconds=0
        ),

        WorkoutExercise(
            workout=workout3,
            exercise=squat,
            reps=15,
            sets=4,
            duration_seconds=0
        ),

        WorkoutExercise(
            workout=workout3,
            exercise=push_up,
            reps=10,
            sets=4,
            duration_seconds=0
        )
    ]

    db.session.add_all(associations)

    db.session.commit()

    print("Workout exercises created.")
    print("Database seeded successfully!")