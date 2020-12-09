#!/bin/python

import requests, re
from pynotifier import Notification


try:

	# Change Jiofi Address if Required
	url = "http://192.168.225.1"
	response = requests.get(url, timeout=1)

	# Finding Battery Percentage From Response
	pattern = r'(id="batterylevel" value=")(\d*)(%")'
	matches = re.findall(pattern, response.text)
	percentage = matches[0][1]

	Notification(title='JioFi Battery Notifier',description='Battery Level ' + percentage, duration=5).send()

except Exception as e:
       	Notification(title='JioFi Battery Notifier',description='JioFi Not Connected', duration=5).send()

