'''
I imported the Flask class and then create an 
instance of Flask class and created an object of 
it and if I'm using a single module (as in this example), 
I should use __name__ with the class.

Next there's the UPLOAD_FOLDER where I will store the uploaded files 
and then in the final line I'm configuring the app variable with the UPLOAD_FOLDER.
'''

from flask import flask
app = Flask (__name__)
UPLOAD_FOLDER = r'./uploads'
app.config ['UPLOAD_FOLDER'] = UPLOAD_FOLDER
