from flask import Blueprint, render_template, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import hashlib
import requests

upload_blueprint = Blueprint('get_temperature', __name__)


@upload_blueprint.route('/api/temperature')
def get_temperature():
    try:
        response = requests.get('http://url:00000/temperature')
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return 'Unknown error' + str(e)
    
    #render_template(message_html, title=title, error_message=str(e))
