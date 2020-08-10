import os
import webview

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from csv_convert import *

app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv']
app.config['UPLOAD_PATH'] = 'static/csv_files'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    ip = request.form['ip']
    device_ID = request.form['device_ID']
    filename = secure_filename(uploaded_file.filename)
    if uploaded_file.filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid File", 400
        f = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(f)
        main(ip, f, device_ID)
        os.remove(f)
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

if __name__ == '__main__':
    webview.create_window('CSV to QLab', app)
    webview.start()
