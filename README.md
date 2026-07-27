# Flask Workout Tracker API

## Project Description

The **Flask Workout Tracker API** is a RESTful backend application built with **Flask**, **SQLAlchemy**, and **Marshmallow** for managing workouts and exercises.

The application allows personal trainers to create and manage workouts, create reusable exercises, and assign exercises to workouts with additional information such as the number of sets, repetitions, or duration.

The project demonstrates the use of:

- Flask REST APIs
- SQLAlchemy ORM
- Many-to-Many Relationships using an Association Object
- Marshmallow Serialization & Deserialization
- Database Migrations using Flask-Migrate
- Database Constraints
- Model Validations
- Schema Validations
- CRUD Operations

---

## Project Structure

```text
server/
│
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── __init__.py
│   ├── exercise.py
│   ├── workout.py
│   └── workout_exercise.py
│
├── schemas/
│   ├── __init__.py
│   ├── exercise_schema.py
│   ├── workout_schema.py
│   └── workout_exercise_schema.py
│
├── routes.py
├── seed.py
├── migrations/
├── instance/
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

# Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask Marshmallow
- Marshmallow
- SQLite
- SQLAlchemy

---

# Installation

## 1. Clone the repository

```bash
git clone <git@github.com:wanja-juma/Flask-SQLAlchemy-Workout-Application.git>

cd Flask-SQLAlchemy-Workout-Application/server
```

---

## 2. Install dependencies

Using Pipenv:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

---

## 3. Initialize the database

Run the following commands:

```bash
flask db init
```

```bash
flask db migrate -m "Initial migration"
```

```bash
flask db upgrade
```

> **Note:** `flask db init` is only required the first time the project is set up.

---

## 4. Seed the database

Populate the database with sample data:

```bash
python seed.py
```

---

# Running the Application

Start the Flask development server:

```bash
python run.py
```

or

```bash
flask run
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## Workout Endpoints

### GET `/workouts`

Returns a list of all workouts.

---

### GET `/workouts/<id>`

Returns a single workout together with its associated exercises, including:

- sets
- reps
- duration_seconds

---

### POST `/workouts`

Creates a new workout.

Example Request

```json
{
    "date": "2026-07-27",
    "duration_minutes": 45,
    "notes": "Upper body workout"
}
```

---

### DELETE `/workouts/<id>`

Deletes a workout from the database.

---

# Exercise Endpoints

### GET `/exercises`

Returns all exercises.

---

### GET `/exercises/<id>`

Returns one exercise together with all workouts that use it.

---

### POST `/exercises`

Creates a new exercise.

Example Request

```json
{
    "name": "Push Up",
    "category": "Strength",
    "equipment_needed": false
}
```

---

### DELETE `/exercises/<id>`

Deletes an exercise from the database.

---

# Workout Exercise Endpoint

### POST `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`

Associates an exercise with a workout.

This endpoint stores the exercise-specific workout information:

- sets
- reps
- duration_seconds

Example Request

```json
{
    "sets": 4,
    "reps": 12,
    "duration_seconds": 0
}
```

---

# Database Models

## Exercise

| Field | Type |
|--------|------|
| id | Integer |
| name | String |
| category | String |
| equipment_needed | Boolean |

---

## Workout

| Field | Type |
|--------|------|
| id | Integer |
| date | Date |
| duration_minutes | Integer |
| notes | Text |

---

## WorkoutExercise

| Field | Type |
|--------|------|
| id | Integer |
| workout_id | Foreign Key |
| exercise_id | Foreign Key |
| reps | Integer |
| sets | Integer |
| duration_seconds | Integer |

---

# Relationships

- A Workout has many WorkoutExercises
- An Exercise has many WorkoutExercises
- A WorkoutExercise belongs to a Workout
- A WorkoutExercise belongs to an Exercise
- A Workout has many Exercises through WorkoutExercises
- An Exercise has many Workouts through WorkoutExercises

---

# Validation

The application includes validation at three different levels.

## Database Constraints

- NOT NULL constraints
- UNIQUE constraints
- Foreign Key constraints

## Model Validations

Examples include:

- Exercise name cannot be empty
- Workout duration must be greater than zero
- Sets must be at least one
- Repetitions cannot be negative
- Duration cannot be negative

## Schema Validations

Marshmallow validates incoming request data before it reaches the database.

Examples include:

- Required fields
- String length validation
- Numeric range validation
- Category validation

---

# Sample Response

```json
{
    "id": 1,
    "date": "2026-07-27",
    "duration_minutes": 45,
    "notes": "Upper body workout",
    "workout_exercises": [
        {
            "sets": 4,
            "reps": 15,
            "duration_seconds": 0,
            "exercise": {
                "id": 1,
                "name": "Push Up",
                "category": "Strength",
                "equipment_needed": false
            }
        }
    ]
}
```

---

# Future Improvements

Possible enhancements include:

- User Authentication
- Role-Based Authorization
- Update (PUT/PATCH) endpoints
- Pagination
- Search and Filtering
- Unit and Integration Testing
- API Documentation using Swagger/OpenAPI

---

# Author

**Ruth Juma**

Junior Software Developer