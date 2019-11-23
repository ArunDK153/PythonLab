import sys
from time import sleep
from urllib.request import *
import json
from requests import *


def send_data_thingspeak():
    fieldid='2'
    writekey='TRV2A3148OPDX7D8'
    code='1'
    baseURL = 'http://api.thingspeak.com/update?api_key='+writekey+'&field'+fieldid+'='
    f = urlopen(baseURL+code)	
    print("Sending",code,"to thingspeak")
    f.read()
    f.close()

def read_data_thingspeak():
	channelid='918879'
	fieldid='2'
	URL='https://api.thingspeak.com/channels/'+channelid+'/fields/'+fieldid+'.json?api_key='
	readkey='Z5PEGCWA99S6A146' #'CU4W1P240P0XK0QP'
	HEADER='&results=1'
	NEW_URL=URL+readkey+HEADER
	print("Contacting URL : ",NEW_URL)
	get_data=get(NEW_URL).json()
	# print(get_data)
	# channel_id=get_data['channel']['id']
	fields=get_data['feeds']
	# print(fields)
	# t=[]
	for x in fields:
		print(x['field'+fieldid])
send_data_thingspeak()
# sleep(5)
read_data_thingspeak()


