# Note you must have enabled using the picamera module already!  
  
# Add this part of the code at the beginning of the python code  
import picamera # this imports the PiCamera library   
from datetime import datetime # Use this line if you want to timestamp your pic  
  
# This creates an instance of the camera  
camera = picamera.PiCamera()  
  
# This takes a picture with the filename in quotes  
camera.capture('image1.jpg')  
  
  
# If you will be taking more than 1 pic, create a timestamp on your filename.  
# Use a function to create a new timestamp for each picture  
def takepicture():      
    dt = datetime.now().isoformat() # This grabs current time  
    dtime = dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19] # This formarts the time to add to filename  
    camera.capture("%d.jpg" % int(dtime))  
  
takepicture() # Takes a pic using the function 
