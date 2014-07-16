import os

from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
import settings
from app import app

@app.route('/')
def index():
    songs = []
    files = os.listdir(os.path.join(settings.STATIC_PATH, 'uploads'))
    for file in files:
        if 'mp3' in file:
            songs.append(file)
    return render_template('index.html', songs=songs)


@app.route('/upload')
def upload_page():
    return render_template('upload.html')


@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(settings.STATIC_PATH, 'uploads', filename))
    return redirect('/')
