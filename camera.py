import picamera
from time import sleep
import datetime
import time
import requests


#camera = picamera.PiCamera()
time = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')
Time = unicode(time)

while True:
	print "Raspberry Pi Camera"
	try:
		#camera.capture('/home/pi/{}.jpg'.format(Time))
		url = 'http://192.168.1.8:5000/postimage/'
		#files = {'file': open('{}.jpg'.format(Time))}
		files = {'file': open('4x6.jpg'.format(Time))}
		r = requests.post(url, files=files)
		r.text
		print "Sending image success"
		sleep(3)
 		
	except KeyboardInterrupt:
        	print "Keyboard Interupt"
        	break
	        ser.close()

