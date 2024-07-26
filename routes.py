from flask import Blueprint

import services

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return services.get_all_user()

@main.route('/api/v1/message', methods=['POST'])
def post_message():
    pass