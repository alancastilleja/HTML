from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Dog: ')
    submit = SubmitField('Add dog to list')

class DelForm(FlaskForm):
    id = IntegerField('Id number of dog you want to remove:')
    submit = SubmitField('Delete dog')