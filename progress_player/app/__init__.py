'''
This flask skeleton file stays empty alot of the time.
However, it can be used to import packages or define classes/functions.

So here we import the Flask class and then create an 
instance of Flask class and created an object of 
it and if you're using a single module (as in this example), use __name__ with the class.

Next there's the UPLOAD_FOLDER where you will store the uploaded files 
and then in the final line we're configuring the app variable with the UPLOAD_FOLDER.

Still having issues getting the uploaded file to load correctly and I'm suspecting it's something
related to the syntax surrounding the UPLOAD_FOLDER variable. 
The commented out code is what I started with. Got ioerror when loading mp3. 
The current code gets me one step further and loads the player but still, no playback.
This is probably the worlds longest comment in a basic ass __init__.py file.
'''

'''from flask import Flask
app = Flask (__name__)
UPLOAD_FOLDER = r'./uploads'
app.config ['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views'''

import os
from flask import Flask
 
app = Flask(__name__)
 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views