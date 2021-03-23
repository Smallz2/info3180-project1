import os

class Config(object):
  """Base Config Object"""
  DEBUG = False
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://hqxmqhexvirwzt:367170a35dba6100675f0383c5045be9b3611ae0b338772965def58931def049@ec2-54-205-183-19.compute-1.amazonaws.com:5432/dejac4lq4sc3ge'
  SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
  UPLOAD_FOLDER = 'uploads/' 

class DevelopmentConfig(Config):
  """Development Config that extends the Base Config Object"""
  DEVELOPMENT = True
  DEBUG = True

class ProductionConfig(Config):
  """Production Config that extends the Base Config Object"""
  DEBUG = False