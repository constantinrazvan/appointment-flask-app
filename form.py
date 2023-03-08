from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField

class AppointmentForm(FlaskForm):
    email = StringField('email')
    date = DateField('date')
    submit = SubmitField('submit')