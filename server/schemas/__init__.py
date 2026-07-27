from .exercise_schema import ExerciseSchema
from .workout_schema import WorkoutSchema
from .workout_exercise_schema import WorkoutExerciseSchema

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)