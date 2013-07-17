#!/usr/bin/env python
'''
Code snippet from www.textlocal.co.uk API for sending a text message. 

You may have to refer to http://www.textlocal.com/simple-developer-sms-api for debugging
'''
import urllib
  
def sendSMS(uname, pword, numbers, sender, message):
    params = {'uname': uname, 'pword': pword, 'selectednums': numbers,
        'message' : message, 'from': sender}
    f = urllib.urlopen('https://www.txtlocal.co.uk/sendsmspost.php?'
        + urllib.urlencode(params))
    return (f.read(), f.code)
  
resp, code = sendSMS('yourusername', 'yourpassword', '447123456789',
    'Jims Autos', 'Test with an ampersand (&) and a £5 note')
