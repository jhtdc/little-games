'''
This flask skeleton file stays empty alot of the time.
However, it can be used to import packages or define classes/functions.

So here we import the Flask class and then create an 
instance of Flask class and created an object of 
it and if you're using a single module (as in this example), use __name__ with the class.

Next there's the UPLOAD_FOLDER where you will store the uploaded files 
and then in the final line we're configuring the app variable with the UPLOAD_FOLDER.
'''

from flask import Flask
app = Flask (__name__)
UPLOAD_FOLDER = r'./uploads'
app.config ['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views

