from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class ExerciseForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    summary = StringField(
        'Summary'
    )
    description = StringField(
        'Description'
    )
    equipment = StringField(
        'Equipment'
    )
    create = SubmitField('Submit')

class WorkoutForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    exercises = SelectMultipleField('Exercises', coerce=int, validate_choice=False)
    create = SubmitField('Submit')
