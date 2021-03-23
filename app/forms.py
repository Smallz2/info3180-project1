from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SelectField, validators
from wtforms.validators import DataRequired, InputRequired


class PropertyForm(FlaskForm):
  title = StringField('Property Title', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  number_of_bedrooms = FloatField('No. of Bedrooms', validators=[InputRequired(), validators.NumberRange(min=0)])
  number_of_bathrooms = FloatField('No. of Bathrooms', validators=[InputRequired(), validators.NumberRange(min=0)])
  price = IntegerField('Price', validators=[InputRequired(), validators.NumberRange(min=0)])
  property_type = SelectField('Property Type', choices=["House", "Apartment"], validators=[DataRequired()])
  location = StringField('Location', validators=[DataRequired()])
  photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
