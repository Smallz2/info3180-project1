"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
	"""Render website's home page."""
	return render_template('home.html')


@app.route('/about/')
def about():
	"""Render the website's about page."""
	return render_template('about.html', name="Property Hunters")


@app.route('/property', methods=["GET", "POST"])
def property():
	form = PropertyForm()
	upload_folder = app.config['UPLOAD_FOLDER']

	if request.method == "POST" and form.validate_on_submit():
		title = form.title.data
		description = form.description.data
		number_of_rooms = form.number_of_bedrooms.data
		number_of_bathrooms = form.number_of_bathrooms.data
		price = form.price.data
		property_type = form.property_type.data
		location = form.location.data
		photo = form.photo.data
		filename = secure_filename(photo.filename)

		# Create new property
		new_property = Property(title, description, number_of_rooms, number_of_bathrooms, price, property_type, location, filename)

		# Add to db 
		db.session.add(new_property)
		db.session.commit()
		photo.save(os.path.join(upload_folder, filename))

		flash("Property was added successfully", 'success')
		return redirect(url_for('properties'))
	flash_errors(form)
	return render_template('new_property.html', form=form)


@app.route('/properties')
def properties():
	return render_template('properties.html', properties=Property.query.all())


@app.route('/uploads/<filename>')
def get_image(filename):
  root_dir = os.getcwd()
  return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)


@app.route('/property/<propertyid>')
def single_property(propertyid):
	single_property = Property.query.filter_by(id=propertyid).first()

	if single_property is None:
		return redirect(url_for('properties'))
	return render_template('property.html', single_property=single_property)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (
					getattr(form, field).label.text,
					error
			), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
	"""Send your static text file."""
	file_dot_text = file_name + '.txt'
	return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also tell the browser not to cache the rendered page. If we wanted
	to we could change max-age to 600 seconds which would be 10 minutes.
	"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response


@app.errorhandler(404)
def page_not_found(error):
	"""Custom 404 page."""
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port="8080")
