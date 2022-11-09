from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), (
        'porcupine', 'Porcupine'), ('fish', 'Fish'), ('turtle', 'Turtle')], validators=[InputRequired()])
    photo = StringField("Photo Url", validators=[Optional()])
    age = IntegerField("Age (years)", validators=[Optional()])
    notes = StringField("Pet notes", validators=[Optional()])
    available = BooleanField("Availability")
