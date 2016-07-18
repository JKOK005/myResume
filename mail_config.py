"""Configure E mail here """

import smtplib
from flask import request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import copy as cp

gmail_usr 	= "autoSenderFlask@gmail.com"
gmail_pass 	= "autoSendMyMail005"

class email_driver():
	"""	Creates a class module to handle all Emailing """

	def __init__(self):
		fromaddr	= "autoSenderFlask@gmail.com"
		toaddr 		= "JKOK005@e.ntu.edu.sg"
		subject 	= "Some viewed your page! Woo Hoo"

		msg 			= MIMEMultipart()
		msg['From']		= fromaddr
		msg['To']		= toaddr
		msg['Subject']	= subject
		self.Message 	= cp.deepcopy(msg)			# Message to send by deepcopying payload

	def _get_viewer_mail(self):
		"""Just gets the content that the user has filled up"""

		Name 		= request.form.get("name")		# Parses each individual component
		Mail 		= request.form.get("email", "")
		Message 	= request.form.get("message")

		body 	= """
		Message from someone who viewed your web page:

		Name: {0}
		Contact: {1}
		Message: {2}

		End of message
		""". format(Name, Mail, Message)

		return body


	def send_payload(self):
		"""Sends the mail that the user keyed in to my account"""
		body 	= self._get_viewer_mail()
		self.Message.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.Message['From'], gmail_pass)
		text = self.Message.as_string()
		server.sendmail(self.Message['From'], self.Message['To'], text)
		server.quit()