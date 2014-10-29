from picamera import PiCamera
#from datetime import datetime
import time
frames = 5
timebetween = 10
actual_timebetween = timebetween - 6
framecount = 0

while framecount < frames: 
	with PiCamera() as camera:
		localtime = time.asctime( time.localtime(time.time()) )
		camera.annotate_text=localtime
		camera.capture('/home/pi/photo_output/image%s.jpg'%(framecount))
		framecount +=1
		time.sleep(actual_timebetween)
		  

