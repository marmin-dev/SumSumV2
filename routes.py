from flask import Blueprint, request

import services

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return services.get_all_user()


@main.route('/api/v1/message', methods=['POST'])
def post_message():
    # 바디에서 json 데이터 추출
    data = request.get_json()
    if not data:
        return {"error": "No input data provided"}, 400
    if 'message' not in data:
        return {"error": "'content' field is required"}, 400
    return services.post_message(data['message'])
