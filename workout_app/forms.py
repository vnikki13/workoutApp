from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
    create = SubmitField('Create')
