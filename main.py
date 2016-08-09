from flask import Flask
from flask import render_template, flash, redirect, session, url_for, request, g, send_file
from mail_config import email_driver
from exception_logger import log_driver

import IPython
import smtplib
import os

app 				= Flask(__name__)
app.secret_key 		= "hello9!m5q^hyiv(rfc&-jf$8@h#*8mvuy#%!17*gff#g+l^rom&fvgyoyo"
app.debug 			= False

@app.route('/message-post', methods=['POST'])
def parse_message():
	# To handle the form submission request by the viewer
	email_agent = email_driver()

	try:
		email_agent.send_payload()
		flash('Message successfully sent. Thank you so much for your time :)')
		
	except Exception as E:
		flash('Error in sending message. Try again later :(')
		logger 		= log_driver(E)
		logger.log_exception()					# Make sure we log the exception for referencing

	return redirect(url_for('home'))		# Sends the user back to the home finally


@app.route('/<file_request>', methods=['POST'])
# @app.route('/resume-request', methods=['POST'])
# @app.route('/BARC-route')
def send_resume(file_request):
	try:
		resume_location 	= "Resume"		# File directory relative to root
		if file_request == "resume-request":
			resume_file 		= resume_location + "/Johankok_resume.pdf"
		elif file_request == "BARC-report":
			resume_file 		= resume_location + "/barc-project.pdf"

		with open(os.path.join(os.getcwd(), resume_file), 'rb') as resume:
			return send_file(resume_file,  as_attachment=True)		# Note that resume_file is the path relative to root path of app

	except Exception:
		flash("Error with retrieving resume. Sorry :(")
		return redirect(url_for('home'))		# Sends the user back to the home finally


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@app.route('/back_home')
def home():
	# Routes to the home page
	return render_template('index.html')


@app.route('/portfolio', methods=['GET', 'POST'])
def project_page():		
	# Routes to the project page

	return render_template('portfolio.html')


@app.route('/portfolio/AutoLab', methods=['GET'])
def show_autolab():
	return render_template('Autolab.html')


@app.route('/portfolio/lumiere', methods=['GET'])
def show_lumiere():
	return render_template('lumiere.html')


@app.route('/portfolio/BARC', methods=['GET'])
def show_BARC():
	return render_template('BARC.html')


@app.route('/portfolio/error', methods=['GET'])
def error_page():
	# Routes to a <page under maintenance> page

	return render_template('error.html')

if __name__ == "__main__":
	app.run()
