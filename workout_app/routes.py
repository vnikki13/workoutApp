from workout_app import app
from workout_app import db
from workout_app.models import Exercise, Workout
from flask import flash, redirect, render_template, request, url_for
from workout_app.forms import ExerciseForm, WorkoutForm

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/workouts", methods=['GET', 'POST'])
def workouts():
    workouts = db.session.execute(
    db.select(Workout).order_by(Workout.title)).scalars()
    return render_template("workouts.html", workouts=workouts)

@app.route('/workout/new', methods=['GET', 'POST'])
def new_workout():
    form = WorkoutForm()
    exercises = db.session.execute(
        db.select(Exercise).order_by(Exercise.title)).scalars()
    form.exercises.choices = [(exercise.id, exercise.title) for exercise in exercises]
    if form.validate_on_submit():
        exercises = [Exercise.query.get_or_404(exercise) for exercise in form.exercises.data]
        db.session.add(Workout(
            title=form.title.data,
            exercises=exercises
        ))
        db.session.commit()
        flash('Workout Created Successfully!', 'success')
        return redirect(url_for('workouts'))
    return render_template('create_workout.html', form=form, legend='Create New Workout')

@app.route('/workout/<int:workout_id>/update', methods=['GET', 'POST'])
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    form = WorkoutForm()
    print(form.exercises.data)

    if request.method == 'GET':
        exercises = db.session.execute(
        db.select(Exercise).order_by(Exercise.title)).scalars()
        form.title.data = workout.title
        form.exercises.choices = [(exercise.id, exercise.title) for exercise in exercises]
        return render_template('create_workout.html', form=form, legend='Update Workout')
    elif form.validate_on_submit():
        workout.title = form.title.data
        workout.exercises = [Exercise.query.get_or_404(exercise) for exercise in form.exercises.data]
        db.session.commit()
        flash('Workout Updated!', 'success')
        return redirect(url_for('workouts'))
    

@app.route('/workout/<int:workout_id>/delete', methods=['POST'])
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Workout Deleted!', 'success')
    return redirect(url_for('workouts'))

@app.route("/exercises", methods=['GET', 'POST'])
def exercises():
    exercises = db.session.execute(
    db.select(Exercise).order_by(Exercise.title)).scalars()
    return render_template("exercises.html", exercises=exercises)
    
@app.route('/exercise/new', methods=['GET', 'POST'])
def new_exercise():
    form = ExerciseForm()
    if form.validate_on_submit():
        db.session.add(Exercise(
            title=form.title.data,
            summary=form.summary.data,
            description=form.description.data,
            equipment=form.equipment.data
        ))
        db.session.commit()
        flash('Exercise Created Successfully!', 'success')
        return redirect(url_for('exercises'))
    return render_template('create_exercise.html', form=form, legend='Create New Exercise')

@app.route('/exercise/<int:exercise_id>/update', methods=['GET', 'POST'])
def update_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    form = ExerciseForm()
    if form.validate_on_submit():
        exercise.title = form.title.data
        exercise.summary = form.summary.data
        exercise.description = form.description.data
        exercise.equipment = form.equipment.data
        db.session.commit()
        flash('Exercise Updated!', 'success')
        return redirect(url_for('exercises'))
    elif request.method == 'GET':
        form.title.data = exercise.title
        form.summary.data = exercise.summary
        form.description.data = exercise.description
        form.equipment.data = exercise.equipment
        return render_template('create_exercise.html', form=form, legend='Update Exercise')

@app.route('/exercise/<int:exercise_id>/delete', methods=['POST'])
def delete_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    flash('Exercise Deleted!', 'success')
    return redirect(url_for('exercises'))

    
    

    