from workout_app import app
from workout_app import db
from workout_app.models import Exercise
from flask import flash, redirect, render_template, request, url_for
from workout_app.forms import ExerciseForm

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/exercises", methods=['GET', 'POST'])
def exercises():
    form = ExerciseForm()
    if request.method == 'POST':
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
    else:
        exercises = db.session.execute(
        db.select(Exercise).order_by(Exercise.title)).scalars()
        return render_template("exercises.html", exercises=exercises, form=form)

    
    

    