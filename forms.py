from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class SearchBar(FlaskForm):
    first = StringField('First Name', validators=[Length(max=20)])
    middle = StringField('Middle Name', validators=[Length(max=20)])
    last = StringField('Last Name', validators=[Length(max=20)])
    city = StringField('Home City (e.g. New York)', validators=[Length(max=25)])
    state = StringField('Home State (e.g. NY)', validators=[Length(max=2)])
    submit = SubmitField('Search')
    reset = SubmitField('Reset')