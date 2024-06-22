from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename
import os
import hashlib

upload_blueprint = Blueprint('upload', __name__)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    title = 'Upload file'
    hashed_password = current_app.config['HASHED_PASSWORD']
    upload_folder = current_app.config['UPLOAD_FOLDER']
    message_html = current_app.config['MESSAGE_HTML']

    password = request.form.get('password', '')
    if not password:
        return 'Password is required!'
    
    input_password_hash = hashlib.md5(password.encode()).hexdigest()

    if input_password_hash != hashed_password:
        return render_template(message_html, title=title, message='Invalid password!', file_path='')

    file = request.files['file']
    if file.filename == '':
        return render_template(message_html, title=title, message='No selected file!', file_path='')

    try:
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            print(f'File uploaded successfully. Path: {file_path}')
            
            return render_template(message_html, title=title, message='File uploaded successfully.', file_path=file_path)

        return 'Unknown error'
    except Exception as e:
        return render_template(message_html, title=title, error_message=str(e))
