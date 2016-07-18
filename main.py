from flask import Flask
from flask import render_template, flash, redirect, session, url_for, request, g, send_file
from mail_config import email_driver
from exception_logger import log_driver

import IPython
import smtplib
import os

app 				= Flask(__name__)
app.secret_key 		= ""
app.debug 			= True

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


@app.route('/resume-request', methods=['POST'])
def send_resume():
	try:
		resume_location 	= "Resume"		# File directory relative to root
		resume_file 		= resume_location + "/Johankok_resume.pdf"

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

@app.route('/portfolio/error', methods=['GET'])
def error_page():
	# Routes to a <page under maintenance> page

	return render_template('error.html')

if __name__ == "__main__":
	app.run()
