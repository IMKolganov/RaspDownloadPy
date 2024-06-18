from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import hashlib

app = Flask(__name__, template_folder='templates', static_folder='static')

hashed_password = '447e4ec3f5804e78d7f952eb359a71e5'

UPLOAD_FOLDER = 'uploads'
MESSAGE_HTML = 'message.html'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password', '')
    if not password:
        return 'Password is required!'
    
    input_password_hash = hashlib.md5(password.encode()).hexdigest()

    if input_password_hash != hashed_password:
        return render_template(MESSAGE_HTML, message='Invalid password!', file_path='')

    
    file = request.files['file']
    if file.filename == '':
        return render_template(MESSAGE_HTML, message='No selected file!', file_path='')
        
    
    try:
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            print(f'File uploaded successfully. Path: {file_path}')
            
            return render_template(MESSAGE_HTML, message='File uploaded successfully.', file_path=file_path)

        return 'Unknown error'
    except Exception as e:
        return render_template(MESSAGE_HTML, error_message=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)