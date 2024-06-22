# RaspDownloadPy

Flask File Upload Project
This project is a simple Flask application that allows users to upload files securely with password protection. The project includes basic features such as password authentication, file upload handling, and user feedback.

Features
Password-protected file upload
Secure filename handling using werkzeug.utils.secure_filename
Configurable upload directory
User feedback through HTML templates
Project Structure

.
├── app.py
├── templates
│   ├── upload.html
│   └── message.html
├── static
└── uploads
Installation
Clone the repository:

git clone ...
cd flask-file-upload
Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate
Install the required packages:

pip install Flask
Configuration
Set the hashed password:
Replace '447e4ec3f5804e78d7f952eb359a71e5' in app.py with the actual hashed password generated by:

import hashlib
password = 'your_password'
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(hashed_password)
Ensure the upload folder exists:

mkdir -p uploads
Running the Application
Start the Flask application:

python app.py
Open your web browser and go to http://0.0.0.0:5000 to access the file upload interface.

Usage
Enter the password in the input field.
Select a file to upload.
Click the "Upload" button.
Receive feedback on the upload status.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Flask framework documentation: Flask
Werkzeug documentation: Werkzeug
Feel free to contribute to this project by opening issues or submitting pull requests.
