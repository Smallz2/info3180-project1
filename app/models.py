from . import db

class Property(db.Model):
  __tablename__ = 'properties'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80))
  description = db.Column(db.String(1000))
  number_of_bedrooms = db.Column(db.Float())
  number_of_bathrooms = db.Column(db.Float())
  price = db.Column(db.Integer)
  property_type = db.Column(db.String(80))
  location = db.Column(db.String(80))
  photo = db.Column(db.String(225))

  def __init__(self, title, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo):
    self.title = title  
    self.description = description
    self.number_of_bedrooms = number_of_bedrooms
    self.number_of_bathrooms = number_of_bathrooms
    self.price = price
    self.property_type = property_type
    self.location = location
    self.photo = photo

  def __repr__(self):
    return '<Property %r>' % (self.title)
