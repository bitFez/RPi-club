#!/usr/bin/python

# follow guide here to configure thermometer to pi
# http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/

id = '28-000004f92c20' # id of thermometer. This will need changing for each device
cel = 0 # this is the variable that we'll use to assign the temp to. 
def gettemp(id):
  global cel
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()
    cel= int(mytemp[1])
    # formats result to include a decimal point
    # you can now also use the variable below to append data to a table etc
    cel = '{:.3f}'.format(cel/float(1000))
    
  except:
    return 99999
 
gettemp(id)

print(cel)
