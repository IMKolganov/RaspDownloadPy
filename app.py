from flask import Flask, render_template
from upload import upload_blueprint  # Импортируем blueprint

app = Flask(__name__, template_folder='templates', static_folder='static')

# Конфигурационные параметры
app.config['HASHED_PASSWORD'] = '447e4ec3f5804e78d7f952eb359a71e5'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MESSAGE_HTML'] = 'message.html'

app.register_blueprint(upload_blueprint)  # Регистрируем blueprint

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)
    
@app.route('/about')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)
    
@app.route('/contact')
def contact():
    title = 'Contact Us'
    return render_template('contact.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
