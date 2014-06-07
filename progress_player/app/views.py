'''
We imported the app object from the app package along with some other imports.

'''

import os
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app


@app.route('/')
def index():
     return render_template('index.html')

