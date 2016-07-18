"""
Logging class to handle all logging capabilites 
We make a file under root > log > error.log that will store all the logged information

Note:
Logging files have different configuration levels. In descending order:
	Critical > Error > Warning > Info > Debug > Notset

We can only log files of a higher level or equivalent to the log file
"""

import logging
import os

class log_driver():
	def __init__(self, exception_msg):
		self.exception 	= exception_msg
		self.log_file 	= 'error.log'
		self.root 		= os.getcwd()

	def log_exception(self):
		# First try to open a file in the right directory
		log_file 	= os.path.join(os.getcwd(), 'log', 'error.log')
		if os.path.exists(os.path.join(os.getcwd(), 'log')):
			pass
		else: 
			os.mkdir(os.path.join(os.getcwd(), 'log'))

		logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO)
		logging.error(self.exception)
		logging.shutdown()
