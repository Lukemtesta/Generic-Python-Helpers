'''
csv_manager.py

Python methods for telecommunications

Dependencies:

Python 3.0+

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

Dependencies:

twilio>=6.0.0
'''

import sys
import os

# For linux support
g_current_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(g_current_dir, 'thirdparty', 'sms-integration-python'))
sys.path.append(os.path.join(g_current_dir, 'thirdparty', 'solinked'))

from logger import Logger
from twilio.rest import Client


'''
Global definitions
'''
g_logger = Logger(__file__)

g_sms_sid 	= "AC6999d068a950993a2e37362164383971"
g_sms_auth 	= "4f862dd07de06bb9996c503da52ae50d"
g_twillio_number = "+441524917376"


'''
Send a message to a device
'''
def send_sms(i_message, i_recipient_number, i_country_code = 44): 

	client = Client(g_sms_sid, g_sms_auth)
	
	i_recipient_number = "+" + str(i_country_code) + str(i_recipient_number)

	client.messages.create(to=i_recipient_number, from_=g_twillio_number, body=i_message)
	
	g_logger.log('Sending sms', i_message, 'to', i_recipient_number)
	g_logger.log(sms)
	
'''
Make a phone call
'''
def call(i_message, i_recipient_number, i_country_code = 44): 

	client = Client(g_sms_sid, g_sms_auth)
	
	i_recipient_number = "+" + str(i_country_code) + str(i_recipient_number)
	
	client.calls.create(
		url='http://demo.twilio.com/docs/voice.xml',
		to=i_recipient_number,
		from_=g_twillio_number)
    