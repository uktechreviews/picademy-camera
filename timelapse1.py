from picamera import PiCamera
import time
from datetime import datetime
with PiCamera() as camera:
	time = str(datetime.now())
#	camera.start_preview()
	camera.annotate_text=time
	camera.capture('/home/pi/photo_output/test.jpg')
#camera.stop_preview()
    
