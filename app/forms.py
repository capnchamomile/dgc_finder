from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Required
from config import Config

class CityStateForm(FlaskForm):
    city_field = StringField('City', validators=[DataRequired('Enter the city')])
    state_field = SelectField('State', choices=Config.STATES, validators=[Required('Select a state')])
    prox_field = SelectField('Proximity', choices=Config.PROXIMITY, validators=[Required('Select proximity')])
    submit = SubmitField('Find Courses by City/State')

class ZipCodeForm(FlaskForm):
    zip_field = StringField('Zip Code', validators=[DataRequired('Enter the Zip')])
    zprox_field = SelectField('Proximity', choices=Config.PROXIMITY, validators=[Required('Select proximity')])
    zip_submit = SubmitField('Find Courses by Zip')